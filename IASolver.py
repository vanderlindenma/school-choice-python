__author__ = 'martinvanderlinden'

# Adapted from : http://jeremykun.com/2014/04/02/stable-marriages-and-designing-markets/

class Student(object):
   def __init__(self, id, prefList):
      self.prefList = prefList
      self.rejections = 0 # num rejections is also the index of the next option
      self.id = id

   def preference(self):
      return self.prefList[self.rejections]

   def __repr__(self):
      return repr(self.id)


class School(object):
   def __init__(self, id, prefList, capacity=1):
      self.prefList = prefList
      self.capacity = capacity
      self.accepted = set()
      self.apply    = set()
      self.id = id

   def reject_accept(self, verbose):

      if not isinstance(verbose,bool):
         raise ValueError('verbose must be a boolean')

      if verbose == False:
         if len(self.accepted) + len(self.apply) <= self.capacity:
            self.accepted |= self.apply
            return set()
         else:
            sortedStudents = sorted(list(self.apply), key=lambda student: self.prefList.index(student.id))
            self.accepted.update(sortedStudents[:self.capacity - len(self.accepted)])
            return set([x for x in self.apply if x not in self.accepted])

      if verbose == True :
         if len(self.accepted) + len(self.apply) <= self.capacity:
            print('School %d has %d seats left' %(self.id,self.capacity - len(self.accepted)) )
            print('Students %s applied to school %d '
                  'and there is enough seats left for every new applicant to be accepted' %(self.apply,self.id)
                  )
            self.accepted |= self.apply
            print('Students %s are accepted at school %d in this round' %(self.apply, self.id) )
            print('The complete set of accepted students at school %d is now %s' %(self.id,self.accepted))
            return set()
         else:
            print('School %d has %d seats left' %(self.id,self.capacity - len(self.accepted)) )
            print('Students %s applied to school %d '
                  'and there is NOT enough seats left for every new applicant to be accepted' %(self.apply,self.id))
            sortedStudents = sorted(list(self.apply), key=lambda student: self.prefList.index(student.id))
            print('The priority order at School %d for new applicants is %s' %(self.id,sortedStudents))
            print('Students %s are accepted at school %d in this round' %(sortedStudents[:self.capacity - len(self.accepted)],self.id))
            self.accepted.update(sortedStudents[:self.capacity - len(self.accepted)])
            print('Students %s are rejected from school %d' %([x for x in self.apply if x not in self.accepted],self.id))
            print('The complete set of accepted students at school %d at this point is %s' %(self.id,self.accepted))

            return set([x for x in self.apply if x not in self.accepted])

   def __repr__(self):
      return repr(self.id)


# stableMarriage: [Student], [School] -> {School -> [Student]}
# construct a matching between students and schools according to the IA procedure

def IAMarriage(students, schools,verbose):

   if not isinstance(verbose,bool):
         raise ValueError('verbose must be a boolean')

   if verbose == True :
      print('FIRST ROUND OF APPLICATIONS')

   unassigned = set(students)

   while len(unassigned) > 0:

      if verbose == True :
         print('')


      for student in unassigned:
         schools[student.preference()].apply.add(student)
      unassigned = set()

      for school in schools:
         unassigned |= school.reject_accept(verbose = verbose)
         school.apply = set()

      for student in unassigned:
         student.rejections += 1

      if verbose == True :
         print('END OF THIS ROUND OF APPLICATIONS')
         print('At the end of this round, the unassigned students are %s' %unassigned)

   marriage = list()

   for student in students:
         marriage.append(student.prefList[student.rejections])

   return marriage


# verifyStable: [Student], [School], {School -> [Student]} -> bool
# check whether the assignment of students to school is a stable assignment

def verifyStable(students, schools, marriage):
   import itertools

   precedes = lambda L, item1, item2: L.index(item1) < L.index(item2)
   partner = lambda student: filter(lambda s: student in marriage[s], schools)[0] # unique

   def studentPrefers(student, school):
      return precedes(student.prefList, school.id, partner(student).id)

   def schoolPrefers(school, student):
      return any(map(lambda x: precedes(school.prefList, student.id, x.id), marriage[school]))

   for (student, school) in itertools.product(students, schools):
      if student not in marriage[school] and studentPrefers(student, school) and schoolPrefers(school, student):
         return False

   return True


if __name__ == "__main__":
   from unittest import test

   students = [Student(0, [0,1]), Student(1, [1,0]),Student(2, [0,1])]
   schools = [School(0, [0,1,2], 1), School(1, [1,0,2], 2)]
   marriage = IAMarriage(students, schools)
   test({schools[0]:[students[0]], schools[1]:[students[1]]}, marriage)
   test(True, verifyStable(students, schools, marriage))

   students = [Student(0, [0]), Student(1, [0]), Student(2, [0]), Student(3, [0])]
   schools = [School(0, [0,1,2,3], 4)]
   marriage = IAMarriage(students, schools)
   test({schools[0]: students}, marriage)
   test(True, verifyStable(students, schools, marriage))

   students = [Student(0, [0,1,2]), Student(1, [0,1,2]), Student(2, [0,1,2]), Student(3, [0,1,2]),Student(4, [1,0,2]), Student(5, [1,0,2])]
   schools = [School(0, [0,1,2,3,4,5], 2), School(1, [3,2,1,0,4,5], 2),School(2, [3,2,1,0,4,5], 2)]
   marriage = IAMarriage(students, schools, verbose = True)
   test({schools[0]: students[:2], schools[1]: students[2:]}, marriage)
   test(True, verifyStable(students, schools, marriage))


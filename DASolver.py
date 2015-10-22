# http://jeremykun.com/2014/04/02/stable-marriages-and-designing-markets/

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
      self.held = set()
      self.id = id

   def reject(self):
      # trim the self.held set down to its capacity, returning the list of rejected students.

      if len(self.held) < self.capacity:
         return set()
      else:
         sortedStudents = sorted(list(self.held), key=lambda student: self.prefList.index(student.id))
         self.held = set(sortedStudents[:self.capacity])

         return set(sortedStudents[self.capacity:])

   def __repr__(self):
      return repr(self.id)


# stableMarriage: [Student], [School] -> {School -> [Student]}
# construct a stable (polygamous) marriage between students and schools
def stableMarriage(students, schools):
   unassigned = set(students)

   while len(unassigned) > 0:
      for student in unassigned:
         schools[student.preference()].held.add(student)
      unassigned = set()

      for school in schools:
         unassigned |= school.reject()

      for student in unassigned:
         student.rejections += 1


   marriage = list()

   for student in students:
         marriage.append(student.prefList[student.rejections])

   return marriage


# verifyStable: [Student], [School], {School -> [Student]} -> bool
# check that the assignment of students to school is a stable marriage
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


# if __name__ == "__main__":
#    from unittest import test
#
   students = [Student(0, [0,1]), Student(1, [1,0]),Student(2, [1,0])]
   schools = [School(0, [0,1,2], 1), School(1, [1,0,2], 2)]
   marriage = stableMarriage(students, schools)
#    test({schools[0]:[students[0]], schools[1]:[students[1]]}, marriage)
#    test(True, verifyStable(students, schools, marriage))
#
#    students = [Student(0, [0]), Student(1, [0]), Student(2, [0]), Student(3, [0])]
#    schools = [School(0, [0,1,2,3], 4)]
#    marriage = stableMarriage(students, schools)
#    test({schools[0]: students}, marriage)
#    test(True, verifyStable(students, schools, marriage))
#
#    students = [Student(0, [0,1]), Student(1, [0,1]), Student(2, [0,1]), Student(3, [0,1])]
#    schools = [School(0, [0,1,2,3], 2), School(1, [3,2,1,0], 2)]
#    marriage = stableMarriage(students, schools)
#    test({schools[0]: students[:2], schools[1]: students[2:]}, marriage)
#    test(True, verifyStable(students, schools, marriage))

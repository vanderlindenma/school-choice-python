# Introduction

This tutorial describes how to use `DASolver.py` and `IASolver.py` in settings where
  * The total number of seats in all the schools is smaller than the total number of students, and some students end up unassigned.
  * The school choice procedure are [constrained](https://scholar.google.be/scholar?cluster=16748092764273030035&hl=en&as_sdt=0,43) in the sense that students can only rank a subset of schools.
  * Some schools are not acceptable to some students.

# Allowing for unassigned students

Per se, neither `DASolver.py` nor `IASolver.py` allow to have unassigned students. For the solvers to work, the total number of seats must be at least as large as the total number of students. 

The trick to allow for unassigned students is to create a special school, say `School(0,...,...)`. Being assigned to `School(0,...,...)` will be interpreted as being unassigned. 

1. Simply endow `School(0,...,...)` with an arbitrarilly large number of seats, larger than the total number of students. For instance, if you have 100 students, set `School(0,...,200)`. 
2. Add `School(0,...,...)` at the very **end** of every student's preferences.
3. Run `DASolver.py` of `IASolver.py`. Every student who end up assigned to school 0 has been rejected by every other school and should therefore be viewed as unassigned.

# [Constrained](https://scholar.google.be/scholar?cluster=16748092764273030035&hl=en&as_sdt=0,43) school choice problem

Again, neither `DASolver.py` nor `IASolver.py` are per se per se able to deal with constrained school choice problem. However, a trick similar to the one described in the former section allows to use `DASolver.py` nor `IASolver.py` to solve constrained school choice problems.

The trick is again to create a special school `School(0,...,...)`. Again, being assigned to `School(0,...,...)` will be interpreted as being unassigned. However, this time, you will use the location of `School(0,...,...)` in student's preferences in order to implement the desired constraint.

1. Endow `School(0,...,...)` with an arbitrarilly large number of seats, larger than the total number of students. For instance, if you have 100 students, set `School(0,...,200)`. 
2. Add `School(0,...,...)` in student's preferences depending on the constraint you want to implement. For instance, if you want to allow all students to only report the ranking over `x` school, place `School(0,...,...)` **right after the `x`-th school in every students' preference list**.
3. Run `DASolver.py` of `IASolver.py`. Every student who end up assigned to school 0 has been rejected by all of its first `x` ranked schools and should therefore be viewed as unassigned.

# Unacceptable Schools

A similar trick allows to model students for which some schools are *unacceptable*, meaning they prefer being unassigned to being assigned to some schools.

1. Endow `School(0,...,...)` with an arbitrarilly large number of seats, larger than the total number of students. For instance, if you have 100 students, set `School(0,...,200)`. 
2. Add `School(0,...,...)` in student's preferences **right after the students' last acceptable school**.
3. Run `DASolver.py` of `IASolver.py`. Every student who end up assigned to school 0 has been rejected by all of its acceptable schools and should therefore be viewed as unassigned.

# References

* Abdulkadiroglu, Atila, and Tayfun Sönmez. "School choice: A mechanism design approach." The American Economic Review 93.3 (2003): 729-747.
* Haeringer, Guillaume, and Flip Klijn. "Constrained school choice." Journal of Economic Theory 144.5 (2009): 1921-1947.

# school_choice_python

This repository contains Python code to compute assignments for school choice problems [Abdulkadiroglu and Sönmez (2003)](https://scholar.google.com/scholar?cluster=8496416599183251074&hl=en&as_sdt=0,43&as_vis=1) according to different assignment procedures. It uses and modigy code from Jeremy Kun, stable-marriage, (2014), GitHub repository, https://github.com/j2kun/stable-marriages, described in one of Jeremy's blog posts at http://jeremykun.com/2014/04/02/stable-marriages-and-designing-markets/.

# Features

The main scripts in this repository are

* `DASolver.py` : an almost exact copy of `stablemarriage.py` from `https://github.com/j2kun/stable-marriages` allowing to compute the outcome of a school choice problem in which schools have many seats available following the [Deferred-Acceptance](http://www.nber.org/papers/w13225) procedure. The only difference with `stablemarriage.py` is the naming of the class which has been altered to fit with the school choice context (classes `Suitor` and `Suited` become `Student` and `School`).
* `IASolver.py` : a variation on `stablemarriage.py` allowing to compute the outcome of a school choice problem using the Immediate Acceptance procedure, also know as [Boston Mechanism](https://scholar.google.com/scholar?cluster=8496416599183251074&hl=en&as_sdt=0,43&as_vis=1). Another difference with `stablemarriage.py` is the addition of a `verbose` option to the main function in  `IASolver.py` which prints a description of the steps followed by the Immediate Acceptance procedure as the procedure unfolds.
* `Extensions.md`: describes how to use `DASolver.py` and `IASolver.py` in settings where
  * The total number of seats in all the schools is smaller than the total number of students, and some students end up unassigned.
  * The school choice procedure are [constrained](https://scholar.google.be/scholar?cluster=16748092764273030035&hl=en&as_sdt=0,43) in the sense that students can only rank a subset of schools.




# References

* Abdulkadiroglu, Atila, and Tayfun Sönmez. "School choice: A mechanism design approach." The American Economic Review 93.3 (2003): 729-747.
* Haeringer, Guillaume, and Flip Klijn. "Constrained school choice." Journal of Economic Theory 144.5 (2009): 1921-1947.

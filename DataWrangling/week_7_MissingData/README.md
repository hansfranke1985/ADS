# Week 7: Missing Data


# Slides
1. [Lecture 1](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_7_MissingData/Slides/imputation_lecture_1.pdf)

# Assignments:
1. [Assigment 1](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_7_MissingData/week_7_Assigments/Assigment_1.md)
2. [Assigment 2]()
3. [Assigment 3]()

# Summary:

1.2 Concepts of MCAR, MAR and MNAR


If the probability of being missing is the same for all cases, then the data are said to be missing completely at random (MCAR).
-> cause for the missing data is unrelated to the data

If the probability of being missing is the same only within groups defined by the observed data, then the data are missing at random (MAR).  
-> MAR is more general and realistic than MCAR 
-> modern missing data models start with this assumption

If neither MCAR nor MAR holds, then we speak of missing not at random (MNAR). == NMAR (not missing at random)
An example of MNAR in public opinion research occurs if those with weaker opinions respond less often.
-> MNAR is the most complex case
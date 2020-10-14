# Week 7: Missing Data


# Slides
1. [Lecture 1](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_7_MissingData/Slides/imputation_lecture_1.pdf)
2. [Lecture 2](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_7_MissingData/Slides/imputation_lecture_2.pdf)

# Assignments:
1. [Assigment 1](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_7_MissingData/week_7_Assigments/Assigment_1.md)
2. [Assigment 2](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_7_MissingData/week_7_Assigments/Assigment_2.md)
3. [Assigment 3](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_7_MissingData/week_7_Assigments/Assigment_3.md)

# Summary:



## 1.2 Concepts of MCAR, MAR and MNAR

In his theory every data point has some likelihood of being missing. The process that governs these probabilities is called the missing data mechanism or response mechanism. The model for the process is called the missing data model or response model.

### MCAR
- If the probability of being missing is the same for all cases, then the data are said to be missing completely at random (MCAR). 
- cause for the missing data is unrelated to the data
- We may consequently ignore many of the complexities that arise because data are missing
- An example of MCAR is a weighing scale that ran out of batteries. Some of the data will be missing simply because of bad luck. Another example is when we take a random sample of a population, where each member has the same chance of being included in the sample. The (unobserved) data of members in the population that were not included in the sample are MCAR.

### MAR
If the probability of being missing is the same only within groups defined by the observed data, then the data are missing at random (MAR).  
-> MAR is more general and realistic than MCAR 
-> modern missing data models start with this assumption
- For example, when placed on a soft surface, a weighing scale may produce more missing values than when placed on a hard surface. Such data are thus not MCAR. If, however, we know surface type and if we can assume MCAR within the type of surface, then the data are MAR. Another example of MAR is when we take a sample from a population, where the probability to be included depends on some known property.

### MNAR
If neither MCAR nor MAR holds, then we speak of missing not at random (MNAR). == NMAR (not missing at random)
An example of MNAR in public opinion research occurs if those with weaker opinions respond less often.
-> MNAR is the most complex case
- MNAR means that the probability of being missing varies for reasons that are unknown to us.


# Solutions 

## Ad-hoc Solutions

## 1. Listwise Deletion

- delete the missing values before the analysis (na.omit = True or complete.cases() )
- may introduce aditional complexities in interpretation 
- Also known as complete case analysis (CCA)
- __Advantage__:
1. Convenience: If the data are MCAR, listwise deletion produces unbiased estimates of means, variances and regression weights. Under MCAR, listwise deletion produces standard errors and significance levels that are correct for the reduced subset of data, but that are often larger relative to all available data.

- __Disavantage__: 
1. Wasteful
2. If the data are not MCAR, listwise deletion can severely bias estimates of means, regression coefficients and correlations.
3. Listwise deletion can introduce inconsistencies in reporting. Since listwise deletion is automatically applied to the active set of variables, different analyses on the same data are often based on different subsamples.
4. can lead to nonsensical subsamples ( p.e change the timeline when deleting days)


## 2. Pair-wise Deletion
also known as available-case analysis, attempts to remedy the data loss problem of listwise deletion. The method calculates the means and (co)variances on all observed data. Thus, the mean of variable  X   is based on all cases with observed data on  X , the mean of variable  Y   uses all cases with observed Y  -values, and so on.


- __Advantage__:
1. Under MCAR, it produces consistent estimates of mean, correlations and covariances 

- __Disavantage__: 
1. First, the estimates can be biased if the data are not MCAR. Further, the covariance and/or correlation matrix may not be positive definite, which is requirement for most multivariate procedures.
2. Problems are generally more severe for highly correlated variables
3. requires numerical data that follow an approximate normal distribution


## 3. Mean Imputation

Mean imputation should perhaps only be used as a rapid fix when a handful of values are missing, and it should be avoided in general.

- __Advantage__:
1. We may use for categorical data
2. Fast and simple

- __Disavantage__: 
1.  Mean imputation distorts the distribution in several ways
2. Understimate the variance, disturb the relation between variables, bias any estimation (other than mean)
3. Bias the estimation of the mean when not MCAR

## 4. Regression Imputation

- __Advantage__:
1. 

- __Disavantage__: 
1. 
2. 

## 5.

- __Advantage__:
1. 

- __Disavantage__: 
1. 
2. 


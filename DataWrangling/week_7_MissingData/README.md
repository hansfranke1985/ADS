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

Regression imputation incorporates knowledge of other variables with the idea of producing smarter imputations. The first step involves building a model from the observed data. Predictions for the incomplete cases are then calculated under the fitted model, and serve as replacements for the missing data.

- __Advantage__:
1. regression weights are unbiased under MAR if the factors that influence the missingness are part of the regression model

- __Disavantage__: 
1. Imputing predicted values also has an effect on the correlation.
2. the ensemble of imputed values vary less than the observed values => variability of the imputed data is systematically underestimated
3. Note that this upward bias grows with the percent missing 
4. In reality however, regression imputation artificially strengthens the relations in the data
5. is a recipe for false positive and spurious relations.

## 5. Stochastic regression imputation
Stochastic regression imputation is a refinement of regression imputation attempts to address correlation bias by adding noise to the predictions.
This method first estimates the intercept, slope and residual variance under the linear model, then calculates the predicted value for each missing value, and adds a random draw from the residual to the prediction.

- __Advantage__:

1. A well-executed stochastic regression imputation preserves not only the regression weights, but also the correlation between variables
2. The main idea to draw from the residuals is very powerful, and forms the basis of more advanced imputation techniques

- __Disavantage__: 
1. Can lead to strange results 
2. 

## 6. LOCF and BOCF

Last observation carried forward (LOCF) and baseline observation carried forward (BOCF) are ad-hoc imputation methods for longitudinal data. The idea is to take the previous observed value as a replacement for the missing data. When multiple values are missing in succession, the method searches for the last observed value.

- __Advantage__:

1. LOCF is convenient because it generates a complete dataset

- __Disavantage__: 
1. Implausive imputation (time series for example...)
2. LOCF can yield biased estimates even under MCAR

## Indicator Method

Suppose that we want to fit a regression, but there are missing values in one of the explanatory variables. The indicator method (Miettinen 1985, 232) replaces each missing value by a zero and extends the regression model by the response indicator. The procedure is applied to each incomplete variable. The user analyzes the extended model instead of the original.

- __Advantage__:
1. is that the indicator method retains the full dataset.
2. it allows for systematic differences between the observed and the unobserved data by inclusion of the response indicator, and could be more efficient.

- __Disavantage__:
1. The conditions under which the indicator method works may not be met in practice. For example, the method does not allow for missing data in the outcome, and generally fails in observational data.

# Multiple Imputation

Multiple imputation creates  m >1 complete datasets. Each of these datasets is analyzed by standard analysis software. The m results are pooled into a final point estimate plus standard error by pooling rules

1. Multiple imputation creates several complete versions of the data by replacing the missing values by plausible data values
2. estimate the parameters of interest from each imputed dataset. This is typically done by applying the analytic method that we would have used had the data been complete.
3. The last step is to pool the  m   parameter estimates into one estimate, and to estimate its variance. The variance combines the conventional sampling variance (within-imputation variance) and the extra variance caused by the missing data extra variance caused by the missing data (between-imputation variance).

Under the appropriate conditions, the pooled estimates are unbiased and have the correct statistical properties.

Another reason to use multiple imputation is that it separates the solution of the missing data problem from the solution of the complete-data problem. The missing-data problem is solved first, the complete-data problem next. Though these phases are not completely independent, the answer to the scientifically interesting question is not obscured anymore by the missing data. The ability to separate the two phases simplifies statistical modeling, and hence contributes to a better insight into the phenomenon of scientific study.
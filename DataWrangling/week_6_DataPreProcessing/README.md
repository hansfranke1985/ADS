# Week 6: Data PREprocessing

# Slides
1. https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_6_DataPreProcessing/Slides/DataPreparationPartA.pdf
2. https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_6_DataPreProcessing/Slides/DataPreparationPartB.pdf

# Assigments:
1. https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_6_DataPreProcessing/Assignment/Week6_Assignments.ipynb
2. https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_6_DataPreProcessing/Assignment/Week6%20Data%20Preparation.ipynb 

# Summary:

## Data Quality

- Accuracy => data was recorded correctly
- Completeness => all relevant data was recorded
- Uniqueness => Entities are recorded once
- Timeliness => the data is keep up to date
- Consistency => the data agress with itself



# Outlier Detection

1. GLobal
2. Local

## Statistical Approaches

1. Parametrics:

- Minimal likelihood Formula (X - mean ) / std ==> if the value is 3x more than std, there is an outlier


2. Non-Parametrics:

- Histogram 
- Density 

## Distance Based Approaches

General Idea:  
- Judge a point based on the distance(s) to its neighbors
- Several variants proposed
Basic Assumption:  
- Normal data objects have a dense neighborhood
- Outliers are far apart from their neighbors, i.e., have a less dense neighborhood

## Density based approaches
General Idea:  
- Compare the density around a point with the density around its local neighbors
- The relative density of a point compared to its neighbors is computed as an outlier score
- Approaches essentially differ in how to estimate density
Basic Assumption:  
- The density around a normal data object is similar to the density around its neighbors
- The density around an outlier is considerably different to the density around its neighbors 

## Model base approches

- Data points that do not conform to the fitting model are potential
outliers

- linear reg / logistic reg / ...


# Review
- Data quality: accuracy, completeness, consistency, timeliness,believability, interpretability
- Data cleaning: e.g. missing/noisy values, outliers
- Data integration from multiple sources:
- Entity identification problem
- Remove redundancies
- Detect inconsistencies
- Data reduction
- Dimensionality reduction
- Numerosity reduction
- Data compression
- Data transformation and data discretization
- Normalization
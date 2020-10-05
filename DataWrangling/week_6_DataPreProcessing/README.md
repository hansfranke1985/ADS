# Week 6: Data PREprocessing

# Slides
1. https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_6_DataPreProcessing/Slides/DataPreparationPartA.pdf
2. https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_6_DataPreProcessing/Slides/DataPreparationPartB.pdf

# Assignments:
1. https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_6_DataPreProcessing/Assignment/Week6_Assignments.ipynb
2. https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_6_DataPreProcessing/Assignment/Week6%20Data%20Preparation.ipynb 

# Summary:

## Data Quality

- Accuracy => data was recorded correctly
- Completeness => all relevant data was recorded
- Uniqueness => Entities are recorded once
- Timeliness => the data is keep up to date
- Consistency => the data agrees with itself

# Outliers Detection

1. GLobal
2. Local

## Statistical Approaches

1. Parametric:

- Minimal likelihood Formula (X - mean ) / std ==> if the value is 3x more than std, there is an outlier


2. Non-Parametric:

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

## Model base approaches

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


Chapter 12 Outlier Detection 543
12.1 Outliers and Outlier Analysis 544
12.1.1 What Are Outliers? 544
12.1.2 Types of Outliers 545
12.1.3 Challenges of Outlier Detection 548
12.2 Outlier Detection Methods 549
12.2.1 Supervised, Semi-Supervised, and Unsupervised Methods 549
12.2.2 Statistical Methods, Proximity-Based Methods, and
Clustering-Based Methods 551
12.3 Statistical Approaches 553
12.3.1 Parametric Methods 553
12.3.2 Nonparametric Methods 558
12.4 Proximity-Based Approaches 560
12.4.1 Distance-Based Outlier Detection and a Nested Loop
Method 561
12.4.2 A Grid-Based Method 562
12.4.3 Density-Based Outlier Detection 564
12.5 Clustering-Based Approaches 567
12.6 Classification-Based Approaches 571
12.7 Mining Contextual and Collective Outliers 573
12.7.1 Transforming Contextual Outlier Detection to Conventional
Outlier Detection 573
HAN 03-toc-ix-xviii-9780123814791 2011/6/1 3:32 Page xviii #10
xviii Contents
12.7.2 Modeling Normal Behavior with Respect to Contexts 574
12.7.3 Mining Collective Outliers 575
12.8 Outlier Detection in High-Dimensional Data 576
12.8.1 Extending Conventional Outlier Detection 577
12.8.2 Finding Outliers in Subspaces 578
12.8.3 Modeling High-Dimensional Outliers 579


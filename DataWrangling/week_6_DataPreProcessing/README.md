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



# Outliers

### 12.1.1 What Are Outliers?
An outlier is a data object that deviates significantly from the rest of the objects, as if it were generated by a different mechanism. For ease of presentation within this chapter, we may refer to data objects that are not outliers as “normal” or expected data. Similarly, we may refer to outliers as “abnormal” data

Outliers are different from noisy data. As mentioned in Chapter 3, noise is a random error or variance in a measured variable. In general, noise is not interesting in
data analysis, including outlier detection. 

### 12.1.2 Types of Outliers 

- Global:  
In a given data set, a data object is a global outlierif it deviates significantly from the rest of the data set. Global outliers are sometimes called point anomalies, and are the simplest type of outliers. Most outlier detection methods are aimed at finding global outliers.  

- Context:  
In a given data set, a data object is a contextual outlier if it deviates significantly with respect to a specific context of the object. Contextual outliers are also known as
conditional outliers because they are conditional on the selected context 

- Collective:  
Given a data set, a subset of data objects forms a collective outlier if the objects as a whole deviate significantly from the entire data set. Importantly, the individual data
objects may not be outliers.


### 12.1.3 Challenges of Outlier Detection 

- Modeling normal objects and outliers effectively
- Application-specific outlier detection
- Handling noise in outlier detection
- Understandability

## 12.2 Outlier Detection Methods 

### supervised
1. definition: Supervised methods model data normality and abnormality. Domain experts examine and label a sample of the underlying data. Outlier detection can then be modeled as a classification problem

2. challenges:
- In summary, supervised methods of outlier detection must be careful in how they train and how they interpret classification rates due to the fact that outliers are rare in
comparison to the other data samples

### Semi-Supervised 
In many applications, although obtaining some labeled examples is feasible, the number of such labeled examples is often small. We may encounter cases where only a small set
of the normal and/or outlier objects are labeled, but most of the data are unlabeled. Semi-supervised outlier detection methods were developed to tackle such scenarios.

### Unsupervised Methods 
Unsupervised outlier detection methods make an implicit assumption: The normal objects are somewhat “clustered.” In other words, an unsupervised outlier detection
method expects that normal objects follow a pattern far more frequently than outliers. Normal objects do not have to fall into one group sharing high similarity. Instead, they
can form multiple groups, where each group has distinct features. However, an outlier is expected to occur far away in feature space from any of those groups of normal objects

## 12.2.2 Statistical Methods, Proximity-Based Methods, and Clustering-Based Methods 
According to the assumptions made, we can categorize outlier detection methods into three types: statistical methods, proximity-based methods, and clustering-based methods.

- Statistical methods (also known as model-based methods) make assumptions of data normality. They assume that normal data objects are generated by a statistical (stochastic) model, and that data not following the model are outliers.

- Proximity-based methods assume that an object is an outlier if the nearest neighbors of the object are far away in feature space, that is, the proximity of the object to its
neighbors significantly deviates from the proximity of most of the other objects to their neighbors in the same data set.

- Clustering-based methods assume that the normal data objects belong to large and dense clusters, whereas outliers belong to small or sparse clusters, or do not belong to
any clusters.
 

## 12.3 Statistical Approaches 553

In summary, statistical methods for outlier detection learn models from data to distinguish normal data objects from outliers. An advantage of using statistical methods is
that the outlier detection may be statistically justifiable. Of course, this is true only if the statistical assumption made about the underlying data meets the constraints in reality.

### 12.3.1 Parametric Methods 553

A parametric method assumes that the normal data objects are generated by a parametric distribution with parameter 2. The probability density function of the parametric distribution f (x,2) gives the probability that object x is generated by the distribution. The smaller this value, the more likely x is an outlier.  

#### 12.3.1.1 Univariate:
- Univariate outlier detection using maximum likelihood ( value => µ ± 3σ)	
- Boxplot => Any object that is more than 1.5 × IQR smaller than Q1 or 1.5 × IQR larger than Q3 is treated as an outlier

#### 12.3.1.2 Multivariate
- Multivariate outlier detection using the Mahalanobis distance
- Multivariate outlier detection using the χ2
-statistic

### 12.3.2 Nonparametric Methods 558
A nonparametric method does not assume an a priori statistical model. Instead, a nonparametric method tries to determine the model from the input data. Note that most nonparametric methods do not assume that the model is completely parameterfree. (Such an assumption would make learning the model from data almost mission impossible.) Instead, nonparametric methods often take the position that the number and nature of the parameters are flexible and not fixed in advance. Examples of nonparametric methods include histogram and kernel density estimation.

- Histogram;
1. define the bins, if the values fits in one bin is normal if not is an outlier. The probability of a object in one bin, be a outlier is 1/(%freq)
2. A drawback to using histograms as a nonparametric model for outlier detection is that it is hard to choose an appropriate bin size. On the one hand, if the bin size is set too
small, many normal objects may end up in empty or rare bins, and thus be misidentified as outliers. This leads to a high false positive rate and low precision. On the other hand,
if the bin size is set too high, outlier objects may infiltrate into some frequent bins and thus be “disguised” as normal. This leads to a high false negative rate and low recall

## 12.4 Proximity-Based Approaches 

There are two types of proximity-based outlier detection methods: distance-based and density-based methods. A distance-based outlier detection method consults the neighborhood of an object, which is defined by a given radius. An object is then considered an outlier if its neighborhood does not have enough other points. A density-based outlier detection method investigates the density of an object and that of its neighbors. Here, an object is identified as an outlier if its density is relatively much lower than that
of its neighbors.

### 12.4.1 Distance-Based Outlier Detection and a Nested Loop Method 
A representative method of proximity-based outlier detection uses the concept of distance-based outliers. For a set, D, of data objects to be analyzed, a user can specify a distance threshold, r, to define a reasonable neighborhood of an object. For each object, o, we can examine the number of other objects in the r-neighborhood of o. If most of the objects in D are far from o, that is, not in the r-neighborhood of o, then o can be regarded as an outlier.

### 12.4.2 A Grid-Based Method 
CELL is a grid-based method for distance-based outlier detection. In this method, the data space is partitioned into a multidimensional grid, where each cell is a hypercube
that has a diagonal of length r 2 , where r is a distance threshold parameter. In other words, if there are l dimensions, the length of each edge of a cell is r / 2√2 .


### 12.4.3 Density-Based Outlier Detection
“How can we formulate the local outliers as illustrated in Example 12.14?” The critical idea here is that we need to compare the density around an object with the density
around its local neighbors. The basic assumption of density-based outlier detection methods is that the density around a nonoutlier object is similar to the density around
its neighbors, while the density around an outlier object is significantly different from the density around its neighbors

## 12.5 Clustering-Based Approaches 
Clustering-based approaches detect outliers by examining the relationship between objects and clusters. Intuitively, an outlier is an object that belongs to a small and remote cluster, or does not belong to any cluster.

- Detecting outliers as objects that do not belong to any cluster
- Clustering-based outlier detection using distance to the closest cluster
- Intrusion detection by clustering-based outlier detection

Note that each of the approaches we have seen so far detects only individual objects as outliers because they compare objects one at a time against clusters in the data set.
However, in a large data set, some outliers may be similar and form a small cluster. In intrusion detection, for example, hackers who use similar tactics to attack a system may
form a cluster. The approaches discussed so far may be deceived by such outliers. To overcome this problem, a third approach to cluster-based outlier detection identifies small or sparse clusters and declares the objects in those clusters to be outliers as well. An example of this approach is the FindCBLOF algorithm

- Detecting outliers in small clusters

__STRENGS__ Clustering-based outlier detection methods have the following advantages. First, they can detect outliers without requiring any labeled data, that is, in an unsupervised ay. They work for many data types. Clusters can be regarded as summaries of the data. Once the clusters are obtained, clustering-based methods need only compare any object against the clusters to determine whether the object is an outlier. This process is typically fast because the number of clusters is usually small compared to the total number of
objects.

A __WEAKNESS__ of clustering-based outlier detection is its effectiveness, which depends highly on the clustering method used. Such methods may not be optimized for outlier
detection. Clustering methods are often costly for large data sets, which can serve as a bottleneck.

## 12.6 Classification-Based Approaches 

Outlier detection can be treated as a classification problem if a training data set with class labels is available. The general idea of classification-based outlier detection methods is to train a classification model that can distinguish normal data from outliers.

**drawback** the number of normal samples likely far exceeds the number of outlier samples. This imbalance, where the number of outlier samples may be insufficient, can prevent us from building an accurate classifier.

To **overcome** this challenge, classification-based outlier detection methods often use a one-class model. That is, a classifier is built to describe only the normal class. Any samples that do not belong to the normal class are regarded as outliers.

Classification-based methods can incorporate human domain knowledge into the detection process by learning from the labeled samples. Once the classification model is constructed, the outlier detection process is fast. It only needs to compare the objects to be examined against the model learned from the training data. The quality of classification-based methods heavily depends on the availability and quality of the training set. In many applications, it is difficult to obtain representative and high-quality training data, which limits the applicability of classification-based methods.


## 12.7 Mining Contextual and Collective Outliers 

An object in a given data set is a contextual outlier (or conditional outlier) if it deviates significantly with respect to a specific context of the object (Section 12.1). The
context is defined using contextual attributes. These depend heavily on the application, and are often provided by users as part of the contextual outlier detection task.
Contextual attributes can include spatial attributes, time, network locations, and sophisticated structured attributes. In addition, behavioral attributes define characteristics of
the object, and are used to evaluate whether the object is an outlier in the context to
which it belongs.

- 12.7.1 Transforming Contextual Outlier Detection to Conventional Outlier Detection 

- 12.7.2 Modeling Normal Behavior with Respect to Contexts 

- 12.7.3 Mining Collective Outliers 

## 12.8 Outlier Detection in High-Dimensional Data 

- 12.8.1 Extending Conventional Outlier Detection 

- 12.8.2 Finding Outliers in Subspaces 

- 12.8.3 Modeling High-Dimensional Outliers 


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




# 3. Data Preprocessing 

## 3.1 Data Preprocessing: An Overview 84

### 3.1.1 Data Quality: Why Preprocess the Data? 

Data quality: checking the data from multiple perspectives
- Accuracy: The data was recorded correctly.
- Completeness: All relevant data was recorded.
- Uniqueness: Entities are recorded once.
- Timeliness: The data is kept up to date. Special problems in federated data: time consistency.
- Consistency: The data agrees with itself.

### 3.1.2 Major Tasks in Data Preprocessing 85

- **Data cleaning** routines work to “clean” the data by filling in missing values, smoothing noisy data, identifying or removing outliers, and resolving inconsistencies. 
- ...This would involve integrating multiple databases, data cubes, or files (i.e., **data integration**). Yet some attributes representing a given concept may have different names in different databases, causing inconsistencies and redundancies.
- **Data reduction** obtains a reduced representation of the data set that is much smaller in volume, yet produces the same (or almost the same) analytical results. Data reduction
strategies include **dimensionality reduction** and **numerosity reduction**
1. **In dimensionality reduction**, data encoding schemes are applied so as to obtain a reduced or “compressed” representation of the original data. Examples include data
compression techniques (e.g., *wavelet transforms and principal components analysis*), attribute subset selection (e.g., removing irrelevant attributes), and attribute construction
(e.g., where a small set of more useful attributes is derived from the original set).
2. **In numerosity reduction**, the data are replaced by alternative, smaller representations using parametric models (e.g., *regression or log-linear models*) or nonparametric
models (e.g., *histograms, clusters, sampling, or data aggregation*). 

-  Normalization, data discretization, and concept hierarchy generation are forms of **data transformation**.

## 3.2 Data Cleaning 88

### 3.2.1 Missing Values 88

- Ignore the tuple
- Use a global constant
- Use a measure of central tendency (e.g. mean or median) by each tuple or by class (e.g mean of females / male ages)
- Use the most probable value ( e.g with regression, decision trees)

### 3.2.2 Noisy Data 89

“What is noise?” Noise is a random error or variance in a measured variable

**Remove Noise**

1. Binning 
2. Regression
3. Outliers Analysis
4. Clustering

### 3.2.3 Data Cleaning as a Process 91

“So, how can we proceed with discrepancy detection?” As a starting point, use any knowledge you may already have regarding properties of the data. Such knowledge or “data about data” is referred to as metadata.  


## 3.3 Data Integration 93

### 3.3.1 Entity Identification Problem 94

### 3.3.2 Redundancy and Correlation Analysis 94

1. X2 for nominal data 
2. Correlation for numeric data
3. Covariance for numeric data 

### 3.3.3 Tuple Duplication 98

### 3.3.4 Data Value Conflict Detection and Resolution 99

## 3.4 Data Reduction 99

### 3.4.1 Overview of Data Reduction Strategies 99

### 3.4.2 Wavelet Transforms 100

The **discrete wavelet transform (DWT)** is a linear signal processing technique that, when applied to a data vector X, transforms it to a numerically different vector, X', of wavelet coefficients. The two vectors are of the same length.
*“How can this technique be useful for data reduction if the wavelet transformed data are of the same length as the original data?”* The usefulness lies in the fact that the wavelet
transformed data can be truncated. A compressed approximation of the data can be retained by storing only a small fraction of the strongest of the wavelet coefficients.

### 3.4.3 Principal Components Analysis 102

Suppose that the data to be reduced consist of tuples or data vectors described by n attributes or dimensions. **Principal components analysis (PCA)**; also called the Karhunen-Loeve, or K-L, method) searches for k n-dimensional orthogonal vectors that can best be used to represent the data, where k ≤ n. The original data are thus projected onto a much smaller space, resulting in dimensionality reduction. Unlike attribute subset selection (Section 3.4.4), which reduces the attribute set size by retaining a subset of the initial set of attributes, PCA “combines” the essence of attributes by creating an alternative, smaller set of variables. 

- Steps:
1. Normalize the data
2. PCA computes k orthonormal vectors
3. principal components are sorted in order of decreasing "significance"
4. Eliminate the least significance => decrease size / number of components 

### 3.4.4 Attribute Subset Selection 103

**Attribute subset selection** reduces the data set size by removing irrelevant or redundant attributes (or dimensions). The goal of attribute subset selection is to find a minimum set of attributes such that the resulting probability distribution of the data classes is as close as possible to the original distribution obtained using all attributes. Mining on a reduced set of attributes has an additional benefit: It reduces the number of attributes appearing in the discovered patterns, helping to make the patterns easier to understand.

1. Stepwise forward selection
2. Setpwise backward elimination 
3. Combination of both
4. Decision Tree induction

### 3.4.5 Regression and Log-Linear Models: Parametric Data Reduction 105

Regression and log-linear models can both be used on sparse data, although their application may be limited. While both methods can handle skewed data, regression does exceptionally well. Regression can be computationally intensive when applied to high-dimensional data, whereas log-linear models show good scalability for up to 10 or so dimensions.


### 3.4.6 Histograms 106

Histograms are highly effective at approximating both sparse and dense data, as well as highly skewed and uniform data.

### 3.4.7 Clustering 108

In data reduction, the cluster representations of the data are used to replace the actual data. The effectiveness of this technique depends on the data’s nature. It is much more
effective for data that can be organized into distinct clusters than for smeared data.

### 3.4.8 Sampling 108

Sampling can be used as a data reduction technique because it allows a large data set to be represented by a much smaller random data sample (or subset).

1. Simple random sample without replacement
2. Simple random sample with replacement
3. Cluster Sample

When applied to data reduction, sampling is most commonly used to estimate the answer to an aggregate query. It is possible (using the central limit theorem) to determine a sufficient sample size for estimating a given function within a specified degree of error. This sample size, s, may be extremely small in comparison to N. Sampling is
a natural choice for the progressive refinement of a reduced data set. Such a set can be further refined by simply increasing the sample size.


### 3.4.9 Data Cube Aggregation 110

Aggregates values. E.g => 12 months to a year data!

## 3.5 Data Transformation and Data Discretization 111

### 3.5.1 Data Transformation Strategies Overview 112

1. Smoothing, which works to remove noise from the data. Techniques include binning, regression, and clustering.
2. Attribute construction (or feature construction), where new attributes are constructed and added from the given set of attributes to help the mining process.
3. Aggregation, where summary or aggregation operations are applied to the data. For example, the daily sales data may be aggregated so as to compute monthly and annual
total amounts. This step is typically used in constructing a data cube for data analysis at multiple abstraction levels.
4. Normalization, where the attribute data are scaled so as to fall within a smaller range, such as −1.0 to 1.0, or 0.0 to 1.0.
5. Discretization, where the raw values of a numeric attribute (e.g., age) are replaced by interval labels (e.g., 0–10, 11–20, etc.) or conceptual labels (e.g., youth, adult, senior). The labels, in turn, can be recursively organized into higher-level concepts, resulting in a concept hierarchy for the numeric attribute. Figure 3.12 shows a concept hierarchy for the attribute price. More than one concept hierarchy can be defined for the same attribute to accommodate the needs of various users.
6. Concept hierarchy generation for nominal data, where attributes such as street can be generalized to higher-level concepts, like city or country. Many hierarchies for
nominal attributes are implicit within the database schema and can be automatically
defined at the schema definition level.

### 3.5.2 Data Transformation by Normalization 113

**Min-max normalization** performs a linear transformation on the original data. Suppose that minA and maxA are the minimum and maximum values of an attribute, A. Min-max normalization maps a value, vi, of A to v0i in the range [new minA,new maxA] by computing

- vi" = vi - minA / (maxA - minA) * (nex_maxA - new_minA) + new_minA

In **z-score normalization** (or zero-mean normalization), the values for an attribute, A, are normalized based on the mean (i.e., average) and standard deviation of A. A value,
vi, of A is normalized to vi' by computing

- vi'= vi - mean(A) / std(A) 

Normalization by **decimal scaling** normalizes by moving the decimal point of values of attribute A. The number of decimal points moved depends on the maximum absolute value of A.


### 3.5.3 Discretization by Binning 115

Binning does not use class information and is therefore an unsupervised discretization technique. It is sensitive to the user-specified number of bins, as well as the presence
of outliers.

### 3.5.4 Discretization by Histogram Analysis 115

### 3.5.5 Discretization by Cluster, Decision Tree, and Correlation Analyses 116

### 3.5.6 Concept Hierarchy Generation for Nominal Data 117

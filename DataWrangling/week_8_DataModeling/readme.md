

# Week 8: Data Modeling -> Regression and Classification

# Slides
1. [Lecture 1](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_8_DataModeling/Slides/RegressionClassificationEvaluation.pdf)

# Assignments:
1. [Assigment 1](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_8_DataModeling/Assigments/Week8_Assigments.ipynb)
2. [Tutorial](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_8_DataModeling/Tutorial/Week08_Regression_Classification_Evaluation_T1.ipynb)

# Summary:

# Classification Algorithms:

## Logistic Regression

1. Advantages
- Probabilistic approach, gives informations about statistical significance of features 
2. Disadvantages
- The Logistic Regression Assumptions	

## Naive Bayes
1. Advantages
- Easy to implement
- Good results obtained in most of the cases
2. Disadvantages
- Assumption: class conditional independence, therefore loss of accuracy
- Practically, dependencies exist among variables E.g., Hospitals: patients: Profile: age, family history, etc. Symptoms: fever, cough etc., Disease: lung cancer, diabetes, etc.
- Dependencies among these cannot be modeled by Naïve Bayes Classifier


## Nearest Neighbors

1. Advantages
- Robust to noisy data by averaging k-nearest neighbors unlike eager learners such as decision tree induction and rule-based systems
- simple to understand


2. Disavantages
- k-NN classifiers are lazy learners
- It does not build models explicitly
- Classifying unknown records are relatively expensive
- need to chose apropriate number of k:
	- If to small => noise
	- if to large => may include points to other classes

## Decision Tree

How to chose nodes:
- Information Gain ( is biased towards attributes with a large number of values)
- Gain Ratio (normalization to information gain) | tend to prefer unbalanced splits in which one partition is much smaller
- Gini Index (that provides the smallest 𝑔𝑖𝑛𝑖𝐴𝑖 (𝐷) (or the largest reduction in impurity) is chosen to split the node ) | Biased towards multivaluated attributes | Difficulties when number of classes is larger | Tends to favor tests that results in equal-sized partitions and purity

Aproaches to reduce Overfitting:
- PREpruning
- POSTpruning

1. Advantages
- Relatively faster learning speed (than other classification methods)
- Convertible to simple and easy to understand classification rules
- Can use SQL queries for accessing databases
- Comparable classification accuracy with other methods
- No need for feature scalling
- both linear and nonlinear problems

2. Disavantages
- poor results on small datasets
- overfitting can easily occur

## Rule-Based Classification

1. Advantages

2. Disavantages

## Neural Networks

1. Advantages
- High tolerance to noisy data
- Ability to classify untrained patterns
- Well-suited for continuous-valued inputs and outputs
- Successful on an array of real-world data, e.g., hand-written letters
- Algorithms are inherently parallel
- Techniques have recently been developed for the extraction of rules from trained neural networks

2. Disavantages
- Long training time
- Require a number of parameters typically best determined empirically, e.g., the network topology or “structure.”
- Poor interpretability: Difficult to interpret the symbolic meaning behind the learned weights and of “hidden units” in the network

## SVM - Support Vector Machines

Find linear hyperplane (decision boundary) that will separate the data that maximizes the margin . Support vector are the points that the margin is pushed up against

1. Advantages
- Effective on High Dimensional Data
- Nice Generalization properties

2. Disavantages
- Hard to learn (learn in batch -> quadratic programming)


# Evaluating the models

1. Hold-out
2. CrossValidation

** Credits: Machine-Learning A-Z (Udemy)

1. ![Regression](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_8_DataModeling/Regression_Pros_Cons.pdf)


2. ![Classification](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_8_DataModeling/Classification_Pros_Cons.pdf)

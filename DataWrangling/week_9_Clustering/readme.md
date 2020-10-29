

# Week 9: Data Modeling -> Clustering

# Slides
1. [Lecture 1](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_9_Clustering/Lectures/clustering_lecture_1.pdf)
2. [Lecture 2] (https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_9_Clustering/Lectures/clustering_lecture_2.pdf)

# Assignments:
1. [Assigment 1](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_9_Clustering/Practicals/Week_9_Clustering/Week9_assigment_1.md)
2. [Assigment 2](https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_9_Clustering/Practicals/Week_9_Clustering/Week9_assigment_2.md)


# Summary:

# Kmeans

1) random assign a class to each point

2) repeat until the algorithm dosent change

2.1) Assign a centroid to each cluster

2.2) Assign each point to the closest centroid (euclidean distance)


Local minium in each group. The function is not convex, so no global optimum

# Hierarchical Clustering

1) Start each point in its own cluster

2) Identify the closets two clusters and merge then

3) Repeat

4) End when all points are in a single cluster

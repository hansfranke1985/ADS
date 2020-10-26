R Notebook
================

    library(tidyverse)

    ## -- Attaching packages ------------------------------------------- tidyverse 1.3.0 --

    ## v ggplot2 3.3.2     v purrr   0.3.4
    ## v tibble  3.0.3     v dplyr   1.0.2
    ## v tidyr   1.1.2     v stringr 1.4.0
    ## v readr   1.3.1     v forcats 0.5.0

    ## -- Conflicts ---------------------------------------------- tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

    distances <- dist(faithful, method = "euclidean")
    result <- hclust(distances, method = "average")

    #install.packages("ggdendro")
    library(ggdendro)

    ## Warning: package 'ggdendro' was built under R version 4.0.3

    ggdendrogram(result)

![](Week9_assigment_1_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->

    df_kmeans <- kmeans(faithful, centers=2)
    str(df_kmeans)

    ## List of 9
    ##  $ cluster     : Named int [1:272] 1 2 1 2 1 2 1 1 2 1 ...
    ##   ..- attr(*, "names")= chr [1:272] "1" "2" "3" "4" ...
    ##  $ centers     : num [1:2, 1:2] 4.3 2.09 80.28 54.75
    ##   ..- attr(*, "dimnames")=List of 2
    ##   .. ..$ : chr [1:2] "1" "2"
    ##   .. ..$ : chr [1:2] "eruptions" "waiting"
    ##  $ totss       : num 50440
    ##  $ withinss    : num [1:2] 5446 3456
    ##  $ tot.withinss: num 8902
    ##  $ betweenss   : num 41538
    ##  $ size        : int [1:2] 172 100
    ##  $ iter        : int 1
    ##  $ ifault      : int 0
    ##  - attr(*, "class")= chr "kmeans"

    df_kmeans$cluster

    ##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20 
    ##   1   2   1   2   1   2   1   1   2   1   2   1   1   2   1   2   2   1   2   1 
    ##  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40 
    ##   2   2   1   1   1   1   2   1   1   1   1   1   2   1   1   2   2   1   2   1 
    ##  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60 
    ##   1   2   1   2   1   1   2   2   1   2   1   1   2   1   2   1   1   2   1   1 
    ##  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80 
    ##   2   1   2   1   2   1   1   1   2   1   1   2   1   1   2   1   2   1   1   1 
    ##  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99 100 
    ##   1   1   1   2   1   1   1   1   2   1   2   1   2   1   2   1   1   1   2   1 
    ## 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 
    ##   2   1   2   1   1   2   1   2   1   1   1   2   1   1   2   1   2   1   2   1 
    ## 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 
    ##   2   1   1   2   1   1   2   1   2   1   2   1   2   1   2   1   2   1   2   1 
    ## 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 
    ##   1   2   1   1   1   2   1   2   1   2   1   1   2   1   1   1   1   1   2   1 
    ## 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 
    ##   2   1   2   1   2   1   2   1   2   1   2   2   1   1   1   1   1   2   1   1 
    ## 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 
    ##   2   1   1   1   2   1   1   2   1   2   1   2   1   1   1   1   1   1   2   1 
    ## 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 
    ##   2   1   1   2   1   2   1   1   2   1   1   1   2   1   2   1   2   1   2   1 
    ## 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 
    ##   2   1   2   1   1   1   1   1   1   1   1   2   1   2   1   2   2   1   1   2 
    ## 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 
    ##   1   2   1   2   1   1   2   1   2   1   2   1   1   1   1   1   1   1   2   1 
    ## 261 262 263 264 265 266 267 268 269 270 271 272 
    ##   1   1   2   1   2   2   1   1   2   1   2   1

    df_kmeans$centers

    ##   eruptions  waiting
    ## 1   4.29793 80.28488
    ## 2   2.09433 54.75000

    #install.packages("factoextra")
    library("factoextra")

    ## Warning: package 'factoextra' was built under R version 4.0.3

    ## Welcome! Want to learn more? See two factoextra-related books at https://goo.gl/ve3WBa

    fviz_cluster(df_kmeans, data = faithful)

![](Week9_assigment_1_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->
\#\# Look for the best number of clusters

    fviz_nbclust(faithful, FUN=hcut, method = "wss") #elbow method

![](Week9_assigment_1_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

    fviz_nbclust(faithful, FUN=hcut, method = "silhouette") #silhouette

![](Week9_assigment_1_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

    library(MASS) # make sure to load mass before tidyverse to avoid conflicts!

    ## 
    ## Attaching package: 'MASS'

    ## The following object is masked from 'package:dplyr':
    ## 
    ##     select

    library(tidyverse)
    #install.packages("patchwork")
    library(patchwork)

    ## Warning: package 'patchwork' was built under R version 4.0.3

    ## 
    ## Attaching package: 'patchwork'

    ## The following object is masked from 'package:MASS':
    ## 
    ##     area

    library(ggdendro)

Hierarchical and k-means clustering Introduction
================================================

We use the following packages:

library(MASS) \# make sure to load mass before tidyverse to avoid
conflicts! library(tidyverse) library(patchwork) library(ggdendro)

In this practical, we will apply hierarchical and k-means clustering to
two synthetic datasets. The data can be generated by running the code
below.

Try to understand what is happening as you run each line of the code
below

    # randomly generate bivariate normal data
    set.seed(123)
    sigma      <- matrix(c(1, .5, .5, 1), 2, 2)
    sim_matrix <- mvrnorm(n = 100, mu = c(5, 5), Sigma = sigma)
    colnames(sim_matrix) <- c("x1", "x2")

    # change to a data frame (tibble) and add a cluster label column
    sim_df <- 
      sim_matrix %>% 
      as_tibble() %>%
      mutate(class = sample(c("A", "B", "C"), size = 100, replace = TRUE))

    # Move the clusters to generate separation
    sim_df_small <- 
      sim_df %>%
      mutate(x2 = case_when(class == "A" ~ x2 + .5,
                            class == "B" ~ x2 - .5,
                            class == "C" ~ x2 + .5),
             x1 = case_when(class == "A" ~ x1 - .5,
                            class == "B" ~ x1 - 0,
                            class == "C" ~ x1 + .5))
    sim_df_large <- 
      sim_df %>%
      mutate(x2 = case_when(class == "A" ~ x2 + 2.5,
                            class == "B" ~ x2 - 2.5,
                            class == "C" ~ x2 + 2.5),
             x1 = case_when(class == "A" ~ x1 - 2.5,
                            class == "B" ~ x1 - 0,
                            class == "C" ~ x1 + 2.5))

Prepare two unsupervised datasets by removing the class feature

For each of these datasets, create a scatterplot. Combine the two plots
into a single frame (look up the “patchwork” package to see how to do
this!) What is the difference between the two datasets?

Hierarchical clustering
=======================

Run a hierarchical clustering on these datasets and display the result
as dendrograms. Use euclidian distances and the complete agglomeration
method. Make sure the two plots have the same y-scale. What is the
difference between the dendrograms? (Hint: functions you’ll need are
hclust, ggdendrogram, and ylim)

For the dataset with small differences, also run a complete
agglomeration hierarchical cluster with manhattan distance.

Use the cutree() function to obtain the cluster assignments for three
clusters and compare the cluster assignments to the 3-cluster euclidian
solution. Do this comparison by creating two scatter plots with cluster
assignment mapped to the colour aesthetic. Which difference do you see?

K-means clustering
==================

Create k-means clusterings with 2, 3, 4, and 6 classes on the large
difference data. Again, create coloured scatter plots for these
clusterings.

Do the same thing again a few times. Do you see the same results every
time? where do you see differences?

Find a way online to perform bootstrap stability assessment for the 3
and 6-cluster solutions.

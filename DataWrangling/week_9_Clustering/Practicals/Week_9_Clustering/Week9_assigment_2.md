Week9\_Assigment 2
================
Hans Franke

``` r
library(MASS) # make sure to load mass before tidyverse to avoid conflicts!
library(tidyverse)
```

    ## -- Attaching packages ------------------------------------------ tidyverse 1.3.0 --

    ## v ggplot2 3.3.2     v purrr   0.3.4
    ## v tibble  3.0.3     v dplyr   1.0.2
    ## v tidyr   1.1.2     v stringr 1.4.0
    ## v readr   1.3.1     v forcats 0.5.0

    ## -- Conflicts --------------------------------------------- tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()
    ## x dplyr::select() masks MASS::select()

``` r
#install.packages("patchwork")
library(patchwork)
```

    ## Warning: package 'patchwork' was built under R version 4.0.3

    ## 
    ## Attaching package: 'patchwork'

    ## The following object is masked from 'package:MASS':
    ## 
    ##     area

``` r
library(ggdendro)
```

    ## Warning: package 'ggdendro' was built under R version 4.0.3

``` r
library(mclust)
```

    ## Warning: package 'mclust' was built under R version 4.0.3

    ## Package 'mclust' version 5.4.6
    ## Type 'citation("mclust")' for citing this R package in publications.

    ## 
    ## Attaching package: 'mclust'

    ## The following object is masked from 'package:purrr':
    ## 
    ##     map

In this practical, we will apply model-based clustering on a dataset of
bank note measurements. The data is built into the mclust package and
can be loaded as a tibble by running the following code:

``` r
df <- as_tibble(banknote)
head(df)
```

    ## # A tibble: 6 x 7
    ##   Status  Length  Left Right Bottom   Top Diagonal
    ##   <fct>    <dbl> <dbl> <dbl>  <dbl> <dbl>    <dbl>
    ## 1 genuine   215.  131   131.    9     9.7     141 
    ## 2 genuine   215.  130.  130.    8.1   9.5     142.
    ## 3 genuine   215.  130.  130.    8.7   9.6     142.
    ## 4 genuine   215.  130.  130.    7.5  10.4     142 
    ## 5 genuine   215   130.  130.   10.4   7.7     142.
    ## 6 genuine   216.  131.  130.    9    10.1     141.

# Data exploration

Read the help file of the banknote dataset to understand what it’s all
about.

Create a scatter plot of the left (x-axis) and right (y-axis)
measurements on the dataset. Map the Status column to colour. Jitter the
points to avoid overplotting. Are the classes easy to distinguish based
on these features?

From now on, we will assume that we don’t have the labels. Remove the
Status column from the dataset.

Create density plots for all columns in the dataset. Which single
feature is likely to be best for clustering?

# Univariate model-based clustering

Use Mclust to perform model-based clustering with 2 clusters on the
feature you chose. Assume equal variances. Name the model object
fit\_E\_2. What are the means and variances of the clusters?

Use the formula from the slides and the model’s log-likelihood
(fit\_E\_2\(loglik) to compute the BIC for this model. Compare it to the BIC stored in the model object (fit_E_2\)bic).
Explain how many parameters (m) you used and which parameters these are.

Plot the model-implied density using the plot() function. Afterwards,
add rug marks of the original data to the plot using the rug() function
from the base graphics system.

Use Mclust to perform model-based clustering with 2 clusters on this
feature again, but now assume unequal variances. Name the model object
fit\_V\_2. What are the means and variances of the clusters? Plot the
density again and note the differences.

How many parameters does this model have? Name them.

According to the deviance, which model fits better?

According to the BIC, which model is better?

# Multivariate model-based clustering

We will now use all available information in the dataset to cluster the
observations.

Use Mclust with all 6 features to perform clustering. Allow all model
types (shapes), and from 1 to 9 potential clusters. What is the optimal
model based on the BIC?

How many mean parameters does this model have?

Run a 2-component VVV model on this data. Create a matrix of bivariate
contour (“density”) plots using the plot() function. Which features
provide good component separation? Which do not?

Create a scatter plot just like the first scatter plot in this tutorial,
but map the estimated class assignments to the colour aesthetic. Map the
uncertainty (part of the fitted model list) to the size aesthetic, such
that larger points indicate more uncertain class assignments. Jitter the
points to avoid overplotting. What do you notice about the uncertainty?

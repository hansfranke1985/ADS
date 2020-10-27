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

``` r
ggplot(df, aes(Left, Right, color=Status))+geom_jitter()
```

![](Week9_assigment_2_files/figure-gfm/scatterplot%20left%20x%20right-1.png)<!-- -->

``` r
#We can see there is overlaping in classes considering only this 2 features, so no clear distinguishing
```

From now on, we will assume that we don’t have the labels. Remove the
Status column from the dataset.

``` r
df_unlabel <- df[,2:7]
head(df_unlabel)
```

    ## # A tibble: 6 x 6
    ##   Length  Left Right Bottom   Top Diagonal
    ##    <dbl> <dbl> <dbl>  <dbl> <dbl>    <dbl>
    ## 1   215.  131   131.    9     9.7     141 
    ## 2   215.  130.  130.    8.1   9.5     142.
    ## 3   215.  130.  130.    8.7   9.6     142.
    ## 4   215.  130.  130.    7.5  10.4     142 
    ## 5   215   130.  130.   10.4   7.7     142.
    ## 6   216.  131.  130.    9    10.1     141.

Create density plots for all columns in the dataset. Which single
feature is likely to be best for clustering?

``` r
(ggplot(df_unlabel )+
     geom_density(aes(x=Length)) ) +

        (ggplot(df_unlabel )+
          geom_density(aes(x=Left)) ) +
  
            (ggplot(df_unlabel )+
                geom_density(aes(x=Right)) ) +
  
              (ggplot(df_unlabel )+
                geom_density(aes(x=Bottom)) ) +
  
                (ggplot(df_unlabel )+
                geom_density(aes(x=Top)) ) +
  
                        (ggplot(df_unlabel )+
                geom_density(aes(x=Diagonal)) ) 
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-1-1.png)<!-- -->

``` r
#Diagonal seems to have a non-normal distribution, so this can explain Clusters better, probably there is two normal distributions (clusters)
```

``` r
(ggplot(df )+
     geom_density(aes(x=Diagonal, color=Status)) ) + theme_minimal()
```

![](Week9_assigment_2_files/figure-gfm/check%20feature-1.png)<!-- -->

``` r
#As we imagine, indeed there is 2 normal distribution explaining the classes
```

``` r
(ggplot(df )+
     geom_density(aes(x=Length, color=Status)) ) + theme_minimal()
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->

# Univariate model-based clustering

``` r
class <- df_unlabel[,6]
fit <- Mclust(class)
summary(fit)
```

    ## ---------------------------------------------------- 
    ## Gaussian finite mixture model fitted by EM algorithm 
    ## ---------------------------------------------------- 
    ## 
    ## Mclust E (univariate, equal variance) model with 3 components: 
    ## 
    ##  log-likelihood   n df       BIC       ICL
    ##       -258.4995 200  6 -548.7889 -556.8668
    ## 
    ## Clustering table:
    ##   1   2   3 
    ##  12  88 100

``` r
plot(fit, what="BIC")
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->

``` r
#fit_E_2$parameters
```

Use Mclust to perform model-based clustering with 2 clusters on the
feature you chose. Assume equal variances. Name the model object
fit\_E\_2. What are the means and variances of the clusters?

``` r
class <- df_unlabel[,6]
fit_E_2 <- Mclust(class, modelNames = c("E"), G=2)
summary(fit_E_2)
```

    ## ---------------------------------------------------- 
    ## Gaussian finite mixture model fitted by EM algorithm 
    ## ---------------------------------------------------- 
    ## 
    ## Mclust E (univariate, equal variance) model with 2 components: 
    ## 
    ##  log-likelihood   n df       BIC       ICL
    ##       -274.1367 200  4 -569.4667 -574.2533
    ## 
    ## Clustering table:
    ##   1   2 
    ## 100 100

``` r
fit_E_2$parameters
```

    ## $pro
    ## [1] 0.5003518 0.4996482
    ## 
    ## $mean
    ##        1        2 
    ## 139.4464 141.5221 
    ## 
    ## $variance
    ## $variance$modelName
    ## [1] "E"
    ## 
    ## $variance$d
    ## [1] 1
    ## 
    ## $variance$G
    ## [1] 2
    ## 
    ## $variance$sigmasq
    ## [1] 0.244004
    ## 
    ## 
    ## $Vinv
    ## NULL

Use the formula from the slides and the model’s log-likelihood
(fit\_E\_2\(loglik) to compute the BIC for this model. Compare it to the BIC stored in the model object (fit_E_2\)bic).
Explain how many parameters (m) you used and which parameters these are.

``` r
#stored
fit_E_2$bic
```

    ## [1] -569.4667

``` r
#m = number of parameters( m = ( k - 1) + k*p + K*p  + K*( (p(p-1))/2) )
#k = 2 (2 clusters)
#p = 1 (variable)
(2-1) + 2*1 +2*1 + 2*(1*(1-1)/2)
```

    ## [1] 5

``` r
#the parameters are (variance in each cluster = 2)
#from book (we can see 5 parameters)
fit_E_2$loglik
```

    ## [1] -274.1367

Plot the model-implied density using the plot() function. Afterwards,
add rug marks of the original data to the plot using the rug() function
from the base graphics system.

``` r
plot(fit_E_2, what="BIC")
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

``` r
plot(fit_E_2, what="classification")
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-6-2.png)<!-- -->

Use Mclust to perform model-based clustering with 2 clusters on this
feature again, but now assume unequal variances. Name the model object
fit\_V\_2. What are the means and variances of the clusters? Plot the
density again and note the differences.

``` r
class <- df_unlabel[,6]
fit_V_2 <- Mclust(class, modelNames = c("V"), G=2)
summary(fit_V_2)
```

    ## ---------------------------------------------------- 
    ## Gaussian finite mixture model fitted by EM algorithm 
    ## ---------------------------------------------------- 
    ## 
    ## Mclust V (univariate, unequal variance) model with 2 components: 
    ## 
    ##  log-likelihood   n df       BIC       ICL
    ##         -268.51 200  5 -563.5115 -571.7465
    ## 
    ## Clustering table:
    ##   1   2 
    ## 104  96

``` r
fit_V_2$parameters
```

    ## $pro
    ## [1] 0.5219834 0.4780166
    ## 
    ## $mean
    ##        1        2 
    ## 139.4973 141.5604 
    ## 
    ## $variance
    ## $variance$modelName
    ## [1] "V"
    ## 
    ## $variance$d
    ## [1] 1
    ## 
    ## $variance$G
    ## [1] 2
    ## 
    ## $variance$sigmasq
    ## [1] 0.3589844 0.1500838
    ## 
    ## $variance$scale
    ## [1] 0.3589844 0.1500838

``` r
plot(fit_V_2, what="BIC")
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-8-1.png)<!-- -->

``` r
plot(fit_V_2, what="classification")
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-8-2.png)<!-- -->

How many parameters does this model have? Name them.

``` r
fit_V_2$parameters
```

    ## $pro
    ## [1] 0.5219834 0.4780166
    ## 
    ## $mean
    ##        1        2 
    ## 139.4973 141.5604 
    ## 
    ## $variance
    ## $variance$modelName
    ## [1] "V"
    ## 
    ## $variance$d
    ## [1] 1
    ## 
    ## $variance$G
    ## [1] 2
    ## 
    ## $variance$sigmasq
    ## [1] 0.3589844 0.1500838
    ## 
    ## $variance$scale
    ## [1] 0.3589844 0.1500838

According to the deviance, which model fits better?

``` r
fit_E_2$loglik
```

    ## [1] -274.1367

``` r
fit_V_2$loglik
```

    ## [1] -268.51

According to the BIC, which model is better?

``` r
fit_E_2$bic
```

    ## [1] -569.4667

``` r
fit_V_2$bic
```

    ## [1] -563.5115

# Multivariate model-based clustering

We will now use all available information in the dataset to cluster the
observations.

Use Mclust with all 6 features to perform clustering. Allow all model
types (shapes), and from 1 to 9 potential clusters. What is the optimal
model based on the BIC?

``` r
fit_multi <- Mclust(df_unlabel, G=2)
summary(fit_multi)
```

    ## ---------------------------------------------------- 
    ## Gaussian finite mixture model fitted by EM algorithm 
    ## ---------------------------------------------------- 
    ## 
    ## Mclust EVE (ellipsoidal, equal volume and orientation) model with 2 components: 
    ## 
    ##  log-likelihood   n df       BIC       ICL
    ##       -755.4051 200 39 -1717.445 -1717.493
    ## 
    ## Clustering table:
    ##   1   2 
    ## 101  99

``` r
plot(fit_multi, what="BIC")
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-12-1.png)<!-- -->

``` r
fit_multi$parameters
```

    ## $pro
    ## [1] 0.5048853 0.4951147
    ## 
    ## $mean
    ##               [,1]       [,2]
    ## Length   214.82375 214.969671
    ## Left     130.29900 129.940499
    ## Right    130.19306 129.715276
    ## Bottom    10.50530   8.308237
    ## Top       11.13364  10.157828
    ## Diagonal 139.45134 141.536032
    ## 
    ## $variance
    ## $variance$modelName
    ## [1] "EVE"
    ## 
    ## $variance$d
    ## [1] 6
    ## 
    ## $variance$G
    ## [1] 2
    ## 
    ## $variance$sigma
    ## , , 1
    ## 
    ##               Length        Left       Right      Bottom         Top
    ## Length    0.12128018  0.02983384  0.02347435 -0.03672751 -0.03497227
    ## Left      0.02983384  0.06523270  0.04428793  0.01572557 -0.04391976
    ## Right     0.02347435  0.04428793  0.07879348  0.01009680 -0.03127613
    ## Bottom   -0.03672751  0.01572557  0.01009680  1.08220619 -0.54662168
    ## Top      -0.03497227 -0.04391976 -0.03127613 -0.54662168  0.58156360
    ## Diagonal  0.01137744 -0.01387210  0.02182986  0.10623771  0.02943227
    ##             Diagonal
    ## Length    0.01137744
    ## Left     -0.01387210
    ## Right     0.02182986
    ## Bottom    0.10623771
    ## Top       0.02943227
    ## Diagonal  0.25794327
    ## 
    ## , , 2
    ## 
    ##               Length        Left       Right       Bottom         Top
    ## Length    0.14709389  0.06327080  0.05401219  0.013895867  0.03314377
    ## Left      0.06327080  0.13447708  0.08768475  0.048515954  0.04643387
    ## Right     0.05401219  0.08768475  0.13475432  0.037696734  0.03936757
    ## Bottom    0.01389587  0.04851595  0.03769673  0.543713908 -0.21666092
    ## Top       0.03314377  0.04643387  0.03936757 -0.216660919  0.33914430
    ## Diagonal -0.01377230 -0.04186735 -0.02238186 -0.002601546 -0.06716311
    ##              Diagonal
    ## Length   -0.013772301
    ## Left     -0.041867348
    ## Right    -0.022381857
    ## Bottom   -0.002601546
    ## Top      -0.067163113
    ## Diagonal  0.164764353
    ## 
    ## 
    ## $variance$scale
    ## [1] 0.1637074
    ## 
    ## $variance$shape
    ##           [,1]      [,2]
    ## [1,] 0.6405685 2.2132067
    ## [2,] 0.1419138 0.2686066
    ## [3,] 0.4856761 0.5519435
    ## [4,] 8.7918070 4.1771161
    ## [5,] 2.0307380 0.7243907
    ## [6,] 1.2686179 1.0072037
    ## 
    ## $variance$orientation
    ##              Length        Left       Right       Bottom         Top   Diagonal
    ## Length    0.3692057 -0.12033415 -0.75112403 -0.007725077 -0.14224443  0.5145157
    ## Left      0.4942600  0.76733963  0.30523083  0.026613098 -0.13703395  0.2329045
    ## Right     0.4419492 -0.61589894  0.55525864  0.020294524 -0.03703309  0.3394907
    ## Bottom    0.2991708 -0.03295933 -0.11157492  0.841327026  0.33205379 -0.2808392
    ## Top       0.4658443 -0.02058586 -0.11775873 -0.535824500  0.59686264 -0.3540414
    ## Diagonal -0.3428718  0.12596816  0.08954664  0.062298792  0.70221937  0.6012979
    ## 
    ## 
    ## $Vinv
    ## NULL

How many mean parameters does this model have?

``` r
fit_multi$df
```

    ## [1] 39

Run a 2-component VVV model on this data. Create a matrix of bivariate
contour (“density”) plots using the plot() function. Which features
provide good component separation? Which do not?

``` r
fit_multi_VVV <- Mclust(df_unlabel, G=2, modelNames = c("VVV"))

plot(fit_multi_VVV, what="density")
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-15-1.png)<!-- -->

Create a scatter plot just like the first scatter plot in this tutorial,
but map the estimated class assignments to the colour aesthetic. Map the
uncertainty (part of the fitted model list) to the size aesthetic, such
that larger points indicate more uncertain class assignments. Jitter the
points to avoid overplotting. What do you notice about the uncertainty?

``` r
ggplot(df, aes(Left, Right, color=fit_multi_VVV$classification, size=fit_multi_VVV$uncertainty))+geom_jitter()
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-16-1.png)<!-- -->

``` r
#now with the best separation between features
ggplot(df, aes(Top, Diagonal, color=fit_multi_VVV$classification, size=fit_multi_VVV$uncertainty))+geom_jitter()
```

![](Week9_assigment_2_files/figure-gfm/unnamed-chunk-17-1.png)<!-- -->

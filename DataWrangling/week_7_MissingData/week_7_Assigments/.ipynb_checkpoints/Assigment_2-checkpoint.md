Assigment 2
================
Hans Franke
October 13, 2020

``` r
#loading libraries
library(tidyverse)
```

    ## -- Attaching packages ------------------------------------------------------------------------------------------------------------------------ tidyverse 1.3.0 --

    ## v ggplot2 3.3.2     v purrr   0.3.4
    ## v tibble  3.0.3     v dplyr   1.0.2
    ## v tidyr   1.1.2     v stringr 1.4.0
    ## v readr   1.3.1     v forcats 0.5.0

    ## -- Conflicts --------------------------------------------------------------------------------------------------------------------------- tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

``` r
library(mice)
```

    ## 
    ## Attaching package: 'mice'

    ## The following objects are masked from 'package:base':
    ## 
    ##     cbind, rbind

``` r
library(dplyr)
```

In this assignment, we will again use the nhanes dataset from the mice
package.

Prepare a data frame for complete case analysis. Call this data frame
df\_cc.

``` r
?nhanes
```

    ## starting httpd help server ... done

``` r
df <- nhanes
df_cc <- na.omit(df) #omiting the n/a values
df_cc
```

    ##    age  bmi hyp chl
    ## 2    2 22.7   1 187
    ## 5    1 20.4   1 113
    ## 7    1 22.5   1 118
    ## 8    1 30.1   1 187
    ## 9    2 22.0   1 238
    ## 13   3 21.7   1 206
    ## 14   2 28.7   2 204
    ## 17   3 27.2   2 284
    ## 18   2 26.3   2 199
    ## 19   1 35.3   1 218
    ## 22   1 33.2   1 229
    ## 23   1 27.5   1 131
    ## 25   2 27.4   1 186

Prepare a dataset by performing mean imputation. Again, give this
dataset a reasonable name.

``` r
#compute the mean
imp_mean <- mice(df, method = "mean", m = 1, maxit = 1)
```

    ## 
    ##  iter imp variable
    ##   1   1  bmi  hyp  chl

``` r
#put on new df to store the missing values as mean values of each colum
df_mean <- complete(imp_mean)
df_mean
```

    ##    age     bmi      hyp   chl
    ## 1    1 26.5625 1.235294 191.4
    ## 2    2 22.7000 1.000000 187.0
    ## 3    1 26.5625 1.000000 187.0
    ## 4    3 26.5625 1.235294 191.4
    ## 5    1 20.4000 1.000000 113.0
    ## 6    3 26.5625 1.235294 184.0
    ## 7    1 22.5000 1.000000 118.0
    ## 8    1 30.1000 1.000000 187.0
    ## 9    2 22.0000 1.000000 238.0
    ## 10   2 26.5625 1.235294 191.4
    ## 11   1 26.5625 1.235294 191.4
    ## 12   2 26.5625 1.235294 191.4
    ## 13   3 21.7000 1.000000 206.0
    ## 14   2 28.7000 2.000000 204.0
    ## 15   1 29.6000 1.000000 191.4
    ## 16   1 26.5625 1.235294 191.4
    ## 17   3 27.2000 2.000000 284.0
    ## 18   2 26.3000 2.000000 199.0
    ## 19   1 35.3000 1.000000 218.0
    ## 20   3 25.5000 2.000000 191.4
    ## 21   1 26.5625 1.235294 191.4
    ## 22   1 33.2000 1.000000 229.0
    ## 23   1 27.5000 1.000000 131.0
    ## 24   3 24.9000 1.000000 191.4
    ## 25   2 27.4000 1.000000 186.0

Hint: use the replace\_na() function from the dplyr package in the
tidyverse

For these two datasets, compute the mean and variance for each feature.
Show how they differ\! Are they the same? Explain why the variance in
the chl feature is lower in the mean imputed dataset.

``` r
var(df)
```

    ##      age bmi hyp chl
    ## age 0.69  NA  NA  NA
    ## bmi   NA  NA  NA  NA
    ## hyp   NA  NA  NA  NA
    ## chl   NA  NA  NA  NA

``` r
#Comparison var ( As u can imagine if u are inputing values as MEAN, the variance will decrease because more points will become "closer to the mean")

var(df_cc)
```

    ##            age        bmi       hyp         chl
    ## age  0.5641026 -1.1621795 0.1602564   21.935897
    ## bmi -1.1621795 21.1158974 0.2153846   83.687179
    ## hyp  0.1602564  0.2153846 0.1923077    9.173077
    ## chl 21.9358974 83.6871795 9.1730769 2378.064103

``` r
var(df_mean)
```

    ##            age         bmi        hyp         chl
    ## age  0.6900000 -0.81718750 0.12254902   10.691667
    ## bmi -0.8171875 11.10489583 0.06041667   41.831771
    ## hyp  0.1225490  0.06041667 0.12745098    4.627451
    ## chl 10.6916667 41.83177083 4.62745098 1192.566667

# Assignment

Perform regression imputation on the fdgs dataset according to the
following paragraph, and compute the estimate of the population mean.
(NB: the paragraph is the example answer from the last exercise in the
previous assignment)

Since the goal is to estimate the mean weight of the population, and we
assume MAR, we have to impute (complete case analysis is only unbiased
under MCAR). Regression imputation will work fine for this purpose. For
the imputation model, I would create a linear model with wgt as the
outcome. The model will include all variables (except id, and hgt.z) and
also a quadratic effect of age (as weight will probably increase less as
the child gets older). Then, I can impute the predicted values for the
missing weight cells. The sample mean will then be the estimate of the
population mean.

``` r
#loading and look for summaries
md.pattern(fdgs)
```

![](Assigment_2_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

    ##      id reg age sex wgt wgt.z hgt hgt.z   
    ## 9987  1   1   1   1   1     1   1     1  0
    ## 23    1   1   1   1   1     1   0     0  2
    ## 20    1   1   1   1   0     0   1     1  2
    ##       0   0   0   0  20    20  23    23 86

``` r
#Original
df_fdgs <- fdgs

#df without n/a
df_fdgs_cc <- na.omit(df_fdgs)

#df with mean imputation
imp_mean <- mice(df_fdgs, method = "mean", m = 1, maxit = 1)
```

    ## 
    ##  iter imp variable
    ##   1   1  hgt  wgt  hgt.z  wgt.z

``` r
df_fgds_mean <- complete(imp_mean)

#look for df`s

md.pattern( df_fgds_mean)
```

    ##  /\     /\
    ## {  `---'  }
    ## {  O   O  }
    ## ==>  V <==  No need for mice. This data set is completely observed.
    ##  \  \|/  /
    ##   `-----'

![](Assigment_2_files/figure-gfm/unnamed-chunk-8-1.png)<!-- -->

    ##       id reg age sex hgt wgt hgt.z wgt.z  
    ## 10030  1   1   1   1   1   1     1     1 0
    ##        0   0   0   0   0   0     0     0 0

``` r
#df with reg manually (u have to use df without the n/a)

df_fdgs_age2 <- df_fdgs %>%
  mutate( age2 = age ** 2) # elevate age to quadratic as question suggests

multi.fit = lm(wgt~reg+age2+sex+hgt, data=df_fdgs_age2)
summary(multi.fit)
```

    ## 
    ## Call:
    ## lm(formula = wgt ~ reg + age2 + sex + hgt, data = df_fdgs_age2)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -30.717  -3.425  -0.106   2.165  69.609 
    ## 
    ## Coefficients:
    ##               Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept) -15.138560   0.396186 -38.211  < 2e-16 ***
    ## regEast       0.067320   0.275119   0.245  0.80670    
    ## regSouth     -0.249943   0.269460  -0.928  0.35365    
    ## regWest      -0.093715   0.273426  -0.343  0.73180    
    ## regCity      -0.904955   0.303294  -2.984  0.00285 ** 
    ## age2          0.077892   0.001044  74.610  < 2e-16 ***
    ## sexgirl      -0.989399   0.130431  -7.586 3.61e-14 ***
    ## hgt           0.321340   0.003094 103.844  < 2e-16 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 6.502 on 9979 degrees of freedom
    ##   (43 observations deleted due to missingness)
    ## Multiple R-squared:  0.9212, Adjusted R-squared:  0.9211 
    ## F-statistic: 1.666e+04 on 7 and 9979 DF,  p-value: < 2.2e-16

``` r
#predict some values
value <- data.frame(
  reg = c("North"),
  age2 = c(20),
  sex = c("girl"),
  hgt = c(30)
)

pred2 <- predict(multi.fit, value)
pred2
```

    ##         1 
    ## -4.929916

``` r
# Use fit to predict the value
df3 <- df_fdgs_age2 %>% 
  #create a pred column to compare with original
  mutate(pred = predict(multi.fit, .)) %>%
  # Replace NA with pred in var1
  mutate(wgt = ifelse(is.na(wgt), pred, wgt))

# See the result
head(df3)
```

    ##       id  reg      age  sex   hgt  wgt  hgt.z  wgt.z     age2     pred
    ## 1 100001 West 13.09514  boy 175.5 75.0  1.751  2.410 171.4827 54.52001
    ## 2 100003 West 13.81793  boy 148.4 40.0 -2.292 -1.494 190.9353 47.32688
    ## 3 100004 West 13.97125  boy 159.9 42.0 -1.000 -1.315 195.1959 51.35416
    ## 4 100005 West 13.98220 girl 159.7 46.5 -0.743 -0.783 195.5020 50.32434
    ## 5 100006 West 13.52225 girl 160.3 47.8 -0.414 -0.355 182.8511 49.53174
    ## 6 100018 East 10.21492  boy 157.8 39.7  2.025  0.823 104.3446 43.76384

``` r
#show original df just to compare
df_fdgs[rowSums(is.na(df_fdgs)) > 0,]
```

    ##          id   reg         age  sex   hgt    wgt  hgt.z  wgt.z
    ## 273  100981  City  7.48802190  boy    NA 23.200     NA -0.932
    ## 275  100984 North  5.76043806 girl 116.6     NA -0.102     NA
    ## 1278 103811 South  6.41204654  boy 115.7     NA -1.392     NA
    ## 1419 104048  City 15.05270363 girl 167.3     NA  0.014     NA
    ## 2034 105706  West  1.01300479  boy    NA  8.445     NA -1.726
    ## 2135 105872 South  2.06707734  boy  85.0     NA -1.376     NA
    ## 2485 106320 South  0.36687201 girl    NA  6.960     NA  0.654
    ## 2573 106453  West  0.93908282  boy    NA 10.420     NA  0.358
    ## 2684 106597 South  1.18822724 girl  77.4     NA -0.212     NA
    ## 2836 106796  West  2.62833676 girl    NA 14.100     NA  0.174
    ## 2940 106924 North  1.59069131  boy  87.3     NA  1.034     NA
    ## 2969 106961  East  3.22245038  boy    NA 16.300     NA  0.331
    ## 3035 107047  West  1.52224504  boy    NA 11.900     NA  0.048
    ## 3069 107106  West  1.82067077  boy  88.0     NA  0.382     NA
    ## 3189 107316 South  0.78850103 girl  74.5     NA  1.105     NA
    ## 3192 107319 South  0.78028747  boy    NA  8.880     NA -0.466
    ## 3316 107491  West  0.10130048  boy    NA  4.815     NA  0.434
    ## 3323 107498 South  1.52224504 girl    NA 10.800     NA -0.260
    ## 3539 200099  West  1.17453799 girl    NA  9.080     NA -1.003
    ## 3540 200100  West  1.32238193  boy    NA 10.295     NA -0.799
    ## 3543 200103  West  3.25804244  boy 100.0     NA -0.032     NA
    ## 4262 202084 South 19.40862423  boy 179.6     NA -0.527     NA
    ## 4298 202160  East  0.19986311  boy    NA  5.295     NA -0.419
    ## 4448 202456  East  0.17522245 girl    NA  4.750     NA -0.317
    ## 4510 202711  East  0.08761123 girl    NA  3.260     NA -1.986
    ## 4561 202797  West  0.50376454  boy    NA  7.950     NA  0.030
    ## 5538 205223  West  4.68172485  boy    NA 15.400     NA -1.757
    ## 5687 205716 North 11.59753593  boy 155.9     NA  0.595     NA
    ## 6485 208005  East  2.66666667 girl  92.2     NA -0.443     NA
    ## 6846 209091  East  0.83778234 girl    NA  8.570     NA -0.395
    ## 6869 209118  East  1.64271047  boy    NA 11.900     NA -0.172
    ## 7010 209385  City  0.64613279 girl    NA  8.180     NA  0.080
    ## 7073 209493  East  6.24229979 girl    NA 20.100     NA -0.802
    ## 7101 209563  West  6.13004791 girl 131.5     NA  2.376     NA
    ## 7108 209586  West  5.95208761  boy 115.0     NA -0.970     NA
    ## 7506 210557 South 15.98083504 girl 165.5     NA -0.463     NA
    ## 8064 211847  City  9.35249829 girl 135.9     NA -0.590     NA
    ## 8065 211853  City  9.38535250  boy 143.0     NA  0.435     NA
    ## 8067 211857  City  9.02669405 girl 144.4     NA  1.101     NA
    ## 8098 211916  City  9.09240246  boy 143.3     NA  0.727     NA
    ## 8581 212986  City 10.57357974 girl    NA 48.900     NA  1.414
    ## 8588 213000  City  9.50581793  boy 144.0     NA  0.494     NA
    ## 8597 213014 South 14.85010267 girl    NA 50.200     NA -0.686

``` r
#look at 3 indexes to compare the values with original df
ids <- df_fdgs[rowSums(is.na(df_fdgs)) > 0,1] #picking every ids with n/a values

filter(df3, id %in% ids)
```

    ##        id   reg         age  sex   hgt       wgt  hgt.z  wgt.z         age2
    ## 1  100981  City  7.48802190  boy    NA 23.200000     NA -0.932 5.607047e+01
    ## 2  100984 North  5.76043806 girl 116.6 23.924980 -0.102     NA 3.318265e+01
    ## 3  103811 South  6.41204654  boy 115.7 24.993041 -1.392     NA 4.111434e+01
    ## 4  104048  City 15.05270363 girl 167.3 54.376298  0.014     NA 2.265839e+02
    ## 5  105706  West  1.01300479  boy    NA  8.445000     NA -1.726 1.026179e+00
    ## 6  105872 South  2.06707734  boy  85.0 12.258248 -1.376     NA 4.272809e+00
    ## 7  106320 South  0.36687201 girl    NA  6.960000     NA  0.654 1.345951e-01
    ## 8  106453  West  0.93908282  boy    NA 10.420000     NA  0.358 8.818765e-01
    ## 9  106597 South  1.18822724 girl  77.4  8.603820 -0.212     NA 1.411884e+00
    ## 10 106796  West  2.62833676 girl    NA 14.100000     NA  0.174 6.908154e+00
    ## 11 106924 North  1.59069131  boy  87.3 13.111547  1.034     NA 2.530299e+00
    ## 12 106961  East  3.22245038  boy    NA 16.300000     NA  0.331 1.038419e+01
    ## 13 107047  West  1.52224504  boy    NA 11.900000     NA  0.048 2.317230e+00
    ## 14 107106  West  1.82067077  boy  88.0 13.303880  0.382     NA 3.314842e+00
    ## 15 107316 South  0.78850103 girl  74.5  7.610387  1.105     NA 6.217339e-01
    ## 16 107319 South  0.78028747  boy    NA  8.880000     NA -0.466 6.088485e-01
    ## 17 107491  West  0.10130048  boy    NA  4.815000     NA  0.434 1.026179e-02
    ## 18 107498 South  1.52224504 girl    NA 10.800000     NA -0.260 2.317230e+00
    ## 19 200099  West  1.17453799 girl    NA  9.080000     NA -1.003 1.379539e+00
    ## 20 200100  West  1.32238193  boy    NA 10.295000     NA -0.799 1.748694e+00
    ## 21 200103  West  3.25804244  boy 100.0 17.728573 -0.032     NA 1.061484e+01
    ## 22 202084 South 19.40862423  boy 179.6 71.665552 -0.527     NA 3.766947e+02
    ## 23 202160  East  0.19986311  boy    NA  5.295000     NA -0.419 3.994526e-02
    ## 24 202456  East  0.17522245 girl    NA  4.750000     NA -0.317 3.070291e-02
    ## 25 202711  East  0.08761123 girl    NA  3.260000     NA -1.986 7.675727e-03
    ## 26 202797  West  0.50376454  boy    NA  7.950000     NA  0.030 2.537787e-01
    ## 27 205223  West  4.68172485  boy    NA 15.400000     NA -1.757 2.191855e+01
    ## 28 205716 North 11.59753593  boy 155.9 45.435039  0.595     NA 1.345028e+02
    ## 29 208005  East  2.66666667 girl  92.2 14.120843 -0.443     NA 7.111111e+00
    ## 30 209091  East  0.83778234 girl    NA  8.570000     NA -0.395 7.018793e-01
    ## 31 209118  East  1.64271047  boy    NA 11.900000     NA -0.172 2.698498e+00
    ## 32 209385  City  0.64613279 girl    NA  8.180000     NA  0.080 4.174876e-01
    ## 33 209493  East  6.24229979 girl    NA 20.100000     NA -0.802 3.896631e+01
    ## 34 209563  West  6.13004791 girl 131.5 28.961558  2.376     NA 3.757749e+01
    ## 35 209586  West  5.95208761  boy 115.0 24.481363 -0.970     NA 3.542735e+01
    ## 36 210557 South 15.98083504 girl 165.5 56.696421 -0.463     NA 2.553871e+02
    ## 37 211847  City  9.35249829 girl 135.9 33.450358 -0.590     NA 8.746922e+01
    ## 38 211853  City  9.38535250  boy 143.0 36.769225  0.435     NA 8.808484e+01
    ## 39 211857  City  9.02669405 girl 144.4 35.715336  1.101     NA 8.148121e+01
    ## 40 211916  City  9.09240246  boy 143.3 36.443996  0.727     NA 8.267178e+01
    ## 41 212986  City 10.57357974 girl    NA 48.900000     NA  1.414 1.118006e+02
    ## 42 213000  City  9.50581793  boy 144.0 37.267826  0.494     NA 9.036057e+01
    ## 43 213014 South 14.85010267 girl    NA 50.200000     NA -0.686 2.205255e+02
    ##         pred
    ## 1         NA
    ## 2  23.924980
    ## 3  24.993041
    ## 4  54.376298
    ## 5         NA
    ## 6  12.258248
    ## 7         NA
    ## 8         NA
    ## 9   8.603820
    ## 10        NA
    ## 11 13.111547
    ## 12        NA
    ## 13        NA
    ## 14 13.303880
    ## 15  7.610387
    ## 16        NA
    ## 17        NA
    ## 18        NA
    ## 19        NA
    ## 20        NA
    ## 21 17.728573
    ## 22 71.665552
    ## 23        NA
    ## 24        NA
    ## 25        NA
    ## 26        NA
    ## 27        NA
    ## 28 45.435039
    ## 29 14.120843
    ## 30        NA
    ## 31        NA
    ## 32        NA
    ## 33        NA
    ## 34 28.961558
    ## 35 24.481363
    ## 36 56.696421
    ## 37 33.450358
    ## 38 36.769225
    ## 39 35.715336
    ## 40 36.443996
    ## 41        NA
    ## 42 37.267826
    ## 43        NA

``` r
md.pattern(df3)
```

![](Assigment_2_files/figure-gfm/unnamed-chunk-14-1.png)<!-- -->

    ##      id reg age sex wgt age2 wgt.z hgt hgt.z pred   
    ## 9987  1   1   1   1   1    1     1   1     1    1  0
    ## 23    1   1   1   1   1    1     1   0     0    0  3
    ## 20    1   1   1   1   1    1     0   1     1    1  1
    ##       0   0   0   0   0    0    20  23    23   23 89

``` r
#lookinf for the mean, removing N/A of the hgt colum
mean(df3$wgt)
```

    ## [1] 32.37947

``` r
mean(df_fdgs_cc$wgt)
```

    ## [1] 32.4271

Extra challenge: now, using the same model, perform stochastic
regression imputation (norm.nob) as explained in section 1.3.5 of FIMD
and compute the sample mean of weight. Do it again. Is the result the
same? What does this variation in the sample mean represent?

``` r
#df with regression imputation Using mice

df_fgds_reg <- df_fdgs

imp <- mice(df_fdgs, method = "norm.nob", seed = 1,
           m = 5, print = FALSE)
xyplot(imp, wgt ~ age )
```

![](Assigment_2_files/figure-gfm/unnamed-chunk-17-1.png)<!-- -->

``` r
df_fgds_reg <- complete(imp)
#mean first time
mean(df_fgds_reg$wgt)
```

    ## [1] 32.38399

``` r
df_fgds_reg <- df_fdgs #clean df


imp <- mice(df_fdgs, method = "norm.nob",
           m = 1, print = FALSE)

df_fgds_reg <- complete(imp)

#mean 2nd time
mean(df_fgds_reg$wgt)
```

    ## [1] 32.38095

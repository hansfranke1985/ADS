Assigment 1
================
Hans Franke
October 12, 2020

    library(tidyverse)

    ## -- Attaching packages ------------------------------------------------------------------------------------------------------------------------ tidyverse 1.3.0 --

    ## v ggplot2 3.3.2     v purrr   0.3.4
    ## v tibble  3.0.3     v dplyr   1.0.2
    ## v tidyr   1.1.2     v stringr 1.4.0
    ## v readr   1.3.1     v forcats 0.5.0

    ## -- Conflicts --------------------------------------------------------------------------------------------------------------------------- tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

    library(mice)

    ## 
    ## Attaching package: 'mice'

    ## The following objects are masked from 'package:base':
    ## 
    ##     cbind, rbind

View Data
---------

Store the nhanes dataset from the mice package in a variable called df.
Print the df variable.

    head(mice::nhanes)

    ##   age  bmi hyp chl
    ## 1   1   NA  NA  NA
    ## 2   2 22.7   1 187
    ## 3   1   NA   1 187
    ## 4   3   NA  NA  NA
    ## 5   1 20.4   1 113
    ## 6   3   NA  NA 184

    df <- nhanes

    view(df)

Show Missing Values
-------------------

Output the percentage missingness for each feature as a vector.

    is.na(df)

    ##      age   bmi   hyp   chl
    ## 1  FALSE  TRUE  TRUE  TRUE
    ## 2  FALSE FALSE FALSE FALSE
    ## 3  FALSE  TRUE FALSE FALSE
    ## 4  FALSE  TRUE  TRUE  TRUE
    ## 5  FALSE FALSE FALSE FALSE
    ## 6  FALSE  TRUE  TRUE FALSE
    ## 7  FALSE FALSE FALSE FALSE
    ## 8  FALSE FALSE FALSE FALSE
    ## 9  FALSE FALSE FALSE FALSE
    ## 10 FALSE  TRUE  TRUE  TRUE
    ## 11 FALSE  TRUE  TRUE  TRUE
    ## 12 FALSE  TRUE  TRUE  TRUE
    ## 13 FALSE FALSE FALSE FALSE
    ## 14 FALSE FALSE FALSE FALSE
    ## 15 FALSE FALSE FALSE  TRUE
    ## 16 FALSE  TRUE  TRUE  TRUE
    ## 17 FALSE FALSE FALSE FALSE
    ## 18 FALSE FALSE FALSE FALSE
    ## 19 FALSE FALSE FALSE FALSE
    ## 20 FALSE FALSE FALSE  TRUE
    ## 21 FALSE  TRUE  TRUE  TRUE
    ## 22 FALSE FALSE FALSE FALSE
    ## 23 FALSE FALSE FALSE FALSE
    ## 24 FALSE FALSE FALSE  TRUE
    ## 25 FALSE FALSE FALSE FALSE

    #Missing values in all columns
    colSums(is.na(df))

    ## age bmi hyp chl 
    ##   0   9   8  10

    # % of Missing values in all columns
    colSums(is.na(df))/nrow(df)*100

    ## age bmi hyp chl 
    ##   0  36  32  40

Use ggplot to show the % of the missing value
---------------------------------------------

    #Put data in the DF
    df_missing <- tibble(
      nmissing = colnames(is.na(df)),
      perc_col = colSums(is.na(df))/nrow(df)*100
    )

    df_missing

    ## # A tibble: 4 x 2
    ##   nmissing perc_col
    ##   <chr>       <dbl>
    ## 1 age             0
    ## 2 bmi            36
    ## 3 hyp            32
    ## 4 chl            40

    #Plotting as a barplot

    ggplot(df_missing, aes(x=nmissing, y = perc_col) ) +
             geom_bar(stat = "identity") +
             labs(y="% Of missing values") + 
             theme_classic()  

![](Assigment_1_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

Now display the missingness pattern per age group (1, 2, 3).
------------------------------------------------------------

    df %>%
      group_by(age)%>%
      summarise_all(function(x) sum(is.na(x))/n()*100)%>%
      round(2)

    ## # A tibble: 3 x 4
    ##     age   bmi   hyp   chl
    ##   <dbl> <dbl> <dbl> <dbl>
    ## 1     1  41.7  33.3  41.7
    ## 2     2  28.6  28.6  28.6
    ## 3     3  33.3  33.3  50

Missing Data Patterns
---------------------

    md.pattern(df)

![](Assigment_1_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

    ##    age hyp bmi chl   
    ## 13   1   1   1   1  0
    ## 3    1   1   1   0  1
    ## 1    1   1   0   1  1
    ## 1    1   0   0   1  2
    ## 7    1   0   0   0  3
    ##      0   8   9  10 27

Questions
---------

1.  how many rows are missing all data except the age feature? A: 7
2.  how many missing values are there in the bmi feature? A: 9
3.  how many rows are completely observed? A: 13
4.  how many missing data patterns are there? A: 5 (we include rows
    without missing values as a pattern too)

<!-- -->

    # Others packages to try :)
    #install.packages("skimr")
    skimr::skim(df)

|                                                  |      |
|:-------------------------------------------------|:-----|
| Name                                             | df   |
| Number of rows                                   | 25   |
| Number of columns                                | 4    |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |      |
| Column type frequency:                           |      |
| numeric                                          | 4    |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |      |
| Group variables                                  | None |

Data summary

**Variable type: numeric**

| skim\_variable | n\_missing | complete\_rate |   mean |    sd |    p0 |    p25 |    p50 |    p75 |  p100 | hist  |
|:---------------|-----------:|---------------:|-------:|------:|------:|-------:|-------:|-------:|------:|:------|
| age            |          0 |           1.00 |   1.76 |  0.83 |   1.0 |   1.00 |   2.00 |   2.00 |   3.0 | ▇▁▅▁▃ |
| bmi            |          9 |           0.64 |  26.56 |  4.22 |  20.4 |  22.65 |  26.75 |  28.92 |  35.3 | ▇▅▆▃▃ |
| hyp            |          8 |           0.68 |   1.24 |  0.44 |   1.0 |   1.00 |   1.00 |   1.00 |   2.0 | ▇▁▁▁▂ |
| chl            |         10 |           0.60 | 191.40 | 45.22 | 113.0 | 185.00 | 187.00 | 212.00 | 284.0 | ▃▁▇▃▁ |

    visdat::vis_dat(df)

![](Assigment_1_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->

Assigment
=========

Analyze the patterns of missing data for the fdgs dataset, and write a small paragraph on how you are going to solve the missingness in this data for an analyst who wants to compute the average weight of the population under study, assuming MAR.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

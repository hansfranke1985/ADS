Quick Summary: Visualisation, Transformation and EDA
================
Hans Franke

``` r
library(tidyverse)
```

    ## -- Attaching packages ----------------------------------------------------------------------------- tidyverse 1.3.0 --

    ## v ggplot2 3.3.2     v purrr   0.3.4
    ## v tibble  3.0.3     v dplyr   1.0.2
    ## v tidyr   1.1.2     v stringr 1.4.0
    ## v readr   1.3.1     v forcats 0.5.0

    ## -- Conflicts -------------------------------------------------------------------------------- tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

``` r
library(ISLR)
library(nycflights13)
```

  - Assigments:

<!-- end list -->

1.  <https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_5_Visualization%20and%20EDA/Practices/Assis_1.md>

2.  <https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_5_Visualization%20and%20EDA/Practices/Assis_2.md>

# Book: <https://r4ds.had.co.nz/>

# chapter 3: visualisation

## Exercises:

<https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_5_Visualization%20and%20EDA/Practices/R_DS_Ex_Ch03.md>

# chapter 5: data transformation

## Exercises

<https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_5_Visualization%20and%20EDA/Practices/R_DS_Ex_Ch05.md>

### Quick Guide to Transformation Functions:

  - Pick observations by their values (filter()).

<!-- end list -->

``` r
  filter(mtcars, mpg > 20)
```

    ##                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
    ## Mazda RX4      21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
    ## Mazda RX4 Wag  21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
    ## Datsun 710     22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
    ## Hornet 4 Drive 21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
    ## Merc 240D      24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
    ## Merc 230       22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
    ## Fiat 128       32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
    ## Honda Civic    30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
    ## Toyota Corolla 33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
    ## Toyota Corona  21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
    ## Fiat X1-9      27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
    ## Porsche 914-2  26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
    ## Lotus Europa   30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
    ## Volvo 142E     21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2

  - Reorder the rows (arrange()).

<!-- end list -->

``` r
head(arrange(mtcars, cyl))
```

    ##                 mpg cyl  disp hp drat    wt  qsec vs am gear carb
    ## Datsun 710     22.8   4 108.0 93 3.85 2.320 18.61  1  1    4    1
    ## Merc 240D      24.4   4 146.7 62 3.69 3.190 20.00  1  0    4    2
    ## Merc 230       22.8   4 140.8 95 3.92 3.150 22.90  1  0    4    2
    ## Fiat 128       32.4   4  78.7 66 4.08 2.200 19.47  1  1    4    1
    ## Honda Civic    30.4   4  75.7 52 4.93 1.615 18.52  1  1    4    2
    ## Toyota Corolla 33.9   4  71.1 65 4.22 1.835 19.90  1  1    4    1

  - Pick variables by their names (select()).

<!-- end list -->

``` r
# Select columns by name
head(select(mtcars, mpg, cyl, hp))
```

    ##                    mpg cyl  hp
    ## Mazda RX4         21.0   6 110
    ## Mazda RX4 Wag     21.0   6 110
    ## Datsun 710        22.8   4  93
    ## Hornet 4 Drive    21.4   6 110
    ## Hornet Sportabout 18.7   8 175
    ## Valiant           18.1   6 105

  - Create new variables with functions of existing variables
    (mutate()).

<!-- end list -->

``` r
flights_sml <- select(flights, 
  year:day, 
  ends_with("delay"), 
  distance, 
  air_time
)

mutate(flights_sml,
  gain = dep_delay - arr_delay,
  speed = distance / air_time * 60 )
```

    ## # A tibble: 336,776 x 9
    ##     year month   day dep_delay arr_delay distance air_time  gain speed
    ##    <int> <int> <int>     <dbl>     <dbl>    <dbl>    <dbl> <dbl> <dbl>
    ##  1  2013     1     1         2        11     1400      227    -9  370.
    ##  2  2013     1     1         4        20     1416      227   -16  374.
    ##  3  2013     1     1         2        33     1089      160   -31  408.
    ##  4  2013     1     1        -1       -18     1576      183    17  517.
    ##  5  2013     1     1        -6       -25      762      116    19  394.
    ##  6  2013     1     1        -4        12      719      150   -16  288.
    ##  7  2013     1     1        -5        19     1065      158   -24  404.
    ##  8  2013     1     1        -3       -14      229       53    11  259.
    ##  9  2013     1     1        -3        -8      944      140     5  405.
    ## 10  2013     1     1        -2         8      733      138   -10  319.
    ## # ... with 336,766 more rows

  - Collapse many values down to a single summary (summarise()).

<!-- end list -->

``` r
by_day <- group_by(flights, year, month, day)
summarise(by_day, delay = mean(dep_delay, na.rm = TRUE))
```

    ## `summarise()` regrouping output by 'year', 'month' (override with `.groups` argument)

    ## # A tibble: 365 x 4
    ## # Groups:   year, month [12]
    ##     year month   day delay
    ##    <int> <int> <int> <dbl>
    ##  1  2013     1     1 11.5 
    ##  2  2013     1     2 13.9 
    ##  3  2013     1     3 11.0 
    ##  4  2013     1     4  8.95
    ##  5  2013     1     5  5.73
    ##  6  2013     1     6  7.15
    ##  7  2013     1     7  5.42
    ##  8  2013     1     8  2.55
    ##  9  2013     1     9  2.28
    ## 10  2013     1    10  2.84
    ## # ... with 355 more rows

# chapter 7: EDA

## Exercises:

<https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_5_Visualization%20and%20EDA/Practices/R_DS_Ex_Ch07.md>

# Further Reading;

# Exploratory Data Analysis;

Read chapter from the suggested book about the checklist:
<https://bookdown.org/rdpeng/exdata/exploratory-data-analysis-checklist.html>

## Peng Check-List

1.  Formulate your question

2.  Read in your data

3.  Check the packaging

4.  Run str()

5.  Look at the top and the bottom of your data

6.  Check your “n”s

7.  Validate with at least one external data source

8.  Try the easy solution first

9.  Challenge your solution

10. Follow up

## Tuckey Principles

1.  Show comparisons

2.  Show Causality

3.  Show Multivariate Data

4.  Integrate Evidence

5.  Describe and Document the evidence

6.  Content, content, content

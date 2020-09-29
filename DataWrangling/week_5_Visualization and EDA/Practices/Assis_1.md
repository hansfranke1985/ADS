Assignment\_1
================
Hans Franke
September 28, 2020

Importing libraries

``` r
library(tidyverse)
```

    ## -- Attaching packages ------------------------------------------------------------------------------------------- tidyverse 1.3.0 --

    ## v ggplot2 3.3.2     v purrr   0.3.4
    ## v tibble  3.0.3     v dplyr   1.0.2
    ## v tidyr   1.1.2     v stringr 1.4.0
    ## v readr   1.3.1     v forcats 0.5.0

    ## -- Conflicts ---------------------------------------------------------------------------------------------- tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

``` r
library(ISLR)
```

## Question 1

## Question 2:

Run the code below to generate data. There will be three vectors in your
environment. Put them in a data frame for entering it in a ggplot() call
using either the data.frame() or the tibble() function. Give informative
names and make sure the types are correct (use the as.<type>()
functions). Name the result gg\_students

``` r
set.seed(1234)
student_grade  <- rnorm(32, 7)
student_number <- round(runif(32) * 2e6 + 5e6)
programme      <- sample(c("Science", "Social Science"), 32, replace = TRUE)
```

Converting to DataFrame:

``` r
gg_students <- tibble( 
                        student_grade = round(student_grade, 2),
                        student_number = student_number, 
                        programme = programme
                        )
```

Print Head of DF:

``` r
head(gg_students)
```

    ## # A tibble: 6 x 3
    ##   student_grade student_number programme     
    ##           <dbl>          <dbl> <chr>         
    ## 1          5.79        5478051 Social Science
    ## 2          7.28        6412989 Science       
    ## 3          8.08        5616190 Social Science
    ## 4          4.65        6017095 Social Science
    ## 5          7.43        5103293 Social Science
    ## 6          7.51        6129140 Science

## Question 2

Plot the first homeruns\_plot again, but map the Hits to the y-axis and
the HmRun to the x-axis instead.

``` r
homeruns_plot <- 
  ggplot(Hitters, aes(x = HmRun, y = Hits)) +
  geom_point() +
  labs(x = "HmRun", y = "Hits")

homeruns_plot
```

![](README_figs/README-unnamed-chunk-6-1.png)<!-- -->

## Question 4:

Recreate the same plot once more, but now also map the variable League
to the colour aesthetic and the variable Salary to the size aesthetic.

``` r
homeruns_plot2 <- 
  ggplot(Hitters, aes(x = HmRun, y = Hits, colour = League, size = Salary)) +
  geom_point() +
  labs(x = "HmRun", y = "Hits")

homeruns_plot2           
```

    ## Warning: Removed 59 rows containing missing values (geom_point).

![](README_figs/README-unnamed-chunk-7-1.png)<!-- -->

## question 5:

Look at the many different geoms on the reference website.
<https://ggplot2.tidyverse.org/reference/#section-layer-geoms>

## Question 6:

Use geom\_histogram() to create a histogram of the grades of the
students in the gg\_students dataset. Play around with the binwidth
argument of the geom\_histogram() function.

``` r
 gg_students_plot <- 
  ggplot(gg_students, aes(x = student_grade))+
  geom_histogram() +
  stat_bin(binwidth = NULL)
  
gg_students_plot 
```

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

![](README_figs/README-unnamed-chunk-8-1.png)<!-- -->

``` r
gg_students_plot <- 
  ggplot(gg_students, aes(x = student_grade))+
  geom_histogram() +
  stat_bin(binwidth = 1)
  
gg_students_plot 
```

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

![](README_figs/README-unnamed-chunk-9-1.png)<!-- -->

## Question 7

Use geom\_density() to create a density plot of the grades of the
students in the gg\_students dataset. Add the argument fill = “light
seagreen” to geom\_density()

``` r
gg_students_plot_3 <- 
  ggplot(gg_students, aes(student_grade))+
 
  geom_density(fill = "light seagreen")


  
gg_students_plot_3 
```

![](README_figs/README-unnamed-chunk-10-1.png)<!-- -->

## Question 8:

Add rug marks to the density plot through geom\_rug(). You can edit the
colour and size of the rug marks using those arguments within the
geom\_rug() function.

``` r
gg_students_plot_3 <- 
  ggplot(gg_students, aes(student_grade))+
 
  geom_density(fill = "light seagreen")+
  geom_rug(colour='red', size=2)


  
gg_students_plot_3
```

![](README_figs/README-unnamed-chunk-11-1.png)<!-- -->

## Question 9:

Increase the data to ink ratio by removing the y axis label, setting the
theme to theme\_minimal(), and removing the border of the density
polygon. Also set the limits of the x-axis to go from 0 to 10 using the
xlim() function, because those are the plausible values for a student
grade.

``` r
gg_students_plot_4 <- 
  ggplot(gg_students, aes(student_grade))+ 
 
  xlim(0,10)+
  labs(y = NULL) + 
  geom_density(fill = "light seagreen", outline.type = "lower")+
  geom_rug(colour='red', size=2)+
  theme_minimal()

  
gg_students_plot_4
```

![](README_figs/README-unnamed-chunk-12-1.png)<!-- -->

# Boxplot

## Question 10

Create a boxplot of student grades per programme in the gg\_students
dataset you made earlier: map the programme variable to the x position
and the grade to the y position. For extra visual aid, you can
additionally map the programme variable to the fill aesthetic

``` r
students_box_plot <-
  ggplot(gg_students, aes( x = programme, y = student_grade, fill = programme ))+
  geom_boxplot()

students_box_plot
```

![](README_figs/README-unnamed-chunk-13-1.png)<!-- -->

## Question 11

What do each of the horizontal lines in the boxplot mean? What do the
vertical lines (whiskers) mean?

Answer: Summary statistics The lower and upper hinges correspond to the
first and third quartiles (the 25th and 75th percentiles). This differs
slightly from the method used by the boxplot() function, and may be
apparent with small samples. See boxplot.stats() for for more
information on how hinge positions are calculated for boxplot().

The upper whisker extends from the hinge to the largest value no further
than 1.5 \* IQR from the hinge (where IQR is the inter-quartile range,
or distance between the first and third quartiles). The lower whisker
extends from the hinge to the smallest value at most 1.5 \* IQR of the
hinge. Data beyond the end of the whiskers are called “outlying” points
and are plotted individually.

In a notched box plot, the notches extend 1.58 \* IQR / sqrt(n). This
gives a roughly 95% confidence interval for comparing medians. See
McGill et al. (1978) for more details

font:
<https://ggplot2.tidyverse.org/reference/geom_boxplot.html?q=boxplot>

# Two Densities

## Question 12:

Comparison of distributions across categories can also be done by adding
a fill aesthetic to the density plot you made earlier. Try this out. To
take care of the overlap, you might want to add some transparency in the
geom\_density() function using the alpha argument.

``` r
gg_students_plot_4 <- 
  ggplot(gg_students, aes(student_grade, colour = programme ))+
 
  geom_density(fill = "light blue" , alpha = 0.1 ) 


  
gg_students_plot_4 
```

![](README_figs/README-unnamed-chunk-14-1.png)<!-- -->

# BarPlots

## Question 13:

Create a bar plot of the variable Years from the Hitters dataset.

``` r
bar_plot <- 
  ggplot(Hitters, aes(Years))+
  stat_count()+
  geom_bar()

bar_plot
```

![](README_figs/README-unnamed-chunk-15-1.png)<!-- -->

``` r
bar_plot <- 
  ggplot(Hitters, aes(Years, fill = League))+
  stat_count()+
  geom_bar()

bar_plot
```

![](README_figs/README-unnamed-chunk-16-1.png)<!-- -->

# Line Plot

## Question 14:

Use geom\_line() to make a line plot out of the first 200 observations
of the variable Volume (the number of trades made on each day) of the
Smarket dataset. You will need to create a Day variable using mutate()
to map to the x-position. This variable can simply be the integers from
1 to 200. Remember, you can select the first 200 rows using
Smarket\[1:200, \].

``` r
head(Smarket)
```

    ##   Year   Lag1   Lag2   Lag3   Lag4   Lag5 Volume  Today Direction
    ## 1 2001  0.381 -0.192 -2.624 -1.055  5.010 1.1913  0.959        Up
    ## 2 2001  0.959  0.381 -0.192 -2.624 -1.055 1.2965  1.032        Up
    ## 3 2001  1.032  0.959  0.381 -0.192 -2.624 1.4112 -0.623      Down
    ## 4 2001 -0.623  1.032  0.959  0.381 -0.192 1.2760  0.614        Up
    ## 5 2001  0.614 -0.623  1.032  0.959  0.381 1.2057  0.213        Up
    ## 6 2001  0.213  0.614 -0.623  1.032  0.959 1.3491  1.392        Up

``` r
# Select only first 200 apperances:
firsts200 <- select(Smarket[1:200,],
                    Volume

)


#Creating the x-positions (Days)
firsts200 <- mutate ( firsts200, days = 1:200 )
```

``` r
#Finally Plotting
smart_line <- 
  ggplot(firsts200, aes(x = days, y = Volume)) + 
  geom_line()

smart_line
```

![](README_figs/README-unnamed-chunk-18-1.png)<!-- -->

## Question 15:

Give the line a nice colour and increase its size. Also add points of
the same colour on top.

``` r
smart_line2 <- 
  ggplot(firsts200, aes(x = days, y = Volume)) + 
  geom_line(colour = "blue", size=2 ) +
  geom_point(colour = "red")


smart_line2
```

![](README_figs/README-unnamed-chunk-19-1.png)<!-- -->

## Question 16:

Use the function which.max() to find out which of the first 200 days has
the highest trade volume and use the function max() to find out how
large this volume was.

Answer Togheter with question 17\!

## Question 17:

Use geom\_label(aes(x = your\_x, y = your\_y, label = “Peak volume”)) to
add a label to this day. You can use either the values or call the
functions. Place the label near the peak\!

``` r
#define in which day
whichday <- which.max(firsts200$Volume)

#define which volume
whichvol <- max(firsts200$Volume)

g1 <- subset(firsts200, firsts200 == whichday) #creating a subset

simple <-
  ggplot(firsts200, aes(x = days, y = Volume))+
  geom_point() +
  geom_text(aes(x = whichday, y = whichvol , label = "Peak" ), colour = "blue" )   # this adds a point
  #geom_label( aes(x = whichday, y = whichvol , label = "Peak Volume", size=1))
 
  

simple
```

![](README_figs/README-unnamed-chunk-20-1.png)<!-- -->

# Faceting

## Question 18:

Create a data frame called baseball based on the Hitters dataset. In
this data frame, create a factor variable which splits players’ salary
range into 3 categories. Tip: use the filter() function to remove the
missing values, and then use the cut() function and assign nice labels
to the categories. In addition, create a variable which indicates the
proportion of career hits that was a home run.

``` r
  baseball <- Hitters 

  baseball <- filter(baseball, !is.na(Salary)) #remove missing values
  
  baseball <- mutate(baseball, Salary_Range = cut(baseball$Salary, 3, labels = c("low","med","high"))) # Adding new Colum = "Salary_Range"
  
  baseball <-mutate(baseball, HmRun_Prop = HmRun / Hits) # Adding new Colum = HmRun_Prop = Home Runs / Total Hits
  
  baseballFilter <- select(baseball, Salary, Salary_Range, Hits, HmRun, HmRun_Prop)
  
  head(baseballFilter)
```

    ##   Salary Salary_Range Hits HmRun HmRun_Prop
    ## 1  475.0          low   81     7 0.08641975
    ## 2  480.0          low  130    18 0.13846154
    ## 3  500.0          low  141    20 0.14184397
    ## 4   91.5          low   87    10 0.11494253
    ## 5  750.0          low  169     4 0.02366864
    ## 6   70.0          low   37     1 0.02702703

## Question 19:

Create a scatter plot where you map CWalks to the x position and the
proportion you calculated in the previous exercise to the y position.
Fix the y axis limits to (0, 0.4) and the x axis to (0, 1600) using
ylim() and xlim(). Add nice x and y axis titles using the labs()
function. Save the plot as the variable baseball\_plot.

``` r
  baseball_plot <- 
    ggplot(baseball, aes(x = CWalks, y = HmRun_Prop)) +
    geom_point(color = "blue") +
    xlim(0,1600) +
    ylim(0,0.4)+
    labs(y = "Home Run`s Proportion", title = "Home Run`s x CWalks")
  

  baseball_plot
```

![](README_figs/README-unnamed-chunk-22-1.png)<!-- -->

## Question 20:

Split up this plot into three parts based on the salary range variable
you calculated. Use the facet\_wrap() function for this; look at the
examples in the help file for tips.

``` r
  baseball_plot2 <- 
    ggplot(baseball, aes(x = CWalks, y = HmRun_Prop)) +
    geom_point(color = "blue") +
    xlim(0,1600) +
    ylim(0,0.4)+
    labs(y = "Home Run`s Proportion", title = "Home Run`s x CWalks") + 
    facet_wrap(vars(Salary_Range))

  

  baseball_plot2
```

![](README_figs/README-unnamed-chunk-23-1.png)<!-- -->

# Final Exercise

Create an interesting data visualisation based on the Carseats data from
the ISLR package.

``` r
  #?Carseats
  #head(Carseats)
  
  #Looking for correlation (Who impacts more the Sales?)
  
  Sales_Corr <-
    ggplot(Carseats, aes(x = Population, y = Sales, color = Urban)) + 
    geom_smooth(method = "lm") +
    geom_point()  +
    facet_grid( ~ Urban) + 
    facet_grid(~ ShelveLoc) + 
    labs(subtitle = "Shelves Location Quality" , caption = "Model = Linear regression" ) + 
    ggtitle('Impact on SALES by POPULATION, considering URBAN and SHELVES location')
    
  
  Sales_Corr
```

    ## `geom_smooth()` using formula 'y ~ x'

![](README_figs/README-unnamed-chunk-24-1.png)<!-- -->

``` r
  Sales_Corr <-
    ggplot(Carseats, aes(x = Advertising, y = Sales, color = ShelveLoc)) + 
    geom_smooth(method = "lm") +
    geom_point()  +
#    facet_grid( ~ Urban) + 
    facet_grid(~ ShelveLoc) + 
    labs(subtitle = "Shelves Location Quality" , caption = "Model = Linear regression" ) + 
    ggtitle('Impact on SALES by ADVERTISING, considering SHELVES location') +
    theme_minimal()
    
  
  Sales_Corr
```

    ## `geom_smooth()` using formula 'y ~ x'

![](README_figs/README-unnamed-chunk-25-1.png)<!-- -->

\`\`\`

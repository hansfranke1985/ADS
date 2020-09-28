
library(tidyverse)
library(ISLR)
Hitters = Hitters

# General Graph Grammar


# ggplot(data = <DATA>) +   
#  <GEOM_FUNCTION>(  
#    mapping = aes( < MAPPINGS > ),  
#    stat = < STAT > ,   
#    position = < POSITION >  
#  ) +  
#  < COORDINATE_FUNCTION > +  
#  < FACET_FUNCTION >  
  
  # Question 1:
  ## Name the aesthetics, geoms, scales, and facets of the above visualisation. Also name any statistical transformations or special coordinate systems.
  

# histogram of the distribution of salary
hist(Hitters$Salary, xlab = "Salary in thousands of dollars")


#1. Aesthetic
#2. Geoms
#3. Scales
#4. Facets


barplot(table(Hitters$League))


#1. Aesthetic
#2. Geoms
#3. Scales
#4. Facets

homeruns_plot <- 
  ggplot(Hitters, aes(x = Hits, y = HmRun)) +
  geom_point() +
  labs(x = "Hits", y = "Home runs")

homeruns_plot

homeruns_plot + 
  geom_density_2d() +
  labs(title = "Cool density and scatter plot of baseball data") +
  theme_minimal()


# Question 1:
## Name the aesthetics, geoms, scales, and facets of the above visualisation. Also name any statistical transformations or special coordinate systems.



library(tidyverse)
library(ISLR)

head(Hitters)
View(Hitters)

#Question 1:
# Name the aesthetics, geoms, scales, and facets of the above visualisation. Also name any statistical transformations or special coordinate systems.

homeruns_plot <- 
  ggplot(Hitters, aes(x = Hits, y = HmRun)) +
  geom_point() +
  labs(x = "Hits", y = "Home runs", title = "Simple Example")

homeruns_plot

homeruns_plot + 
  geom_density_2d() +
  labs(title = "Cool density and scatter plot of baseball data") +
  theme_minimal()

homeruns_plot

# Question 2:
# Run the code below to generate data. There will be three vectors in your environment. Put them in a data frame for entering it in a ggplot() call using either the data.frame() or the tibble() function. Give informative names and make sure the types are correct (use the as.<type>() functions). Name the result gg_students


set.seed(1234)
student_grade  <- rnorm(32, 7)
student_number <- round(runif(32) * 2e6 + 5e6)
programme      <- sample(c("Science", "Social Science"), 32, replace = TRUE)

gg_students <- tribble (student_grade, student_number, programme)


library(tidyverse)

batters <- as_tibble(Lahman::Batting)
data(iris)

head(batters)
?iris

iris <- iris

plot(iris)
plot(iris$Petal.Length)
?Titanic

library(nycflights13)
flights <- flights
test <- flights %>% 
  group_by(year, month, day) %>% 
  summarise(
    first = min(dep_time),
    last = max(dep_time)
  )

daily <- group_by(flights, year, month, day)
(per_day   <- summarise(daily, flights = n()))
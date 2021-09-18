library(lubridate)
library(ggplot2)
library(tidyverse)

clim_data <- read_csv("../R BootCamp/BootCamp #2/Dataset/MTMetStations.csv")
clim_vars_longer <- clim_data %>% pivot_longer(cols = !Date,
                                               names_to = "climvar_station",
                                               values_to = "value")
clim_vars_separate <-
  clim_vars_longer %>% separate(col = climvar_station,
                                into = c("Station", "climvar"))

tidy_clim_data <-
  clim_vars_separate %>% pivot_wider(names_from = climvar,
                                     values_from = value)

tidy_clim_data <- tidy_clim_data %>%
  mutate(Date = mdy(Date))
tidy_clim_data <- tidy_clim_data %>% mutate(Year = year(Date))

sumry <- tidy_clim_data %>%
  group_by(Year) %>%
  summarize(mTM = mean(TMaxF))

ggplot(sumry, aes(Year, mTM, colour = factor(mTM))) +
  geom_point(size = 3, stroke = 1.5) + theme_classic() + theme(legend.position = "none") +
  labs(x = "Year",
       y = "Mean Temp. Value",)


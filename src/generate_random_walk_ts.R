# Generate random data

library(ggplot2)
library(tidyverse)

set.seed(42)

# Generate ARMA data
y <- arima.sim(model = list(order = c(0, 1, 0)),
               n = 200,
               sd = 0.5) + 20

m <- length(y)
y_df <- data.frame(time = 1:m, y =  y)

# Plot random walk time series
y_df %>%
  ggplot(aes(x = time, y = y)) +
  geom_line() +
  labs(
    title = "Random Walk Time Series",
    x = "Time",
    y = "y"
  ) +
  scale_y_continuous() +
  theme_minimal()

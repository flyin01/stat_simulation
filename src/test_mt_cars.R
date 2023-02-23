# Run test by executing this command in the console:
# library(testhat)
# testhat::test_file("test_mt_cars.R)

library(testthat)
testthat::local_edition(3)
library(data.table)

# Load mtcars data set
data("mtcars")
dt_mt_cars <- as.data.table(mtcars)[am == 1 & cyl == 6]

# write test to check that data table has correct numer of rows
test_that("mt_cars data table has correct number of rows", {
  expect_equal(nrow(dt_mt_cars), 3)
})

# write test to check that the data table has the correct columns
test_that("mt_cars data table has correct columns", {
  expected_cols <- c("mpg", "cyl", "disp", "hp", "drat", "wt",
                   "qsec", "vs", "am", "gear", "carb")
  expect_equal(colnames(dt_mt_cars), expected_cols)
})

# write a test to check that the data table is filtered correctly
test_that("mt_cars data table is filtered correctly", {
  expected_mpg <- c(21.0, 21.0, 19.7)
  expected_cyl <- c(6, 6, 6)
  expected_hp  <- c(110, 110, 175)
  expected_wt  <- c(2.620, 2.875, 2.771) # change last element to 2.770 to pass test.
  
  expect_equal(dt_mt_cars[, .(mpg, cyl, hp, wt)],
               data.table(mpg = expected_mpg,
                          cyl = expected_cyl,
                          hp = expected_hp,
                          wt = expected_wt))
})
# The latest test will fail! 
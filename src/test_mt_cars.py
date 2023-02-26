# -*- coding: utf-8 -*-
"""test_mt_cars.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ydaqCE2ZWk-2FHAfuWYf4tmXrvD8d-cE
"""

# Run test by executing this command in the console:
# python -m unittest test_mt_cars

import pandas as pd
import unittest

# load the data set
url = "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
df_mt_cars = pd.read_csv(url)
df_mt_cars = (df_mt_cars[(df_mt_cars['am'] == 1) & (df_mt_cars['cyl'] == 6)] \
                # .drop('Unnamed: 0', axis = 1)
                .reset_index(drop = True))

class TestMTCarsDataFrame(unittest.TestCase):

  def test_has_correct_number_of_rows(self):
    self.asserEqual(len(df_mt_cars), 3)
  
  def test_has_correct_columns(self):
    expected_cols = ["mpg", "cyl", "disp", "hp", "drat", "wt", \
                     "qsec", "vs", "am", "gear", "carb"]
    self.assertListEqual(list(df_mt_cars.columns), expected_cols)

  def test_is_filtered_correctly(self):
    expected_mpg = [21.0, 21.0, 19.7]
    expected_cyl = [6, 6, 6]
    expected_hp = [110, 110, 175]
    expected_wt = [2.620, 2.875, 2.770]

    (self.assertTrue(df_mt_cars[['mpg','cyl','hp','wt']]
                     .equals(pd.DataFrame({
                         'mpg': expected_mpg,
                         'cyl': expected_cyl,
                         'hp': expected_hp,
                         'wt': expected_wt
                     }))))
  
# if __name__ == '__main__':
#     unittest.main()

# The `if __name__ == '__main__' `statement is a pattern used to separate code that is executed when 
# the script is run as the main program from code that is imported as a module by another script.
# Note that to run the Python test we have invoked the following commands from the terminal. 
# The -m flag is used to run the 'unittest' module as a script with 'test_mt_cars' as the argument of the script.
# Generate random data

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import arma_generate_sample
np.random.seed(42)

# Coefficients
ar_coefs = [1]
ma_coefs = [1]

# Generate ARMA data
y = arma_generate_sample(ar_coefs, ma_coefs, nsample = 200, scale = .5)
y = np.cumsum(y) + 20

# Plot random walk time series
plt.clf()
plt.plot(y)
plt.ylabel(r'$y_t$')
plt.xlabel(r'$t$')
plt.title("Random Walk Time Series")
plt.show()
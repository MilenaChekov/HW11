from scipy.stats import binom
import numpy as np

rv = binom(5, 0.5)
sample = rv.rvs(size=10000)
m = np.mean(sample)
# n * тета
Var = 1/9999 * np.sum((sample-m)**2)
# n * тета * (1-тета)
t = -(Var/m-1)
print('m = ',  m/t, 'T = ', t)


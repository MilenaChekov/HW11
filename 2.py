from scipy.stats import poisson
import numpy as np

rv = poisson(17)
for i in range(15):
    sample = rv.rvs(size=100)
    E = np.mean(sample)
    Var = 1/99 * np.sum((sample-E)**2)
    print(np.abs(17-E), np.abs(17-Var))


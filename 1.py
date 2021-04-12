from scipy.stats import uniform
import numpy as np

rv = uniform()
sample = rv.rvs(size=10000)
print(sample)

print(sample.min(), sample.max())

m = np.mean(sample)
print(m)
# Мат ожидание можно оценить средним - a+b/2
var2 = 1/9999 * np.sum((sample-m)**2)
print(var2)
# Дисперсию можно оценить дисперсией выборки - (b-a)^2/12
sum = m * 2
dif = np.sqrt(12 * var2)

print('a = ', (sum - dif)/2)
print('b = ', (sum + dif)/2)



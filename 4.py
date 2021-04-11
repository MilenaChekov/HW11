import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('breast_cancer_1000_genes.tsv', sep='\t')

df = df.set_index('Unnamed: 0')
df['max-min'] = df.max(axis=1) - df.min(axis=1)
df = df.sort_values('max-min')
df = df.drop(columns=['max-min'])
h1 = df.iloc[:10]
h1 = h1.T
print(h1)
b1 = sns.boxplot(data=h1)
plt.tight_layout()
plt.close()
b1.figure.savefig('boxplot1.png')

df['var'] = df.var(axis=1)
df = df.sort_values('var')
df = df.drop(columns=['var'])
h2 = df.iloc[:10]
h2 = h2.T
print(h2)
b2 = sns.boxplot(data=h2)
plt.tight_layout()
b2.figure.savefig('boxplot2.png')
plt.close()

df['qq'] = df.quantile(q=0.75, axis=1)-df.quantile(q=0.25, axis=1)
df = df.sort_values('qq')
df = df.drop(columns=['qq'])
h3 = df.iloc[:10]
h3 = h3.T
print(h3)
b3 = sns.boxplot(data=h3)
plt.tight_layout()
b3.figure.savefig('boxplot3.png')
plt.close()

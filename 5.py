import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('breast_cancer_key_genes.tsv', sep='\t')
df = df.drop(columns=['ERBB2', 'MKI67'])
a = sns.kdeplot(data=df)
plt.tight_layout()
a.figure.savefig('kdeplot.png')
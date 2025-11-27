import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn as sk

df = pd.read_csv('datasets/college_data.csv')
df['Application Volume (Students)'] = df['Application Volume (Students)'].replace({',': ''}, regex=True).astype(int)

plt.figure(figsize=(12,6))
sns.barplot(data=df, x='College', y='Application Volume (Students)')
plt.xticks(rotation=45)
plt.title('Application Volume by College')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(data=df, x='College', y='Admission Rates')
plt.xticks(rotation=45)
plt.title('Admission Rates by College')
plt.tight_layout()
plt.show()

df_melted = df.melt(id_vars='College', value_vars=['Graduation Rate (4 Years)', 'Graduation Rate (6 Years)'], var_name='Graduation Period', value_name='Rate')
plt.figure(figsize=(12,6))
sns.barplot(data=df_melted, x='College', y='Rate', hue='Graduation Period')
plt.xticks(rotation=45)
plt.title('Graduation Rates by College')
plt.tight_layout()
plt.show()

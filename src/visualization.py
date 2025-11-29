import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('datasets/college_data.csv')
df['Application Volume (Students)'] = df['Application Volume (Students)'].replace({',': ''}, regex=True).astype(int)

# Create a single figure with three stacked subplots so all plots appear in one window
fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# Application volume
sns.barplot(data=df, x='College', y='Application Volume (Students)', ax=axes[0])
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45)
axes[0].set_title('Application Volume by College')

# Admission rates
sns.barplot(data=df, x='College', y='Admission Rates', ax=axes[1])
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45)
axes[1].set_title('Admission Rates by College')

# Graduation rates (4- and 6-year)
df_melted = df.melt(id_vars='College', value_vars=['Graduation Rate (4 Years)', 'Graduation Rate (6 Years)'],
                    var_name='Graduation Period', value_name='Rate')
sns.barplot(data=df_melted, x='College', y='Rate', hue='Graduation Period', ax=axes[2])
axes[2].set_xticklabels(axes[2].get_xticklabels(), rotation=45)
axes[2].set_title('Graduation Rates by College')
axes[2].legend(loc='best')

# Pairplot
sns.pairplot(data=df, kind='kde', diag_kind='none')

plt.tight_layout()
plt.show()



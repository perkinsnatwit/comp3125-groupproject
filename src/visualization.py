import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "datasets/college_data.csv"
df = pd.read_csv(file_path)

df["Application Volume (Students)"] = (
    df["Application Volume (Students)"].astype(str).str.replace(",", "").astype(int)
)

sns.set(style="whitegrid", palette="muted")


plt.figure(figsize=(10, 6))
sns.barplot(x="Admission Rates", y="College", data=df, color="skyblue")
plt.title("Admission Rates by College")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x="Admission Rates", y="Graduation Rate (6 Years)", hue="College", data=df, s=100)
plt.title("Admission Rate vs 6-Year Graduation Rate")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of College Metrics")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x="Application Volume (Students)", y="Admission Rates", hue="College", data=df, s=120)
plt.title("Application Volume vs Admission Rate")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
df_melt = df.melt(id_vars="College", value_vars=["Graduation Rate (4 Years)", "Graduation Rate (6 Years)"], var_name="Graduation Type", value_name="Rate")
sns.barplot(x="Rate", y="College", hue="Graduation Type", data=df_melt)
plt.title("4-Year vs 6-Year Graduation Rates by College")
plt.tight_layout()
plt.show()

# 1. Cohort Size vs Grad Rate (4-year)
plt.figure(figsize=(8,6))
sns.scatterplot(x="Application Volume (Students)", y="Graduation Rate (4 Years)", hue="College", data=df, s=100)
plt.title("Cohort Size vs 4-Year Graduation Rate")
plt.tight_layout()
plt.show()

# 1. Cohort Size vs Grad Rate (6-year)
plt.figure(figsize=(8,6))
sns.scatterplot(x="Application Volume (Students)", y="Graduation Rate (6 Years)", hue="College", data=df, s=100)
plt.title("Cohort Size vs 6-Year Graduation Rate")
plt.tight_layout()
plt.show()

# 2. Selective Score vs Grad Rate (4-year)
plt.figure(figsize=(8,6))
sns.scatterplot(x="Selective Score", y="Graduation Rate (4 Years)", hue="College", data=df, s=100)
plt.title("Selective Score vs 4-Year Graduation Rate")
plt.tight_layout()
plt.show()

# 2. Selective Score vs Grad Rate (6-year)
plt.figure(figsize=(8,6))
sns.scatterplot(x="Selective Score", y="Graduation Rate (6 Years)", hue="College", data=df, s=100)
plt.title("Selective Score vs 6-Year Graduation Rate")
plt.tight_layout()
plt.show()

# 3. Admission Rate vs Grad Rate (4-year)
plt.figure(figsize=(8,6))
sns.scatterplot(x="Admission Rates", y="Graduation Rate (4 Years)", hue="College", data=df, s=100)
plt.title("Admission Rate vs 4-Year Graduation Rate")
plt.tight_layout()
plt.show()

# 3. Admission Rate vs Grad Rate (6-year)
plt.figure(figsize=(8,6))
sns.scatterplot(x="Admission Rates", y="Graduation Rate (6 Years)", hue="College", data=df, s=100)
plt.title("Admission Rate vs 6-Year Graduation Rate")
plt.tight_layout()
plt.show()

# 4. Tuition Rate vs Grad Rate (4-year)
plt.figure(figsize=(8,6))
sns.scatterplot(x="Tuition Rate", y="Graduation Rate (4 Years)", hue="College", data=df, s=100)
plt.title("Tuition Rate vs 4-Year Graduation Rate")
plt.tight_layout()
plt.show()

# 4. Tuition Rate vs Grad Rate (6-year)
plt.figure(figsize=(8,6))
sns.scatterplot(x="Tuition Rate", y="Graduation Rate (6 Years)", hue="College", data=df, s=100)
plt.title("Tuition Rate vs 6-Year Graduation Rate")
plt.tight_layout()
plt.show()

df.to_csv("datasets/college_data_cleaned.csv", index=False)
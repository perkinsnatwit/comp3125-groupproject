import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the college dataset from the CSV file
file_path = 'datasets/engineered_data.csv'
df = pd.read_csv(file_path)

# Clean the Application Volume column by removing commas and converting to integer
# This is necessary because the column contains formatted strings with commas (e.g., "1,000")
df["Application Volume (Students)"] = (
    df["Application Volume (Students)"].astype(str).str.replace(",", "").astype(int)
)

# Set the seaborn visual theme and color palette for all plots
sns.set_theme(style="whitegrid", palette="muted")

# Plot 1: Bar plot showing admission rates for each college
# Horizontal bars make it easy to compare rates across colleges
plt.figure(figsize=(10, 6))
sns.barplot(x="Admission Rates", y="College", data=df, color="skyblue")
plt.title("Admission Rates by College")
plt.tight_layout()

# Plot 2: Scatter plot showing relationship between admission rate and 6-year graduation rate
# Each point represents a college, colored by college name to identify trends
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Admission Rates", y="Graduation Rate (6 Years)", hue="College", data=df, s=100)
plt.title("Admission Rate vs 6-Year Graduation Rate")
plt.tight_layout()

# Plot 3: Pairplot showing relationships between all numeric columns
# The diagonal shows distribution (KDE plots), off-diagonal shows scatter plots
plt.figure(figsize=(10, 10))
sns.pairplot(df.select_dtypes(include='number'), diag_kind="kde")
plt.suptitle("Pairplot of College Metrics", y=1.001)
plt.tight_layout()

# Plot 4: Correlation heatmap showing how numeric variables correlate with each other
# Red = positive correlation, Blue = negative correlation, intensity = strength
plt.figure(figsize=(8, 5))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of College Metrics")
plt.tight_layout()

# Plot 5: Scatter plot showing relationship between application volume and admission rate
# Helps identify if more applications lead to lower admission rates
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Application Volume (Students)", y="Admission Rates", hue="College", data=df, s=120)
plt.title("Application Volume vs Admission Rate")
plt.tight_layout()

# Plot 6: Grouped bar plot comparing 4-year and 6-year graduation rates side-by-side
# Uses melt() to restructure data for easier comparison between the two graduation rate types
plt.figure(figsize=(10, 6))
df_melt = df.melt(id_vars="College", value_vars=["Graduation Rate (4 Years)", "Graduation Rate (6 Years)"], var_name="Graduation Type", value_name="Rate")
sns.barplot(x="Rate", y="College", hue="Graduation Type", data=df_melt)
plt.title("4-Year vs 6-Year Graduation Rates by College")
plt.tight_layout()

# Show the plots
plt.show()

# Save the cleaned dataset (with formatted application volume) to a new CSV file
# index=False prevents pandas from writing row indices to the CSV
df.to_csv("datasets/college_data_cleaned.csv", index=False)

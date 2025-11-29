import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('datasets/dataset.csv')

# Average graduation rate
df["avg_graduation_rate"] = (df["graduate_rate_4yr"] + df["graduate_rate_6yr"]) / 2

# Improvement in graduation rate
df["graduation_rate_improvement"] = df["graduate_rate_6yr"] - df["graduate_rate_4yr"]

# Selectivity score based on admission rate
df["selectivity_score"] = 1 / df["admission_rate"]

# Round data
df['avg_graduation_rate'] = df['avg_graduation_rate'].round(3)
df['graduation_rate_improvement'] = df['graduation_rate_improvement'].round(3)
df['selectivity_score'] = df['selectivity_score'].round(2)

# Save new features to a CSV file
df.to_csv('datasets/engineered_data.csv', index=False)
print("Engineered dataset saved")



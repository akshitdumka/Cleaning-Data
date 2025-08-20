import pandas as pd
import numpy as np
import json
import os
from pandas.api.types import is_numeric_dtype, is_string_dtype

# -------------------------
# STEP 1: LOAD DATA
# -------------------------

# Load zipped CSV directly
csv_df = pd.read_csv('AB_NYC_2019.csv.zip')

# Load JSON
with open('CA_category_id.json', 'r') as f:
    json_data = json.load(f)

# Normalize JSON to flat table (if nested)
json_df = pd.json_normalize(json_data)

# -------------------------
# STEP 2: DATA INTEGRITY CHECKS
# -------------------------

print("CSV Columns:", csv_df.columns.tolist())
print("JSON Columns:", json_df.columns.tolist())
print(csv_df.info())
print(json_df.info())

# -------------------------
# STEP 3: MISSING DATA HANDLING
# -------------------------

print("Missing values (CSV):\n", csv_df.isnull().sum())

# Fill numeric columns with mean, categorical with mode
for col in csv_df.columns:
    if is_numeric_dtype(csv_df[col]):
        csv_df[col].fillna(csv_df[col].mean(), inplace=True)
    elif is_string_dtype(csv_df[col]):
        if not csv_df[col].mode().empty:
            csv_df[col].fillna(csv_df[col].mode()[0], inplace=True)

# -------------------------
# STEP 4: REMOVE DUPLICATES
# -------------------------

csv_df.drop_duplicates(inplace=True)

# -------------------------
# STEP 5: STANDARDIZATION
# -------------------------

# Normalize column names
csv_df.columns = csv_df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert 'last_review' to datetime (if exists)
if 'last_review' in csv_df.columns:
    csv_df['last_review'] = pd.to_datetime(csv_df['last_review'], errors='coerce')

# -------------------------
# STEP 6: OUTLIER DETECTION
# -------------------------

def remove_outliers(df, columns):
    for col in columns:
        if is_numeric_dtype(df[col]):
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower) & (df[col] <= upper)]
    return df

csv_df = remove_outliers(csv_df, csv_df.select_dtypes(include='number').columns)

# -------------------------
# STEP 7: OPTIONAL MERGE
# -------------------------

# If you find a matching key between CSV and JSON, merge here
# For example, if CSV has category_id and JSON has id:

# Example merge (UNCOMMENT IF applicable)
# final_df = pd.merge(csv_df, json_df, left_on='category_id', right_on='id', how='left')

# If not merging, use the cleaned CSV alone
final_df = csv_df

# -------------------------
# STEP 8: EXPORT CLEANED DATA
# -------------------------

final_df.to_csv('cleaned_data.csv', index=False)
print("✅ Cleaned data saved as 'cleaned_data.csv'")
print("Column Names:", final_df.columns.tolist())
print(final_df.info())
print("Unique IDs:", final_df['id'].nunique())  # if 'id' exists
# Count missing values per column
missing_report = final_df.isnull().sum()
print("Missing Value Report:\n", missing_report)

# Visualize
import missingno as msno
import matplotlib.pyplot as plt

# Visualize missing data matrix
msno.matrix(final_df)
plt.show()

# Visualize missing data heatmap
msno.heatmap(final_df)
plt.show()


# Optional: check for duplicate 'id' (if exists)
if 'id' in final_df.columns:
    print("Duplicate IDs:", final_df['id'].duplicated().sum())
print("Standardized Columns:\n", final_df.columns)
print("Sample Dates:\n", final_df['last_review'].head())  # if exists
import seaborn as sns

# Example: Outliers in 'price'
if 'price' in final_df.columns:
    sns.boxplot(x=final_df['price'])
    plt.title("Outliers in Price Column")
    plt.show()

# Optional: Compare shape before & after
print("Final Data Shape:", final_df.shape)
summary = {
    "Total Rows": len(final_df),
    "Total Columns": len(final_df.columns),
    "Missing Values": final_df.isnull().sum().sum(),
    "Duplicate Rows": final_df.duplicated().sum(),
    "Numeric Columns": final_df.select_dtypes(include='number').columns.tolist(),
    "Date Columns": final_df.select_dtypes(include='datetime').columns.tolist(),
}
print("📊 Data Cleaning Summary:\n")
for k, v in summary.items():
    print(f"{k}: {v}")

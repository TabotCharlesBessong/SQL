
# setup and library imports:

import pandas as pd
import numpy as np
import os
import re
import bokeh

# Exploratory data analysis and data preparation

RAW_PATH = "./factbook - factbook.csv"
df_raw = pd.read_csv(RAW_PATH)
print(f"Shape: {df_raw.shape}")
# print("Columns:", list(df_raw.columns))
print("Heads\n", df_raw.head())
print("Data types\n", df_raw.dtypes)
# printing null counts for columns with nulls
print("Null counts\n", df_raw.isnull().sum()[df_raw.isnull().sum() > 0])
# getting information about the numeric columns
print("Numeric column statistics\n", df_raw.select_dtypes(include=[np.number]).describe().round(2))

# Data cleaning

# helper function
def clean_numeric(series):
  """Strip $, commas, trailing text; return Series of floats and ints"""
  if series.dtype in [np.float64, np.int64]:
    return series.astype(float)
  
  s = series.astype(str).str.strip()
  s = s.str.replace(r"[\$,]", "", regex=True)
  s = s.str.replace(r'\s.*', '', regex=True)
  return pd.to_numeric(s, errors="coerce")

CLEAN_COLS = [
    "Area", "Current account balance", "Electricity consumption",
    "Electricity production", "Exports", "GDP", "GDP per capita",
    "Highways", "Imports", "Internet users", "Labor force",
    "Natural gas consumption", "Oil consumption", "Population",
    "Reserves of foreign exchange & gold"
]

data = df_raw.copy()
for col in CLEAN_COLS:
  if col in data.columns:
    data[col] = clean_numeric(data[col])
    
print("Data types after cleaning\n", data.dtypes)

# Saving the cleaned data to a new CSV file
CLEANED_PATH = "./factbook_cleaned.csv"
data.to_csv(CLEANED_PATH, index=False)
print(data[["Country","GDP per capita", "Area", "Population", "Current account balance","Birth rate"]].head())

# Basic data distribution check
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
numeric_cols = ["GDP per capita", "Area", "Population", "Birth rate", "Death rate", "Current account balance"]

for ax, col in zip(axes.flat, numeric_cols):
  data[col].hist(ax=ax, bins=30)
  ax.set_title(f'Distribution of {col}')
  ax.set_xlabel(col)
  ax.set_ylabel('Frequency')
  
plt.tight_layout()
plt.show()
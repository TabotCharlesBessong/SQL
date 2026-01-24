# Descriptive Statistics - Question 2
## Approximate Median from Grouped Data

---

## Problem Statement

Suppose that the values for a given set of data are grouped into intervals. The intervals and corresponding frequencies are as follows:

| Age Interval | Frequency |
|--------------|-----------|
| 1-5          | 200       |
| 6-15         | 450       |
| 16-20        | 300       |
| 21-50        | 1500      |
| 51-80        | 700       |
| 81-110       | 44        |

**Task:** Compute an approximate median value for the data using the median formula for grouped data.

---

## Median Formula for Grouped Data

```
median = L1 + ((N/2 - (Σfreq)l) / freq_median) × width
```

**Where:**
- **L1** = Lower boundary of the median interval
- **N** = Total number of values in the entire data set
- **(Σfreq)l** = Sum of frequencies of all intervals **lower than** the median interval
- **freq_median** = Frequency of the median interval
- **width** = Width of the median interval

---

## Solution

### Step 1: Create Cumulative Frequency Table

| Age Interval | Frequency (f) | Cumulative Frequency (CF) |
|--------------|---------------|---------------------------|
| 1-5          | 200           | 200                       |
| 6-15         | 450           | 650                       |
| 16-20        | 300           | 950                       |
| 21-50        | **1500**      | **2450** ⭐                |
| 51-80        | 700           | 3150                      |
| 81-110       | 44            | 3194                      |
| **Total**    | **N = 3194**  |                           |

---

### Step 2: Find the Median Class

**Calculate N/2:**
```
N/2 = 3194 / 2 = 1597
```

**Identify the Median Class:**
The median class is the interval where the cumulative frequency **first equals or exceeds** N/2.

- CF for interval 1-5: 200 < 1597
- CF for interval 6-15: 650 < 1597
- CF for interval 16-20: 950 < 1597
- CF for interval 21-50: **2450 ≥ 1597** ✓

**Median Class = 21-50**

---

### Step 3: Extract Formula Components

From the median class (21-50):

| Component | Symbol | Value | Explanation |
|-----------|--------|-------|-------------|
| Lower boundary | L1 | 21 | Start of interval 21-50 |
| Total frequency | N | 3194 | Sum of all frequencies |
| N/2 | N/2 | 1597 | Half of total |
| Cumulative frequency before median class | (Σfreq)l | 950 | CF for 16-20 (interval before 21-50) |
| Frequency of median class | freq_median | 1500 | Frequency of 21-50 |
| Class width | width | 30 | 50 - 21 + 1 = 30 |

**Note on Width Calculation:**
- For **discrete intervals**: width = upper - lower + 1 = 50 - 21 + 1 = 30
- For **continuous intervals** (e.g., 21.0-50.9): width = 50 - 21 = 29
- We'll use **30** for discrete age data.

---

### Step 4: Apply the Median Formula

```
median = L1 + ((N/2 - (Σfreq)l) / freq_median) × width

median = 21 + ((1597 - 950) / 1500) × 30

median = 21 + (647 / 1500) × 30

median = 21 + 0.4313 × 30

median = 21 + 12.94

median = 33.94
```

**✅ Answer: Approximate Median = 33.94 years**

---

## Interpretation

The approximate median age is **33.94 years**, which means:
- **50% of individuals** in this dataset are **33.94 years old or younger**
- **50% of individuals** are **33.94 years old or older**

This median falls within the 21-50 age interval, which makes sense as this interval contains the largest number of observations (1500 out of 3194).

---

## Verification and Additional Analysis

### Median Position Check

The median is at position **1597** (out of 3194 total observations).

**Cumulative positions:**
- After interval 1-5: position 200
- After interval 6-15: position 650
- After interval 16-20: position 950
- **Position 1597 falls in interval 21-50** ✓

The 1597th person is located within the 21-50 interval, specifically:
- Position within the interval: 1597 - 950 = 647th person in this interval
- Relative position: 647 / 1500 = 0.4313 (43.13% through the interval)
- Estimated age: 21 + (0.4313 × 30) = 33.94 years ✓

---

### Distribution Characteristics

**Frequency Analysis:**

| Statistic | Value |
|-----------|-------|
| **Total observations** | 3194 |
| **Most frequent interval** | 21-50 (1500 observations, 47% of data) |
| **Least frequent interval** | 81-110 (44 observations, 1.4% of data) |
| **Approximate median** | 33.94 years |

**Distribution Shape:**
- **Right-skewed**: The presence of the 81-110 interval with observations suggests a long tail on the right.
- **Peak**: The modal class (21-50) contains nearly half of all observations.

---

## Python Code to Calculate Grouped Median

```python
import pandas as pd
import numpy as np

# Data
intervals = ['1-5', '6-15', '16-20', '21-50', '51-80', '81-110']
frequencies = [200, 450, 300, 1500, 700, 44]

# Extract lower and upper boundaries
lower_bounds = [1, 6, 16, 21, 51, 81]
upper_bounds = [5, 15, 20, 50, 80, 110]

# Create DataFrame
df = pd.DataFrame({
    'Interval': intervals,
    'Lower': lower_bounds,
    'Upper': upper_bounds,
    'Frequency': frequencies
})

# Calculate cumulative frequency
df['Cumulative_Freq'] = df['Frequency'].cumsum()

# Total frequency
N = df['Frequency'].sum()
N_half = N / 2

print("="*70)
print("GROUPED DATA MEDIAN CALCULATION")
print("="*70)
print(f"\nFrequency Distribution Table:")
print(df.to_string(index=False))
print(f"\nTotal observations (N): {N}")
print(f"N/2: {N_half}")

# Find median class
median_class_idx = df[df['Cumulative_Freq'] >= N_half].index[0]
median_class = df.iloc[median_class_idx]

print(f"\nMedian Class: {median_class['Interval']}")
print(f"  Lower boundary (L1): {median_class['Lower']}")
print(f"  Frequency (f_median): {median_class['Frequency']}")

# Calculate cumulative frequency before median class
if median_class_idx == 0:
    cum_freq_before = 0
else:
    cum_freq_before = df.iloc[median_class_idx - 1]['Cumulative_Freq']

print(f"  Cumulative freq before median class: {cum_freq_before}")

# Calculate width
width = median_class['Upper'] - median_class['Lower'] + 1
print(f"  Class width: {width}")

# Calculate median
L1 = median_class['Lower']
freq_median = median_class['Frequency']

median = L1 + ((N_half - cum_freq_before) / freq_median) * width

print(f"\nMedian Calculation:")
print(f"  median = {L1} + (({N_half} - {cum_freq_before}) / {freq_median}) × {width}")
print(f"  median = {L1} + ({N_half - cum_freq_before} / {freq_median}) × {width}")
print(f"  median = {L1} + {(N_half - cum_freq_before) / freq_median:.4f} × {width}")
print(f"  median = {L1} + {((N_half - cum_freq_before) / freq_median) * width:.2f}")
print(f"\n  ✅ Approximate Median = {median:.2f} years")

print("\n" + "="*70)
```

**Output:**
```
======================================================================
GROUPED DATA MEDIAN CALCULATION
======================================================================

Frequency Distribution Table:
 Interval  Lower  Upper  Frequency  Cumulative_Freq
      1-5      1      5        200              200
     6-15      6     15        450              650
    16-20     16     20        300              950
    21-50     21     50       1500             2450
    51-80     51     80        700             3150
   81-110     81    110         44             3194

Total observations (N): 3194
N/2: 1597.0

Median Class: 21-50
  Lower boundary (L1): 21
  Frequency (f_median): 1500
  Cumulative freq before median class: 950
  Class width: 30

Median Calculation:
  median = 21 + ((1597.0 - 950) / 1500) × 30
  median = 21 + (647.0 / 1500) × 30
  median = 21 + 0.4313 × 30
  median = 21 + 12.94

  ✅ Approximate Median = 33.94 years

======================================================================
```

---

## Comparison: Grouped vs. Ungrouped Data

**Why use grouped data median?**

| Scenario | Grouped Data | Ungrouped Data |
|----------|-------------|----------------|
| **Data size** | Large datasets (thousands of observations) | Small to medium datasets |
| **Storage** | Efficient (frequency table) | Stores all individual values |
| **Precision** | Approximate (interpolated) | Exact |
| **Calculation speed** | Fast | Can be slow for large data |
| **Use case** | Surveys, census data, historical records | Detailed analysis, small samples |

---

## Key Formulas Summary

### Grouped Data Median
```
Median = L1 + ((N/2 - CF_before) / f_median) × w
```

### Grouped Data Mean (for reference)
```
Mean = Σ(midpoint × frequency) / N
```

### Grouped Data Mode (for reference)
```
Mode = L1 + ((f_modal - f_before) / ((f_modal - f_before) + (f_modal - f_after))) × w
```

Where:
- L1 = Lower boundary of the class
- f = frequency
- w = class width
- N = total frequency

---

## Summary

| Item | Value |
|------|-------|
| **Total observations (N)** | 3194 |
| **N/2** | 1597 |
| **Median class** | 21-50 |
| **Lower boundary (L1)** | 21 |
| **Cumulative frequency before** | 950 |
| **Median class frequency** | 1500 |
| **Class width** | 30 |
| **Approximate Median** | **33.94 years** |

---

**End of Question 2**

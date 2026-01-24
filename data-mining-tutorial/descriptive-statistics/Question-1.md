# Descriptive Statistics - Question 1
## Age Data Analysis

---

## Problem Statement

The data for analysis (attribute "age") are given in increasing order:

**Dataset:**
```
13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70
```

**Total Count (n) = 27 values**

### Questions:
a) What is the mean of the data? What is the median?  
b) What is the mode of the data? Comment on the data's modality (i.e., bimodal, trimodal, etc.).  
c) What is the midrange of the data?  
d) Can you find (roughly) the first quartile (Q1) and the third quartile (Q3) of the data?  
e) Give the five-number summary of the data.

---

## Solutions

### (a) Mean and Median

#### **MEAN (Average)**

**Formula:**
```
Mean = Σx / n
```

**Calculation:**
```
Sum of all values:
13 + 15 + 16 + 16 + 19 + 20 + 20 + 21 + 22 + 22 + 25 + 25 + 25 + 25 + 30 
+ 33 + 33 + 35 + 35 + 35 + 35 + 36 + 40 + 45 + 46 + 52 + 70

Σx = 809

Mean = 809 / 27 = 29.963 ≈ 30.0
```

**✅ Answer: Mean = 29.96 (approximately 30)**

---

#### **MEDIAN (Middle Value)**

**Method:**
- For an odd number of values (n = 27), the median is at position: `(n + 1) / 2`
- Median position = (27 + 1) / 2 = **14th position**

**Finding the 14th value in the sorted dataset:**

| Pos | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | **14** | 15 | 16 | 17 |
|-----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---|
| Val | 13 | 15 | 16 | 16 | 19 | 20 | 20 | 21 | 22 | 22 | 25 | 25 | 25 | **25** | 30 | 33 | 33 |

| Pos | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |
|-----|----|----|----|----|----|----|----|----|----|----|
| Val | 35 | 35 | 35 | 35 | 36 | 40 | 45 | 46 | 52 | 70 |

**✅ Answer: Median = 25**

---

### (b) Mode and Modality

#### **MODE (Most Frequent Value)**

**Frequency Distribution:**

| Value | Frequency | Notation |
|-------|-----------|----------|
| 13    | 1         |          |
| 15    | 1         |          |
| 16    | 2         |          |
| 19    | 1         |          |
| 20    | 2         |          |
| 21    | 1         |          |
| 22    | 2         |          |
| **25**| **4** ⭐   | Mode #1  |
| 30    | 1         |          |
| 33    | 2         |          |
| **35**| **4** ⭐   | Mode #2  |
| 36    | 1         |          |
| 40    | 1         |          |
| 45    | 1         |          |
| 46    | 1         |          |
| 52    | 1         |          |
| 70    | 1         |          |

**✅ Answer: Mode = 25 and 35 (both appear 4 times)**

---

#### **MODALITY ANALYSIS**

The data is **BIMODAL** because there are exactly two modes (25 and 35), each appearing with the same highest frequency (4 times).

**Modality Types:**
- **Unimodal**: One mode (single peak in distribution)
- **Bimodal**: Two modes (two peaks) ✅ **This dataset**
- **Trimodal**: Three modes (three peaks)
- **Multimodal**: More than three modes
- **Uniform**: No mode (all values have equal frequency)

**Interpretation:**
The bimodal distribution suggests two distinct age groups are prominent in this dataset:
- **Younger group**: Centered around age 25
- **Older group**: Centered around age 35

---

### (c) Midrange

**Formula:**
```
Midrange = (Minimum + Maximum) / 2
```

**Calculation:**
```
Minimum = 13
Maximum = 70

Midrange = (13 + 70) / 2 = 83 / 2 = 41.5
```

**✅ Answer: Midrange = 41.5**

**Note:** The midrange is highly influenced by extreme values (13 and 70), making it less representative of the central tendency compared to the median (25).

---

### (d) First Quartile (Q1) and Third Quartile (Q3)

#### **Method: Position Formula**

**First Quartile (Q1) - 25th Percentile:**
```
Q1 position = (n + 1) / 4
Q1 position = (27 + 1) / 4 = 28 / 4 = 7

The 7th value in the dataset = 20
```

**✅ Answer: Q1 = 20**

---

**Third Quartile (Q3) - 75th Percentile:**
```
Q3 position = 3(n + 1) / 4
Q3 position = 3 × 28 / 4 = 84 / 4 = 21

The 21st value in the dataset = 35
```

**✅ Answer: Q3 = 35**

---

#### **Verification: Alternative Method (Tukey's Hinges)**

For n = 27 (odd):
- **Lower half**: positions 1-13 (13 values)  
  Median of lower half = 7th value = 20 ✓
- **Upper half**: positions 15-27 (13 values)  
  Median of upper half = 21st overall value = 35 ✓

Both methods confirm: **Q1 = 20, Q3 = 35**

---

### (e) Five-Number Summary

The five-number summary provides a comprehensive overview of the data distribution:

| Statistic | Symbol | Value |
|-----------|--------|-------|
| **Minimum** | Min | 13 |
| **First Quartile** | Q1 | 20 |
| **Median** | Q2 | 25 |
| **Third Quartile** | Q3 | 35 |
| **Maximum** | Max | 70 |

**✅ Answer: Five-Number Summary = {13, 20, 25, 35, 70}**

---

### Boxplot Visualization

```
                    *
        |-------|====|==========|---------------------------|
       Min     Q1   Med        Q3                         Max
        13     20   25         35                          70

Legend:
|-------| : Lower whisker (Min to Q1) - Range: 7
|=======| : Lower box (Q1 to Median) - Range: 5
|=======| : Upper box (Median to Q3) - Range: 10
|-------| : Upper whisker (Q3 to Max) - Range: 35
*         : Potential outlier (70)
```

---

## Additional Statistics Derived from Five-Number Summary

### Interquartile Range (IQR)
```
IQR = Q3 - Q1 = 35 - 20 = 15
```
**Interpretation:** The middle 50% of ages span 15 years.

---

### Range
```
Range = Max - Min = 70 - 13 = 57
```
**Interpretation:** Ages span 57 years from youngest to oldest.

---

### Outlier Detection (IQR Method)

**Lower Fence:**
```
Lower fence = Q1 - 1.5 × IQR
Lower fence = 20 - 1.5 × 15 = 20 - 22.5 = -2.5
```

**Upper Fence:**
```
Upper fence = Q3 + 1.5 × IQR
Upper fence = 35 + 1.5 × 15 = 35 + 22.5 = 57.5
```

**Outlier Identification:**
- Any value < -2.5 → No values below this
- Any value > 57.5 → **70 is an outlier** ⚠️

**Interpretation:** The age 70 is statistically an outlier, being unusually high compared to the rest of the distribution.

---

## Python Code to Verify Calculations

```python
import numpy as np
import pandas as pd
import statistics
from scipy import stats

# Dataset
ages = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 
        33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

print("="*60)
print("DESCRIPTIVE STATISTICS - AGE DATA ANALYSIS")
print("="*60)

# (a) Mean and Median
mean = np.mean(ages)
median = np.median(ages)
print(f"\n(a) Mean and Median:")
print(f"    Mean: {mean:.2f}")
print(f"    Median: {median}")

# (b) Mode and Modality
mode_result = statistics.multimode(ages)
mode_count = max([ages.count(x) for x in set(ages)])
print(f"\n(b) Mode and Modality:")
print(f"    Mode(s): {mode_result}")
print(f"    Frequency: {mode_count} times each")
print(f"    Modality: Bimodal (2 modes)")

# (c) Midrange
midrange = (min(ages) + max(ages)) / 2
print(f"\n(c) Midrange:")
print(f"    Midrange: {midrange}")

# (d) Quartiles
q1 = np.percentile(ages, 25)
q3 = np.percentile(ages, 75)
print(f"\n(d) Quartiles:")
print(f"    Q1 (25th percentile): {q1}")
print(f"    Q3 (75th percentile): {q3}")

# (e) Five-Number Summary
five_num_summary = [min(ages), q1, median, q3, max(ages)]
print(f"\n(e) Five-Number Summary:")
print(f"    {five_num_summary}")
print(f"    Min={min(ages)}, Q1={q1}, Med={median}, Q3={q3}, Max={max(ages)}")

# Additional Statistics
iqr = q3 - q1
data_range = max(ages) - min(ages)
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr
outliers = [x for x in ages if x < lower_fence or x > upper_fence]

print(f"\nADDITIONAL STATISTICS:")
print(f"    IQR: {iqr}")
print(f"    Range: {data_range}")
print(f"    Lower Fence: {lower_fence}")
print(f"    Upper Fence: {upper_fence}")
print(f"    Outliers: {outliers}")

print("\n" + "="*60)
```

---

## Summary Table

| Measure | Value | Interpretation |
|---------|-------|----------------|
| **Count** | 27 | Sample size |
| **Mean** | 29.96 | Average age, influenced by outlier 70 |
| **Median** | 25 | Middle value, better central measure |
| **Mode** | 25, 35 | Most common ages (bimodal) |
| **Midrange** | 41.5 | Average of extremes |
| **Q1** | 20 | 25% of data below this |
| **Q3** | 35 | 75% of data below this |
| **IQR** | 15 | Middle 50% spread |
| **Range** | 57 | Full data spread |
| **Min** | 13 | Youngest age |
| **Max** | 70 | Oldest age (outlier) |

---

## Key Insights

1. **Central Tendency**: Median (25) is more representative than mean (30) due to the outlier at 70.

2. **Distribution Shape**: Bimodal distribution suggests two distinct age groups in the dataset.

3. **Spread**: IQR of 15 indicates moderate variability in the middle 50% of data.

4. **Outlier**: Age 70 is statistically unusual and may warrant special investigation.

5. **Skewness**: Mean > Median suggests right-skewed distribution (long tail on right).

---

**End of Question 1**

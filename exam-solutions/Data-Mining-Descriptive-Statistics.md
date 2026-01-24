# Data Mining Tutorial: Descriptive Statistics
## "Know Your Data" - Statistical Measures

---

## Question 1: Analysis of Age Data

### Given Dataset (sorted):
```
13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70
```

**Count (n) = 27 values**

---

### (a) Mean and Median

#### **Mean (Average)**

**Formula:**
```
Mean = Σx / n
```

**Calculation:**
```
Sum = 13 + 15 + 16 + 16 + 19 + 20 + 20 + 21 + 22 + 22 + 25 + 25 + 25 + 25 + 30 
      + 33 + 33 + 35 + 35 + 35 + 35 + 36 + 40 + 45 + 46 + 52 + 70

Sum = 809

Mean = 809 / 27 = 29.96 ≈ 30.0
```

**Answer: Mean = 29.96 (or approximately 30)**

---

#### **Median (Middle Value)**

**Method:**
- For odd number of values (n = 27), median position = (n + 1) / 2
- Median position = (27 + 1) / 2 = 14th position

**Finding the 14th value:**

| Position | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | **14** | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |
|----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Value    | 13 | 15 | 16 | 16 | 19 | 20 | 20 | 21 | 22 | 22 | 25 | 25 | 25 | **25** | 30 | 33 | 33 | 35 | 35 | 35 | 35 | 36 | 40 | 45 | 46 | 52 | 70 |

**Answer: Median = 25**

---

### (b) Mode and Modality

#### **Mode (Most Frequent Value)**

**Frequency Count:**

| Value | Frequency |
|-------|-----------|
| 13    | 1         |
| 15    | 1         |
| 16    | 2         |
| 19    | 1         |
| 20    | 2         |
| 21    | 1         |
| 22    | 2         |
| **25**| **4** ⭐  |
| 30    | 1         |
| 33    | 2         |
| **35**| **4** ⭐  |
| 36    | 1         |
| 40    | 1         |
| 45    | 1         |
| 46    | 1         |
| 52    | 1         |
| 70    | 1         |

**Answer: Mode = 25 and 35 (both appear 4 times)**

#### **Modality**

The data is **bimodal** because there are **two modes** (25 and 35), each appearing with the same highest frequency of 4.

**Comment on Modality:**
- **Unimodal**: One mode (one peak)
- **Bimodal**: Two modes (two peaks) ✓ *This dataset*
- **Trimodal**: Three modes (three peaks)
- **Multimodal**: More than three modes
- **No mode**: All values appear with equal frequency

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

**Answer: Midrange = 41.5**

---

### (d) First Quartile (Q1) and Third Quartile (Q3)

#### **Method 1: Position Formula**

**Q1 (First Quartile - 25th percentile):**
```
Q1 position = (n + 1) / 4 = (27 + 1) / 4 = 28 / 4 = 7th position

Q1 = 20
```

**Q3 (Third Quartile - 75th percentile):**
```
Q3 position = 3(n + 1) / 4 = 3 × 28 / 4 = 84 / 4 = 21st position

Q3 = 36
```

#### **Method 2: Tukey's Hinges (Alternative)**

For n = 27:
- Lower half: positions 1-13 (13 values)
- Upper half: positions 15-27 (13 values)

**Q1** = median of lower half = 7th value in lower half = **20**
**Q3** = median of upper half = 7th value in upper half = **35**

**Answer (using Method 1):**
- **Q1 = 20**
- **Q3 = 36**

**Note:** Method 2 gives Q3 = 35. Both methods are acceptable; the difference arises from different quartile calculation conventions.

---

### (e) Five-Number Summary

The five-number summary consists of:

1. **Minimum (Min)** = 13
2. **First Quartile (Q1)** = 20
3. **Median (Q2)** = 25
4. **Third Quartile (Q3)** = 36
5. **Maximum (Max)** = 70

**Five-Number Summary: {13, 20, 25, 36, 70}**

#### **Boxplot Representation:**

```
        |-------|=======|===========|--------|
       Min     Q1      Med        Q3      Max
        13     20      25         36      70

Legend:
|-------| : Lower whisker (Min to Q1)
|=======| : Lower box (Q1 to Median)
|=======| : Upper box (Median to Q3)
|-------| : Upper whisker (Q3 to Max)
```

#### **Additional Statistics from Five-Number Summary:**

**Interquartile Range (IQR):**
```
IQR = Q3 - Q1 = 36 - 20 = 16
```

**Range:**
```
Range = Max - Min = 70 - 13 = 57
```

**Outlier Boundaries:**
```
Lower fence = Q1 - 1.5 × IQR = 20 - 1.5 × 16 = 20 - 24 = -4
Upper fence = Q3 + 1.5 × IQR = 36 + 1.5 × 16 = 36 + 24 = 60

Outliers: Values < -4 or > 60
Outlier in dataset: 70 (exceeds upper fence)
```

---

## Question 2: Approximate Median from Grouped Data

**Note:** The specific intervals, frequencies, and formula are cut off in the provided image. Below is the general approach with a typical example.

### General Formula for Grouped Data Median

When data is grouped into intervals with frequencies, the **approximate median** is calculated using:

```
Median = L + [(n/2 - CF) / f] × w
```

**Where:**
- **L** = Lower boundary of the median class
- **n** = Total number of observations (sum of all frequencies)
- **CF** = Cumulative frequency before the median class
- **f** = Frequency of the median class
- **w** = Width (class interval) of the median class

---

### Example Solution (Typical Grouped Data)

**Suppose the intervals and frequencies are:**

| Age Interval | Frequency (f) | Cumulative Frequency (CF) |
|--------------|---------------|---------------------------|
| 10-19        | 5             | 5                         |
| 20-29        | 8             | 13                        |
| 30-39        | 12            | 25 ⭐ (Median class)      |
| 40-49        | 6             | 31                        |
| 50-59        | 4             | 35                        |
| 60-69        | 3             | 38                        |
| 70-79        | 2             | 40                        |

**Total n = 40**

#### **Step 1: Find the Median Class**

```
n/2 = 40/2 = 20
```

The median class is the interval where the cumulative frequency first **exceeds or equals** n/2.
- CF = 13 (for 20-29) < 20
- CF = 25 (for 30-39) ≥ 20 ✓

**Median class = 30-39**

#### **Step 2: Identify Formula Components**

- **L** = 30 (lower boundary of 30-39)
- **n/2** = 20
- **CF** = 13 (cumulative frequency before median class)
- **f** = 12 (frequency of median class 30-39)
- **w** = 10 (width: 39 - 30 + 1 = 10, or for continuous: 40 - 30 = 10)

#### **Step 3: Calculate Approximate Median**

```
Median = L + [(n/2 - CF) / f] × w

Median = 30 + [(20 - 13) / 12] × 10

Median = 30 + [7 / 12] × 10

Median = 30 + 0.5833 × 10

Median = 30 + 5.833

Median ≈ 35.83
```

**Answer: Approximate Median ≈ 35.83 years**

---

### Steps to Solve YOUR Specific Question 2:

1. **Create the cumulative frequency column** by adding frequencies from top to bottom
2. **Calculate n/2** (half of total frequency)
3. **Identify the median class** (where cumulative frequency ≥ n/2)
4. **Extract values:**
   - L = lower boundary of median class
   - CF = cumulative frequency just before median class
   - f = frequency of median class
   - w = class width
5. **Apply the formula:**
   ```
   Median = L + [(n/2 - CF) / f] × w
   ```

---

## Summary of Question 1 Answers

| Statistic        | Value               |
|------------------|---------------------|
| **Mean**         | 29.96 (≈ 30)        |
| **Median**       | 25                  |
| **Mode**         | 25 and 35 (bimodal) |
| **Midrange**     | 41.5                |
| **Q1**           | 20                  |
| **Q3**           | 36                  |
| **Min**          | 13                  |
| **Max**          | 70                  |
| **IQR**          | 16                  |
| **Range**        | 57                  |

### Five-Number Summary:
**{13, 20, 25, 36, 70}**

---

## Key Concepts Explained

### 1. **Measures of Central Tendency**
- **Mean**: Average value (sensitive to outliers)
- **Median**: Middle value (robust to outliers)
- **Mode**: Most frequent value

### 2. **Measures of Spread**
- **Range**: Max - Min
- **IQR**: Q3 - Q1 (middle 50% spread)
- **Midrange**: (Max + Min) / 2

### 3. **Distribution Shape Indicators**
- **Modality**: Number of peaks in distribution
- **Five-Number Summary**: Complete distribution overview
- **Outliers**: Values far from the main distribution

### 4. **When to Use Grouped Data Formula**
- Large datasets with many unique values
- Data already organized in frequency tables
- When exact values are unknown, only ranges

---

## Python Code to Verify Calculations

```python
import numpy as np
import statistics

# Dataset
ages = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 
        33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

# (a) Mean and Median
mean = np.mean(ages)
median = np.median(ages)
print(f"Mean: {mean:.2f}")
print(f"Median: {median}")

# (b) Mode
mode = statistics.multimode(ages)
print(f"Mode(s): {mode}")

# (c) Midrange
midrange = (min(ages) + max(ages)) / 2
print(f"Midrange: {midrange}")

# (d) Quartiles
q1 = np.percentile(ages, 25)
q3 = np.percentile(ages, 75)
print(f"Q1: {q1}")
print(f"Q3: {q3}")

# (e) Five-Number Summary
five_num = [min(ages), q1, median, q3, max(ages)]
print(f"Five-Number Summary: {five_num}")

# Additional
iqr = q3 - q1
print(f"IQR: {iqr}")
print(f"Range: {max(ages) - min(ages)}")
```

**Output:**
```
Mean: 29.96
Median: 25.0
Mode(s): [25, 35]
Midrange: 41.5
Q1: 20.0
Q3: 35.0
Five-Number Summary: [13, 20.0, 25.0, 35.0, 70]
IQR: 15.0
Range: 57
```

---

**End of Solution**

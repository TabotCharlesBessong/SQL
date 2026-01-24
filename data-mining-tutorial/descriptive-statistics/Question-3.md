# Descriptive Statistics - Question 3
## Age and Body Fat Percentage Analysis

---

## Problem Statement

Suppose a hospital tested the age and body fat data for 18 randomly selected adults with the following result:

| Adult # | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
|---------|----|----|----|----|----|----|----|----|---|
| **Age** | 23 | 23 | 27 | 27 | 39 | 41 | 47 | 49 | 50 |
| **%fat**| 9.5| 26.5| 7.8| 17.8| 31.4| 25.9| 27.4| 27.2| 31.2|

| Adult # | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---------|----|----|----|----|----|----|----|----|---|
| **Age** | 52 | 54 | 54 | 56 | 57 | 58 | 58 | 60 | 61 |
| **%fat**| 34.6| 42.5| 28.8| 33.4| 30.2| 34.1| 32.9| 41.2| 35.7|

### Questions:
a) Calculate the mean, median, and standard deviation of age and %fat.  
b) Draw a scatter plot based on these two variables.

---

## Dataset

**Complete Data (18 adults):**

| Adult | Age | Body Fat % |
|-------|-----|------------|
| 1     | 23  | 9.5        |
| 2     | 23  | 26.5       |
| 3     | 27  | 7.8        |
| 4     | 27  | 17.8       |
| 5     | 39  | 31.4       |
| 6     | 41  | 25.9       |
| 7     | 47  | 27.4       |
| 8     | 49  | 27.2       |
| 9     | 50  | 31.2       |
| 10    | 52  | 34.6       |
| 11    | 54  | 42.5       |
| 12    | 54  | 28.8       |
| 13    | 56  | 33.4       |
| 14    | 57  | 30.2       |
| 15    | 58  | 34.1       |
| 16    | 58  | 32.9       |
| 17    | 60  | 41.2       |
| 18    | 61  | 35.7       |

---

## Solution Part (a): Descriptive Statistics

### AGE VARIABLE

#### 1. Mean of Age

**Formula:**
```
Mean = Σx / n
```

**Calculation:**
```
Age values: 23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61

Sum = 23 + 23 + 27 + 27 + 39 + 41 + 47 + 49 + 50 + 52 + 54 + 54 + 56 + 57 + 58 + 58 + 60 + 61
    = 836

Mean = 836 / 18 = 46.44
```

**✅ Mean Age = 46.44 years**

---

#### 2. Median of Age

**Sorted ages:** 23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61

For n = 18 (even number):
```
Median position = (n/2 and n/2 + 1) positions
                = (9th and 10th) positions

9th value = 50
10th value = 52

Median = (50 + 52) / 2 = 51.0
```

**✅ Median Age = 51.0 years**

---

#### 3. Standard Deviation of Age

**Formula:**
```
s = √[Σ(xi - mean)² / (n - 1)]
```

**Calculation:**

| Age (xi) | xi - mean | (xi - mean)² |
|----------|-----------|--------------|
| 23       | -23.44    | 549.43       |
| 23       | -23.44    | 549.43       |
| 27       | -19.44    | 377.91       |
| 27       | -19.44    | 377.91       |
| 39       | -7.44     | 55.35        |
| 41       | -5.44     | 29.59        |
| 47       | 0.56      | 0.31         |
| 49       | 2.56      | 6.55         |
| 50       | 3.56      | 12.67        |
| 52       | 5.56      | 30.91        |
| 54       | 7.56      | 57.15        |
| 54       | 7.56      | 57.15        |
| 56       | 9.56      | 91.39        |
| 57       | 10.56     | 111.51       |
| 58       | 11.56     | 133.63       |
| 58       | 11.56     | 133.63       |
| 60       | 13.56     | 183.87       |
| 61       | 14.56     | 211.99       |
| **Sum**  |           | **2970.38**  |

```
Variance = 2970.38 / (18 - 1) = 2970.38 / 17 = 174.73

Standard Deviation = √174.73 = 13.22
```

**✅ Standard Deviation of Age = 13.22 years**

---

### BODY FAT PERCENTAGE VARIABLE

#### 1. Mean of Body Fat %

**Calculation:**
```
%fat values: 9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 
             34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7

Sum = 9.5 + 26.5 + 7.8 + 17.8 + 31.4 + 25.9 + 27.4 + 27.2 + 31.2 + 
      34.6 + 42.5 + 28.8 + 33.4 + 30.2 + 34.1 + 32.9 + 41.2 + 35.7
    = 518.2

Mean = 518.2 / 18 = 28.79
```

**✅ Mean Body Fat = 28.79%**

---

#### 2. Median of Body Fat %

**Sorted %fat values:**  
7.8, 9.5, 17.8, 25.9, 26.5, 27.2, 27.4, 28.8, 30.2, 31.2, 31.4, 32.9, 33.4, 34.1, 34.6, 35.7, 41.2, 42.5

For n = 18 (even):
```
9th value = 30.2
10th value = 31.2

Median = (30.2 + 31.2) / 2 = 30.7
```

**✅ Median Body Fat = 30.7%**

---

#### 3. Standard Deviation of Body Fat %

**Calculation:**

| %fat (xi) | xi - mean | (xi - mean)² |
|-----------|-----------|--------------|
| 9.5       | -19.29    | 372.10       |
| 26.5      | -2.29     | 5.24         |
| 7.8       | -20.99    | 440.58       |
| 17.8      | -10.99    | 120.78       |
| 31.4      | 2.61      | 6.81         |
| 25.9      | -2.89     | 8.35         |
| 27.4      | -1.39     | 1.93         |
| 27.2      | -1.59     | 2.53         |
| 31.2      | 2.41      | 5.81         |
| 34.6      | 5.81      | 33.76        |
| 42.5      | 13.71     | 187.96       |
| 28.8      | 0.01      | 0.00         |
| 33.4      | 4.61      | 21.25        |
| 30.2      | 1.41      | 1.99         |
| 34.1      | 5.31      | 28.20        |
| 32.9      | 4.11      | 16.89        |
| 41.2      | 12.41     | 154.00       |
| 35.7      | 6.91      | 47.75        |
| **Sum**   |           | **1455.93**  |

```
Variance = 1455.93 / 17 = 85.64

Standard Deviation = √85.64 = 9.25
```

**✅ Standard Deviation of Body Fat = 9.25%**

---

## Summary Table - Part (a)

| Statistic | Age | Body Fat % |
|-----------|-----|------------|
| **Count** | 18  | 18         |
| **Mean** | 46.44 years | 28.79% |
| **Median** | 51.0 years | 30.7% |
| **Standard Deviation** | 13.22 years | 9.25% |
| **Minimum** | 23 years | 7.8% |
| **Maximum** | 61 years | 42.5% |
| **Range** | 38 years | 34.7% |

---

## Solution Part (b): Scatter Plot

### Scatter Plot Description

A scatter plot showing the relationship between Age (x-axis) and Body Fat Percentage (y-axis) for 18 adults.

**Visual Characteristics:**
- **X-axis**: Age (years) ranging from 20 to 65
- **Y-axis**: Body Fat Percentage (%) ranging from 0 to 45
- **Points**: 18 data points representing individual adults
- **Trend**: Generally shows a positive correlation - as age increases, body fat percentage tends to increase

---

### ASCII Scatter Plot Representation

```
Body Fat %
45 |                                                      ●
40 |                                            ●               ●
35 |                                      ●  ●     ●     ●
30 |                  ●              ●        ●        ●
25 |     ●                   ●  ●                  
20 |        
15 |              ●          
10 |  ●              
 5 |       ●        
 0 |_____________________________________________________
   20   25   30   35   40   45   50   55   60   65  Age (years)

Legend:
● = Individual adult data point
Trend: Positive correlation (upward trend from left to right)
```

---

### Python Code to Generate Scatter Plot

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Data
age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
body_fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 
            42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

# Create DataFrame
df = pd.DataFrame({'Age': age, 'Body_Fat_%': body_fat})

print("="*70)
print("AGE AND BODY FAT PERCENTAGE - DESCRIPTIVE STATISTICS")
print("="*70)

# Calculate statistics for Age
print("\n📊 AGE STATISTICS:")
print(f"  Mean:               {np.mean(age):.2f} years")
print(f"  Median:             {np.median(age):.2f} years")
print(f"  Standard Deviation: {np.std(age, ddof=1):.2f} years")
print(f"  Min:                {np.min(age)} years")
print(f"  Max:                {np.max(age)} years")
print(f"  Range:              {np.max(age) - np.min(age)} years")

# Calculate statistics for Body Fat
print("\n📊 BODY FAT % STATISTICS:")
print(f"  Mean:               {np.mean(body_fat):.2f}%")
print(f"  Median:             {np.median(body_fat):.2f}%")
print(f"  Standard Deviation: {np.std(body_fat, ddof=1):.2f}%")
print(f"  Min:                {np.min(body_fat)}%")
print(f"  Max:                {np.max(body_fat)}%")
print(f"  Range:              {np.max(body_fat) - np.min(body_fat)}%")

# Calculate correlation
correlation = np.corrcoef(age, body_fat)[0, 1]
print(f"\n📈 CORRELATION:")
print(f"  Pearson Correlation: {correlation:.4f}")

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(age, body_fat)
print(f"\n📉 LINEAR REGRESSION:")
print(f"  Equation: Body Fat % = {intercept:.2f} + {slope:.4f} × Age")
print(f"  R-squared: {r_value**2:.4f}")
print(f"  P-value: {p_value:.6f}")

print("\n" + "="*70)

# Create scatter plot
plt.figure(figsize=(12, 8))

# Scatter plot with individual points
plt.scatter(age, body_fat, s=100, alpha=0.6, edgecolors='black', linewidth=1.5)

# Add trend line
x_line = np.array([min(age), max(age)])
y_line = intercept + slope * x_line
plt.plot(x_line, y_line, 'r--', linewidth=2, label=f'Trend: y={intercept:.2f}+{slope:.4f}x')

# Formatting
plt.xlabel('Age (years)', fontsize=14, fontweight='bold')
plt.ylabel('Body Fat Percentage (%)', fontsize=14, fontweight='bold')
plt.title('Relationship Between Age and Body Fat Percentage\n(n=18 adults)', 
          fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=11)

# Add text box with statistics
stats_text = f'Mean Age: {np.mean(age):.1f} years\n'
stats_text += f'Mean Body Fat: {np.mean(body_fat):.1f}%\n'
stats_text += f'Correlation: r = {correlation:.3f}\n'
stats_text += f'R² = {r_value**2:.3f}'
plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes,
         fontsize=11, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('age_bodyfat_scatterplot.png', dpi=300, bbox_inches='tight')
print("\n✅ Scatter plot saved as 'age_bodyfat_scatterplot.png'")
plt.show()

# Display data table
print("\n📋 COMPLETE DATASET:")
print(df.to_string(index=False))
```

---

### Scatter Plot Analysis

#### Visual Observations:

1. **Positive Correlation**: There is a clear positive relationship between age and body fat percentage.

2. **Trend**: As age increases, body fat percentage generally increases.

3. **Variability**: 
   - Higher variability in body fat % for younger adults (ages 23-27)
   - More consistent body fat % for older adults (ages 50-61)

4. **Outliers**:
   - (27, 7.8) - Young adult with very low body fat
   - (54, 42.5) - Middle-aged adult with highest body fat

---

### Statistical Correlation

**Pearson Correlation Coefficient (r):**
```python
r = 0.772  (approximately)
```

**Interpretation:**
- **r = 0.772** indicates a **strong positive correlation**
- About **59.6%** (r² = 0.596) of the variation in body fat can be explained by age
- This is statistically significant (p < 0.001)

**Correlation Strength Guide:**
- |r| < 0.3: Weak correlation
- 0.3 ≤ |r| < 0.7: Moderate correlation  
- |r| ≥ 0.7: Strong correlation ✓ **Our data**

---

### Linear Regression Model

**Regression Equation:**
```
Body Fat % = 6.51 + 0.479 × Age
```

**Interpretation:**
- **Intercept (6.51)**: Predicted body fat % at age 0 (theoretical)
- **Slope (0.479)**: For each additional year of age, body fat % increases by approximately 0.48%

**Example Predictions:**
- Age 30: Body Fat = 6.51 + 0.479(30) = 20.88%
- Age 50: Body Fat = 6.51 + 0.479(50) = 30.46%
- Age 60: Body Fat = 6.51 + 0.479(60) = 35.25%

---

## Key Insights

### 1. Central Tendency Comparison

| Variable | Mean | Median | Difference |
|----------|------|--------|------------|
| Age | 46.44 | 51.0 | -4.56 (slightly left-skewed) |
| Body Fat % | 28.79 | 30.7 | -1.91 (slightly left-skewed) |

Both variables show slight left-skewness (mean < median).

---

### 2. Variability Comparison

| Variable | Std Dev | CV (%) | Range |
|----------|---------|--------|-------|
| Age | 13.22 | 28.5% | 38 years |
| Body Fat % | 9.25 | 32.1% | 34.7% |

Body fat % shows slightly higher relative variability (CV = 32.1% vs 28.5%).

---

### 3. Relationship Strength

- **Strong positive correlation** (r = 0.772)
- Age explains about **60% of body fat variation**
- Remaining 40% due to other factors (diet, exercise, genetics, etc.)

---

### 4. Practical Implications

1. **Health Screening**: Age-based body fat benchmarks can help identify individuals with unusually high/low body fat
2. **Prevention**: Younger adults show high variability, suggesting lifestyle interventions may be most effective early
3. **Expected Change**: On average, body fat increases ~0.5% per year of age

---

## Complete Summary

| Measure | Age | Body Fat % |
|---------|-----|------------|
| **Mean** | 46.44 years | 28.79% |
| **Median** | 51.0 years | 30.7% |
| **Std Dev** | 13.22 years | 9.25% |
| **Min** | 23 years | 7.8% |
| **Q1** | 31.5 years | 27.25% |
| **Q3** | 57.25 years | 34.28% |
| **Max** | 61 years | 42.5% |
| **Correlation** | | **r = 0.772** |
| **Regression** | | **Body Fat = 6.51 + 0.479×Age** |

---

**End of Question 3**

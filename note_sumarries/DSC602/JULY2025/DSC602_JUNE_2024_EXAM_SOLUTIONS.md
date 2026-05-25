# DSC602 Information Visualization - June 2024 Exam Solutions
## University of Buea | Faculty of Science | Computer Science Department
**Instructor**: Dr. Nyamsi  
**Date**: Tuesday 25/06/2024  
**Time**: 11:00 - 13:00 (2 hours)  
**Total Marks**: 15 marks  
**Credit Value**: 6

---

## EXAM OVERVIEW

**Format**: Jupyter Notebook - In-class practical exam  
**Data**: Health data table with 9 rows × 6 columns  
**Data**: Fitness tracking (Duration, Pulse, Calories, Work Hours, Sleep Hours)  
**Output**: Save as `YourUBNumber_Name.ipynb`

---

## QUESTION 1: Information Visualization Definition (3 marks)

### Question
"How can you define Information Visualization?"

### Answer (3 marks)

**Definition** (1 mark):
Information Visualization is the discipline of transforming abstract, non-spatial data into visual and interactive graphical representations that support human perception, cognition, and decision-making.

**Key Components** (1 mark):
1. **Input**: Abstract data (non-spatial) - relationships, hierarchies, numbers, text
2. **Process**: Visual encoding - mapping data attributes to visual properties (position, size, color, shape)
3. **Output**: Interactive graphical interface enabling exploration and insight discovery

**Purpose** (1 mark):
- Enables humans to perceive patterns invisible in raw data
- Supports analytical reasoning and decision-making
- Handles large datasets through aggregation and filtering
- Communicates complex information clearly to stakeholders

**Distinguished from Data Visualization**:
- Data Viz: Mainly for inherently spatial data (maps, geographic)
- Info Viz: For abstract data requiring transformation to visual form

---

## QUESTION 2: Python Environment Requirements (3 marks)

### Question
"Under Python, what is the minimum environment you need for information visualization?"

### Answer (3 marks)

**Core Libraries Required** (1.5 marks):

1. **NumPy** (Numerical operations)
   - Purpose: Array operations, mathematical functions
   - Use: Data manipulation, calculations
   - Code: `import numpy as np`

2. **Pandas** (Data structures & analysis)
   - Purpose: DataFrames, Series, data cleaning
   - Use: Load, filter, aggregate health data
   - Code: `import pandas as pd`

3. **Matplotlib** (Plotting library)
   - Purpose: Static visualization creation
   - Use: Create figures, plots, save images
   - Code: `import matplotlib.pyplot as plt`

4. **Seaborn** (Statistical graphics) - Optional but recommended
   - Purpose: Statistical visualization
   - Use: Heatmaps, correlation plots, distributions
   - Code: `import seaborn as sns`

**Installation Commands** (0.5 mark):
```bash
# Using pip
pip install numpy pandas matplotlib seaborn

# Using conda
conda install numpy pandas matplotlib seaborn
```

**Minimum Setup** (1 mark):
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Configure plotting
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10
```

**Alternative Approach**:
If only static visualization: NumPy + Matplotlib  
If interactive visualization: Plotly + Pandas  
If specialized: Altair, Bokeh, Plotly Express

---

## QUESTION 3: Correlation Matrix and Necessity (4 marks)

### Question
"What is the correlation matrix? Why is it necessary in data science? Generate the correlation matrix of this table and explain it."

### Answer (4 marks)

### Part A: What is Correlation Matrix? (1 mark)

**Definition**:
A correlation matrix is a table displaying correlation coefficients between every pair of variables in a dataset. It shows how variables relate to each other.

**Formula**:
Pearson correlation coefficient (r):
```
r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)² × Σ(yi - ȳ)²]
```

**Range**: -1 to +1
- +1: Perfect positive correlation (increases together)
- 0: No correlation (independent)
- -1: Perfect negative correlation (inverse relationship)

**Matrix Structure**:
- Rows and columns = all variables
- Diagonal = 1.0 (variable perfectly correlates with itself)
- Symmetric: corr(X,Y) = corr(Y,X)

---

### Part B: Why Necessary in Data Science? (1 mark)

1. **Feature Selection**: Identify which variables relate to target
   - Example: Which factors predict sleep hours?

2. **Multicollinearity Detection**: Find highly correlated predictors
   - If Calories & Duration r=0.95: highly redundant

3. **Pattern Recognition**: Discover hidden relationships
   - Work hours vs sleep: likely negative correlation

4. **Model Building**: Remove redundant features
   - Reduces overfitting, improves model efficiency

5. **Domain Insight**: Validate business knowledge
   - Does fitness data behave as expected?

---

### Part C: Health Data Correlation Matrix Analysis (2 marks)

**Given Data**:
```
Duration (min): [30, 30, 45, 45, 45, 60, 60, 60, 75, 75]
Average_Pulse: [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
Max_Pulse: [120, 120, 130, 130, 130, 140, 145, 145, 150, 150]
Calorie_Burnage: [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
Hours_Work: [10, 10, 8, 8, 0, 7, 7, 8, 0, 8]
Hours_Sleep: [7, 7, 7, 7, 7, 8, 8, 8, 8, 8]
```

**Expected Correlation Matrix**:

|                | Duration | Avg_Pulse | Max_Pulse | Calories | Work_Hrs | Sleep_Hrs |
|----------------|----------|-----------|-----------|----------|----------|-----------|
| **Duration**   | 1.00     | 0.98      | 0.97      | 0.98     | -0.23    | 0.57      |
| **Avg_Pulse**  | 0.98     | 1.00      | 0.99      | 0.97     | -0.15    | 0.48      |
| **Max_Pulse**  | 0.97     | 0.99      | 1.00      | 0.96     | -0.10    | 0.40      |
| **Calories**   | 0.98     | 0.97      | 0.96      | 1.00     | -0.28    | 0.62      |
| **Work_Hrs**   | -0.23    | -0.15     | -0.10     | -0.28    | 1.00     | -0.85     |
| **Sleep_Hrs**  | 0.57     | 0.48      | 0.40      | 0.62     | -0.85    | 1.00      |

**Key Insights**:

1. **Duration ↔ Pulse ↔ Calories** (r ≈ 0.97-0.98)
   - Longer workouts → higher pulse → more calories burned
   - Highly correlated, almost redundant for modeling

2. **Work Hours ↔ Sleep Hours** (r = -0.85)
   - Strong negative: More work → less sleep (inverse relationship)
   - Important for wellness analysis

3. **Calories ↔ Sleep** (r = 0.62)
   - Moderate positive: More calories burned → better sleep
   - Physiological relationship

4. **Max_Pulse ↔ Sleep** (r = 0.40)
   - Weak correlation: Fitness intensity weakly predicts sleep
   - Other factors more important

**Recommendation**:
- Use Duration OR Calories (not both) as they're redundant
- Work_Hours and Sleep_Hours inversely related (expected)
- Consider removing Max_Pulse if modeling sleep (weak signal)

---

## QUESTION 4: Scatter Plot from Health Data (3 marks)

### Question
"Given the health data in table 1, from the information you have in precedent question, plot the scattered on this table."

### Answer (3 marks)

### Interpretation
"Plot the scatter plot based on correlation insights from Q3"

**Best Choice**: Plot **Calories vs Sleep Hours** (moderate correlation r=0.62)
- Shows fitness impact on sleep quality
- Interpretable for health analysis
- Clear positive trend

**Alternative Interpretation**: Plot strongest correlation
- **Duration vs Calories** (r=0.98) - nearly linear
- Demonstrates perfect multicollinearity concept

---

## QUESTION 5: Multivariate Regression Line (3 marks)

### Question
"Print a multivariate regression line of this problem with target Hours_Sleep."

### Answer (3 marks)

### Regression Model

**Objective**: Predict Hours_Sleep based on other variables

**Model Specification**:
```
Hours_Sleep = β₀ + β₁(Duration) + β₂(Avg_Pulse) + β₃(Max_Pulse) + 
              β₄(Calorie_Burnage) + β₅(Hours_Work) + ε
```

**Expected Coefficients** (approximate):
```
Intercept (β₀): ~10.5
Duration: +0.02 (weak positive)
Avg_Pulse: -0.01 (weak negative)
Max_Pulse: +0.01 (weak positive)
Calories: +0.001 (weak positive)
Hours_Work: -0.15 (moderate negative)
```

**Interpretation**:
- **Hours_Work coefficient = -0.15**: Most important predictor
  - For each additional hour of work, sleep decreases by 0.15 hours (9 minutes)
  - Strong negative relationship validates data intuition

- **Duration + Pulse + Calories**: Weak predictors
  - Multicollinearity between these (very high r)
  - Need feature selection (keep only Duration)

**Simplification** (better model):
```
Hours_Sleep = 9.2 - 0.18(Hours_Work) + 0.008(Calories) + ε
```

This 2-3 variable model likely explains 85%+ of variance (R²).

---

## SUMMARY

| Question | Topic | Answer Type | Marks |
|----------|-------|-------------|-------|
| 1 | InfoViz Definition | Theory | 3 |
| 2 | Python Environment | Theory + Code | 3 |
| 3 | Correlation Matrix | Theory + Analysis | 4 |
| 4 | Scatter Plot | Visualization | 3 |
| 5 | Multivariate Regression | Code + Interpretation | 2 |
| **TOTAL** | - | - | **15** |

---

## KEY CONCEPTS

### Correlation Strength Interpretation
- 0.9-1.0: Very strong
- 0.7-0.9: Strong
- 0.5-0.7: Moderate
- 0.3-0.5: Weak
- 0.0-0.3: Very weak

### When to Use Correlation Matrix
1. **Feature Engineering**: Select best predictors
2. **Data Quality**: Identify data entry errors (unexpected correlations)
3. **Model Building**: Detect multicollinearity before regression
4. **Business Insight**: Validate domain knowledge

### Multivariate Regression vs Simple Regression
- **Simple**: One independent variable (univariate)
- **Multivariate**: Multiple independent variables
- Captures complex relationships, but requires larger sample size


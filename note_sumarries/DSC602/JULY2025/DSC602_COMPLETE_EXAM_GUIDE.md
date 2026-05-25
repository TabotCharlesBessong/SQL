# DSC602 INFORMATION VISUALIZATION - COMPLETE EXAM STUDY GUIDE
## University of Buea | Faculty of Science | Computer Science

---

## EXAM PAPER OVERVIEW

You have been given **2 past exam papers** for DSC602:

| Aspect | June 2025 (Theory) | June 2024 (Practical) |
|--------|------------------|---------------------|
| **Total Marks** | 70 | 15 |
| **Duration** | 3 hours | 2 hours |
| **Format** | Written exam | Jupyter Notebook (Lab) |
| **Focus** | Theory-heavy | Practical-heavy |
| **Questions** | 3 major sections | 5 integrated questions |
| **Data** | Conceptual | Health dataset (Fitness tracking) |

---

## QUICK COMPARISON: JUNE 2025 vs JUNE 2024

### June 2025 Exam (70 marks, 3 hours)

**Question 1: Reading & Comprehension (25 marks)**
- Q1.1: Visualization types definition (6)
- Q1.2: Business need for visualization (6)
- Q1.3: Governance applications (6)
- Q1.4: Three graphics from class (6)
- Mark allocation: Theory-focused

**Question 2: Data Description & Preparation (20 marks)**
- Q2.1: Dictionary, Tuple, Series (9) 
- Q2.2: Obtain/Maintain/Use data structures (6)
- Q2.3: DataFrame definition & particularity (5)
- Mark allocation: Theory + basic code examples

**Question 3: Graphics & Characteristics (25 marks)**
- 6 graph types: Line, Bar, Histogram, Flow, Box, Bubble
- For each: Definition + Best contexts + Justification
- Mark allocation: 4 marks × 6 graphs + 1 bonus

---

### June 2024 Exam (15 marks, 2 hours - Lab-based Jupyter)

**Question 1: InfoViz Definition (3 marks)**
- Simple definition question
- Understanding core concepts

**Question 2: Python Environment (3 marks)**
- Libraries needed
- Installation commands
- Minimum setup

**Question 3: Correlation Matrix (4 marks)**
- What is it (1)
- Why necessary (1)
- Generate matrix (1)
- Analyze results (1)

**Question 4: Scatter Plots (3 marks)**
- Create visualizations from correlation insights
- Multiple plot types
- Statistical validation

**Question 5: Multivariate Regression (3 marks)**
- Build regression model
- Target: Hours_Sleep
- Predict and analyze

---

## KEY CONCEPTS MASTERY

### CONCEPT 1: Information Visualization vs Data Visualization

**Information Visualization (InfoViz):**
- Abstract, non-spatial data → visual form
- Maps concepts to graphics
- Examples: Org charts, network diagrams, timelines
- Requires transformation step

**Data Visualization:**
- Inherently spatial data
- Geographic context preserved
- Examples: Maps, satellite imagery
- Minimal transformation needed

**Key Difference**: InfoViz creates visual representations where none existed; Data Viz displays existing spatial information.

---

### CONCEPT 2: Data Structures for Visualization

#### Dictionary
```python
config = {'plot_type': 'bar', 'colors': ['red', 'blue']}
# Unordered, mutable, access by key
# Use: Store configuration parameters
```

#### Tuple
```python
point = (10, 20)  # Coordinates
colors = (255, 128, 0)  # RGB
# Ordered, immutable, indexed access
# Use: Ensure data integrity
```

#### Series (Pandas)
```python
sales = pd.Series([100, 150, 120], index=['Q1', 'Q2', 'Q3'])
# Labeled, 1D, optimized for data ops
# Use: Direct plotting, time series
```

#### DataFrame
```python
df = pd.DataFrame({'Name': ['A', 'B'], 'Sales': [100, 200]})
# 2D, labeled, heterogeneous, vectorized ops
# Use: Core data structure for analysis
```

**Why DataFrame Particularly Efficient:**
1. **Vectorized Operations**: `df['Bonus'] = df['Salary'] * 0.1` (100x faster than loops)
2. **Built-in Methods**: `df.groupby()`, `df.fillna()`, `df.corr()`
3. **Automatic Indexing**: Semantic meaning in row/column labels
4. **Operations Integration**: Filter, aggregate, join, reshape - all efficient

---

### CONCEPT 3: Graph Type Selection

| Graph | Best For | Why Useful | Example |
|-------|----------|-----------|---------|
| **Line** | Temporal trends | Pattern recognition, trends, seasonality | Stock prices over time |
| **Bar** | Category comparison | Precise magnitudes, simplicity | Sales by region |
| **Histogram** | Distribution analysis | Distribution shape, outliers | Age distribution |
| **Flow Chart** | Process/decisions | Clarity, branching logic | Customer service process |
| **Box Plot** | Statistical summary | Multi-group comparison, outliers | Salary by department |
| **Bubble Map** | Geographic analysis | Multi-dimensional, spatial patterns | Sales by location |

---

### CONCEPT 4: Correlation Matrix Interpretation

**Correlation Strength:**
- 0.9-1.0: Very strong
- 0.7-0.9: Strong
- 0.5-0.7: Moderate
- 0.3-0.5: Weak
- 0.0-0.3: Very weak/None

**Using Correlation Matrix:**
1. **Feature Selection**: Which variables predict the target?
2. **Multicollinearity**: Are predictors redundant?
3. **Pattern Recognition**: What hidden relationships exist?
4. **Model Building**: What features should we keep/remove?

**Health Data Example:**
- Duration ↔ Calories: r = 0.98 (multicollinearity - keep one only)
- Work_Hours ↔ Sleep: r = -0.85 (strong inverse - important predictor)
- Calories ↔ Sleep: r = 0.62 (moderate positive - fitness helps sleep)

---

### CONCEPT 5: Regression Modeling

**Simple vs Multivariate:**
- **Simple**: One predictor → One line
- **Multivariate**: Multiple predictors → Better predictions

**Regression Equation:**
```
Target = Intercept + (Coef₁ × Var₁) + (Coef₂ × Var₂) + ...
```

**Model Evaluation:**
- **R²**: Explains what % of variance (0.75 = good, 0.9 = excellent)
- **RMSE**: Average prediction error (lower is better)
- **MAE**: Absolute average deviation (interpretable in original units)

**From June 2024 Exam:**
```
Hours_Sleep = 9.2 - 0.18×Hours_Work + 0.008×Calories + ...
```
- Interpretation: Each work hour → 0.18 hours (11 minutes) less sleep
- Important insight: Work-life balance impacts sleep significantly

---

## PYTHON CODE PATTERNS

### Pattern 1: Load & Explore Data
```python
import pandas as pd
import numpy as np

df = pd.read_csv('health.csv')
df.head()      # First few rows
df.describe()  # Statistics
df.dtypes      # Column types
```

### Pattern 2: Calculate Correlations
```python
import seaborn as sns
import matplotlib.pyplot as plt

corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
```

### Pattern 3: Create Scatter Plot
```python
plt.scatter(df['X'], df['Y'], alpha=0.6, s=100)
z = np.polyfit(df['X'], df['Y'], 1)
p = np.poly1d(z)
plt.plot(df['X'], p(df['X']), "r--", label='Trend')
plt.show()
```

### Pattern 4: Build Regression Model
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = df.drop('Target', axis=1)
y = df['Target']

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

print(f"R² = {r2_score(y, y_pred):.4f}")
```

### Pattern 5: Create Multiple Visualizations
```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1
axes[0, 0].scatter(...)

# Plot 2
axes[0, 1].plot(...)

# Plot 3
axes[1, 0].hist(...)

# Plot 4
axes[1, 1].bar(...)

plt.tight_layout()
plt.show()
```

---

## EXAM STRATEGY & TIME MANAGEMENT

### Before Exam
- [ ] Memorize 6 graph types with definitions & use cases
- [ ] Practice correlation matrix interpretation
- [ ] Understand regression coefficient interpretation
- [ ] Know Python library minimum requirements
- [ ] Review June 2024 practical (6-8 mark questions possible)
- [ ] Practice explaining concepts simply (non-technical audience)

### During Exam

**June 2025 Style (Written, 3 hours):**
- **First 5 min**: Read all questions, identify easy vs hard
- **Q1 (45 min)**: Theory answers - can do partial credit for partial explanations
- **Q2 (30 min)**: Data structure definitions - use simple Python examples
- **Q3 (45 min)**: For each graph: 1-2 min definition, 2 min best uses, 1 min justification
- **Review (5 min)**: Check completeness, add examples if time

**June 2024 Style (Practical, 2 hours):**
- **First 5 min**: Understand health data structure
- **Q1-Q2 (10 min)**: Quick definition answers
- **Q3 (30 min)**: Generate correlation matrix, interpret correlations
- **Q4 (20 min)**: Create 3 scatter plots with trend lines
- **Q5 (40 min)**: Build regression, analyze coefficients, create diagnostic plots
- **Final (5 min)**: Verify all code runs, exports cleanly

---

## COMMON MISTAKES TO AVOID

### Mistake 1: Dictionary vs Tuple Confusion
❌ "Dictionaries are ordered arrays"
✅ "Dictionaries are unordered key-value pairs; Tuples are ordered and immutable"

### Mistake 2: Wrong Graph for Context
❌ Using pie charts (pie charts are rarely best choice)
✅ Using bar chart for categorical comparison

### Mistake 3: No Justification
❌ "Bar charts are good for data"
✅ "Bar charts enable precise height comparison for 5 regions; alternative line graph would create visual clutter"

### Mistake 4: Correlation = Causation
❌ "Since Work and Sleep correlate -0.85, work causes poor sleep"
✅ "Correlation -0.85 shows inverse relationship; causation unclear (could be stress, could be schedule)"

### Mistake 5: Ignoring Multicollinearity
❌ Using Duration + Average_Pulse + Max_Pulse (all r>0.95)
✅ Using Duration only (removes redundancy)

### Mistake 6: Not Interpreting R²
❌ Just printing "R² = 0.76"
✅ "Model explains 76% of variance; 24% due to other factors (stress, schedule, genetics)"

---

## MARK ALLOCATION CHECKLIST

### June 2025 (70 marks)

**Q1: Reading & Comprehension (25 marks)**
- [ ] Q1.1a: InfoViz definition (3)
- [ ] Q1.1b: Modern context (3)
- [ ] Q1.2: 6 business reasons (6)
- [ ] Q1.3: 6 governance examples (6)
- [ ] Q1.4: 3 graphs with explanation (6)

**Q2: Data Structures (20 marks)**
- [ ] Q2.1: Dict+Tuple+Series definitions (9)
- [ ] Q2.2: Obtain/Maintain/Use (6)
- [ ] Q2.3: DataFrame definition + efficiency (5)

**Q3: Graphics (25 marks)**
- [ ] Graph 1 (Line): 4
- [ ] Graph 2 (Bar): 4
- [ ] Graph 3 (Histogram): 4
- [ ] Graph 4 (Flow): 4
- [ ] Graph 5 (Box): 4
- [ ] Graph 6 (Bubble): 4
- [ ] Bonus: 1

**TOTAL: 70 marks**

---

### June 2024 (15 marks)

- [ ] Q1: Definition (3)
- [ ] Q2: Python environment (3)
- [ ] Q3: Correlation matrix (4)
- [ ] Q4: Scatter plots (3)
- [ ] Q5: Regression model (2-3)

**TOTAL: 15 marks**

---

## STUDY RESOURCES PROVIDED

**Markdown Files (Theory):**
1. `DSC602_JUNE_2025_EXAM_SOLUTIONS.md` - Complete theory answers (70 marks)
2. `DSC602_JUNE_2024_EXAM_SOLUTIONS.md` - Complete theory answers (15 marks)
3. `DSC602_JUNE_2025_QUICK_REFERENCE.md` - Study guide for June 2025
4. `DSC602_JUNE_2024_EXAM_QUICK_REFERENCE.md` - Study guide for June 2024

**Jupyter Notebooks (Interactive Practice):**
1. `DSC602_JUNE_2025_TITANIC_Q3_VISUALIZATIONS.ipynb` - All 6 graph types (run cells to learn)
2. `DSC602_JUNE_2024_EXAM_PRACTICAL.ipynb` - Full practical exam walkthrough

**Python Scripts (Standalone Execution):**
1. `DSC602_JUNE_2025_Q3_VISUALIZATIONS.py` - Run: `python DSC602_JUNE_2025_Q3_VISUALIZATIONS.py`
2. `DSC602_JUNE_2024_EXAM.py` - Run: `python DSC602_JUNE_2024_EXAM.py`

---

## 30-MINUTE CRASH COURSE

### If you have 30 minutes before exam:

**5 min:** Graph types
- Line = Trends, Bar = Categories, Histogram = Distribution, Flow = Process, Box = Multi-group, Bubble = Geographic

**5 min:** Data structures
- Dictionary: key-value (flexible)
- Tuple: immutable (fixed)
- Series: labeled 1D (for plotting)
- DataFrame: 2D labeled (core analytics)

**5 min:** Python basics
- `import pandas as pd`, `import matplotlib.pyplot as plt`, `import seaborn as sns`
- `df.corr()` for correlations
- `LinearRegression().fit(X, y)` for modeling

**5 min:** Correlation interpretation
- r > 0.9: Very strong (multicollinearity)
- r = 0.6: Moderate (useful predictor)
- r = -0.85: Strong negative (inverse relationship)

**5 min:** Regression interpretation
- R² = what % variance explained
- Coefficients: change per unit increase
- RMSE: average prediction error

**5 min:** Last minute prayers 🙏

---

## FINAL TIPS

### ✅ DO THIS
1. **Be specific**: Don't say "visualization helps" - say "bar charts enable 3-second comparison of 5 regions"
2. **Use examples**: Abstract + concrete = highest marks
3. **Show working**: Partial credit for correct method even if calculation wrong
4. **Organize**: Bullet points, clear sections, bold key terms
5. **Proofread**: 2-3 min check at end catches silly errors

### ❌ AVOID THIS
1. **Generic definitions**: "A line graph shows lines" (too vague)
2. **Missing justification**: Why use this graph? For whom?
3. **Confusing structure**: Does your answer flow logically?
4. **No code examples**: For data structures, simple Python code helps
5. **Rushing**: Slower, complete answer > faster, incomplete answer

---

## YOUR EXAM FILES

```
d:\charlesDevelopment\SQL\note_sumarries\DSC602\
├── DSC602_JUNE_2025_EXAM_SOLUTIONS.md
├── DSC602_JUNE_2025_QUICK_REFERENCE.md
├── DSC602_JUNE_2025_TITANIC_Q3_VISUALIZATIONS.ipynb
├── DSC602_JUNE_2025_Q3_VISUALIZATIONS.py
│
├── DSC602_JUNE_2024_EXAM_SOLUTIONS.md
├── DSC602_JUNE_2024_EXAM_PRACTICAL.ipynb
├── DSC602_JUNE_2024_EXAM.py
│
└── (This file)
```

**How to use:**
1. **Study**: Read `.md` files first (understand concepts)
2. **Practice**: Run `.ipynb` files in Jupyter (interactive learning)
3. **Execute**: Run `.py` scripts (see complete output)
4. **Review**: Use quick reference guides before exam

---

## FINAL CHECKLIST

### Before June 2025 Exam (Written, 70 marks):
- [ ] Can define all 6 graph types without notes
- [ ] Can explain why each graph type is useful
- [ ] Can describe 3 governance use cases
- [ ] Understand difference: Dictionary vs Tuple vs Series
- [ ] Know why DataFrame is "particularly efficient"
- [ ] Can interpret correlation coefficients
- [ ] Managed timing: 45+30+45 min = 120 min (1 hr buffer)

### Before June 2024 Exam (Practical, 15 marks):
- [ ] Can generate correlation matrix in Python
- [ ] Can create scatter plots with trend lines
- [ ] Can build LinearRegression model
- [ ] Can interpret R², RMSE, coefficients
- [ ] Can create diagnostic plots (4-subplot layout)
- [ ] All code runs without errors (tested)

---

**GOOD LUCK! You've thoroughly prepared.** 📊✨

Remember: The examiners want to see that you **understand concepts** and can **apply them to real situations**. Depth beats breadth. A detailed, well-explained answer to one question beats brief answers to everything.

**You've got this! 💪**

# DSC602 June 2025 Exam - QUICK REFERENCE & STUDY GUIDE
## Information Visualization | 70 Total Marks | 3 Hours

---

## EXAM STRUCTURE

| Section | Questions | Marks | Time |
|---------|-----------|-------|------|
| **Q1: Reading & Comprehension** | 1.1-1.4 | 25 | 45 min |
| **Q2: Data Description & Preparation** | 2.1-2.3 | 20 | 30 min |
| **Q3: Graphics & Characteristics** | 6 graph types | 25 | 45 min |
| **TOTAL** | 3 questions | **70** | **3 hours** |

---

## QUESTION 1: READING & COMPREHENSION (25 marks)

### Q1.1: Information Visualization Definition (6 marks)

**Part A: What is InfoVis? (3 marks)**
- Transformation of abstract, non-spatial data into visual forms
- Supports human perception, cognition, decision-making
- Key: NOT naturally spatial data (unlike maps)

**Key Components (For full 3 marks):**
1. **Input**: Abstract data (financials, text, relationships)
2. **Process**: Visual encoding (map data to visual properties)
3. **Output**: Interactive representations enabling insight

**Part B: Meaning in Modern Context (3 marks)**
1. Handles terabytes of data → makes invisible visible
2. Enables data-driven decision-making
3. Handles multi-dimensional complexity
4. Democratizes analytics to non-experts

✅ **Model Answer Structure**:
- Definition (1 mark)
- Key components explained (1.5 marks)
- Modern importance (0.5 marks)

---

### Q1.2: Why Businesses Need Data Visualization (6 marks)

**6 Key Reasons (1 mark each):**

1. **Cognitive Advantage**: Humans process visuals 60,000× faster than text
2. **Pattern Recognition**: Visual cortex detects trends, outliers, clusters
3. **Decision Support**: Faster insights = quicker, better decisions
4. **Competitive Advantage**: Companies with better insights win
5. **Communication**: Replaces 50-page reports with one chart
6. **Handling Big Data**: Aggregation + interaction for massive datasets

✅ **Answer Strategy**:
- State the reason (0.5 mark)
- Explain how it helps (0.5 mark)
- Example: Business impact (optional, helps with clarity)

---

### Q1.3: Governance and Information Visualization (6 marks)

**6 Applications of Visualization in Governance (1 mark each):**

1. **Performance Monitoring**: Track healthcare/education/finance metrics
2. **Budget Allocation**: Optimize resource distribution
3. **Policy Impact**: Evaluate if policies are working
4. **Citizen Engagement**: Transparency → public trust
5. **Identifying Issues**: Discover problems requiring intervention
6. **Benchmarking**: Compare with peer regions/nations

✅ **Answer Pattern**:
- Name application (0.3 mark)
- Specific use case (0.4 mark)
- Expected outcome (0.3 mark)

**Real Examples to Mention**:
- Singapore: Smart city dashboards
- Denmark: Government spending transparency
- USA: CDC disease tracking
- UN: SDG (Sustainable Development Goals) monitoring

---

### Q1.4: Three Different Graphics from Class (6 marks)

**Format: 3 graphs × 2 marks each**

**For EACH graph (2 marks total):**
1. **Description** (1 mark):
   - What it looks like (visual representation)
   - When to use it
   - Example

2. **Why Useful** (1 mark):
   - 2-3 key advantages
   - Business context

**Common Options (Choose any 3):**

| Graph | Description | Why Useful |
|-------|-------------|-----------|
| **Line** | Points connected by lines over time | Trends, seasonality, comparison |
| **Bar** | Rectangular bars representing values | Category comparison, simplicity |
| **Histogram** | Adjacent bins showing distribution | Distribution shape, outliers |
| **Scatter** | Points plotted on x-y axes | Correlation, relationships |
| **Pie** | Slices of circle (avoid if possible) | Part-to-whole only |
| **Heatmap** | Color intensity showing values | Multi-dimensional patterns |

✅ **Model Answer for 1 Graph (2 marks)**:

**"The Bar Chart shows categorical data as rectangular bars proportional to values. 
In business, we use bar charts for sales by region - instantly see which regions perform best. 
This is useful because (1) heights are directly comparable, (2) can handle many categories, 
(3) easy for any audience to understand. Example: Our 5 regional sales can be compared in seconds, 
unlike tables which require manual scanning."**

---

## QUESTION 2: DATA DESCRIPTION & PREPARATION (20 marks)

### Q2.1: Dictionary, Tuple, Series (9 marks)

**Format: 3 data structures × 3 marks each**

#### DICTIONARY (3 marks)

**Definition** (1 mark):
- Unordered collection of key-value pairs: `{'key': value}`
- Mutable, flexible types

**Characteristics** (1 mark):
- Access by key (not position)
- Unordered (but insertion order maintained in Python 3.7+)
- Flexible types for keys and values

**Data Viz Application** (1 mark):
- Store configuration parameters
- Map category names to values
- Organize metadata

**Code Example**:
```python
config = {'plot_type': 'bar', 'colors': ['red', 'blue'], 'title': 'Sales'}
country_data = {'France': 85, 'Germany': 95, 'Italy': 62}
# Used for flexible visualization parameter passing
```

---

#### TUPLE (3 marks)

**Definition** (1 mark):
- Ordered, immutable collection: `(element1, element2)`
- Fixed size, cannot modify after creation

**Characteristics** (1 mark):
- Indexed access: `tuple[0]`, `tuple[1]`
- Immutable (ensures data integrity)
- Hashable (can be dictionary keys)
- Lightweight, memory efficient

**Data Viz Application** (1 mark):
- Store coordinates (x, y), (x, y, z)
- Store RGB colors: (255, 128, 0)
- Store figure dimensions: (width, height)
- Return multiple values from functions

**Code Example**:
```python
point = (10, 20)  # 2D coordinate
colors = [(255, 0, 0), (0, 255, 0)]  # RGB tuples
figure_size = (12, 8)  # (width, height)
```

---

#### SERIES (3 marks)

**Definition** (1 mark):
- Pandas 1D labeled array with index labels and values
- Built on NumPy, optimized for data operations

**Characteristics** (1 mark):
- Labeled (semantic meaning)
- Homogeneous (same type)
- Mutable, operations-rich
- Direct plotting capability

**Data Viz Application** (1 mark):
- Core data structure for visualization
- Direct `.plot()` method integration
- Filtering before visualization
- Time series with date indices

**Code Example**:
```python
import pandas as pd
sales = pd.Series([100, 150, 120], index=['Q1', 'Q2', 'Q3'])
sales.plot(kind='bar', title='Quarterly Sales')  # Direct plotting
```

---

### Q2.2: Obtain, Maintain, Use for Visualization (6 marks)

**Format: 3 structures × 2 marks each**

**DICTIONARY - Full 2 marks**:
- **Obtain** (0.5): Direct creation, from JSON, from DataFrame
- **Maintain** (0.5): Add/update with `d['key'] = value`, delete with `del d['key']`
- **Use** (1): Pass config to plotting functions, map labels to values

**TUPLE - Full 2 marks**:
- **Obtain** (0.5): Direct `(x, y)`, from list `tuple([...])`, unpacking `x, y = tuple_of_2`
- **Maintain** (0.5): Immutable - replace entirely, not modify
- **Use** (1): Store coordinates, colors, dimensions - ensures data integrity

**SERIES - Full 2 marks**:
- **Obtain** (0.5): Direct creation, from dict, from DataFrame column, from CSV
- **Maintain** (0.5): Modify values, fillna, dropna, reindex
- **Use** (1): Direct `.plot()`, filtering `series[series > threshold]`, time series

---

### Q2.3: Data Frame Particularity (5 marks)

**Part A: What is a DataFrame? (3 marks)**
- 2D labeled structure (rows × columns)
- Each column is a Series
- Heterogeneous types (different columns different types)
- Index (labels rows), Column names (labels columns)

**Definition** (1 mark):
"A DataFrame is a 2-dimensional data structure with labeled rows and columns, where each column is a Series and data types can vary by column."

**Structure** (1 mark):
```
        Name   Age  Salary  Department
    0   Alice   30   50000   IT
    1   Bob     25   45000   HR
    2   Carol   35   60000   IT
```

**Key Features** (1 mark):
- Labeled: Semantic meaning (column names, row indices)
- Mutable: Can add/remove rows/columns
- Indexed: Both label-based and position-based access
- Operations: Built-in methods for filtering, grouping, aggregation

---

**Part B: Why Particularly Efficient for Programming (2 marks)**

**Efficiency 1: Vectorized Operations** (1 mark):
- Instead of: Manual loop over each row
- Use: `df['Bonus'] = df['Salary'] * 0.1` (one-liner!)
- 100x faster execution, cleaner code, automatic optimization

**Efficiency 2: Built-in Methods Eliminate Code** (1 mark):
- Grouping: `df.groupby('Dept')['Salary'].mean()`
- Filtering: `df[df['Age'] > 30]`
- Missing data: `df.fillna(df.mean())`
- All accomplished in single expressions vs. manual loops

✅ **Model Answer (5 marks)**:

"A DataFrame is a 2-dimensional labeled structure with rows and columns, where each column is a Series and can have different data types. It's particularly efficient for programming because: (1) Vectorized operations - `df['Bonus'] = df['Salary'] * 0.1` is 100x faster than looping, and (2) Built-in methods eliminate code - `df.groupby()`, `df.fillna()`, filtering with `df[df['Age'] > 30]` accomplish complex operations in single expressions. This makes data preparation extremely efficient."

---

## QUESTION 3: GRAPHICS & CHARACTERISTICS (25 marks)

### Overview

**Task**: Identify which graph type is suitable for which context and justify.

**6 Graph Types**: Line, Bar, Histogram, Flow Chart, Box Plot, Bubble Map

**Marks per Graph**: 4 marks = (1) Definition + (2) Best Contexts + (1) Justification

---

### GRAPH 1: LINE GRAPH (4 marks)

**Definition** (1 mark):
Connects data points with lines, showing change over time or ordered sequence.

**Best Contexts** (2 marks):
1. **Temporal Trends**: Stock prices, website traffic, patient health
2. **Multiple Series**: Revenue vs. Expenses over time, product comparison

**Justification** (1 mark):
- Pattern recognition: Trends visible instantly
- Seasonality detection: Cycles apparent
- Multiple series comparison
- Intuitive for general audiences

**Example**: Stock price chart showing 3 companies' performance over 100 days

---

### GRAPH 2: BAR CHART (4 marks)

**Definition** (1 mark):
Rectangular bars representing values, heights proportional to magnitudes.

**Best Contexts** (2 marks):
1. **Category Comparison**: Sales by region, market share by competitor
2. **Part-to-Whole (Stacked)**: Revenue breakdown by product category

**Justification** (1 mark):
- Precise magnitude comparison
- Simplicity for any audience
- Multiple categories without clutter
- Composition analysis (stacked variant)

**Example**: Sales by 5 geographic regions with stacked breakdown by product

---

### GRAPH 3: HISTOGRAM (4 marks)

**Definition** (1 mark):
Distribution of continuous data using adjacent bins with frequency heights.

**Best Contexts** (2 marks):
1. **Distribution Analysis**: Age, income, test scores
2. **Outlier Detection**: Quality control, identify anomalies

**Justification** (1 mark):
- Distribution shape visible (normal, skewed, bimodal)
- Central tendency shown
- Outliers easily identified
- Data quality assessment

**Example**: Customer age distribution showing mostly 30-60 years with outliers

---

### GRAPH 4: FLOW CHART (4 marks)

**Definition** (1 mark):
Diagram showing processes, decisions (diamonds), and flow (arrows) of steps.

**Best Contexts** (2 marks):
1. **Process Documentation**: Software workflows, customer service procedures
2. **Decision Trees**: Medical diagnosis, troubleshooting guides

**Justification** (1 mark):
- Sequential steps instantly clear
- Non-technical people understand
- Branching logic visible
- Identifies bottlenecks for optimization

**Example**: Customer service process with 3 branches (billing/tech/product)

---

### GRAPH 5: BOX PLOT (4 marks)

**Definition** (1 mark):
Five-number summary visualization: min, Q1, median, Q3, max, with outliers.

**Best Contexts** (2 marks):
1. **Distribution Comparison**: Salary by department, test scores by school
2. **Outlier Identification**: Detect unusual measurements

**Justification** (1 mark):
- Compact multi-group comparison
- Statistical summary visible
- Outliers automatically marked
- Skewness detection (asymmetric boxes)

**Example**: Salary distribution across 4 departments with outlier identification

---

### GRAPH 6: BUBBLE MAP (4 marks)

**Definition** (1 mark):
Geographic visualization with bubbles (circles) where size = magnitude, color = category.

**Best Contexts** (2 marks):
1. **Geographic Distribution**: Sales by city, population by region
2. **Multi-Dimensional**: Sales (size) by location + product type (color)

**Justification** (1 mark):
- Geographic context enables spatial pattern discovery
- Multiple dimensions (position + size + color)
- Intuitive for business stakeholders
- Identifies clusters and anomalies geographically

**Example**: Store locations with bubble size = sales, color = store type (Premium/Standard/Budget)

---

### BONUS (1 mark)

- Overall integration/understanding
- Clear presentation
- Proper use of terminology

---

## STUDY TIPS & COMMON MISTAKES

### ✅ DO THIS

1. **Be Specific**: Don't say "visualization is useful" - say WHY (with specific advantage)
2. **Provide Examples**: Abstract definitions are weak - use business examples
3. **Show Understanding**: Connect graph type to context and problem it solves
4. **Use Terminology**: "Central tendency", "outliers", "multi-dimensional", "vectorized"
5. **Structure Answers**: Use bullet points, clear sections, bold key terms
6. **Time Management**: 
   - Q1: 45 minutes (6.25 min/part)
   - Q2: 30 minutes (10 min/section)
   - Q3: 45 minutes (7.5 min/graph)
   - Review: 5 minutes

### ❌ AVOID THIS

1. **Generic Definitions**: "A line graph shows lines" - too vague
2. **No Justification**: Don't list contexts without explaining WHY
3. **Confusing Structures**: Dictionary vs Tuple - know the key difference (ordered? mutable?)
4. **Missing Code**: For Q2, simple Python code examples help
5. **Wrong Graph for Context**: Don't use pie charts, don't use line for categories
6. **No Data Examples**: Theoretical without examples gets lower marks

---

## MARK ALLOCATION CHECKLIST

### Q1 (25 marks)

- [ ] Q1.1a: Definition with components (3 marks)
- [ ] Q1.1b: Modern context importance (3 marks)
- [ ] Q1.2: 6 business reasons explained (6 marks)
- [ ] Q1.3: 6 governance applications (6 marks)
- [ ] Q1.4: 3 graphs with description + why useful (6 marks)
- **Subtotal: 25 marks**

### Q2 (20 marks)

- [ ] Q2.1a: Dictionary - def + chars + app (3 marks)
- [ ] Q2.1b: Tuple - def + chars + app (3 marks)
- [ ] Q2.1c: Series - def + chars + app (3 marks)
- [ ] Q2.2: Obtain/Maintain/Use for each (6 marks)
- [ ] Q2.3: DataFrame def (3) + efficiency (2) (5 marks)
- **Subtotal: 20 marks**

### Q3 (25 marks)

- [ ] Graph 1 (Line): 4 marks
- [ ] Graph 2 (Bar): 4 marks
- [ ] Graph 3 (Histogram): 4 marks
- [ ] Graph 4 (Flow): 4 marks
- [ ] Graph 5 (Box): 4 marks
- [ ] Graph 6 (Bubble): 4 marks
- [ ] Bonus/Integration: 1 mark
- **Subtotal: 25 marks**

### **TOTAL: 70 marks**

---

## KEY FORMULAS & FACTS

### Data Structure Characteristics

| Feature | Dictionary | Tuple | Series |
|---------|-----------|-------|--------|
| Ordered | No* | Yes | Yes |
| Mutable | Yes | **No** | Yes |
| Access | By key | By index | By label/index |
| Type | Heterogeneous | Heterogeneous | Homogeneous |
| Example | `{'a': 1}` | `(1, 2)` | `pd.Series([1,2])` |

### Visualization Effectiveness Rule of Thumb

**Cognitive Load**: Visual ÷ Text = 60,000:1
- 1 chart ≈ 60,000 words
- Better than tables for patterns

### Five-Number Summary (Box Plot)

- Min, Q1 (25%), Median (50%), Q3 (75%), Max
- IQR = Q3 - Q1
- Outliers = values > Q3 + 1.5×IQR OR < Q1 - 1.5×IQR

---

## FINAL EXAM STRATEGY

### Pre-Exam (Preparation)
- [ ] Memorize 3 graphs with definition, contexts, justification
- [ ] Practice defining data structures with Python examples
- [ ] Understand vectorized operations vs loops
- [ ] Know 3 governance examples

### During Exam
- [ ] Read all questions first (5 min)
- [ ] Q1: Answer from stronger area first
- [ ] Q2: Use code examples for full marks
- [ ] Q3: Draw simple diagrams if describing graphs
- [ ] Review answers for terminology accuracy

### Common High-Mark Patterns
- Specific examples from lecture or real business
- Clear structure with bullet points
- Theoretical explanation + practical application
- Connection between concepts

---

## RESOURCES MENTIONED IN EXAM

**Files Provided:**
1. `DSC602_JUNE_2025_EXAM_SOLUTIONS.md` - Complete theory answers
2. `DSC602_JUNE_2025_TITANIC_Q3_VISUALIZATIONS.ipynb` - All 6 graphs in Jupyter
3. `DSC602_JUNE_2025_Q3_VISUALIZATIONS.py` - Python script version
4. `DSC602_JUNE_2025_QUICK_REFERENCE.md` - This file

---

## LAST-MINUTE TIPS (15 minutes before exam)

1. **Dictionary vs Tuple**: Dict = flexibility (keys), Tuple = immutability (fixed)
2. **Line vs Bar**: Line = TRENDS (time), Bar = COMPARISON (categories)
3. **Histogram vs Box**: Histogram = DISTRIBUTION SHAPE, Box = GROUP COMPARISON
4. **Why Visualization Matters**: Humans see patterns faster in visuals than numbers
5. **Governance Example**: Use Singapore/Denmark/CDC examples if stuck
6. **Flow Chart**: Non-technical people must understand (simplicity)
7. **Bubble Map**: Size + Color + Position = 3 dimensions

---

**GOOD LUCK! You've got this! 📊📈📉**

**Remember: The exam tests your ability to:**
- Define and explain concepts (theory)
- Connect concepts to business applications (context)
- Choose appropriate visualization for scenarios (judgment)
- Support arguments with examples (communication)

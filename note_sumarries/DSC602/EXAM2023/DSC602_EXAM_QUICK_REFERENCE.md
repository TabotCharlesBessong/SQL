# DSC602 Information Visualization - Exam Quick Reference Guide

## Quick Answer Summary

### QUESTION 1: TRUE/FALSE STATEMENTS (18 marks - 2 marks each)

| # | Statement | Answer | Key Point |
|---|-----------|--------|-----------|
| 1.1 | Process of interpreting data in pictorial/graphical format | **TRUE** | Definition of visualization |
| 1.2 | Convert business data into interactive graphs for business goals | **TRUE** | Interactivity & business value |
| 1.3 | Transform data into dashboards from multiple sources | **TRUE** | Multi-source integration |
| 1.4 | Create active and informative dashboards with graphics | **TRUE** | Multiple visualization types |
| 1.5 | Make appropriate designs by drilling into data | **TRUE** | Data exploration drives design |
| 1.6 | Figure out patterns, trends, correlations for improvement | **TRUE** | Core analytical benefit |
| 1.7 | Give full picture of data under analysis | **TRUE** | Detailed data visibility principle |
| 1.8 | Visualize massive data intuitively to present findings | **TRUE** | Cognitive efficiency |
| 1.9 | Make better, quick and informed decisions | **TRUE** | Business value proposition |

**Total Q1: 18/18 marks** ✓

---

### QUESTION 2: PRACTICAL IMPLEMENTATION (20 marks)

#### 2.1 Create DataFrame (5 marks)
```python
import pandas as pd
data = {
    'Sales_Name': ['Henry', 'Peter', 'Nichoulas', 'Mary', 'Dan', 'Oussy', 'Maboukam'],
    'Land_sales': [12, 15, 25, 8, 5, 0, 10],
    'Clothe_sales': [2500, 1900, 1800, 5000, 2850, 8005, 5000],
    'Book_sales': [2300, 2000, 180, 5000, 20, 12, 15]
}
df = pd.DataFrame(data)
```
**What to show**: DataFrame structure, data types, basic statistics

#### 2.2 Bar Plot (5 marks)
**Purpose**: Compare total sales volume by representative
**Code**: `plt.bar(df['Sales_Name'], total_sales)`
**What to show**: 
- Properly labeled axes
- Title
- Value labels on bars
- Clear visual comparison

#### 2.3 Pie Chart (5 marks)
**Purpose**: Show proportion of sales by product category
**Code**: `plt.pie(category_totals.values())`
**What to show**:
- Three product categories (Land, Clothing, Books)
- Percentage labels
- Different colors for each slice
- Legend

#### 2.4 Box Plot (5 marks)
**Purpose**: Show distribution of sales across categories
**Code**: `plt.boxplot([land_sales, clothing_sales, book_sales])`
**What to show**:
- Box-and-whisker for each category
- Quartiles and median visible
- Outliers if any
- Statistical summary

#### 2.5 Area Plot (5 marks)
**Purpose**: Show sales trends by representative and category
**Code**: `plt.stackplot()` and `plt.fill_between()`
**What to show**:
- Two versions (stacked + individual)
- Clear legend
- Filled areas with transparency
- Individual data points

**Total Q2: 20/20 marks** ✓

---

### QUESTION 3: NEURAL NETWORKS & VISUALIZATION (30 marks)

#### Core Arguments to Cover (30 marks total):

**1. Trust & Explainability (8 marks)**
- Black box problem with neural networks
- Saliency maps reveal what network "sees"
- Feature visualization shows learned representations
- Critical for high-stakes domains (medical, autonomous driving)

**2. Model Validation & Debugging (7 marks)**
- Millions of parameters impossible to validate manually
- Weight distribution visualization catches anomalies
- Activation patterns show what each layer learned
- Training curves reveal convergence problems
- Dead neurons identification

**3. Error Analysis (7 marks)**
- Misclassification visualization groups failures
- Adversarial examples show robustness limits
- Attention mechanisms show focus patterns
- Failure mode identification enables improvements
- Edge case discovery

**4. Application Domain Examples (6 marks)**
- **Autonomous Driving**: Saliency maps show what influenced steering
- **Medical Imaging**: Highlight suspicious regions for radiologist review
- **Satellite Imagery**: Change detection and anomaly identification
- Each requires domain-specific visualization approaches

**5. Technical Considerations (2 marks)**
- Scalability of visualization with model size
- Trade-off between interpretability and fidelity
- Integration with expert workflows

**Total Q3: 30/30 marks** ✓

---

## File References

### Theory & Explanations
- **Main Document**: `DSC602_EXAM_COMPLETE_SOLUTIONS.md`
  - Q1: Detailed explanations for each true/false statement
  - Q3: Comprehensive neural network visualization analysis

### Practical Code
- **Jupyter Notebook**: `DSC602_EXAM_QUESTION2_SOLUTION.ipynb`
  - Ready to run
  - Includes visualizations and explanations
  - Can export to HTML or PDF

- **Python Script**: `DSC602_EXAM_QUESTION2_SOLUTION.py`
  - Standalone executable
  - Detailed comments
  - Extensible functions
  - Can run directly: `python DSC602_EXAM_QUESTION2_SOLUTION.py`

### Lecture Materials
- **Lecture Summaries**: `INFORMATION_VISUALIZATION_LECTURE_SUMMARIES.md`
  - Lecture 1: Fundamentals
  - Lecture 2: Data types and abstraction
  - Lecture 3: Nested model
  - Lecture 4: Task abstraction
  - Lecture 5-6: Marks and channels

---

## Key Concepts by Question Type

### True/False Questions (Q1)
**Success Strategy:**
1. Understand definition of visualization (Lecture 1)
2. Know three core benefits (cognitive, communication, decision support)
3. Understand practical applications in business
4. Recognize Anscombe's Quartet principle (show all data)
5. Know why interactivity matters (complexity handling)

**Common Theme**: All statements are TRUE because they describe valid and important aspects of visualization

### Practical Questions (Q2)
**Success Strategy:**
1. Import required libraries (pandas, matplotlib)
2. Create DataFrame exactly as specified
3. Create each visualization type with proper:
   - Labels (title, x-axis, y-axis)
   - Legend/annotations
   - Theoretical explanation comment
4. Include summary statistics
5. Show 4 different visualization types

**Theoretical Component**: Explain WHY each visualization type is appropriate

### Theoretical Questions (Q3)
**Success Strategy:**
1. Start with the black-box problem
2. Progress through trust → validation → error analysis → applications
3. Use specific examples (medical, autonomous, satellite)
4. Reference specific visualization techniques (saliency maps, attention, etc.)
5. Include technical considerations
6. Show understanding of interdisciplinary nature (computer science + domain expertise)

---

## Visualization Type Reference

### Bar Plot
- **Use For**: Comparing values across categories
- **Strength**: Easy value reading, clear rankings
- **Mark**: Rectangles (1D constrained)
- **Channel**: Length/height
- **Example**: Sales by representative

### Pie Chart
- **Use For**: Part-to-whole relationships
- **Strength**: Shows composition, proportions instantly
- **Mark**: Circular sectors
- **Channel**: Angle/area
- **Example**: Category distribution (31% + 61% + 8% = 100%)

### Box Plot
- **Use For**: Distribution comparison
- **Strength**: Shows outliers, spread, median, quartiles
- **Mark**: Box + whiskers
- **Channel**: Position + length
- **Example**: Sales spread across product categories

### Area Plot
- **Use For**: Trends over ordered dimension
- **Strength**: Shows magnitude and cumulative totals
- **Mark**: Area under line
- **Channel**: Position + area
- **Example**: Sales trends by representative

---

## Common Mistakes to Avoid

### In Theory Questions
❌ Saying false when statement is true (all Q1 are true!)
❌ Generic explanation without specifics
❌ Not referencing lecture material
❌ Missing examples
✓ Use specific terms from course material
✓ Reference Lecture 1, 2, 3, 5-6 concepts

### In Practical Questions
❌ Wrong data structure or types
❌ Missing labels, legends, or titles
❌ No value labels on bars
❌ No theoretical explanation
❌ Incomplete data frame
✓ Test code before submission
✓ Include detailed comments
✓ Verify all 4 plot types created
✓ Include summary statistics

### In Neural Network Questions
❌ Only describing existing visualization techniques
❌ No mention of trust/explainability
❌ Missing application examples
❌ No explanation of why visualization helps
❌ Technical details without business context
✓ Start with the problem (black box)
✓ Show specific solutions (saliency, attention, etc.)
✓ Give concrete examples (medical, autonomous, satellite)
✓ Balance technical + practical

---

## Scoring Checklist

### Question 1 (18 marks)
- [ ] All 9 answers marked as TRUE
- [ ] Each answer has detailed explanation (2 marks each)
- [ ] References course material (Lectures 1, 2, 3, 5-6)
- [ ] Includes specific examples for each
- [ ] Clear connection to visualization benefits

### Question 2 (20 marks)
- [ ] DataFrame created correctly (5 marks)
  - [ ] Correct data values
  - [ ] Proper column names
  - [ ] Data types correct
  - [ ] Total sales calculated

- [ ] Bar plot (5 marks)
  - [ ] Shows total sales by representative
  - [ ] Proper labels and title
  - [ ] Value labels on bars
  - [ ] Clear comparison

- [ ] Pie chart (5 marks)
  - [ ] Shows 3 product categories
  - [ ] Percentage labels
  - [ ] Different colors
  - [ ] Legend

- [ ] Box plot (5 marks)
  - [ ] Shows distribution
  - [ ] Quartiles visible
  - [ ] Outliers identified
  - [ ] Statistical summary

- [ ] Area plot (5 marks)
  - [ ] Shows trends
  - [ ] Filled areas with transparency
  - [ ] Clear legend
  - [ ] Multiple series comparison

### Question 3 (30 marks)
- [ ] Explains why neural networks are black boxes (5 marks)
- [ ] Describes trust/explainability solutions (6 marks)
- [ ] Covers validation and debugging (7 marks)
- [ ] Error analysis section (6 marks)
- [ ] Application examples (4 marks)
- [ ] Technical considerations (2 marks)

---

## Total Possible Score

| Question | Marks | Status |
|----------|-------|--------|
| Q1 (True/False) | 18 | ✓ Complete |
| Q2 (Practical) | 20 | ✓ Complete |
| Q3 (Theoretical) | 30 | ✓ Complete |
| **TOTAL** | **68** | **✓ FULL SOLUTIONS PROVIDED** |

---

## How to Use These Materials

### For Study:
1. Read `INFORMATION_VISUALIZATION_LECTURE_SUMMARIES.md` for theory
2. Review `DSC602_EXAM_COMPLETE_SOLUTIONS.md` for detailed answers
3. Study visualization type reference above

### For Practice:
1. Try creating the visualizations without looking at code
2. Compare your approach to solutions
3. Run the Python script/notebook to see output
4. Modify code to explore variations

### For Exam Preparation:
1. Memorize Q1 answers are all TRUE
2. Practice creating all 4 visualization types from scratch
3. Prepare Q3 answer structure (problem → solutions → examples)
4. Time yourself (approximately 3 hours for full exam)

### Time Allocation (3 hour exam):
- Q1: 30 minutes (18 marks)
- Q2: 60 minutes (20 marks) - code + explanations
- Q3: 60 minutes (30 marks) - detailed theoretical answer
- Review: 30 minutes

---

**Last Updated**: May 25, 2026
**Course**: DSC602 - Information Visualization
**Exam Date**: 20/06/2023
**Total Credit Value**: 6 credits

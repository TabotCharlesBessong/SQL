# DSC602 Information Visualization - July 2024 Exam Solutions
## University of Buea | Faculty of Science | 70 Total Marks

---

## PART 1: READING AND COMPREHENSION QUESTIONS (20 marks)

### Question 1: What are the three visualization use cases? (6 marks)

The three primary visualization use cases are:

#### 1. **Explore** (Exploratory Visualization) - 2 marks
**Definition**: The process of discovering patterns, relationships, outliers, and insights in data without predefined hypotheses.

**Characteristics**:
- Used when analysts don't know what to look for
- Driven by curiosity and investigation
- Interactive with multiple views
- Focus on data discovery

**Example**: Analyzing Titanic data to discover which passenger groups had higher survival rates, identifying age groups with suspicious patterns, finding correlations between variables.

**Business Value**: Generates new hypotheses and identifies unexpected trends that can guide further investigation.

#### 2. **Confirm** (Confirmatory Visualization) - 2 marks
**Definition**: The process of validating or testing predetermined hypotheses using visualization as evidence.

**Characteristics**:
- Used when specific questions need answering
- Hypothesis-driven approach
- Focused visualization design
- Statistical validation support

**Example**: Testing the hypothesis "women and children had higher survival rates on the Titanic" by comparing survival rates across gender and age groups visually.

**Business Value**: Provides evidence-based confirmation or rejection of business hypotheses, supporting decision-making.

#### 3. **Present** (Presentational Visualization) - 2 marks
**Definition**: The process of communicating findings and insights to stakeholders through clear, persuasive visualizations designed for comprehension.

**Characteristics**:
- Audience-focused design
- Clear messaging and storytelling
- Simplified for non-expert consumption
- High visual impact

**Example**: Creating a dashboard showing survival statistics by passenger class for executive presentation, highlighting key findings with annotations.

**Business Value**: Effectively communicates analytical findings to decision-makers, enabling informed business actions.

---

### Question 2: Name a visualization technique for exploration/confirmation/presentation and describe it. (4 marks)

**Visualization Technique: Scatter Plot** (1 mark for naming)

#### For Exploration (Interactive Scatter Plot with Filtering):
**Description**: 
A 2D plot showing individual data points positioned by two continuous variables (e.g., Age vs. Fare). Encoded with color for categorical variable (e.g., Survival status).

**Why for Exploration**: 
- Reveals outliers immediately (passengers with very high fares, unusual ages)
- Shows clusters (first-class passengers group differently than third-class)
- Interactions (hover for details, brush to filter) enable discovery
- Multiple patterns visible simultaneously

**Example Application**: Explore Titanic data by plotting Age (x-axis) vs Fare (y-axis), colored by Survival status. This quickly reveals that higher fares correlate with better survival, and certain age groups behaved differently.

#### For Confirmation (Scatter Plot with Regression Line):
**Description**: 
The same scatter plot with added trend line, confidence intervals, and statistical correlation coefficient.

**Why for Confirmation**: 
- Visually validates the strength of relationships
- Regression line confirms expected trends
- Confidence interval shows uncertainty
- Statistical values provide evidence

**Example Application**: Confirm that "higher fare correlates with survival" by overlaying a trend line on the scatter plot, showing clear separation and R² value.

#### For Presentation (Annotated Scatter Plot):
**Description**: 
Clean scatter plot with selected annotations, legend, title, axis labels, and highlights of key insights.

**Why for Presentation**: 
- Focuses viewer attention on key findings
- Annotations explain significance
- Clean design maximizes comprehension
- Tells a clear story to non-technical audience

**Example Application**: Present finding "Passengers who paid higher fares had better survival chances" with annotations highlighting the high-fare survival cluster and statistics.

---

### Question 3: What are the main visualization changes in visual data science? (8 marks)

Visual data science has undergone several major transformations:

#### 1. **From Static to Interactive (2 marks)**

**Historical**: Fixed, printed visualizations with single perspective
- Limited to what designer anticipated
- No user interaction possible
- Expensive to create alternative views

**Modern**: Dynamic, interactive visualizations with multiple perspectives
- Users can filter, zoom, brush, hover
- Enables real-time exploration
- Responsive to user questions
- Examples: Dashboards, web-based analytics

**Impact**: Democratizes data exploration; non-technical users can discover insights independently.

#### 2. **From Aggregated to Individual (2 marks)**

**Historical**: Summary statistics and aggregated plots (bar charts showing totals)
- Loss of detail in individual records
- Potential hiding of important patterns
- Anscombe's Quartet problem: different datasets with identical summaries

**Modern**: Individual data points visible with aggregation available
- Scatterplots showing every passenger's age/fare
- Linked views combining detail with summary
- Both individual anomalies AND patterns visible

**Impact**: More honest representations; individual outliers and edge cases now visible.

#### 3. **From Single View to Multiple Coordinated Views (2 marks)**

**Historical**: Single visualization analyzed in isolation
- Difficult to relate multiple aspects of data
- Required mental integration of separate plots

**Modern**: Multiple linked visualizations (small multiples, brushing and linking)
- Change selection in one view highlights in others
- Age view linked to survival view linked to class view
- Holistic understanding through coordinated updates

**Impact**: Complex relationships become apparent through coordinate interaction.

#### 4. **From Designer-Driven to Data-Driven (2 marks)**

**Historical**: Designer determines what to show and how
- Requires designer expertise
- Manual updates when data changes
- Fixed narratives

**Modern**: Automated visualization generation, Grammar of Graphics
- Specify what data to show, system determines best encoding
- Updates automatically as data changes
- Exploratory possibilities easily generated

**Impact**: Scales visualization creation; enables rapid iteration and experimentation.

---

### Question 4: What is the difference between data visualization and information visualization? (2 marks)

#### **Data Visualization** (1 mark)

**Definition**: Visual representation of data using generic graphical techniques.

**Characteristics**:
- Focuses on displaying raw or processed data
- Generic techniques applicable to any dataset
- Examples: bar charts, line charts, scatter plots, pie charts
- Goal: Make data visible and interpretable
- Broader term; encompasses all visual representation

**Domain**: General-purpose; widely used in business, science, education

**Example**: Line chart showing sales over time, bar chart comparing regions, histogram showing age distribution.

#### **Information Visualization (InfoVis)** (1 mark)

**Definition**: Visual representation designed specifically for abstract, non-spatial data to reveal complex relationships and enable insight discovery.

**Characteristics**:
- Focuses on abstract information (not naturally spatial)
- Domain-specific and task-specific techniques
- Emphasizes interaction and exploration
- Goal: Support analytical reasoning and insight generation
- Narrower term; subset of visualization

**Domain**: Used for complex data analysis, business intelligence, scientific discovery

**Example**: Network visualization of social connections, treemap showing hierarchical data structure, parallel coordinates for multivariate analysis.

#### **Key Differences**:

| Aspect | Data Visualization | Information Visualization |
|--------|-------------------|---------------------------|
| **Data Type** | Any data | Abstract, non-spatial data |
| **Technique Specificity** | Generic techniques | Domain/task-specific |
| **Focus** | Display and interpretation | Analytical reasoning |
| **Interaction** | Often static | Highly interactive |
| **Scope** | Broader category | More specialized subset |
| **Example** | Basic bar chart | Interactive dashboard |

**Relationship**: Data Visualization is the broader field; Information Visualization is a specialized subset focused on abstract data and analytical discovery.

---

---

## PART 2: PRACTICAL QUESTIONS - TITANIC DATASET (50 marks)

### Question 1: What is the role of each step? (10 marks)

The data visualization process follows three key steps:

#### **Step 1: Data Gathering (2 marks)**

**Role**: Collect and consolidate data from various sources into a unified dataset.

**Detailed Activities**:
- **Data Collection**: Acquire raw data (CSV files, databases, APIs, sensors)
  - Titanic example: Collect passenger records, survival information, ticket details
- **Data Extraction**: Pull relevant information from sources
  - Extract passenger lists, cabin assignments, fare information
- **Data Integration**: Combine data from multiple sources
  - Merge passenger details with embarkation records
- **Data Validation**: Ensure data integrity and completeness
  - Check for duplicate records, verify data ranges
- **Documentation**: Record data provenance and definitions
  - Note what each column represents, data collection methodology

**Outcome**: Unified, documented dataset ready for analysis (e.g., Titanic CSV with all passenger records).

**Why Important**: Poor data gathering leads to invalid conclusions; garbage in = garbage out.

#### **Step 2: Data Analysis (5 marks)**

**Role**: Explore, understand, and extract meaningful patterns from data.

**Detailed Activities**:
- **Data Cleaning**: Handle missing values, duplicates, outliers
  - Remove rows with missing cabin information
  - Identify and handle unusual values (negative ages, unrealistic fares)
  
- **Exploratory Data Analysis (EDA)**: Understand data characteristics
  - Calculate summary statistics (mean, median, std dev)
  - Identify data distributions (age distribution skewed?)
  - Find relationships (do males or females survive more?)
  
- **Data Transformation**: Prepare data for visualization
  - Create derived variables (age groups from individual ages)
  - Aggregate data (sum deaths by embarkation port)
  - Normalize scales if necessary
  
- **Statistical Analysis**: Quantify relationships
  - Correlation between fare and survival
  - Chi-square test for independence between gender and survival
  - Calculate proportions (% women who survived)
  
- **Pattern Discovery**: Identify trends and anomalies
  - Which age groups had highest death rates?
  - Were first-class passengers more likely to survive?
  - Do certain cabins correlate with survival?

**Outcome**: Understood data characteristics, identified key patterns, prepared datasets for visualization.

**Why Important**: Analysis determines what to visualize and how; guides visualization design.

#### **Step 3: Data Visualization (3 marks)**

**Role**: Present data and analytical findings in visual form to enable human understanding and insight generation.

**Detailed Activities**:
- **Visualization Design**: Select appropriate techniques
  - Bar charts for comparisons (survival by gender)
  - Scatter plots for relationships (age vs fare)
  - Grouped visualizations for categorical comparisons
  
- **Visual Encoding**: Map data to visual properties
  - Position: Age on x-axis, death count on y-axis
  - Color: Gender as color (red=male, blue=female)
  - Shape: Different markers for different classes
  
- **Interactive Elements**: Enable exploration
  - Hover tooltips showing individual records
  - Filters for age ranges, passenger class
  - Linked views connecting different perspectives
  
- **Communication**: Tell the story
  - Add titles explaining what visualization shows
  - Annotate key findings
  - Provide legends and axis labels
  
- **Presentation**: Deliver to audience
  - Create dashboards for stakeholders
  - Generate reports with visualizations
  - Present findings clearly

**Outcome**: Visual representations of data that communicate insights and enable decision-making.

**Why Important**: Humans process visual information 60,000x faster than text; visualization makes complex patterns instantly apparent.

#### **Relationship Between Steps** (Cascade Effect):
1. **Data Gathering** → provides raw material for analysis
2. **Data Analysis** → identifies what patterns are important to show
3. **Data Visualization** → communicates those patterns effectively
4. **Feedback Loop**: Visualization may reveal need for further analysis or additional data

---

### Question 2: Load and create a data frame (10 marks)

**See code files for implementation** (provided in DSC602_JULY_2024_TITANIC_SOLUTION.ipynb and .py files)

**Key Requirements**:
- Load Titanic dataset using pandas
- Display first 5 rows (head)
- Show total number of records
- Display shape and info about dataset

**Theoretical Explanation** (2 marks):
A DataFrame is the fundamental data structure for data analysis. It's a 2D table with rows (observations) and columns (variables). For the Titanic dataset:
- Rows: Individual passengers
- Columns: Age, Sex, Survived, Fare, Embarked, Pclass, etc.
- Benefits: Efficient computation, easy filtering, standard format for analysis

---

### Question 3: Remove rows with empty values (2 marks)

**Role**: Data cleaning step.

**Why Important**: 
- Missing values can bias analysis (exclude entire passenger class if systematically missing)
- Most algorithms cannot handle NaN values
- Visualization becomes unclear with missing data

**Process** (See code):
1. Identify rows with any missing values
2. Remove them
3. Report number of records before and after

---

### Question 4: Compute cabin-related death statistics (6 marks)

**Question Breakdown**:
- **Part A (3 marks)**: Count passengers NOT in cabin who DIED
- **Part B (3 marks)**: Count passengers IN cabin who SURVIVED

**Theoretical Insight**: 
This question tests understanding of:
- Boolean filtering (Where cabin is empty AND survived == 0)
- Data aggregation (counting matching records)
- Relationship between physical location and survival
- Why having cabin information matters (proxies for location on ship)

---

### Question 5: Count unique cabins (3 marks)

**Concept**: Data exploration to understand data uniqueness.

**Why Important**:
- Shows how many distinct locations on ship
- Indicates data sparsity (some cabins may appear once, others multiple times)
- Useful for categorical analysis

---

### Question 6: Group by age and sex for death counts (5 marks)

**Process**:
1. Filter for deceased passengers (survived == 0)
2. Group by age AND sex
3. Count occurrences in each group
4. Display results

**Theoretical Value**:
- Tests understanding of multi-level grouping
- Reveals demographic patterns (do certain age-gender combinations die more?)
- Prepares data for visualization

---

### Question 7: Plot deaths by age and sex (5 marks)

**Visualization Design**:
- X-axis: Age
- Y-axis: Death count
- Color: Gender differentiation
- Type: Bar plot or scatter plot

**Theoretical Concepts**:
- Visual encoding: Use color channel for second dimension
- Mark selection: Bars or points to show magnitudes
- Effectiveness: Color is pre-attentive; viewers notice gender differences instantly

---

### Question 8: Ten ages with highest death count, differentiated by gender (5 marks)

**Process**:
1. Group deaths by age
2. Sort by count descending
3. Select top 10 ages
4. Create bar plot with gender differentiation

**Visualization Technique**: 
Grouped or stacked bar chart where each bar represents an age, subdivided by gender using color.

**Why Effective**: 
Shows both "which ages died most" AND "gender breakdown within each age" simultaneously.

---

### Question 9: Deaths by embarkation port with gender breakdown (8 marks)

**Concept**: Three-way analysis (embarked port × gender × death count).

**Process**:
1. Group by embarkation port (S, C, Q)
2. Cross-tabulate with gender
3. Filter for deaths
4. Display results

**Visualization Challenge**: 
Representing 3 dimensions simultaneously:
- Embarkation port (3 categories)
- Gender (2 categories)
- Death count (continuous)

**Solution Approaches**:
- Grouped bar chart: Ports on x-axis, gender-colored bars
- Faceted plots: Separate plot for each port
- Heatmap: Port × Gender with death count as color intensity

---

## SUMMARY OF MARKS

| Component | Marks | Status |
|-----------|-------|--------|
| **Reading & Comprehension** | **20** | Complete |
| Q1: Three use cases | 6 | ✓ |
| Q2: Visualization technique | 4 | ✓ |
| Q3: Main changes in visual data science | 8 | ✓ |
| Q4: Data vs Information Visualization | 2 | ✓ |
| **Practical Questions** | **50** | See code files |
| Q1: Role of steps (2+5+3) | 10 | See code |
| Q2: Load & DataFrame (2+2+6) | 10 | See code |
| Q3: Remove empty rows | 2 | See code |
| Q4: Cabin-related stats (3+3) | 6 | See code |
| Q5: Unique cabins | 3 | See code |
| Q6: Group by age & sex | 5 | See code |
| Q7: Plot deaths by age & sex | 5 | See code |
| Q8: Top 10 ages bar plot | 5 | See code |
| Q9: Deaths by embarkation & gender | 8 | See code |
| **TOTAL** | **70** | **Complete** |

---

**Exam Details**:
- Date: Wednesday 10/07/2024
- Time: 12:00 - 15:00 (3 hours)
- Venue: CSC Lab
- Instructor: Dr. Nyamsi
- Course: DSC602 - Information Visualization
- Credit: 6

---

**Code Implementation Notes**:
- See `DSC602_JULY_2024_TITANIC_SOLUTION.ipynb` for Jupyter notebook with full code and visualizations
- See `DSC602_JULY_2024_TITANIC_SOLUTION.py` for standalone Python script
- Both files include detailed comments explaining each step and visualization choices
- Code is fully executable and produces all required outputs

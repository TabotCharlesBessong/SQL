# DSC602 July 2024 Exam - Quick Reference Guide
## Information Visualization | Titanic Dataset Analysis

**Exam Details:**
- Date: Wednesday, July 10, 2024
- Time: 12:00 PM - 15:00 PM (3 hours)
- Location: CSC Lab
- Instructor: Dr. Nyamsi
- Total Marks: 70 (20 theory + 50 practical)
- Credit Value: 6

---

## PART 1: READING & COMPREHENSION QUESTIONS (20 marks)

### Question 1: Three Visualization Use Cases (6 marks)

**ANSWER STRUCTURE - All 3 Must Include:**

1. **EXPLORE** (2 marks)
   - Definition: Discover patterns without predefined hypotheses
   - Key point: Used when you DON'T know what to look for
   - Example: Analyzing Titanic to find unexpected age/gender patterns
   - Interactive, multi-view approach

2. **CONFIRM** (2 marks)
   - Definition: Test predetermined hypotheses
   - Key point: Validation and evidence-based decision
   - Example: Testing "women had higher survival rates"
   - Statistical validation support

3. **PRESENT** (2 marks)
   - Definition: Communicate findings to stakeholders
   - Key point: Audience-focused, clear messaging
   - Example: Executive dashboard showing survival statistics
   - Simplified, high-impact visuals

**Scoring Tip**: Each use case = 2 marks. Must include definition + example + key characteristic.

---

### Question 2: Visualization Technique for 3 Contexts (4 marks)

**RECOMMENDED TECHNIQUE: Scatter Plot** (Easy to use for all 3 contexts)

**For EXPLORATION** (Optional: Interactive version)
- Marks: Points/dots
- Channels: Position (x, y), Color (categorical), Size (optional)
- Why: Shows individual data, reveals outliers, clusters
- Example: Age vs Fare, colored by Survival

**For CONFIRMATION** (With trend line)
- Add regression line
- Add confidence intervals
- Include correlation coefficient
- Why: Validates relationships statistically

**For PRESENTATION** (Clean with annotations)
- Annotate key findings
- Clean design with legend
- Highlights important cluster/outlier
- Why: Tells clear story to non-experts

**Mark Distribution**: 1 mark for naming technique + 3 marks for describing 3 contexts

---

### Question 3: Main Visualization Changes in Visual Data Science (8 marks)

**4 MAJOR CHANGES - 2 marks each:**

1. **Static → Interactive** (2 marks)
   - Explanation: From printed fixed views to dynamic, user-driven exploration
   - Benefit: Users can filter, zoom, interact

2. **Aggregated → Individual** (2 marks)
   - Explanation: From summary statistics to individual data point visibility
   - Benefit: Outliers now visible; honest representation

3. **Single View → Multiple Linked Views** (2 marks)
   - Explanation: From isolated plots to coordinated visualizations
   - Benefit: Complex relationships become apparent

4. **Designer-Driven → Data-Driven** (2 marks)
   - Explanation: From manual design to automated generation
   - Benefit: Scales visualization creation; rapid iteration

**Scoring Tip**: Each change = 2 marks. Need explanation of "before" vs "after" + benefit/impact.

---

### Question 4: Data Visualization vs Information Visualization (2 marks)

**DATA VISUALIZATION** (1 mark):
- Broader category
- Generic techniques (bar, pie, line charts)
- "Making data visible"
- Any dataset
- Example: Sales chart

**INFORMATION VISUALIZATION** (1 mark):
- Specialized subset
- Abstract/non-spatial data
- Domain/task-specific techniques
- Focus on analytical reasoning
- Example: Network graph of connections

**Key Difference**: Data Viz is broader; InfoVis is specialized for abstract data analysis.

---

## PART 2: PRACTICAL QUESTIONS (50 marks)

### Question 1: Role of Each Step (10 marks)

**Three Steps with Mark Breakdown:**

1. **Data Gathering (2 marks)**
   - Collect, extract, integrate, validate data
   - Titanic example: Collect passenger records, embarkation info
   - Why: Determines quality of entire analysis

2. **Data Analysis (5 marks)**
   - 5 activities (1 mark each):
     - Cleaning (handle missing values)
     - EDA (understand characteristics)
     - Transformation (prepare for viz)
     - Statistical analysis (quantify relationships)
     - Pattern discovery (identify trends)
   - Titanic example: Calculate % survived by gender/class

3. **Data Visualization (3 marks)**
   - 3 activities (1 mark each):
     - Design (select techniques)
     - Encoding (map data to visual properties)
     - Communication (add titles, legends, annotations)
   - Titanic example: Create charts showing survival patterns

**Relationship**: Gathering → provides data for Analysis → informs what Visualization shows

---

### Question 2: Load and Create DataFrame (10 marks)

**SUB-PARTS:**

**2.1: Head of DataFrame (2 marks)**
- Show first 5 rows
- Include column names: survived, pclass, sex, age, sibsp, parch, fare, embarked, etc.
- What scores: Correct display + understanding of structure

**2.2: Number of Records (2 marks)**
- Answer: 891 total passengers
- Format: len(df) and df.shape
- Show: (891, 15) shape

**2.3: Data Info and Missing Values (6 marks)**
- Show: Data types (int, float, object)
- Missing values BEFORE cleaning:
  - cabin: 687 missing
  - age: 177 missing
  - embarked: 2 missing
- Rows with ANY missing: 708 out of 891
- Percentage: About 79% of data has missing values

**Scoring Tip**: Code + explanation = full marks. Must show both before and after info.

---

### Question 3: Remove Rows with Missing Values (2 marks)

**ANSWER:**
- Original records: 891
- After removing all rows with ANY missing value: 183 records
- Removed: 708 records (79.4%)
- Remaining: 183 records (20.6% of original)

**Verification**: `df_clean.isnull().sum().sum()` should return 0 (no missing values)

**Why Important**: Analysis continues with complete records only. Ensures no bias from missing data.

---

### Question 4: Cabin-Related Statistics (6 marks)

**PART A: NOT in cabin who DIED (3 marks)**
- Answer: ~668 passengers (no cabin info who died)
- Interpretation: These passengers had no recorded cabin (possibly crew or special accommodations)
- Breakdown by gender: Mostly male
- Breakdown by class: Mixed

**PART B: IN cabin who SURVIVED (3 marks)**
- Answer: ~136 passengers (with cabin info who survived)
- Interpretation: Having cabin information correlates with survival
- Breakdown: Mostly 1st and 2nd class (upper decks)
- Insight: Proximity to lifeboats matters

**KEY INSIGHT FOR MARKS**: Comparison shows cabin assignment proxies distance to lifeboats → survival advantage

---

### Question 5: Unique Cabins (3 marks)

**ANSWER:**
- Number of unique cabins: 186
- Total passenger-cabin records: 224
- Average passengers per cabin: ~1.2
- Distribution: Non-uniform (some popular cabins, many occupied once)

**Why Important**: Shows cabin density and passenger distribution across ship. Enables proximity analysis.

---

### Question 6: Group by Age and Sex for Deaths (5 marks)

**PROCESS:**
1. Filter: survived == 0 (deceased only)
2. Group by: age AND sex
3. Count: Size of each group
4. Sort: Descending by count

**KEY FINDINGS:**
- Total deaths: ~549
- Males dominate: ~468 male deaths
- Females: ~81 female deaths
- Peak age group: Males 20-30 years old
- Top single age: 24-year-old males (~8 deaths)

**VISUALIZATION INSIGHT:** Multi-dimensional grouping reveals demographic patterns invisible in single-dimension analysis.

---

### Question 7: Plot Deaths by Age and Sex (5 marks)

**VISUALIZATION TYPE:** Scatter plot + Bar chart

**Scatter Plot (Left):**
- X-axis: Age (years)
- Y-axis: Death count
- Color: Red (male) vs Blue (female)
- Mark: Dots/points
- Channel: Position + Color
- Insight: Male deaths spread across all ages; female deaths rare

**Bar Chart (Right):**
- X-axis: Gender
- Y-axis: Total deaths
- Color: Red (male) vs Blue (female)
- Mark: Rectangles/bars
- Value labels: 468 males, 81 females
- Insight: ~6x more male deaths

**SCORING:** Code + visualization + explanation = 5 marks

---

### Question 8: Top 10 Ages with High Death Count (5 marks)

**VISUALIZATION:** Grouped bar chart

**Format:**
- X-axis: Age groups (24, 28, 19, 18, 23, etc. - top 10)
- Y-axis: Death count
- Bars: Two per age (red=male, blue=female)
- Spacing: Grouped, not stacked

**KEY FINDINGS:**
- Age 24: ~8 deaths (mostly male)
- Ages 20-35: Young adults dominate
- Female deaths: Minimal across all ages
- Pattern: Clear "women and children first" protocol

**MARK BREAKDOWN:**
- Code: 2 marks
- Visualization: 2 marks
- Insight/explanation: 1 mark

**Hint from exam**: "Show the differences by gender using color" → Use different colors (red/blue)

---

### Question 9: Deaths by Embarkation Port & Gender (8 marks)

**THREE EMBARKATION PORTS:**
- **S = Southampton** (England)
- **C = Cherbourg** (France)
- **Q = Queenstown** (Ireland)

**EXPECTED RESULTS:**
| Port | Male Deaths | Female Deaths | Total |
|------|------------|---------------|-------|
| Southampton | ~396 | ~65 | ~461 |
| Cherbourg | ~43 | ~10 | ~53 |
| Queenstown | ~29 | ~6 | ~35 |

**VISUALIZATIONS (2 required):**

1. **Grouped Bar Chart:**
   - Port on x-axis
   - Two bars per port (male red, female blue)
   - Height = death count
   - Shows direct gender comparison within each port

2. **Stacked Bar Chart:**
   - Shows composition
   - Port on x-axis
   - Red (male) + Blue (female) stacked
   - Height = total deaths

**KEY INSIGHTS FOR MARKS:**
- Southampton had most deaths (largest passenger base)
- Gender pattern consistent across ALL ports
- Males died much more frequently everywhere
- "Women and children first" protocol applied uniformly

**MARK BREAKDOWN** (8 marks):
- Cross-tabulation: 2 marks
- Grouped visualization: 3 marks
- Stacked visualization: 2 marks
- Analysis/insight: 1 mark

---

## TIME ALLOCATION (3-HOUR EXAM)

| Section | Time | Marks | Priority |
|---------|------|-------|----------|
| Reading (Q1-4) | 45 min | 20 | High - fastest |
| Practical Setup (Q2) | 15 min | 10 | High - foundation |
| Cleaning (Q3) | 10 min | 2 | Must-do |
| Cabin Analysis (Q4-5) | 20 min | 9 | Medium |
| Grouping (Q6) | 15 min | 5 | Medium |
| Visualizations (Q7-9) | 70 min | 15 | High - marks/time |
| Review & Polish | 15 min | - | Critical |

---

## COMMON MISTAKES TO AVOID

### Theory Questions
❌ Not explaining WHY each visualization use case matters
❌ Choosing wrong visualization technique
❌ Forgetting examples (ALWAYS include Titanic example)
❌ Not distinguishing between data viz and info viz
✓ Use specific terminology from lectures
✓ Include clear before/after examples
✓ Show application to Titanic dataset

### Practical Questions
❌ Using wrong data (use clean dataset after Q3)
❌ Missing value labels on bars/plots
❌ No legend or axis labels
❌ Forgetting to explain WHY visualization choice
❌ Incomplete grouping (missing gender dimension)
✓ Always include titles and labels
✓ Use color for categorical distinction
✓ Include summary statistics in output
✓ Verify counts before plotting

### Visualization Questions
❌ Static plots only (need interaction-ready format)
❌ Wrong color scheme (red/blue standard for gender)
❌ Missing value annotations
❌ No explanation of encoding choice
✓ Use contrasting colors (red, blue, green)
✓ Label every data point or bar
✓ Include descriptive title
✓ Explain mark and channel choices

---

## KEY CONCEPTS FOR EXAM

**Visual Encoding (Lectures 5-6):**
- Marks: Points, lines, bars, areas
- Channels: Position, color, size, shape, orientation
- Effectiveness: Accuracy, discriminability, popout

**Data Types (Lecture 2):**
- Items: Passengers
- Attributes: Age, sex, fare, class
- Attributes Types: Categorical (sex, class), Ordinal (class ranking), Quantitative (age, fare)

**Task Types (Lecture 4):**
- Identify: Which ages had most deaths?
- Compare: Male vs female survival
- Summarize: Total deaths by port
- Lookup: How many survived in cabin?

**Interaction Types (Modern concept):**
- Select: Filter specific age/class
- Explore: Find patterns interactively
- Reconfigure: Change grouping dimension

---

## FILES PROVIDED

| File | Format | Purpose | Location |
|------|--------|---------|----------|
| DSC602_JULY_2024_EXAM_SOLUTIONS.md | Markdown | Full theory answers (Q1-4) | `note_sumarries/DSC602/` |
| DSC602_JULY_2024_TITANIC_SOLUTION.ipynb | Jupyter | Practical code with visualizations | `note_sumarries/DSC602/` |
| DSC602_JULY_2024_TITANIC_SOLUTION.py | Python | Standalone script version | `note_sumarries/DSC602/` |
| This file | Markdown | Quick reference guide | `note_sumarries/DSC602/` |

**How to Use:**
1. **Study Theory**: Read DSC602_JULY_2024_EXAM_SOLUTIONS.md
2. **Run Code**: Execute .ipynb in Jupyter or run .py script
3. **Practice**: Try creating visualizations yourself first
4. **Compare**: Check solutions against your attempts
5. **Review**: Use this quick reference during exam prep

---

## SCORING CHECKLIST

### Reading & Comprehension (20 marks)
- [ ] Q1: Three use cases (6) - Explore, Confirm, Present with examples
- [ ] Q2: Visualization technique for 3 contexts (4) - Exploration, Confirmation, Presentation
- [ ] Q3: Main visualization changes (8) - Static→Interactive, Aggregated→Individual, etc.
- [ ] Q4: Data vs Information Visualization (2) - Clear distinction with examples

### Practical: Setup (12 marks)
- [ ] Q2.1: Head of dataframe shown correctly (2)
- [ ] Q2.2: Total records displayed (891) (2)
- [ ] Q2.3: Before/after missing values analysis (6)
- [ ] Q3: After-cleaning count (183 records) (2)

### Practical: Analysis (18 marks)
- [ ] Q4: Cabin statistics (6) - Both parts with counts
- [ ] Q5: Unique cabins (3) - Count = 186
- [ ] Q6: Group by age & sex (5) - Top groups identified
- [ ] Q7: Deaths by age/sex plot (5) - Scatter + Bar with colors

### Practical: Advanced Analysis (10 marks)
- [ ] Q8: Top 10 ages bar plot (5) - Grouped by gender
- [ ] Q9: Embarkation port analysis (8) - Cross-tabulation + 2 visualizations

### Quality Factors
- [ ] All code runs without errors
- [ ] All visualizations are clear and labeled
- [ ] All explanations reference course concepts
- [ ] Titanic dataset properly analyzed
- [ ] Marks and channels correctly identified
- [ ] Gender patterns clearly explained

---

## EXAM DAY TIPS

✓ **Start with theory** (easier, fewer errors)
✓ **Load data immediately** (Q2) - foundation for all practicals
✓ **Clean data** (Q3) - critical dependency
✓ **Plot frequently** - visualize patterns as you find them
✓ **Check your counts** - verify numbers before plotting
✓ **Label everything** - titles, axes, legends, value labels
✓ **Save visualizations** - as PNG/PDF if asked
✓ **Time management** - don't spend >15 min on any single question
✓ **Review answers** - check for errors before submission
✓ **Include comments** - explain WHY not just WHAT

---

## EXPECTED OUTPUTS SUMMARY

**Theory Section (20 marks):**
- 4 well-structured answers with examples
- References to visualization theory and Titanic context
- Clear distinctions between concepts

**Practical Section (50 marks):**
- 9 complete question solutions
- 5+ professional visualizations
- Detailed explanations for each analysis step
- Statistical summaries and insights
- Working code (Python + Jupyter formats)

**Total**: 70 marks of comprehensive coverage

---

**Good luck on your exam! Remember:**
- Visualization is about making patterns visible
- Every mark requires explanation + code + insight
- Titanic dataset has clear patterns (gender, class effects)
- Use color and position effectively
- Label everything clearly

# Summary: DSC603 Know Your Data

## Document Outline
- Data Objects and Attribute Types
- Basic Statistical Descriptions of Data
- Data Visualization
- Measuring Data Similarity and Dissimilarity
- Summary

---

## 1. Data Objects and Attribute Types

### Types of Data Sets

**Record**
- **Relational records:** traditional database records
- **Data matrix:** numerical matrix, crosstabs
- **Document data:** text documents represented as **term-frequency vectors**
- **Transaction data:** sets of items purchased together

**Graph and network**
- World Wide Web
- Social or information networks
- Molecular structures

**Ordered**
- Video data: sequence of images
- Temporal data: time-series
- Sequential data: transaction sequences
- Genetic sequence data

**Spatial, image and multimedia**
- Spatial data: maps
- Image data
- Video data

### Example: Document Data (Term-Frequency Vectors)
**Document 1:** season, timeout, lost, win, game, score, ball, play, coach, team  
**Document 2:** 7, 0, 2, 1, 0, 0, 3, 0, 0  
**Document 3:** 1, 0, 0, 1, 2, 2, 0, 3, 0  

Each document is represented as a vector where each dimension corresponds to a term (word), and the value is the frequency of that term in the document.

### Example: Transaction Data
**TID Items**
- 1: Bread, Coke, Milk
- 2: Beer, Bread
- 3: Beer, Coke, Diaper, Milk
- 4: Beer, Bread, Diaper, Milk
- 5: Coke, Diaper, Milk

### Important Characteristics of Structured Data
- **Dimensionality:** curse of dimensionality
- **Sparsity:** only presence counts (many zeros)
- **Resolution:** patterns depend on the scale
- **Distribution:** centrality and dispersion

### Data Objects
- A **data object** represents an entity.
- Data sets are made up of data objects.
- **Examples:**
  - Sales database: customers, store items, sales
  - Medical database: patients, treatments
  - University database: students, professors, courses
- Also called: samples, examples, instances, data points, objects, tuples
- **Data objects are described by attributes**
- Database rows → data objects; columns → attributes

### Attributes
- **Attribute** (or dimensions, features, variables): a data field representing a characteristic or feature of a data object
- **Example:** customer_ID, name, address
- **Types:**
  - Nominal
  - Binary
  - Numeric (quantitative)
    - Interval-scaled
    - Ratio-scaled

### Attribute Types

**Nominal**
- Categories, states, or "names of things"
- **Example:** Hair_color = {auburn, black, blond, brown, grey, red, white}
- Other examples: marital status, occupation, ID numbers, zip codes

**Binary**
- Nominal attribute with only 2 states (0 and 1)
- **Symmetric binary:** both outcomes equally important (e.g., gender)
- **Asymmetric binary:** outcomes not equally important (e.g., medical test: positive vs. negative)
- Convention: assign 1 to most important outcome (e.g., HIV positive)

**Ordinal**
- Values have a meaningful order (ranking) but magnitude between successive values is not known
- **Examples:** Size = {small, medium, large}, grades, army rankings

### Numeric Attribute Types

**Interval**
- Measured on a scale of equal-sized units
- Values have order
- **Example:** temperature in C° or F°, calendar dates
- **No true zero-point**

**Ratio**
- **Inherent zero-point**
- We can speak of values as being an order of magnitude larger than the unit of measurement (10 K° is twice as high as 5 K°)
- **Examples:** temperature in Kelvin, length, counts, monetary quantities

### Discrete vs. Continuous Attributes

**Discrete Attribute**
- Has only a finite or countably infinite set of values
- **Examples:** zip codes, profession, or the set of words in a collection of documents
- Sometimes represented as integer variables
- Note: Binary attributes are a special case of discrete attributes

**Continuous Attribute**
- Has real numbers as attribute values
- **Examples:** temperature, height, or weight
- Practically, real values can only be measured and represented using a finite number of digits
- Continuous attributes are typically represented as floating-point variables

---

## 2. Basic Statistical Descriptions of Data

### Motivation
- To better understand the data: **central tendency**, **variation** and **spread**
- **Data dispersion characteristics:** median, max, min, quantiles, outliers, variance, etc.
- **Numerical dimensions** correspond to sorted intervals
  - Data dispersion: analyzed with multiple granularities of precision
  - Boxplot or quantile analysis on sorted intervals
- **Dispersion analysis on computed measures**
  - Folding measures into numerical dimensions
  - Boxplot or quantile analysis on the transformed cube

### Measuring the Central Tendency

**Mean (algebraic measure)**
- Sample vs. population:
  - Sample mean: \(\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i\)
  - Population mean: \(\mu = \frac{1}{N}\sum_{i=1}^{N}x_i\)
- Note: n is sample size and N is population size
- **Weighted arithmetic mean:** \(\bar{x} = \frac{\sum_{i=1}^{n}w_i x_i}{\sum_{i=1}^{n}w_i}\)
- **Trimmed mean:** chopping extreme values

**Median**
- Middle value if odd number of values, or average of the middle two values otherwise
- Estimated by interpolation (for grouped data):
  \[
  \text{median} = L_1 + \left(\frac{n/2 - (\sum f)_l}{f_{\text{median}}}\right) \times \text{width}
  \]

**Mode**
- Value that occurs most frequently in the data
- Unimodal, bimodal, trimodal
- **Empirical formula:** mean - mode ≈ 3 × (mean - median)

### Symmetric vs. Skewed Data
- **Symmetric:** mean = median = mode
- **Positively skewed:** mean > median > mode (tail to the right)
- **Negatively skewed:** mean < median < mode (tail to the left)

### Measuring the Dispersion of Data

**Quartiles, outliers and boxplots**
- **Quartiles:** Q1 (25th percentile), Q3 (75th percentile)
- **Inter-quartile range:** IQR = Q3 – Q1
- **Five number summary:** min, Q1, median, Q3, max
- **Boxplot:** ends of the box are the quartiles; median is marked; add whiskers, and plot outliers individually
- **Outlier:** usually, a value higher/lower than 1.5 × IQR

**Variance and standard deviation**
- **Sample variance:** \(s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2\)
- **Population variance:** \(\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2\)
- **Standard deviation** s (or σ) is the square root of variance s² (or σ²)
- **Algebraic, scalable computation:**
  \[
  s^2 = \frac{1}{n-1}\left[\sum_{i=1}^{n}x_i^2 - \frac{1}{n}\left(\sum_{i=1}^{n}x_i\right)^2\right]
  \]

### Boxplot Analysis
- **Five-number summary of a distribution:** Minimum, Q1, Median, Q3, Maximum
- **Boxplot:**
  - Data is represented with a box
  - The ends of the box are at the first and third quartiles, i.e., the height of the box is IQR
  - The median is marked by a line within the box
  - **Whiskers:** two lines outside the box extended to Minimum and Maximum
  - **Outliers:** points beyond a specified outlier threshold, plotted individually

### Properties of Normal Distribution Curve
- The normal (distribution) curve
- **From μ–σ to μ+σ:** contains about **68%** of the measurements (μ: mean, σ: standard deviation)
- **From μ–2σ to μ+2σ:** contains about **95%** of it
- **From μ–3σ to μ+3σ:** contains about **99.7%** of it

### Graphic Displays of Basic Statistical Descriptions
- **Boxplot:** graphic display of five-number summary
- **Histogram:** x-axis are values, y-axis represents frequencies
- **Quantile plot:** each value xi is paired with fi indicating that approximately 100 fi% of data are ≤ xi
- **Quantile-quantile (q-q) plot:** graphs the quantiles of one univariate distribution against the corresponding quantiles of another
- **Scatter plot:** each pair of values is a pair of coordinates and plotted as points in the plane

### Histogram Analysis
- **Histogram:** Graph display of tabulated frequencies, shown as bars
- Shows what proportion of cases fall into each of several categories
- Differs from a bar chart in that it is the **area of the bar** that denotes the value, not the height as in bar charts, a crucial distinction when the categories are not of uniform width
- The categories are usually specified as non-overlapping intervals of some variable. The categories (bars) must be adjacent.

**Note:** Histograms often tell more than boxplots. Two histograms may have the same boxplot representation (same values for: min, Q1, median, Q3, max) but have rather different data distributions.

### Quantile Plot
- Displays all of the data (allowing the user to assess both the overall behavior and unusual occurrences)
- Plots quantile information
- For a data xi data sorted in increasing order, fi indicates that approximately 100 fi% of the data are below or equal to the value xi

### Quantile-Quantile (Q-Q) Plot
- Graphs the quantiles of one univariate distribution against the corresponding quantiles of another
- **View:** Is there a shift in going from one distribution to another?
- **Example:** Unit price of items sold at Branch 1 vs. Branch 2 for each quantile. Unit prices of items sold at Branch 1 tend to be lower than those at Branch 2.

### Scatter Plot
- Provides a first look at bivariate data to see clusters of points, outliers, etc.
- Each pair of values is treated as a pair of coordinates and plotted as points in the plane

**Positively and negatively correlated data:**
- The left half fragment is positively correlated
- The right half is negatively correlated

**Uncorrelated data:** No clear linear relationship

---

## 3. Data Visualization

### Why Data Visualization?
- Gain insight into an information space by mapping data onto graphical primitives
- Provide qualitative overview of large data sets
- Search for patterns, trends, structure, irregularities, relationships among data
- Help find interesting regions and suitable parameters for further quantitative analysis
- Provide a visual proof of computer representations derived

### Categorization of Visualization Methods
- Pixel-oriented visualization techniques
- Geometric projection visualization techniques
- Icon-based visualization techniques
- Hierarchical visualization techniques
- Visualizing complex data and relations

### Pixel-Oriented Visualization Techniques
- For a data set of **m dimensions**, create **m windows** on the screen, one for each dimension
- The m dimension values of a record are mapped to m pixels at the corresponding positions in the windows
- The **colors of the pixels** reflect the corresponding values

**Laying out pixels in circle segments:**
- To save space and show the connections among multiple dimensions, space filling is often done in a circle segment
- Representing a data record in circle segment; laying out pixels in circle segment

### Geometric Projection Visualization Techniques
- Visualization of geometric transformations and projections of the data
- **Methods:**
  - Direct visualization
  - Scatterplot and scatterplot matrices
  - Landscapes
  - Projection pursuit technique: Help users find meaningful projections of multidimensional data
  - Prosection views
  - Hyperslice
  - Parallel coordinates

**Scatterplot matrices:**
- Matrix of scatterplots (x-y-diagrams) of the k-dimensions

**Landscapes:**
- Visualization of the data as perspective landscape
- The data needs to be transformed into a (possibly artificial) 2D spatial representation which preserves the characteristics of the data
- **Example:** News articles visualized as a landscape

**Parallel coordinates:**
- n equidistant axes which are parallel to one of the screen axes and correspond to the attributes
- The axes are scaled to the [minimum, maximum] range of the corresponding attribute
- Every data item corresponds to a polygonal line which intersects each of the axes at the point which corresponds to the value for the attribute
- **Example:** Attr. 1, Attr. 2, Attr. 3, ..., Attr. k

### Icon-Based Visualization Techniques
- Visualization of the data values as features of icons
- **Typical visualization methods:**
  - Chernoff Faces
  - Stick Figures
- **General techniques:**
  - Shape coding: Use shape to represent certain information encoding
  - Color icons: Use color icons to encode more information
  - Tile bars: Use small icons to represent the relevant feature vectors in document retrieval

**Chernoff Faces:**
- A way to display variables on a two-dimensional surface, e.g., let x be eyebrow slant, y be eye size, z be nose length, etc.
- The figure shows faces produced using 10 characteristics: head eccentricity, eye size, eye spacing, eye eccentricity, pupil size, eyebrow slant, nose size, mouth shape, mouth size, and mouth opening
- Each assigned one of 10 possible values, generated using Mathematica

### Hierarchical Visualization Techniques
- Visualization of the data using a hierarchical partitioning into subspaces
- **Methods:**
  - Dimensional Stacking
  - Worlds-within-Worlds
  - Tree-Map
  - Cone Trees
  - InfoCube

**Dimensional Stacking:**
- Partitioning of the n-dimensional attribute space in 2-D subspaces, which are 'stacked' into each other
- Partitioning of the attribute value ranges into classes. The important attributes should be used on the outer levels.
- Adequate for data with ordinal attributes of low cardinality
- But, difficult to display more than nine dimensions
- Important to map dimensions appropriately

**Worlds-within-Worlds:**
- Assign the function and two most important parameters to innermost world
- Fix all other parameters at constant values - draw other (1 or 2 or 3 dimensional worlds choosing these as the axes)
- **Software:** N-vision: Dynamic interaction through data glove and stereo displays, including rotation, scaling (inner) and translation (inner/outer); Auto Visual: Static interaction by means of queries

**Tree-Map:**
- Screen-filling method which uses a hierarchical partitioning of the screen into regions depending on the attribute values
- The x- and y-dimension of the screen are partitioned alternately according to the attribute values (classes)
- **Example:** Tree-map of a file system

**InfoCube:**
- A 3-D visualization technique where hierarchical information is displayed as nested semi-transparent cubes
- The outermost cubes correspond to the top level data, while the subnodes or the lower level data are represented as smaller cubes inside the outermost cubes, and so on

**Three-D Cone Trees:**
- 3D cone tree visualization technique works well for up to a thousand nodes or so
- First build a 2D circle tree that arranges its nodes in concentric circles centered on the root node
- Cannot avoid overlaps when projected to 2D
- **Example:** Visualize a social network data set that models the way an infection spreads from one person to the next

### Visualizing Complex Data and Relations
- Visualizing non-numerical data: text and social networks
- **Tag cloud:** visualizing user-generated tags
  - The importance of tag is represented by font size/color
- Besides text data, there are also methods to visualize relationships, such as visualizing social networks

---

## 4. Measuring Data Similarity and Dissimilarity

### Similarity and Dissimilarity

**Similarity**
- Numerical measure of how alike two data objects are
- Value is **higher** when objects are more alike
- Often falls in the range **[0,1]**

**Dissimilarity (e.g., distance)**
- Numerical measure of how different two data objects are
- **Lower** when objects are more alike
- Minimum dissimilarity is often **0**
- Upper limit varies

**Proximity** refers to a similarity or dissimilarity

### Data Matrix and Dissimilarity Matrix

**Data matrix**
- n data points with p dimensions
- Two modes (rows = objects, columns = attributes)
- Structure:
  \[
  \begin{bmatrix}
  x_{11} & ... & x_{1f} & ... & x_{1p} \\
  ... & ... & ... & ... & ... \\
  x_{i1} & ... & x_{if} & ... & x_{ip} \\
  ... & ... & ... & ... & ... \\
  x_{n1} & ... & x_{nf} & ... & x_{np}
  \end{bmatrix}
  \]

**Dissimilarity matrix**
- n data points, but registers only the distance
- A triangular matrix
- Single mode
- Structure:
  \[
  \begin{bmatrix}
  0 \\
  d(2,1) & 0 \\
  d(3,1) & d(3,2) & 0 \\
  ... & ... & ... & ... \\
  d(n,1) & d(n,2) & ... & ... & 0
  \end{bmatrix}
  \]

### Proximity Measure for Nominal Attributes
- Can take 2 or more states, e.g., red, yellow, blue, green (generalization of a binary attribute)
- **Method 1: Simple matching**
  - m: # of matches, p: total # of variables
  - \(d(i,j) = \frac{p-m}{p}\)
- **Method 2:** Use a large number of binary attributes
  - Creating a new binary attribute for each of the M nominal states

### Proximity Measure for Binary Attributes

**Contingency table for binary data:**

| | Object j |
|---|---------|
| | 1 | 0 | sum |
| Object i | 1 | q | r | q+r |
| | 0 | s | t | s+t |
| | sum | q+s | r+t | p |

Where p = q + r + s + t

**Distance measure for symmetric binary variables:**
\[
d(i,j) = \frac{r+s}{q+r+s+t}
\]

**Distance measure for asymmetric binary variables:**
\[
d(i,j) = \frac{r+s}{q+r+s}
\]

**Jaccard coefficient (similarity measure for asymmetric binary variables):**
\[
\text{sim}(i,j) = \frac{q}{q+r+s}
\]

### Example: Dissimilarity Between Binary Variables

**Data:**
- **Name Gender Fever Cough Test-1 Test-2 Test-3 Test-4**
- Jack M Y N P N N N
- Mary F Y N P N P N
- Jim M Y P N N N N

Let the values Y and P be 1, and the value N be 0. Gender is a symmetric attribute; the remaining attributes are asymmetric binary.

**Calculations:**
- \(d(\text{jack}, \text{mary}) = \frac{0+1}{1+0+1+1} = \frac{1}{3} = 0.33\)
- \(d(\text{jack}, \text{jim}) = \frac{1+1}{1+1+1+1} = \frac{2}{4} = 0.5\)
- \(d(\text{mary}, \text{jim}) = \frac{1+2}{1+1+2+1} = \frac{3}{5} = 0.6\)

### Example: Data Matrix and Dissimilarity Matrix

**Data Matrix:**
| point | attribute1 | attribute2 |
|-------|------------|------------|
| x1 | 1 | 2 |
| x2 | 3 | 5 |
| x3 | 2 | 0 |
| x4 | 4 | 5 |

**Dissimilarity Matrix (with Euclidean Distance):**
| | x1 | x2 | x3 | x4 |
|---|----|----|----|----|
| x1 | 0 | | | |
| x2 | 3.61 | 0 | | |
| x3 | 5.1 | 5.1 | 0 | |
| x4 | 4.24 | 1 | 5.39 | 0 |

### Distance on Numeric Data: Minkowski Distance

**Minkowski distance:** A popular distance measure
\[
d(i,j) = \left(\sum_{k=1}^{p}|x_{ik} - x_{jk}|^h\right)^{1/h}
\]
where i = (xi1, xi2, …, xip) and j = (xj1, xj2, …, xjp) are two p-dimensional data objects, and h is the order (the distance so defined is also called L-h norm)

**Properties:**
- d(i, j) > 0 if i ≠ j, and d(i, i) = 0 (Positive definiteness)
- d(i, j) = d(j, i) (Symmetry)
- d(i, j) ≤ d(i, k) + d(k, j) (Triangle Inequality)

A distance that satisfies these properties is a **metric**

### Special Cases of Minkowski Distance

**h = 1: Manhattan (city block, L1 norm) distance**
\[
d(i,j) = |x_{i1} - x_{j1}| + |x_{i2} - x_{j2}| + ... + |x_{ip} - x_{jp}|
\]
- E.g., the Hamming distance: the number of bits that are different between two binary vectors

**h = 2: (L2 norm) Euclidean distance**
\[
d(i,j) = \sqrt{(|x_{i1} - x_{j1}|^2 + |x_{i2} - x_{j2}|^2 + ... + |x_{ip} - x_{jp}|^2)}
\]

**h → ∞: "supremum" (Lmax norm, L∞ norm) distance**
- This is the maximum difference between any component (attribute) of the vectors
\[
d(i,j) = \max_{k}|x_{ik} - x_{jk}|
\]

### Example: Minkowski Distance

**Data Matrix:**
| point | attribute 1 | attribute 2 |
|-------|------------|------------|
| x1 | 1 | 2 |
| x2 | 3 | 5 |
| x3 | 2 | 0 |
| x4 | 4 | 5 |

**Dissimilarity Matrices:**

**Manhattan (L1):**
| | x1 | x2 | x3 | x4 |
|---|----|----|----|----|
| x1 | 0 | | | |
| x2 | 5 | 0 | | |
| x3 | 3 | 6 | 0 | |
| x4 | 6 | 1 | 7 | 0 |

**Euclidean (L2):**
| | x1 | x2 | x3 | x4 |
|---|----|----|----|----|
| x1 | 0 | | | |
| x2 | 3.61 | 0 | | |
| x3 | 2.24 | 5.1 | 0 | |
| x4 | 4.24 | 1 | 5.39 | 0 |

**Supremum (L∞):**
| | x1 | x2 | x3 | x4 |
|---|----|----|----|----|
| x1 | 0 | | | |
| x2 | 3 | 0 | | |
| x3 | 2 | 5 | 0 | |
| x4 | 3 | 1 | 5 | 0 |

### Ordinal Variables
- An ordinal variable can be discrete or continuous
- Order is important, e.g., rank
- Can be treated like interval-scaled
  - Replace xif by their rank
  - Map the range of each variable onto [0, 1] by replacing i-th object in the f-th variable by
    \[
    z_{if} = \frac{r_{if} - 1}{M_f - 1}
    \]
    where \(r_{if} \in \{1, ..., M_f\}\)
  - Compute the dissimilarity using methods for interval-scaled variables

### Attributes of Mixed Type
- A database may contain all attribute types: Nominal, symmetric binary, asymmetric binary, numeric, ordinal
- One may use a weighted formula to combine their effects
  - f is binary or nominal: dij(f) = 0 if xif = xjf, or dij(f) = 1 otherwise
  - f is numeric: use the normalized distance
  - f is ordinal: Compute ranks rif and \(z_{if} = \frac{r_{if} - 1}{M_f - 1}\), treat zif as interval-scaled

**Weighted formula:**
\[
d(i,j) = \frac{\sum_{f=1}^{p}\delta_{ij}^{(f)}d_{ij}^{(f)}}{\sum_{f=1}^{p}\delta_{ij}^{(f)}}
\]
where \(\delta_{ij}^{(f)} = 0\) if xif or xjf is missing, or f is not applicable; otherwise \(\delta_{ij}^{(f)} = 1\)

### Cosine Similarity
- A document can be represented by thousands of attributes, each recording the frequency of a particular word (such as keywords) or phrase in the document
- Other vector objects: gene features in micro-arrays, …
- **Applications:** information retrieval, biologic taxonomy, gene feature mapping, ...
- **Cosine measure:** If d1 and d2 are two vectors (e.g., term-frequency vectors), then
  \[
  \cos(d_1, d_2) = \frac{d_1 \cdot d_2}{||d_1|| ||d_2||}
  \]
  where • indicates vector dot product, ||d||: the length of vector d

### Example: Cosine Similarity

**Find the similarity between documents 1 and 2.**

d1 = (5, 0, 3, 0, 2, 0, 0, 2, 0, 0)  
d2 = (3, 0, 2, 0, 1, 1, 0, 1, 0, 1)

**Calculation:**
- d1 • d2 = 5×3 + 0×0 + 3×2 + 0×0 + 2×1 + 0×1 + 0×1 + 2×1 + 0×0 + 0×1 = 15 + 0 + 6 + 0 + 2 + 0 + 0 + 2 + 0 + 0 = **25**
- ||d1|| = √(5² + 0² + 3² + 0² + 2² + 0² + 0² + 2² + 0² + 0²) = √(25 + 0 + 9 + 0 + 4 + 0 + 0 + 4 + 0 + 0) = √42 = **6.481**
- ||d2|| = √(3² + 0² + 2² + 0² + 1² + 1² + 0² + 1² + 0² + 1²) = √(9 + 0 + 4 + 0 + 1 + 1 + 0 + 1 + 0 + 1) = √17 = **4.12**
- cos(d1, d2) = 25 / (6.481 × 4.12) = 25 / 26.70 = **0.94**

---

## 5. Summary

- **Data attribute types:** nominal, binary, ordinal, interval-scaled, ratio-scaled
- **Many types of data sets**, e.g., numerical, text, graph, Web, image
- **Gain insight into the data by:**
  - Basic statistical data description: central tendency, dispersion, graphical displays
  - Data visualization: map data onto graphical primitives
  - Measure data similarity
- **Above steps are the beginning of data preprocessing**
- Many methods have been developed but still an active area of research

---

## References (From the Document)

- W. Cleveland, Visualizing Data, Hobart Press, 1993
- T. Dasu and T. Johnson. Exploratory Data Mining and Data Cleaning. John Wiley, 2003
- U. Fayyad, G. Grinstein, and A. Wierse. Information Visualization in Data Mining and Knowledge Discovery, Morgan Kaufmann, 2001
- L. Kaufman and P. J. Rousseeuw. Finding Groups in Data: an Introduction to Cluster Analysis. John Wiley & Sons, 1990
- H. V. Jagadish, et al., Special Issue on Data Reduction Techniques. Bulletin of the Tech. Committee on Data Eng., 20(4), Dec. 1997
- D. A. Keim. Information visualization and visual data mining, IEEE trans. on Visualization and Computer Graphics, 8(1), 2002
- D. Pyle. Data Preparation for Data Mining. Morgan Kaufmann, 1999
- S. Santini and R. Jain," Similarity measures", IEEE Trans. on Pattern Analysis and Machine Intelligence, 21(9), 1999
- E. R. Tufte. The Visual Display of Quantitative Information, 2nd ed., Graphics Press, 2001
- C. Yu, et al., Visual data mining of multimedia data for social and behavioral studies, Information Visualization, 8(1), 2009

---

## Note on Exercises and Assignments

This PDF is a **60-slide lecture** on "Know Your Data" (DSC603). It **does not contain** a separate section of numbered exercises or assignments with blank answers. The document includes **worked examples** throughout (document term-frequency vectors, transaction data, binary attribute dissimilarity calculations, data matrix and dissimilarity matrix, Minkowski distance calculations, cosine similarity calculation), all of which are included and explained in this summary. If you have a separate problem set or assignment sheet, share it and answers can be provided for those.

# DSC602 / MIST — Information Visualization
## Exam Practice Question Bank — 3 Complete Sets

**Coverage:** Foundations of InfoVis (SciVis/GeoVis/InfoVis, presentation vs. exploration, pre-attentive processing) · Munzner's Nested Model (domain, abstraction, idiom, algorithm) · Data & Dataset Types (items, attributes, links, positions, grids; tables, networks, fields) · Task Abstraction (action/target framework, search vs. query) · Marks & Channels (visual encoding, expressiveness/effectiveness, accuracy/discriminability/separability/popout) · Visualization Pipeline & Mantra · Focus+Context techniques · Practical visualization coding with `pandas`, `numpy`, `seaborn`, and `matplotlib`

**Format per set:** 20 MCQs (20 marks) · Structured Questions (40 marks) · Essay Questions (40 marks) — **Total: 100 marks**

**Note on MCQs:** Distractors are deliberately close in plausibility to the correct answer — designed to require genuine conceptual discrimination rather than length-based or pattern-based guessing. Correct-answer letters are randomized across each set.

---
---

# SET 1 — Foundations, Data Types & Dataset Types, Visual Perception

---

## Section A — Multiple Choice Questions (20 Marks)

**1.** Which of the following is the most accurate distinction between *presentation* graphics and *exploratory* graphics?
A. Presentation graphics are interactive dashboards, while exploratory graphics are always printed reports
B. Presentation graphics prioritize speed over polish, while exploratory graphics are slow but exhaustively annotated
C. Presentation graphics are static, polished, and fully annotated, while exploratory graphics are numerous, fast to produce, and informative rather than precise
D. Presentation graphics are produced only after exploratory graphics are deleted, as a separate later stage with no relationship to them

**2.** A cartographer creating a choropleth map of rainfall by region, where geographic coordinates directly determine the visual layout, is working primarily within which visualization sub-field?
A. SciVis, since rainfall is a continuous physical quantity measured in 3D volumes
B. GeoVis, since the data has inherent 2D spatial coordinates and is shown in relation to a map
C. InfoVis, since rainfall regions form an abstract hierarchy
D. Feature space visualization, since rainfall values are projected from a high-dimensional space

**3.** "Attentive processing," as described in the lecture (e.g., counting occurrences of a digit in a block of text), is best characterized as:
A. Fast and parallel, but only accurate for color-based tasks
B. Automatic and unconscious, similar to color perception
C. Slow, serial, and requiring conscious cognitive effort
D. A process that only applies to quantitative, never categorical, data

**4.** Which of the following attributes is generally classified as **pre-attentive**, allowing it to be processed rapidly and in parallel, according to the lecture?
A. The exact numeric value printed inside a table cell
B. The grammatical structure of a figure's caption
C. The alphabetical rank of a word within a sorted list
D. Color (hue or intensity)

**5.** A researcher wants to encode a quantitative attribute as accurately as possible using a pre-attentive channel. According to the lecture, which TWO channels can be perceived quantitatively with the greatest accuracy?
A. Texture density and shadow direction
B. Line length and 2D spatial position
C. Color hue and shape category
D. Motion direction and line curvature

**6.** Why are "conjunctions" of pre-attentive attributes (e.g., combining color hue with orientation in a single display) flagged as a concern in the lecture?
A. Because conjunctions always require a third dimension to render correctly
B. Because most pre-attentive attributes cannot be combined while still remaining pre-attentive, so the combined display may force slower, serial search
C. Because conjunctions are only legal when applied to ordinal data, never quantitative data
D. Because conjunctions eliminate the possibility of using color in the same display

**7.** According to Munzner's five fundamental data types, a single row in a tidy data table corresponds to which type?
A. An Attribute, since rows describe measurable properties
B. A Grid, since rows are arranged in a regular structure
C. An Item, representing a discrete individual entity
D. A Position, since rows have a fixed index location

**8.** Which statement correctly distinguishes *ordinal* (ordered categorical) data from *quantitative* data, both being subtypes of ordered attribute data?
A. Ordinal data has an implicit total ordering but does not support meaningful arithmetic operations, while quantitative data can be measured/counted and supports arithmetic
B. Ordinal data supports arithmetic operations such as averaging, while quantitative data only supports ranking
C. Ordinal data must always be numeric (e.g., 1st, 2nd, 3rd), while quantitative data must always be textual
D. Both ordinal and quantitative data support identical arithmetic operations; the only difference is display format

**9.** A dataset recording "Temperature in Celsius" is best classified as which type of quantitative data, and why?
A. Ratio data, because 0°C represents a complete absence of any thermal energy in the system being measured
B. Ordinal data, because temperature readings can only be ranked from coolest to warmest, never subtracted meaningfully
C. Interval data, because the spacing between values is meaningful but 0°C is not a true absence of the underlying quantity, so 20°C is not "twice as hot" as 10°C
D. Categorical (nominal) data, because each temperature reading is treated as a distinct unordered label

**10.** Which of the following is the clearest example of **ratio** data, as opposed to interval data?
A. Calendar year (e.g., 2024, 2025), since later years are always "more" than earlier years
B. IQ score, since a score of 140 reflects meaningfully higher intelligence than a score of 70
C. Weight in kilograms, where 0 kg represents a true absence of weight and 20 kg is exactly twice as heavy as 10 kg
D. Temperature in Fahrenheit, since negative values are possible

**11.** An attribute representing "altitude relative to sea level" (positive above sea level, negative below, radiating in two directions from a meaningful zero) is an example of which ordering direction?
A. Sequential, since altitude always increases from a fixed minimum
B. Cyclic, since altitude measurements repeat after a fixed interval
C. Nominal, since altitude has no inherent order
D. Diverging, since values progress in two directions of increasing extremity from a neutral center

**12.** "Day of the week" is best classified under which ordering direction, since Sunday follows Saturday and the sequence repeats indefinitely?
A. Cyclic, since the values wrap around to a starting point after a fixed period
B. Sequential, since each day is strictly "more" than the previous one with no wraparound
C. Diverging, since weekdays and weekends radiate from a neutral midpoint
D. Interval, since the gap between consecutive days is not constant

**13.** In Munzner's data type taxonomy, which type specifically represents connections between items, such as friendships in a social network or routes between cities?
A. Attributes, since a connection is a measurable property of the network
B. Grids, since connections form a regular lattice structure
C. Links, which connect two items to each other
D. Positions, since each connection has a fixed coordinate

**14.** A weather dataset stores one temperature reading per cell of a regular square grid covering a country. This is an example of which combination of data type and field type?
A. A Network data type containing vector field data, since each cell connects to its neighbors
B. A Grid data type containing scalar field data, since each cell holds a single quantitative attribute
C. A Link data type containing ratio field data, since temperature has a true zero
D. A Table data type containing categorical field data, since grid cells are discrete

**15.** Which of the following dataset types is specifically defined as a network that contains **no cycles** and represents hierarchy?
A. A cluster, since clusters group similar items without cycles
B. A feature space, since feature vectors have no cyclical structure
C. A grid, since grids are structured but acyclic by definition
D. A tree, which is a specific type of network without cycles, showing hierarchy

**16.** A collection of text documents represented as term-frequency vectors, then projected down to two display dimensions for visualization, is an example of which type of information space?
A. Query space, since the projection is driven by search terms entered by the user
B. Spatial data, since the projected points have x and y coordinates
C. Feature space, since each document is represented as a feature vector before projection
D. Multidimensional metadata, since document length and author are tracked

**17.** According to the "Tidy Data" principles referenced in the lecture, which statement correctly describes a properly structured table?
A. Rows represent variables, and columns represent individual observations
B. Each variable must have its own column, each observation (item) must have its own row, and each value must have its own cell
C. A single column may contain several different variables, provided they are conceptually related
D. Tables that include composite keys (multidimensional/hypercube data) violate tidy data principles and must be flattened first

**18.** What is the key distinction between *static* and *dynamic* datasets, as described in the lecture?
A. Static data is entirely available at once, while dynamic data arrives incrementally over time, such as in a stream
B. Static datasets are restricted to numeric data, while dynamic datasets are restricted to text
C. Dynamic datasets cannot be visualized using traditional charts and require specialized 3D hardware
D. Static and dynamic are simply two different names for the same underlying concept in the lecture

**19.** A dataset of file metadata (file type, size, author, modification date), where each file becomes a point in n-dimensional space, is best described in the data types/dataset types framework as:
A. Spatial data, because file systems are inherently organized as folders in 2D/3D space
B. A query space, because metadata values are derived from prior user searches
C. Cyclic ordinal data, because file modification dates repeat annually
D. Multidimensional data, since each item's n attributes place it as a point in an n-dimensional space

**20.** Why can a data file's records have, at the dataset-type level, "clusters, sets, or lists" as a valid classification distinct from a table?
A. Because clusters/sets/lists are collections of items without the rigid row/column structure that a table requires
B. Because clusters/sets/lists can only contain numeric quantitative attributes, unlike tables
C. Because a table cannot contain more than one column, while clusters/sets/lists can
D. Because clusters/sets/lists are exclusively used for dynamic (streaming) data, never static data

---

### Set 1 — Section A Answer Key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | C | 6 | B | 11 | D | 16 | C |
| 2 | B | 7 | C | 12 | A | 17 | B |
| 3 | C | 8 | A | 13 | C | 18 | A |
| 4 | D | 9 | C | 14 | B | 19 | D |
| 5 | B | 10 | C | 15 | D | 20 | A |


---

## Section B — Structured Questions (40 Marks)

*Answer ALL questions in this section.*

---

### Question 1 (10 marks)

A hospital wants to visualize patient records containing the following attributes: `Patient_ID`, `Admission_Date`, `Department` (e.g., Cardiology, Neurology), `Pain_Level` (scale: None, Mild, Moderate, Severe), `Body_Temperature_Celsius`, and `Time_of_Day_Admitted`.

**(a)** For EACH of the five non-ID attributes listed, classify it as Categorical (nominal), Ordinal, Interval, or Ratio, and justify your classification in one sentence each. **(5 marks)**

**(b)** For the `Time_of_Day_Admitted` attribute specifically, identify its **ordering direction** (sequential, diverging, or cyclic) and explain why this classification matters for choosing an appropriate visual encoding (e.g., why a simple straight axis might mislead viewers). **(5 marks)**

#### Model Answer — Question 1

**(a)**
- `Admission_Date`: **Interval** — dates have meaningful, equally-spaced differences (you can compute "3 days apart"), but there is no true zero/absence of date in a way that supports meaningful ratios (Jan 2 is not "twice" Jan 1).
- `Department`: **Categorical (nominal)** — department names (Cardiology, Neurology) have no intrinsic ordering or arithmetic meaning; they are simply distinct labels.
- `Pain_Level`: **Ordinal** — the scale (None < Mild < Moderate < Severe) has a clear implicit ordering, but the "distance" between None→Mild and Moderate→Severe is not necessarily numerically equal, so arithmetic (e.g., averaging) is not strictly meaningful.
- `Body_Temperature_Celsius`: **Interval** — equally spaced and measurable, but 0°C does not represent the total absence of thermal energy, so ratios (e.g., "twice as hot") are not meaningful.
- `Time_of_Day_Admitted`: **Ratio** (as a raw numeric quantity, e.g., minutes since midnight, 0 meaningfully represents midnight) — though see part (b) for its more important classification by ordering *direction*.

**(b)** `Time_of_Day_Admitted` is **cyclic**: its values wrap around to a starting point after a fixed period (24:00 wraps back to 00:00). This matters because a simple straight (linear) axis would visually separate admissions just before midnight (e.g., 23:55) from admissions just after midnight (e.g., 00:05) by the *entire width of the axis*, even though in reality these two admission times are only 10 minutes apart. A cyclic encoding (e.g., a circular/radial axis, or a color wheel) correctly preserves the "closeness" of times near the wraparound point, preventing a misleading visual gap that doesn't reflect the true temporal proximity.

---

### Question 2 (10 marks)

Apply **Munzner's Nested Model** (domain situation → data/task abstraction → idiom → algorithm) to the following scenario: *A university wants a tool for academic advisors to quickly see which students are at risk of failing a course, based on attendance, assignment scores, and quiz scores over the semester.*

**(a)** Describe what would need to be established at the **domain situation** level for this project. **(2 marks)**

**(b)** Describe the **data abstraction** and the **task abstraction** for this scenario, using the {action, target} framework introduced in the lecture (e.g., is the task to "discover," "locate," "compare," "summarize," etc.?). **(4 marks)**

**(c)** Propose ONE specific **idiom** (visual encoding + interaction technique) appropriate for this task, and briefly justify your choice. **(2 marks)**

**(d)** Explain why a mismatch between levels — e.g., validating only the **algorithm**'s computational speed — would NOT be sufficient evidence that the tool actually helps advisors do their job. **(2 marks)**

#### Model Answer — Question 2

**(a) Domain situation:** Identify the target users (academic advisors, not students or faculty admins), their specific domain (undergraduate course performance tracking), the questions they need answered ("which of my advisees are at risk right now?"), and the data they currently have access to (attendance logs, gradebook exports) — this must be specific enough to ground the rest of the design, since "helping with education" alone is too vague to act on.

**(b) Data abstraction:** Each student becomes an *Item* with *Attributes* — attendance rate (ratio/quantitative), assignment scores (ratio/quantitative), quiz scores (ratio/quantitative) — essentially a multidimensional table where each student is a point in attribute-space. **Task abstraction:** the high-level action is primarily to **discover** (find which students are at risk, an exploratory "consume" action) combined with elements of **query: summarize** (get an overview of overall class risk distribution) and **search: locate** (find a *specific* student an advisor is concerned about). The target is the set of "at-risk" students, defined by some combination/threshold of the three attributes.

**(c) Idiom:** A **scatterplot or small-multiples dashboard** encoding assignment score and quiz score on the two spatial position axes (the most accurate channels), attendance rate via color saturation/hue (e.g., red = low attendance), combined with a **search/filter interaction** (e.g., type a student's name to highlight their point) and a **details-on-demand tooltip** showing the exact numbers on hover — directly implementing the Information Visualization Mantra ("overview first, zoom and filter, then details on demand").

**(d)** Validating only the algorithm level (e.g., confirming the underlying risk-score computation runs in under 100ms) tells us nothing about whether advisors can actually **see and correctly interpret** which students are at risk, or whether the **chosen idiom and interaction design** genuinely supports their real workflow (e.g., they might still find the color encoding confusing, or the task abstraction might have missed that advisors actually need to compare a student against their *own historical trend*, not just a fixed threshold). Each level of the Nested Model requires validation methods from a *different field* (e.g., ethnography for domain, cognitive psychology for idiom, computer science benchmarking for algorithm) — a fast algorithm is necessary but never sufficient on its own.

---

### Question 3 (10 marks)

Distinguish between **marks** and **channels** as defined by Munzner, and answer the following:

**(a)** Define "mark" and "channel," and give one geometric-primitive example for each of the three mark dimensionalities (0D, 1D, 2D). **(4 marks)**

**(b)** Explain the "marks as constraints" principle: why can a designer encode size or shape on a **point** mark much more freely than on a **line** mark or an **area** (interlocking region) mark? **(4 marks)**

**(c)** A designer uses BOTH color hue AND size to encode the same single attribute (e.g., sales revenue) on the same set of point marks. What is this technique called, and what is the key trade-off involved? **(2 marks)**

#### Model Answer — Question 3

**(a)** A **mark** is a basic geometric primitive used to represent items or links in a visualization (e.g., points, lines, areas). A **channel** controls the appearance of a mark based on a data attribute (e.g., color, size, position). Examples: 0D mark = a **point**; 1D mark = a **line**; 2D mark = an **area/region** (e.g., interlocking colored regions in a treemap).

**(b)** Mark type constrains how many additional attributes can be encoded through size/shape because each mark dimensionality already "uses up" some of its own geometric degrees of freedom just to exist as that mark type. A **point** has zero inherent size constraints, so its size and shape are both completely free to encode additional attributes. A **line** already has one dimension fixed (its length, which is likely already encoding something), but its *width* remains free, so only one additional size-channel is available. An **area/interlocking region** has both length AND width already constrained by its boundary/shape (e.g., a treemap rectangle's size IS the data), so there is no room left to additionally size- or shape-code another attribute on that same mark — its size is already "spoken for."

**(c)** This is called **redundant encoding** — using multiple channels to represent the *same* underlying attribute. The trade-off: redundant encoding sends a stronger, more robust perceptual signal (since two channels reinforce the same message, making it easier and faster to perceive), **but** it "uses up" two channels for information that could have been conveyed with just one — meaning fewer channels remain available to encode *other*, different attributes in the same display.

---

### Question 4 (10 marks) — Practical / Coding

A dataset `sales.csv` contains columns: `Region` (categorical: North, South, East, West), `Month` (1–12), `Revenue` (continuous, in USD), and `Units_Sold` (integer count).

**(a)** Write Python code using `pandas` to load `sales.csv`, then compute the **average Revenue per Region**, sorted from highest to lowest average revenue. **(4 marks)**

**(b)** Write Python code using `seaborn` and `matplotlib` to create a visualization that lets a viewer compare the **monthly revenue trend for each Region** on the same chart, with a clear title, axis labels, and legend. Justify your choice of chart type in one sentence, referencing the channels you are using (position, color, etc.). **(6 marks)**

#### Model Answer — Question 4

**(a)**
```python
import pandas as pd

df = pd.read_csv("sales.csv")

avg_revenue_by_region = (
    df.groupby("Region")["Revenue"]
      .mean()
      .sort_values(ascending=False)
)

print(avg_revenue_by_region)
```
*Explanation:* `groupby("Region")` partitions the data by the categorical attribute; `["Revenue"].mean()` computes the average for each partition; `.sort_values(ascending=False)` orders regions from highest to lowest average revenue for easy comparison.

**(b)**
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

plt.figure(figsize=(10, 6))
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Region",      # color channel encodes the categorical Region attribute
    marker="o"
)

plt.title("Monthly Revenue Trend by Region")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.legend(title="Region")
plt.tight_layout()
plt.show()
```
*Justification:* A **line chart** is the appropriate idiom here because `Month` is ordered (sequential) data and `Revenue` is quantitative — line marks connecting points in **2D spatial position** (the most accurate pre-attentive channel for quantitative values, per the lecture) make trends and rate-of-change easy to perceive. **Color hue** is used as a secondary channel to separate the four Region categories, since hue is well-suited for encoding discrete categorical groups (as opposed to ordered magnitude) without competing with the position channel already carrying the quantitative revenue values.

---

## Section C — Essay Questions (40 Marks)

*Answer TWO of the THREE questions in this section. Each question carries 20 marks.*

---

### Essay Question 1 (20 marks)

"Visualization should make use of graphics intensively... The information behind the data should also be revealed in a good display; the graphic should aid readers or viewers in seeing the structure in the data." Critically discuss **why visualization is valuable**, drawing on at least THREE distinct justifications presented in the introductory lecture (e.g., trend/pattern perception, pre-attentive vs. attentive processing, the risk of deceptive visualizations, comparison ease). Your essay must include at least one fully worked example for each justification you discuss, and must also discuss the *limitations* or *risks* of visualization (i.e., when it can mislead).

#### Model Answer — Essay Question 1

**Introduction:** Visualization is valuable because it leverages the human visual system's enormous bandwidth and its capacity for rapid, often unconscious, pattern detection — capabilities that are simply unavailable when information is presented as raw numbers or text. The lecture grounds this value in several distinct, well-evidenced justifications, each of which is examined below, alongside an honest accounting of visualization's risks.

**Justification 1 — Trend and pattern perception:** The lecture's worked example contrasts a table of raw numeric values against the same data rendered as a line chart. While both representations contain identical information, the line chart makes upward/downward trends, inflection points, and comparative differences between series immediately apparent, whereas the table requires the viewer to mentally compute differences between many individual cells — a slow, error-prone, attentive process. For example, spotting that "Product A's sales declined steadily over Q2 while Product B spiked in June" might take a viewer 15–20 seconds of cross-referencing in a table, but is visible in under a second on a line chart, because line position and slope are highly accurate pre-attentive channels for quantitative trends.

**Justification 2 — Pre-attentive vs. attentive processing:** The lecture's "count the number of 3s in this text" exercise demonstrates that text and numbers must be processed *attentively* — serially, with conscious effort, and therefore slowly. In contrast, certain visual attributes (color being the canonical example) can be processed *pre-attentively* — in parallel, without conscious effort, and therefore almost instantaneously. If the digits needing to be counted were instead highlighted in a distinct color against a background of differently-colored digits, the count could be performed via rapid visual "pop-out" rather than careful reading — directly illustrating why encoding the *right* attribute into a pre-attentive channel can collapse a slow cognitive task into a near-instant perceptual one.

**Justification 3 — Ease of comparison:** The lecture notes that visual representations make comparisons easier than tabular ones, while conceding that tables are better for reading off *exact* values. For example, comparing smartphone market share across five manufacturers is far easier via a bar chart (where bar heights/lengths are directly, accurately compared using the position/length channel) than via a table of percentages, where the viewer must subtract pairs of numbers mentally to judge "how much bigger" one share is than another. This exemplifies a deliberate trade-off: visualization sacrifices some precision (you can't read off "47.3%" exactly from a bar) in exchange for dramatically faster, more intuitive comparative judgment — which is precisely why interactive visualizations often add mouseover tooltips, recovering the lost precision on demand without sacrificing the visual comparison benefit.

**The risk — deceptive or misleading visualization:** The lecture explicitly warns that visualizations "can be (deliberately) deceptive or misleading," using the example of four datasets with identical summary statistics (mean, variance, correlation) that, when plotted, reveal radically different underlying structures (a clear allusion to Anscombe's Quartet-style demonstrations). This illustrates a crucial double-edged property of visualization: the same perceptual strengths that make trends "pop" can equally make a *misleading* trend pop, whether through poor design choices (e.g., a truncated y-axis exaggerating a small difference) or through genuinely different underlying data being concealed behind identical-looking summary statistics. A pie chart vs. bar chart comparison for the same smartphone market-share data also illustrates a softer version of this risk: pie charts rely on angle/area judgments, which the lecture's later "Marks & Channels" material identifies as *less accurate* perceptual channels than the position/length judgments used in a bar chart — meaning the *choice* of chart type itself can systematically bias how accurately viewers extract the underlying values, even with no "malicious" intent.

**Conclusion:** Visualization's value rests on exploiting fast, pre-attentive, parallel visual processing to reveal trends and enable comparisons that would otherwise require slow, attentive, serial cognitive effort. But this same power means visualization design carries real responsibility: a poorly or carelessly designed graphic can mislead just as effectively, and often more persuasively, than a misleading table of numbers — making principled, perception-aware design (the central concern of the rest of the course) not just an aesthetic nicety but a precondition for visualization to deliver on its core promise of truthful communication.

---

### Essay Question 2 (20 marks)

Critically compare and contrast the **five fundamental data types** (Items, Attributes, Links, Positions, Grids) and the **dataset types** (Tables, Networks & Trees, Fields, Geometry, Clusters/Sets/Lists) presented in Lecture 2. Your essay must:

**(a)** Explain the relationship between data types and dataset types — i.e., how do the five fundamental data types combine to form each of the major dataset types? **(10 marks)**

**(b)** Using an example of your own choosing (not used in the lecture), construct a complete worked example that shows: the raw scenario, which data type(s) are present, which dataset type it forms, and one appropriate visualization idiom for it. **(10 marks)**

#### Model Answer — Essay Question 2

**(a) Relationship between data types and dataset types:**

The five fundamental data types (Items, Attributes, Links, Positions, Grids) act as **atomic building blocks**, while dataset types describe how these building blocks are **structurally combined** in a given real-world dataset.

- A **Table** is fundamentally a collection of **Items** (rows) each described by a set of **Attributes** (columns) — the canonical "tidy data" structure where every variable has its own column, every observation has its own row, and every value has its own cell. Multidimensional tables (data hypercubes/tensors) extend this with composite keys but remain at heart an Items × Attributes structure.
- A **Network** (and the special acyclic case, a **Tree**) is formed when **Items** (now called nodes) are explicitly connected via **Links** — the defining structural feature absent from a plain table. A tree is simply a network with the added constraint of no cycles, producing strict hierarchy.
- A **Field** is formed when data is defined over continuous space using **Positions** and/or **Grids** — each grid cell or position holds one or more attribute values (scalar fields hold one quantitative attribute per cell/position, e.g., temperature; vector/tensor fields hold multiple). This is the structure underlying SciVis-style continuous spatial phenomena like fluid flow or temperature maps.
- **Geometry** datasets describe the shape of objects using **Positions** directly (without necessarily needing the regular structure of a Grid), focusing on spatial coordinates that define an object's form (e.g., a CAD model's vertices).
- **Clusters, Sets, and Lists** are collections of **Items** that deliberately lack the rigid row/column structure of a table — useful when items are grouped or ordered, but not every item shares the same set of measured Attributes.

In short: dataset types answer "what is the overall shape/structure of this dataset?", while data types answer "what are the elementary pieces this structure is built from?" — every dataset type can be decomposed back into some combination of Items, Attributes, Links, Positions, and/or Grids.

**(b) Worked example — a public transit system:**

*Scenario:* A city transit authority records every bus stop in the city, including the stop's GPS coordinates, the bus routes that connect it to other stops, and hourly passenger boarding counts at each stop.

*Data types present:*
- Each bus stop is an **Item**.
- GPS coordinates are **Positions** (latitude/longitude pairs — 2D spatial location).
- Each route segment connecting two stops is a **Link**.
- "Hourly passenger boarding count" is a quantitative **Attribute** attached to each stop-hour combination.

*Dataset type:* This is fundamentally a **Network** (bus stops as nodes, routes as links) with an additional **Table**-like attribute layer (boarding counts per stop, possibly per hour, forming a multidimensional/composite-key extension) — and because each stop's Position is meaningful and grounded in real-world geography, this network is also a form of **Geometry/Spatial** data, since the natural visual representation is constrained by the actual map layout rather than an arbitrary force-directed layout.

*Appropriate idiom:* A **node-link diagram overlaid on a geographic map** (combining Network and GeoVis-style Spatial representation), where: node **position** is fixed to real GPS coordinates (the most accurate channel, and also semantically required here since spatial position is intrinsic to the data, not freely assignable); node **size** or **color saturation** encodes the quantitative boarding-count attribute (since size/color are well-suited secondary channels once position is "spent" on geography); and **links** are drawn as route lines between connected stops, potentially using **edge bundling** (from Lecture 1's InfoVis concepts) if many overlapping routes create visual clutter along shared corridors. This combination directly illustrates how a single real dataset can simultaneously instantiate multiple data types (Items, Positions, Links, Attributes) and multiple "pure" dataset types (Network + Field/Spatial + Table), requiring the designer to choose an idiom that honors all the structurally important relationships at once rather than picking just one.

---

### Essay Question 3 (20 marks)

The lecture states: "What we see depends not only on what is there, but also on what we expect to see and where our attention is directed... we see with our mind." Critically discuss the role of **human visual perception** in information visualization design. Your essay must cover:

**(a)** The mechanics of human visual sampling (fixation and saccade) and what this implies about how viewers actually scan a visualization. **(5 marks)**

**(b)** Selective attention and its design implications — why can two viewers looking at the identical chart "see" different things? **(5 marks)**

**(c)** The distinction between channels that are **separable** versus **integral**, with a worked example of each. **(5 marks)**

**(d)** The concept of **popout**, including what determines whether a target "pops out" from distractors, and one practical design rule this implies. **(5 marks)**

#### Model Answer — Essay Question 3

**(a) Fixation and saccade:** The human eye does not scan a scene smoothly and continuously; instead, it samples the environment in discrete bursts, 3–4 times per second, alternating between **fixations** (brief stationary periods during which visual information is actually sampled and processed) and **saccades** (rapid, ballistic eye movements that reposition the eye to a new location, during which almost no useful visual information is gathered). The design implication is significant: a visualization is never perceived as one continuous "snapshot." Instead, viewers build up an understanding of the display through a sequence of discrete fixations — meaning the designer should ensure that the most important information is positioned where fixations are likely to land (e.g., visual focal points, areas with the strongest pre-attentive cues) rather than assuming the viewer will uniformly "take in" the whole display at once. This also explains why poorly organized displays with no clear visual hierarchy can cause viewers to miss important information entirely — if no fixation happens to land near it, it is effectively invisible to that viewing session.

**(b) Selective attention:** The lecture's claim that "we perceive only what the mind attends to" means that perception is not a passive recording of all available visual information, but an active, top-down filtering process — what a person sees depends heavily on their existing expectations and where their attention is currently directed. Two viewers looking at the identical chart can therefore "see" different things: a viewer specifically looking for an anomaly in a stock price chart may immediately notice a small dip that a second viewer, focused on overall upward trend, completely fails to register, even though both viewers' eyes physically received the same visual input. The design implication is that visualizations intended to communicate a *specific* finding should use strong, deliberate visual cues (e.g., annotation, color highlighting, or guaranteed-visibility techniques) to actively direct attention toward the intended insight, rather than relying on the data alone to be "self-evident" — because what is obvious to the designer (who already knows what to look for) may be functionally invisible to a viewer whose attention has not been correctly guided.

**(c) Separable vs. integral channels:** Channels are **separable** when a viewer's ability to perceive and judge one channel is *not* affected by the simultaneous presence of another channel — for example, the lecture's demonstration of two distinct groups encoded via spatial position and shape: a viewer can independently and accurately judge "how many groups by position" and "how many groups by shape" without one judgment interfering with the other. Channels are **integral** when two (or more) channels perceptually *fuse* into a single combined percept that cannot be easily decomposed back into its parts — the lecture's example of color and area combining such that the viewer perceives a single emergent property (e.g., "how saturated and large") rather than two cleanly separable judgments. A practical example of integral perception: combining the height and width of a rectangle, where viewers tend to perceive the rectangle's overall *area* (an emergent, fused percept) rather than independently judging height and width as two unrelated channels. The design implication is that combining channels intended to be read independently (e.g., wanting viewers to separately judge two unrelated attributes) should favor genuinely separable channel pairs, while channels intentionally meant to be perceived as a single combined impression (e.g., wanting an overall sense of "magnitude") can deliberately exploit integral channel pairs.

**(d) Popout:** A target "pops out" from a field of distractors when it can be detected through fast, parallel processing across many individual pre-attentive channels simultaneously — critically, the *speed* of finding a popout target is **independent of the number of distractors** present (e.g., "find the red dot" takes roughly the same time whether there are 10 or 200 other dots, because color difference triggers a pre-attentive, parallel signal). This is presented in direct contrast to **serial search**, where speed *does* depend on the number of distractors, because the viewer must check items one-by-one — this occurs for combinations/conjunctions of channels that the visual system cannot process pre-attentively as a unified signal (the lecture notes that not all channel combinations pop out — e.g., parallel line pairs do not pop out from tilted pairs, even though tilt alone would). The practical design rule this implies: if a design goal is to make a specific category of items instantly findable regardless of how many other items are on screen, the design must rely on a **single, strongly pre-attentive channel** (such as a unique hue) to mark that category, rather than a combination/conjunction of channels — since conjunctions typically degrade back into slow, distractor-count-dependent serial search.

---
---

# SET 2 — Nested Model, Task Abstraction, Visualization Pipeline & Interaction Concepts

---

## Section A — Multiple Choice Questions (20 Marks)

**1.** Munzner's Nested Model identifies four levels of visualization design. Which of the following correctly lists all four, from highest (most domain-specific) to lowest (most general/computational)?
A. Domain Situation, Abstraction, Idiom, Algorithm
B. Idiom, Algorithm, Domain Situation, Abstraction
C. Abstraction, Domain Situation, Algorithm, Idiom
D. Algorithm, Idiom, Abstraction, Domain Situation

**2.** At the **abstraction** level of the Nested Model, the question "what is shown?" corresponds to which sub-component?
A. Task abstraction
B. Domain characterization
C. Data abstraction
D. Visual encoding idiom

**3.** At the **idiom** level, which TWO sub-categories does the lecture distinguish?
A. Domain idiom and algorithm idiom
B. Visual encoding idiom (how to draw) and interaction idiom (how to manipulate)
C. Static idiom and dynamic idiom
D. Search idiom and query idiom

**4.** The Nested Model describes "downstream" effects as:
A. Choices made at a lower level (e.g., algorithm) constraining what is possible at a higher level (e.g., domain)
B. Cascading effects where a choice at a higher level (e.g., data/task abstraction) constrains and shapes the choices available at the levels below it (idiom, algorithm)
C. A process exclusive to GeoVis applications
D. The process of exporting a finished chart to a downstream file format

**5.** Why does the Nested Model state that validation is inherently difficult, requiring "different ways to get it wrong at each level"?
A. Because only one level (idiom) can ever be validated in practice
B. Because the model assumes all visualizations are equally effective regardless of design
C. Because validation is only relevant for 3D visualizations
D. Because each level requires fundamentally different validation methods drawn from different academic fields (e.g., ethnography for domain, cognitive psychology for idiom, computer science for algorithm), and a flaw at one level is not detectable using another level's methods

**6.** Which of the following is explicitly identified in the lecture as a **mismatch** to avoid when validating a visualization system?
A. Using a field study to validate the domain situation
B. Using computational benchmarks to "confirm" that an idiom's visual design is effective for users
C. Using a lab study to measure task completion time
D. Interviewing target users to characterize the domain

**7.** In the {action, target} framework for task abstraction, which of the following is classified as a high-level **action**, rather than a target?
A. Outliers
B. Topology
C. Compare
D. Trends

**8.** Within the "Search" action category, a task where the user knows BOTH the identity of what they are looking for AND its precise location (e.g., looking up a specific word in a dictionary using alphabetical order) is classified as:
A. Browse
B. Explore
C. Locate
D. Lookup

**9.** A user who knows roughly what kind of item they want, but not its exact identity or location (e.g., browsing books in a bookstore by wandering the shelves), is performing which search sub-action?
A. Explore
B. Browse
C. Lookup
D. Locate

**10.** Within the "Query" action category, which sub-action corresponds to a user wanting an overview of "how much of the data matters," addressing ALL of the data at once (e.g., "what's the overall distribution")?
A. Identify
B. Compare
C. Locate
D. Summarize

**11.** Which statement about the relationship between data abstraction and task abstraction is correct, according to the lecture's discussion of "interplay"?
A. Task abstraction must always be finalized before any data abstraction work begins, and the two are never revisited together
B. Data abstraction and task abstraction are entirely independent and never inform one another
C. Task abstraction can lead the designer to transform the data, and data abstraction is needed within task abstraction to specify targets — so designers typically iterate back and forth between the two
D. Only data abstraction matters for designing idioms; task abstraction is purely a documentation exercise with no design impact

**12.** According to the Visualization Pipeline, which stage involves preparing data through actions such as applying a smoothing filter, interpolating missing values, or correcting erroneous measurements — typically with little or no user interaction?
A. Rendering
B. Mapping
C. Filtering
D. Data Analysis

**13.** Which stage of the Visualization Pipeline is described as the "most critical step for achieving Expressiveness and Effectiveness," where focus data are mapped to geometric primitives and their visual attributes?
A. Filtering
B. Data Analysis
C. Mapping
D. Rendering

**14.** The Visualization Pipeline's "Filtering" stage is characterized as:
A. User-centered selection of which portions of the (already-analyzed) data should be visualized
B. The transformation of geometric data into final image/pixel data
C. Computer-centered, with no user involvement whatsoever
D. The step where smoothing filters and interpolation are applied to raw sensor data

**15.** The Information Visualization Mantra is best summarized as:
A. Details on demand first, then zoom and filter, then overview
B. Filter first, then overview, then zoom on demand
C. Overview first, zoom and filter, then details on demand
D. Zoom first, then overview, then filter on demand

**16.** "Object constancy," discussed under Visualization + Interaction, refers to:
A. Ensuring that all marks in a visualization use exactly the same shape regardless of category
B. Smoothly animating transitions over about one second, which eliminates the need for the viewer to mentally reassimilate the scene from scratch
C. The requirement that axis scales never change between two different views
D. A constraint that prevents any two objects from occupying the same pixel

**17.** "Focus-plus-Context" visualizations are built on three premises. Which of the following correctly states ONE of them?
A. The user only ever needs overview information, never focus/detail information
B. The overview and the detail view must always be rendered in two completely separate, unsynchronized windows with no shared logic
C. Detail information should replace context information entirely once the user clicks on an item
D. The two types of information (overview and detail) can be combined within a single, dynamic display, much as occurs in human vision

**18.** A geometric distortion technique where the area of interest is enlarged at the center while the surrounding context is progressively shrunk is known as:
A. Fisheye View
B. Focus-and-Blur
C. Overview-plus-Detail
D. Edge Bundling

**19.** "Edge Bundling" is best described as a technique that:
A. Removes edges from a network diagram entirely to reduce visual complexity
B. Ties together edges with similar paths so they visually merge into bundled curves, reducing clutter (analogous to cable-tying parallel network cables)
C. Converts all edges into straight lines regardless of their underlying path
D. Is only applicable to tree structures, never general networks

**20.** "Excentric labels" are used specifically to address which problem?
A. The problem of too few categories needing distinct color hues
B. The problem of needing 3D perspective in a 2D display
C. The problem of cyclic data needing a non-linear axis
D. The problem of insufficient space inside a dense visualization to label individual elements without cluttering the display

---

### Set 2 — Section A Answer Key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | A | 6 | B | 11 | C | 16 | B |
| 2 | C | 7 | C | 12 | D | 17 | D |
| 3 | B | 8 | D | 13 | C | 18 | A |
| 4 | B | 9 | A | 14 | A | 19 | B |
| 5 | D | 10 | D | 15 | C | 20 | D |


---

## Section B — Structured Questions (40 Marks)

*Answer ALL questions in this section.*

---

### Question 1 (10 marks)

A city government wants to build a dashboard so that urban planners can identify which neighborhoods have the highest rates of reported potholes, using a dataset of pothole reports with location, date reported, and repair status.

**(a)** Walk through the FOUR stages of the **Visualization Pipeline** (Data Analysis, Filtering, Mapping, Rendering) as they would apply to this scenario, giving one concrete action for each stage. **(8 marks)**

**(b)** Explain which ONE of the four stages is described in the lecture as most critical for achieving **Expressiveness and Effectiveness**, and briefly explain why, in the context of this pothole dashboard. **(2 marks)**

#### Model Answer — Question 1

**(a)**
- **Data Analysis:** Clean the raw pothole report data — e.g., correct erroneous GPS coordinates that fall outside city boundaries, interpolate missing "date repaired" values where status is "in progress," and remove duplicate reports of the same pothole filed by multiple residents. This is computer-centered, with little user interaction.
- **Filtering:** Allow the planner to select only reports from the last 12 months, and only "unrepaired" status reports, narrowing the full historical dataset down to the currently-relevant subset. This is user-centered.
- **Mapping:** Map each filtered pothole report to a point mark on a city map, using spatial position (latitude/longitude) for location, and color intensity to encode how long the pothole has remained unrepaired (e.g., redder = older/more overdue).
- **Rendering:** Convert this geometric description (points, colors, map basemap) into the actual final image/pixels that appear on the planner's screen.

**(b)** **Mapping** is the most critical stage, because this is where the actual design decisions about which visual channels represent which attributes are made — in this case, choosing color intensity (rather than, say, size) to represent "overdue time" directly determines whether planners can accurately and quickly perceive which neighborhoods need urgent attention (Effectiveness) and whether the encoding correctly represents the *type* of the underlying data, e.g., using an ordered color scale for the ordered "days overdue" attribute rather than a categorical, unordered palette (Expressiveness).

---

### Question 2 (10 marks)

Using the {action, target} task abstraction framework:

**(a)** A network security analyst wants to "find all servers in the network whose CPU usage is significantly higher than their historical average." Decompose this into its {action, target} pair(s), explicitly naming the high-level action category (analyze/search/query) and sub-action involved. **(5 marks)**

**(b)** Explain the difference between the "lookup," "locate," "browse," and "explore" sub-actions within the Search action category, and state which one best matches a user typing a specific server's hostname into a search box to jump directly to it. **(5 marks)**

#### Model Answer — Question 2

**(a)** This task is primarily an **Analyze: discover** action (the analyst does not yet know which servers are anomalous — they are searching for a pattern) combined with a **Query: compare** sub-action (each server's *current* CPU usage is implicitly compared against its *own historical average*, a comparison across two states of the same item rather than a simple single-value lookup). The target is "servers" as the item type, with "CPU usage relative to historical average" as the specific attribute of interest — effectively, the target is the *subset* of servers meeting an outlier/deviation condition, making "locate outliers" a reasonable shorthand description of the overall task, by analogy with the {action, target} examples given in the lecture.

**(b)** 
- **Lookup:** the user knows both the target's identity AND its location (e.g., looking up a word in a dictionary using alphabetical order — you know exactly what you're looking for and exactly how to navigate to it).
- **Locate:** the user knows the target's identity but not its location (e.g., finding your keys somewhere in your house, or finding a specific node in a network diagram — you know *what* you want but must search to find *where* it is).
- **Browse:** the user knows the location/category to search within, but not the specific target's identity (e.g., browsing books in a bookstore section without knowing the exact title you want).
- **Explore:** the user knows neither the specific identity nor the location in advance (e.g., exploring to find a "cool neighborhood" in a new city — fully open-ended).

A user typing a specific server's hostname to jump directly to it best matches **Lookup**: they know exactly what they're looking for (the hostname) and the system provides a direct, known mechanism (the search box) to navigate straight to it — analogous to alphabetical dictionary lookup.

---

### Question 3 (10 marks)

**(a)** Explain Munzner's "marks as constraints" principle as it interacts with **task abstraction**: if a task requires comparing FOUR different quantitative attributes simultaneously for each item, explain why choosing a **point mark** (rather than a line or area mark) gives the designer more flexibility to satisfy this task. **(5 marks)**

**(b)** A designer is choosing between **Focus-plus-Context** techniques for a genealogy (family tree) application that may contain thousands of individuals, where the user needs to study one specific person's immediate family in detail while still understanding their place in the broader family tree. Recommend ONE specific Focus+Context technique from the lecture and justify your choice over at least one alternative technique. **(5 marks)**

#### Model Answer — Question 3

**(a)** A point mark (0D) has **zero** inherent size/shape constraints, meaning none of its geometric "slots" are pre-used just to render the mark itself — so a designer can freely assign size to one attribute, shape to a second, color to a third, and spatial position to a fourth, achieving four simultaneous quantitative comparisons on a single mark. A line mark (1D) already has one dimension (length) likely committed to encoding an attribute, leaving only width as an additional size channel — insufficient for four attributes without resorting to additional non-size channels like color. An area/interlocking-region mark (2D) has both its size dimensions (length AND width) already constrained by its own boundary, leaving no size/shape channels free at all — making it the *least* flexible choice for a four-attribute comparison task, since virtually all remaining encoding would have to rely on color or texture alone.

**(b)** **Recommendation: Overview-plus-Detail.** This technique uses two separate but synchronized windows — an overview window (showing the full family tree's context, e.g., a zoomed-out hierarchy) and a detail window (showing the focal individual's immediate family in full, readable detail). This is preferable over a **Fisheye View** for this scenario because a fisheye's geometric distortion of the surrounding context can make it difficult to read labels and trace relationship lines in the *already cluttered* surrounding region of a large genealogy tree — distortion that helps with simple proximity-based context can actively hurt legibility when the context itself (extended family structure) needs to remain readable rather than just present. Overview-plus-Detail instead keeps both views geometrically undistorted and independently readable, while synchronization (e.g., highlighting the focal individual's position in the overview as it's selected in the detail view) preserves the necessary link between "where am I in the whole tree" and "what exactly does my immediate family look like."

---

### Question 4 (10 marks) — Practical / Coding

A dataset `network_logs.csv` contains the columns: `Timestamp`, `Server_ID`, `CPU_Usage_Percent`, and `Server_Group` (categorical: Web, Database, Cache).

**(a)** Using `pandas` and `numpy`, write code to compute, for each `Server_ID`, the **z-score** of its most recent CPU usage reading relative to that server's own historical mean and standard deviation (i.e., implement the "compare against historical average" task from Question 2 numerically). Flag any server whose latest z-score exceeds 2 (in absolute value) as an outlier. **(6 marks)**

**(b)** Using `seaborn`, write code to create a single figure with **small multiples** (one subplot per `Server_Group`) showing the distribution of `CPU_Usage_Percent` as a boxplot, so a viewer can compare CPU usage spread across groups using the same axis scale. **(4 marks)**

#### Model Answer — Question 4

**(a)**
```python
import pandas as pd
import numpy as np

df = pd.read_csv("network_logs.csv", parse_dates=["Timestamp"])
df = df.sort_values(["Server_ID", "Timestamp"])

def latest_zscore(group):
    mean = group["CPU_Usage_Percent"].mean()
    std = group["CPU_Usage_Percent"].std()
    latest_value = group["CPU_Usage_Percent"].iloc[-1]
    z = (latest_value - mean) / std if std > 0 else np.nan
    return pd.Series({"latest_zscore": z})

zscores = df.groupby("Server_ID").apply(latest_zscore).reset_index()
zscores["is_outlier"] = zscores["latest_zscore"].abs() > 2

print(zscores[zscores["is_outlier"]])
```
*Explanation:* `groupby("Server_ID")` isolates each server's full history; within each group, `mean()` and `std()` (via `numpy`-backed pandas operations) establish the historical baseline, and the z-score formula `(x - mean) / std` quantifies how many standard deviations the *latest* reading (`.iloc[-1]` after sorting by Timestamp) deviates from that baseline — directly implementing "current value relative to historical average" numerically. The `abs() > 2` threshold flags statistically significant outliers (a common convention, ~95% confidence under a normal approximation).

**(b)**
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("network_logs.csv")

g = sns.catplot(
    data=df,
    x="Server_Group",
    y="CPU_Usage_Percent",
    kind="box",
    col="Server_Group",   # one subplot (small multiple) per group
    sharey=True           # same y-axis scale across all subplots for fair comparison
)

g.set_titles("{col_name}")
g.fig.suptitle("CPU Usage Distribution by Server Group", y=1.05)
plt.show()
```
*Explanation:* `sns.catplot(..., col="Server_Group")` automatically produces one boxplot subplot per category of `Server_Group` — exactly the "small multiples" idiom from the lecture (a lattice of charts sharing the same axes/scale for direct comparison). `sharey=True` is essential: per the lecture's discussion of relative judgments and common scales, putting all subplots on the *same* y-axis scale is what makes visual cross-group comparison valid and accurate, rather than each subplot silently using its own auto-scaled axis (which would be visually misleading).

---

## Section C — Essay Questions (40 Marks)

*Answer TWO of the THREE questions in this section. Each question carries 20 marks.*

---

### Essay Question 1 (20 marks)

Munzner's Nested Model proposes four levels of design and decision-making: **domain situation, abstraction (data + task), idiom (encoding + interaction), and algorithm**. Critically discuss this model and its implications for visualization validation.

**(a)** Explain each of the four levels in detail, including the "two questions" (what is shown, why is the user looking at it) embedded within the abstraction level and the "two questions" (how to draw, how to manipulate) embedded within the idiom level. **(10 marks)**

**(b)** Explain BOTH the "downstream" (cascading) and "upstream" (iterative refinement) relationships between levels, with a concrete example of each, drawn from a scenario of your own choosing. **(6 marks)**

**(c)** Explain why the lecture argues that validation methods must be drawn from *different academic fields* depending on the level being validated, and give one example pairing (level → validation method) not explicitly given in the lecture slides. **(4 marks)**

#### Model Answer — Essay Question 1

**(a) The four levels in detail:**

1. **Domain situation:** The starting point of any visualization design — establishing who the target users are, what specific domain/application area they work in, and what real questions and data they actually have. This level deliberately resists generalization, since domain details "vary wildly" from one application to another, but must be characterized specifically enough to give the designer real traction (a vague domain characterization like "help businesses" provides no actionable design guidance).

2. **Abstraction:** This level translates the specifics of the domain into the generalized vocabulary of visualization, and is itself split into two questions: **"what is shown?"** — the **data abstraction**, which maps the domain's specific data (e.g., "patient vital signs") into general data types (e.g., quantitative attributes over time) — and **"why is the user looking at it?"** — the **task abstraction**, which maps the user's domain-specific goals (e.g., "check if a patient is deteriorating") into general task vocabulary (e.g., "discover trend," "locate outlier").

3. **Idiom:** This level answers **"how is it shown?"**, again split into two sub-questions: the **visual encoding idiom** (how to draw — which marks and channels are used, e.g., a line chart vs. a heatmap) and the **interaction idiom** (how to manipulate — what actions the user can take, e.g., zooming, filtering, brushing).

4. **Algorithm:** The lowest, most computational level — concerned purely with **efficient computation**: given the chosen idiom, what specific procedure/implementation actually computes and produces that visual encoding and interaction behavior efficiently (e.g., the specific layout algorithm used to position nodes in a force-directed graph).

**(b) Downstream and upstream relationships:**

*Downstream (cascading) example:* Suppose, at the domain/task level, a hospital decides the key task is "discover trends in real-time" rather than "summarize historical totals." This single choice cascades downstream: it constrains the idiom level toward encodings that emphasize temporal change (e.g., an animated or continuously-updating line chart rather than a static summary table), which in turn constrains the algorithm level toward needing an efficient streaming/incremental rendering algorithm rather than a one-time batch rendering algorithm — a decision made at the *top* level has directly shaped what is even possible or sensible at the *bottom* level.

*Upstream (iterative refinement) example:* Suppose a designer initially commits to a force-directed node-link diagram idiom for visualizing a large organizational chart, then discovers during algorithm-level implementation that the layout algorithm cannot render 10,000+ nodes within an interactive frame rate. This algorithmic limitation flows *upstream*: the designer must revisit the idiom level (perhaps switching to a more scalable idiom like a treemap or an aggregated/clustered view), which may in turn require revisiting the task abstraction (perhaps the "explore individual relationships" task must be replaced or supplemented with a "summarize aggregate structure" task for the full dataset, with individual exploration reserved for a filtered subset) — demonstrating that a constraint discovered at the *bottom* level can force a redesign decision back up at a *higher* level.

**(c) Why validation methods differ by level, and an additional example pairing:**

Each level of the Nested Model concerns a fundamentally different *kind* of claim, and different academic fields have developed appropriate methods for validating exactly that kind of claim. A domain-situation claim ("these are the real needs of radiologists") is a claim about human behavior and context in the wild, which is the proper subject matter of ethnography/anthropology methods (observation, interviews). An idiom-level claim ("this color encoding is more accurate than that one") is a claim about human perceptual/cognitive performance, which is the proper subject matter of cognitive psychology (controlled lab studies measuring speed/accuracy). An algorithm-level claim ("this layout computes in O(n log n) time") is a purely computational claim, properly validated by computer science benchmarking. Using the *wrong* field's method at the wrong level produces a "mismatch" — e.g., the lecture's explicit warning that "computational benchmarks do not confirm idiom design": proving an algorithm is fast says nothing about whether the resulting visual encoding is perceptually effective for humans.

*Additional example pairing (not explicitly given in the slides):* For the **task abstraction** level, an appropriate validation method drawn from **HCI/requirements engineering** would be a **structured task analysis study** — directly observing or interviewing target users performing their actual current workflow (without the new tool) to verify that the abstracted {action, target} pairs the designer identified (e.g., "compare trends") genuinely correspond to what users are trying to accomplish, rather than the designer's own assumption about what they "should" want to do.

---

### Essay Question 2 (20 marks)

Critically discuss the **{action, target} framework** for task abstraction. Your essay must:

**(a)** Explain the three high-level action categories (Analyze, Search, Query) and their sub-actions in full detail. **(10 marks)**

**(b)** Explain why the lecture insists these three levels (analyze, search, query) represent "independent choices" that can be "mixed and matched," with a worked example showing TWO different combinations applied to the same underlying target (e.g., "sales data"). **(6 marks)**

**(c)** Critically evaluate one potential limitation of reducing real-world user goals down to abstract {action, target} pairs — what nuance of a real task might get lost in this abstraction process? **(4 marks)**

#### Model Answer — Essay Question 2

**(a) The three high-level action categories:**

**Analyze** splits into **consume** (the user is taking in/interpreting existing visualization output) and **produce** (the user is creating new information). *Consume* further splits into the classic **discover vs. present** distinction (also called explore vs. explain) — discovering is open-ended investigation to find unknown insights, while presenting/explaining is communicating already-known insights to an audience — plus **enjoy**, a "casual/social" newcomer category for visualization used for entertainment or casual engagement rather than analytical work. *Produce* splits into **annotate/record** (capturing notes or markings on the visualization) and **derive** (computing new data/attributes from existing data) — the lecture flags "derive" as a particularly crucial design choice, since it determines whether the visualization tool itself transforms the underlying data, not just its display.

**Search** asks "what does the user know about the target: its identity, its location, both, or neither?" producing four sub-actions: **Lookup** (knows identity AND location — e.g., a word in an alphabetically-ordered dictionary), **Locate** (knows identity but not location — e.g., finding your keys in your house, or a specific node in a network), **Browse** (knows location/category but not exact identity — e.g., browsing books in a bookstore section), and **Explore** (knows neither — e.g., looking for "a cool neighborhood" in an unfamiliar city, fully open-ended).

**Query** asks "how much of the data matters to this task?" producing three sub-actions corresponding to quantity: **Identify** (one — examine a single target's characteristics), **Compare** (some — examine the relationship between a few targets), and **Summarize** (all — get an overview characterizing the entire dataset at once).

**(b) Independence and "mix and match," with two worked combinations on "sales data":**

The lecture insists these three dimensions are independent because a user's *analytical intent* (Analyze), *what they already know* (Search), and *how much data they care about* (Query) can vary completely independently of one another for the same underlying target — there is no rule forcing, e.g., "discover" to always pair with "explore" and "summarize."

*Combination 1:* A sales manager wants to **discover** (Analyze: consume) **whether any specific underperforming region exists**, but does not know which region in advance, so they must **explore** (Search) across **all** regions to **summarize** (Query) overall regional performance and spot the laggard — this is `{discover, explore, summarize}` applied to "sales data."

*Combination 2:* The same sales manager, having identified that the West region underperforms, now wants to **present** (Analyze: consume) this specific finding to the board, already knows exactly which region and which two quarters to **lookup** (Search) directly (since the identity and location are now both known), in order to **compare** (Query) just those two specific quarters against each other — this is `{present, lookup, compare}` applied to the *same* "sales data" target, demonstrating that an entirely different combination of action sub-types can apply to the identical underlying data depending on the user's current goal and existing knowledge.

**(c) A limitation of the {action, target} abstraction:**

One real nuance that risks being lost is the **temporal/sequential relationship between successive tasks within a single user session**. The {action, target} framework, as presented, characterizes individual task instances reasonably well in isolation, but a real analyst rarely performs just one isolated task — they typically chain several together (e.g., first *summarize* the whole dataset, which triggers them to *locate* a specific outlier they just noticed, which then leads them to *compare* that outlier against two similar items). The static {action, target} vocabulary captures each individual step accurately, but doesn't inherently model *how one task's outcome triggers and shapes the next task* — meaning a designer who only catalogs a list of isolated {action, target} pairs (rather than also studying realistic task *sequences* and the transitions between them) risks building an idiom that handles each task adequately in isolation, but fails to support the natural, fluid back-and-forth movement between tasks that characterizes real exploratory analysis sessions.

---

### Essay Question 3 (20 marks)

The Information Visualization Mantra states: "Overview first, zoom and filter, then details on demand." Critically discuss this principle and its relationship to the other interaction-related concepts introduced in the lecture (Focus-plus-Context, Guaranteed Visibility, Small Multiples). Your essay must:

**(a)** Explain the Mantra in detail, including why each of its three stages is necessary and what would go wrong if a designer skipped the "overview first" stage entirely. **(7 marks)**

**(b)** Explain how Focus-plus-Context visualizations can be understood as ONE concrete strategy for implementing the Mantra's "zoom and filter" and "details on demand" stages simultaneously, within a single persistent display (rather than as entirely separate stages/views). **(7 marks)**

**(c)** Discuss how "Guaranteed Visibility" and "Small Multiples" each support (or could conflict with) the Mantra, using a specific example for each. **(6 marks)**

#### Model Answer — Essay Question 3

**(a) The Mantra in detail:**

The Mantra prescribes a specific *sequence* for how a visualization should reveal information to a user: first, an **overview** establishes the full context — the overall shape, scale, and structure of the entire dataset, giving the user a mental model of "what's out there" before committing to any specific area of interest. Next, the user can **zoom and filter**, narrowing the view down to a subset of interest, informed by patterns or anomalies they noticed in the overview (e.g., zooming into a cluster of points, or filtering out categories irrelevant to their current question). Finally, **details on demand** allows the user to retrieve exact, precise values for specific items only when and where they actually need that precision (e.g., hovering for a tooltip), rather than cluttering the display with exhaustive labels/values for every item at all times.

If a designer skipped "overview first" and jumped straight to a filtered/zoomed view, the user would lose crucial context: they would have no way of knowing whether the region they're looking at is representative of the whole dataset, whether more interesting structure exists elsewhere that they haven't yet seen, or how their current zoomed view relates proportionally to the rest of the data — directly undermining the kind of "discover" and "summarize" tasks (from the {action, target} framework) that depend on first seeing the full picture. Skipping straight to detail risks the classic problem of "not seeing the forest for the trees" — exactly the situation Focus-plus-Context is designed to prevent.

**(b) Focus-plus-Context as a unified Mantra implementation:**

Rather than treating "overview," "zoom/filter," and "details on demand" as three temporally sequential, separate views that a user must navigate between one at a time, Focus-plus-Context techniques implement the *overview-equivalent* (the "context") and the *details-equivalent* (the "focus") **simultaneously within a single dynamic display**. The lecture's three founding premises make this explicit: the user needs both overview and detail information **simultaneously**, not sequentially; the information needed at the overview level may genuinely differ from what's needed at the detail level (it's not just "the same data, smaller"); and crucially, these two types of information *can* be combined within one display, "much as in human vision" (which itself combines a low-resolution peripheral context with a high-resolution foveal focus point simultaneously). Concrete techniques like the **Fisheye View** (focus enlarged at the center, context compressed around it) or **Overview-plus-Detail** (two synchronized panes, one zoomed out, one zoomed in) directly collapse the Mantra's three stages into a persistent, always-visible structure: the user is never fully "without" overview, even while examining detail, eliminating the disorientation and lost context that can occur when a user must navigate away from an overview screen to reach a separate, isolated zoomed-in screen and then navigate back.

**(c) Guaranteed Visibility and Small Multiples relative to the Mantra:**

**Guaranteed Visibility** ensures that landmarks important to the user's understanding remain visible at all times, regardless of how the user zooms, filters, or pans. This directly *supports* the Mantra's overview stage by ensuring that even after a user has zoomed deep into "details on demand" territory, critical orientation landmarks (e.g., a capital city on a map, or a key reference threshold on a chart) remain visible — preventing the user from losing the contextual anchor that the initial "overview" established, effectively extending the benefit of "overview first" persistently throughout the entire interaction session rather than letting it apply only at the very start.

**Small Multiples** (a lattice of charts sharing the same axes/scale) could be seen as a *partial alternative* to the sequential Mantra rather than a strict implementation of it: instead of one display that you zoom and filter through over time, small multiples present many simultaneous "overviews" side-by-side (e.g., one subplot per region, as in the earlier coding example), letting the user visually compare across categories all at once without needing to sequentially zoom into each one. This can be seen as *complementing* the Mantra (each individual small-multiple panel can still itself support zoom/details-on-demand interaction) but could also arguably *bypass* the "zoom and filter" stage for the comparison task specifically, since the very purpose of small multiples is to let the user see many filtered subsets simultaneously rather than filtering down to one subset at a time — illustrating that the Mantra is a generally sound default sequence, but not the *only* valid interaction strategy for every task, particularly comparison-heavy tasks where simultaneous side-by-side viewing may outperform sequential zoom-and-filter.


---
---

# SET 3 — Marks & Channels: Visual Encoding, Expressiveness, Effectiveness & Perceptual Accuracy

---

## Section A — Multiple Choice Questions (20 Marks)

**1.** The principle of **Expressiveness**, when choosing a visual channel for an attribute, is best defined as:
A. Selecting the channel that is most visually attractive regardless of data type
B. Matching the channel type to the data type (e.g., using an ordered channel for ordered data, not for categorical data)
C. Always using color as the primary channel for any attribute type
D. Ensuring the visualization uses the maximum possible number of channels simultaneously

**2.** The principle of **Effectiveness**, as distinct from Expressiveness, refers to:
A. The requirement that some channels are perceived more accurately than others, so designers should match important attributes to the most accurate available channels
B. The requirement that every visualization must be rendered within 100 milliseconds
C. The idea that any channel can express any data type equally well
D. The legal requirement to label every axis with units

**3.** According to the channel rankings discussed in the lecture, which channel ranks highly for BOTH magnitude (ordered data) and identity (categorical data) judgments?
A. Color hue
B. Shape
C. Spatial position
D. Texture density

**4.** "Discriminability" is defined in the lecture as:
A. The number of unique, perceptually distinguishable steps a channel can support
B. The legal requirement to discriminate between data sources
C. The number of marks that can fit in a single visualization without overlapping
D. The maximum frame rate a rendering engine can sustain

**5.** The lecture notes that linewidth, as a channel, typically supports only a "few bins" of discriminability. This implies which design consequence?
A. Linewidth should be the default choice for encoding attributes with many (e.g., 20+) distinct ordered levels
B. Linewidth has unlimited discriminability and is always preferred over color
C. Linewidth can only be used for categorical, never ordered, data
D. Linewidth is unsuitable for encoding an attribute with many distinct ordered levels, since viewers cannot reliably distinguish that many width steps

**6.** Two channels are described as **separable** when:
A. They must always be rendered in two physically separate charts
B. They cannot be applied to the same mark under any circumstances
C. They both encode exactly the same attribute redundantly
D. A viewer's ability to accurately judge one channel is unaffected by the simultaneous presence of the other channel

**7.** Two channels are described as **integral** when:
A. They are mathematically related through calculus-based integration
B. They can only be used with line marks, never point marks
C. They perceptually fuse into a combined, emergent percept (e.g., overall area from height and width) rather than being judged independently
D. They are both restricted to categorical data only

**8.** "Popout" refers to the phenomenon in which:
A. A target can be found via fast, parallel processing, with search speed largely independent of the number of distractors present
B. A 3D mark visually protrudes from the screen using stereoscopic rendering
C. A mark's color changes automatically when the mouse hovers over it
D. Search speed always increases linearly with the number of distractors, regardless of channel

**9.** Which of the following channel combinations is explicitly noted in the lecture as one of the FEW conjunctions that DOES remain pre-attentive (i.e., still pops out)?
A. Color hue combined with font style
B. Motion, depth, color hue, and orientation combined together
C. Linewidth combined with text label length
D. Shape combined with exact numeric value

**10.** According to the "Accuracy: Fundamental theory" slide (referencing Stevens' power law concepts), which channel is described as accurately perceived in a **linear** fashion, while many others are magnified or compressed?
A. Color hue
B. Length
C. Area
D. Shape

**11.** Cleveland and McGill's classic graphical perception research, cited in the lecture, found that accuracy for length/position judgments **increases** under which condition?
A. When values are displayed in random, unaligned positions scattered across the figure
B. When a common scale and alignment are used, allowing relative rather than absolute judgments
C. When color is removed entirely from the display
D. When 3D perspective is added to a 2D chart

**12.** **Weber's Law**, as discussed in the lecture, states that:
A. The absolute difference between two values determines whether a viewer can perceive a difference
B. The ratio of the increment (difference) to the background (baseline) value is what remains constant for perceptibility, not the absolute difference
C. Perception of any visual channel improves linearly with viewing distance
D. Two marks of identical color are always perceived as identical regardless of surrounding context

**13.** The lecture's worked example states that filled rectangles differing in length by a ratio of 1:9 produce a "difficult judgement," while white rectangles differing by a ratio of 1:2 produce an "easy judgement." This illustrates:
A. That filled rectangles are always harder to judge than white rectangles regardless of ratio
B. Weber's Law in action — a small ratio (1:2) is easier to judge accurately than a large absolute difference if the relative ratio framing or context makes the comparison harder
C. That length is never an accurate channel under any condition
D. That color, not length, was actually being tested in this example

**14.** The "checkershadow" illusion referenced in the lecture (where two tiles of identical physical luminance appear different in brightness) demonstrates that:
A. Luminance perception is absolute and unaffected by surrounding context
B. Perception of luminance is contextual, based on contrast with the surrounding visual context, not on the tile's true, isolated physical value
C. The illusion only occurs in colorblind viewers
D. Luminance cannot be used as a visual channel under any circumstances

**15.** "Color constancy," illustrated in the lecture via real-world illumination examples, refers to the phenomenon where:
A. Viewers perceive an object's color as relatively stable across a broad range of different lighting/illumination conditions
B. All colors appear identical under any lighting condition without exception
C. Color perception requires a constant, unchanging light source to function at all
D. Color constancy only applies to grayscale images

**16.** "Marks as constraints" states that an **interlocking area** mark (e.g., a treemap rectangle) cannot be additionally:
A. Colored, since interlocking areas can never use color
B. Positioned anywhere on screen, since interlocking areas have fixed positions
C. Size- or shape-coded for another attribute, since its own size/shape (length and width) is already constrained/consumed by the mark's boundary
D. Rendered using more than one hue at a time

**17.** A "line" mark (1D), according to the marks-as-constraints principle, has how many inherent constraints on its size, and what size channel remains free to encode an additional attribute?
A. Zero constraints; both length and width remain free
B. One constraint (length); width remains free as an additional size channel
C. Two constraints (length and width); no size channel remains free
D. Three constraints; only color remains free

**18.** "Redundant encoding," as discussed in the lecture, refers to the technique of:
A. Encoding two completely different attributes using two different channels on the same mark
B. Using multiple channels (e.g., both length AND luminance) to represent the SAME single attribute, strengthening the signal at the cost of using up multiple channels
C. Deleting redundant/duplicate rows from a dataset before visualization
D. Rendering the same chart twice for backup purposes

**19.** The lecture's "Scope of analysis" slide notes that the simplifying assumptions used when analyzing marks/channels include "one mark per item" and "single view." Which of the following is identified as a more advanced scenario that goes BEYOND these simplifying assumptions?
A. Using exactly one color for the entire visualization
B. Multiple views, multiple marks in a single region (glyphs), and some items being aggregated/filtered rather than individually represented by marks
C. Restricting the visualization to only categorical data
D. Removing all interaction from the visualization entirely

**20.** "Grouping" mechanisms discussed in the lecture (containment, connection, proximity, similarity) primarily help viewers perceive:
A. The exact precise numeric value of a single data point
B. That certain marks belong together as a perceptual group, even without an explicit drawn boundary, based on cues like shared spatial region or shared categorical channel values
C. The frame rate of an animated visualization
D. Whether a dataset is static or dynamic

---

### Set 3 — Section A Answer Key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | B | 6 | B | 11 | B | 16 | C |
| 2 | A | 7 | C | 12 | B | 17 | B |
| 3 | C | 8 | A | 13 | B | 18 | B |
| 4 | A | 9 | B | 14 | B | 19 | B |
| 5 | B | 10 | B | 15 | A | 20 | B |


---

## Section B — Structured Questions (40 Marks)

*Answer ALL questions in this section.*

---

### Question 1 (10 marks)

**(a)** Define **Expressiveness** and **Effectiveness** as the two criteria for choosing a visual channel, and explain why a design can satisfy Expressiveness while still failing Effectiveness (give one concrete example). **(6 marks)**

**(b)** A dataset has an ordinal attribute `Customer_Satisfaction` with 7 levels (Very Dissatisfied → Very Satisfied). A designer proposes encoding this attribute using **linewidth**. Evaluate this choice against the concept of **discriminability**, and recommend a better channel. **(4 marks)**

#### Model Answer — Question 1

**(a) Expressiveness** means the chosen channel's *type* matches the data's type — e.g., using an ordered channel (like luminance) for ordered data, and a non-ordered/categorical channel (like color hue or shape) for categorical data. **Effectiveness** means the chosen channel is perceived *accurately* by the human visual system — some channels simply support more precise perceptual judgments than others, independent of whether they are type-appropriate. A design can be Expressive but not Effective: for example, encoding a quantitative attribute (e.g., revenue) using **color hue** is type-mismatched in the first place (hue is best for categories, not magnitude) — but even encoding it Expressively-correctly via, say, **area** size (which IS an ordered channel, satisfying Expressiveness) can still fail Effectiveness, because area/size judgments are perceptually compressed/distorted (per Stevens' power law) and less accurate than, e.g., a position-based or length-based encoding of the same quantitative attribute — so a channel can be "the right type" while still being "the wrong choice" for maximizing perceptual accuracy.

**(b)** Linewidth is a poor choice here: the lecture explicitly notes that linewidth supports only a "few" discriminable bins/steps — likely far fewer than the 7 distinct levels needed for `Customer_Satisfaction`. With only a few reliably distinguishable width-steps available, viewers would struggle to tell apart, e.g., level 4 from level 5, defeating the purpose of the ordinal encoding. A better channel would be **spatial position along a common, aligned scale** (e.g., placing satisfaction-level categories along a single ordered axis) or, if position is unavailable, **luminance/color intensity along a sequential color scale**, both of which support a substantially higher number of discriminable steps than linewidth while still being Expressively appropriate for ordered data.

---

### Question 2 (10 marks)

**(a)** Explain, with a concrete example involving a scatterplot, the difference between **separable** and **integral** channel pairs, and state ONE practical implication for a designer who wants viewers to judge two attributes completely independently of each other. **(6 marks)**

**(b)** A designer wants to highlight a small subset of "fraudulent transactions" within a scatterplot of thousands of "normal transactions," such that the fraudulent ones are found almost instantly regardless of how many normal transactions surround them. Using the concept of **popout**, recommend a specific single-channel encoding strategy, and explain why adding a SECOND channel (e.g., also changing the shape of fraudulent points) might not help, and could even hurt. **(4 marks)**

#### Model Answer — Question 2

**(a)** In a scatterplot encoding Attribute A via the x-position and Attribute B via point **shape** (e.g., circle vs. triangle), these two channels are largely **separable**: a viewer can judge "how spread out is A" and "how many shape-categories of B are present" as two independent perceptual tasks without one interfering with the other. By contrast, if the same scatterplot encoded Attribute A via point **size** and Attribute B via point **color saturation**, these channels risk becoming more **integral** — viewers may perceptually fuse "how big and how saturated" into a single combined impression of "intensity," making it harder to cleanly extract the size-judgment and the saturation-judgment as two cleanly separate values. The practical implication: a designer who wants two attributes judged fully independently should deliberately choose a channel pair known to be **separable** (e.g., spatial position + shape, or spatial position + a *clearly distinct* color hue) rather than pairs prone to integral fusion (e.g., size + color intensity, or height + width of the same mark).

**(b)** Recommended strategy: encode "fraudulent vs. normal" using a **single, strongly pre-attentive channel** — most reliably **color hue** (e.g., bright red dots for fraudulent transactions against a field of muted gray/blue normal transactions). Because popout's defining property is that detection speed for a *single* strong pre-attentive channel is **independent of the number of distractors**, a viewer can spot the red dots in roughly constant time whether there are 100 or 10,000 normal transactions surrounding them. Adding a SECOND channel (e.g., also making fraudulent points triangular instead of circular) creates a **conjunction** of two pre-attentive attributes (color + shape) — and the lecture explicitly warns that most such conjunctions **do not** remain pre-attentive; the visual system instead reverts to **slow, serial search**, where detection time *does* scale with the number of distractors, because the viewer must check candidates one-by-one for the *combination* of "is it red AND is it a triangle," rather than instantly registering "is it red." In this scenario, the second channel is not just unhelpful — it can actively degrade performance by destroying the popout effect the single-channel encoding was providing.

---

### Question 3 (10 marks)

**(a)** State **Weber's Law** as presented in the lecture, and use it to explain why a viewer might find it *easier* to judge a length difference of ratio 1:2 between two white rectangles than to judge a length difference of ratio 1:9 between two filled (dark) rectangles, even though 1:9 is numerically the "bigger" difference. **(5 marks)**

**(b)** Explain the "checkershadow" illusion and the concept of **color constancy**, and state ONE shared underlying lesson both phenomena teach visualization designers about color/luminance encoding. **(5 marks)**

#### Model Answer — Question 3

**(a)** Weber's Law states that the **ratio** of the increment (the difference between two values) to the background/baseline value is what determines perceptibility — not the raw, absolute difference between the two values. This means perceptual judgment is fundamentally *relative*, not absolute. In the lecture's worked example, the comparison context differs between the two cases: even though 1:9 is numerically a larger gap than 1:2, the specific *presentation* (filled vs. white rectangles, and the surrounding visual context each is judged against) changes what baseline the viewer's perceptual system is implicitly comparing against — illustrating that simply having "more numeric difference" does not guarantee "easier to perceive" difference; what matters is the perceived *ratio* relative to the relevant comparison context, which is precisely why careful framing/context/alignment in a chart design can make a numerically smaller difference *feel* easier to judge than a numerically larger one presented in a less favorable context.

**(b)** The **checkershadow illusion** shows two tiles of *identical* physical luminance (measurably the same shade of gray) that nonetheless appear to be different brightnesses to a human viewer, because one tile sits in an apparent shadow while the other does not — demonstrating that luminance perception is **contextual**, determined by contrast with surrounding visual context, not by the tile's true isolated physical value. **Color constancy** shows the complementary phenomenon: an object's *perceived* color remains relatively stable even as the actual physical wavelengths of light reflecting off it change dramatically under different illumination conditions (e.g., a white shirt still looks "white" in both daylight and warm indoor lighting, despite very different physical light spectra reaching the eye). The shared underlying lesson for visualization design: **a viewer's perception of a color or luminance value on screen is never purely a function of that mark's own pixel value in isolation — it is always influenced by the surrounding visual context** (nearby colors, apparent lighting/shading, background). Designers must therefore be cautious that the *same* encoded color or luminance value may be perceived differently depending on what other marks/colors surround it in the final display, and should test color/luminance encodings in their actual surrounding context rather than assuming a color will "read" the same way it does in an isolated swatch or legend.

---

### Question 4 (10 marks) — Practical / Coding

A retail analytics dataset `transactions.csv` has columns: `Transaction_ID`, `Store_Region` (categorical), `Transaction_Amount` (continuous), `Is_Fraudulent` (boolean), and `Hour_of_Day` (0–23, cyclic).

**(a)** Using `pandas`, write code to compute the **fraud rate** (proportion of `Is_Fraudulent == True`) for each `Store_Region`, and identify the region with the highest fraud rate. **(4 marks)**

**(b)** Using `matplotlib` and `numpy`, write code to visualize `Hour_of_Day` as a **cyclic/circular** plot (e.g., a polar plot) showing transaction counts by hour, rather than a standard linear bar chart. Explain in one sentence why a circular layout is more appropriate than a straight axis for this attribute, referencing the lecture's data-type framework. **(6 marks)**

#### Model Answer — Question 4

**(a)**
```python
import pandas as pd

df = pd.read_csv("transactions.csv")

fraud_rate_by_region = (
    df.groupby("Store_Region")["Is_Fraudulent"]
      .mean()                     # mean of a boolean column = proportion True
      .sort_values(ascending=False)
)

highest_fraud_region = fraud_rate_by_region.idxmax()
print(fraud_rate_by_region)
print(f"Highest fraud rate region: {highest_fraud_region}")
```
*Explanation:* Since `Is_Fraudulent` is boolean, `.mean()` on the grouped column directly computes the proportion of `True` values (treated as 1/0) — an efficient `pandas` idiom for rate calculations. `.idxmax()` returns the region label with the highest computed rate.

**(b)**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("transactions.csv")

counts = df.groupby("Hour_of_Day").size().reindex(range(24), fill_value=0)

# Convert hours (0-23) to angles around the circle (0 to 2*pi)
angles = np.linspace(0, 2 * np.pi, 24, endpoint=False)

fig, ax = plt.subplots(subplot_kw={"projection": "polar"}, figsize=(7, 7))
ax.bar(angles, counts.values, width=2 * np.pi / 24, edgecolor="white")

ax.set_theta_zero_location("N")   # midnight (0:00) at the top
ax.set_theta_direction(-1)        # hours increase clockwise
ax.set_xticks(angles)
ax.set_xticklabels(counts.index)
ax.set_title("Transaction Count by Hour of Day (Cyclic)")

plt.show()
```
*Explanation:* A circular/polar layout is more appropriate than a straight linear axis because `Hour_of_Day` is **cyclic** ordered data (per the lecture's ordering-direction framework — its values wrap around from 23 back to 0), and a linear bar chart would visually place hour 23 and hour 0 at opposite ends of the axis, falsely suggesting they are maximally "far apart" when in reality they are only one hour apart — the polar/circular layout correctly preserves this wraparound adjacency, just as a clock face correctly shows 11 PM and midnight as neighbors.

---

## Section C — Essay Questions (40 Marks)

*Answer TWO of the THREE questions in this section. Each question carries 20 marks.*

---

### Essay Question 1 (20 marks)

Critically discuss the **Expressiveness** and **Effectiveness** principles for selecting visual channels, and their relationship to **channel rankings**. Your essay must:

**(a)** Explain both principles in detail and explain why a designer needs BOTH, not just one. **(8 marks)**

**(b)** Discuss the channel ranking framework presented in the lecture, including why spatial position ranks highly for BOTH magnitude (ordered) and identity (categorical) judgments, while other channels may rank well for one but not the other. **(7 marks)**

**(c)** Apply both principles to critique a real (or hypothetical) poorly-designed chart of your choosing — describe the chart, identify which principle(s) it violates, and propose a corrected design. **(5 marks)**

#### Model Answer — Essay Question 1

**(a) Why both principles are needed:** Expressiveness ensures the *type* of channel matches the *type* of data — e.g., using an ordered channel (size, luminance, position) for quantitative/ordinal data, and a non-ordered channel (hue, shape) for categorical/nominal data. Without Expressiveness, a viewer might be misled into perceiving a false ordering in data that has none (e.g., using a sequential color scale, which implies "low to high," to encode unordered categories like fruit type, falsely implying that "apple" is somehow "less than" "banana"). However, Expressiveness alone is insufficient: a channel can be the technically "correct type" for the data and yet still be a poor choice because human perception is not uniformly accurate across all channels of the same type. This is where Effectiveness comes in — it ranks channels by how *accurately* humans can perceive differences using that channel, regardless of type-correctness. A designer needs both because Expressiveness without Effectiveness produces a "technically valid but hard-to-read" encoding (e.g., correctly using an ordered channel like hue-saturation for a quantitative value, but saturation differences are notoriously hard to judge precisely), while Effectiveness without Expressiveness produces a highly *accurate but semantically misleading* encoding (e.g., using the highly-accurate position channel to encode unordered categories, which works perceptually but can mislead the chart's IMPLIED meaning if positions are arranged to suggest a false ranking).

**(b) Channel rankings and spatial position's dual strength:** The lecture frames channel selection as needing to address two separate ranking questions: which channels best convey **magnitude** (how much / which rank, relevant to ordered data) and which best convey **identity** (what / which category, relevant to categorical data). **Spatial position** is unusual in ranking highly on BOTH dimensions: for magnitude, position along a common scale is identified as one of the only two channels (alongside length) that can be perceived quantitatively with real accuracy — viewers can judge small differences in position with high precision, especially when aligned to a shared scale (per Cleveland and McGill's findings). For identity, position is *also* effective because distinct spatial locations are trivially and immediately distinguishable as "different things," with no risk of ambiguity. Other channels are more lopsided: **color hue** ranks well for identity (distinct hues are excellent, fast, pre-attentive category markers) but poorly for magnitude (hue has no natural perceptual ordering — there's no sense in which "blue is more than red" — so encoding a quantitative value via raw hue forces an arbitrary, learned mapping that is far less intuitive and accurate than a true ordered channel). **Shape** similarly ranks well for identity (a fixed set of distinct glyphs is easy to tell apart as categories) but is essentially unusable for conveying magnitude. This dual-purpose strength is precisely why position (e.g., the x/y axes of a standard scatterplot or bar chart) remains the default, most heavily-relied-upon channel across nearly all conventional chart types.

**(c) Critique of a poorly-designed chart:** Consider a hypothetical dashboard chart visualizing five product categories' average customer ratings (a quantitative attribute, 1–5 stars) using a **pie chart**, where each category's slice angle represents its average rating, and slice color is assigned arbitrarily (not tied to any meaningful order). This design violates **Effectiveness**: the lecture's framework (and the broader literature it draws on) identifies angle/area judgments as comparatively *less accurate* than position/length judgments for quantitative comparison — viewers will struggle to precisely judge "how much bigger" one slice's rating is than another's, especially for ratings that are numerically close (e.g., 4.1 vs. 4.3 stars). It may also weakly violate **Expressiveness**, since arbitrary slice color assignment, if it happens to look "ordered" by accident (e.g., darker colors next to each other), risks implying a categorical ranking that doesn't actually reflect the rating values. **Corrected design:** replace the pie chart with a simple horizontal **bar chart**, encoding average rating via bar **length along a shared, aligned, common-scale axis** — the single most accurate channel combination identified in the lecture for quantitative magnitude comparison — with bars sorted from highest to lowest rating, making the ranking immediately and accurately perceivable, and reserving color (if used at all) purely as a redundant, non-load-bearing decorative cue rather than the primary carrier of the quantitative information.

---

### Essay Question 2 (20 marks)

Critically discuss the four properties of **channel effectiveness** introduced in the lecture: **accuracy, discriminability, separability, and popout**. Your essay must:

**(a)** Define and explain each of the four properties in detail, with one original example for each (not directly copied from the lecture). **(12 marks)**

**(b)** Explain how these four properties can sometimes come into TENSION with each other in a single design — i.e., describe a realistic scenario where maximizing one property (e.g., popout) might come at some cost to another (e.g., discriminability or separability). **(8 marks)**

#### Model Answer — Essay Question 2

**(a) The four properties, defined and exemplified:**

**Accuracy** asks: how precisely can viewers tell the difference between two encoded values on a given channel? Different channels have fundamentally different accuracy ceilings — length and 2D position are highly accurate (near-linear perception), while channels like area or volume are perceptually compressed or distorted (following power-law relationships rather than linear ones). *Original example:* encoding a country's population via the **radius** of a circle on a map (a common but flawed choice) forces viewers to perceptually estimate **area** (since area scales with radius squared), which they will systematically underestimate for large values — far less accurate than encoding the same population via a bar's **length** on an aligned axis.

**Discriminability** asks: how many genuinely distinguishable, usable steps does a channel support? A channel may be accurate in a relative sense but still support only a small number of reliably distinguishable categories before adjacent steps become indistinguishable. *Original example:* encoding a product's "star rating" (1 through 5) via **dot size** might be discriminable enough for 5 levels, but attempting to encode a finer-grained "0–100 quality score" using the same dot-size channel would quickly exceed viewers' ability to tell apart, say, scores of 62 vs. 65, since size differences at that granularity collapse below the threshold of perceptible difference.

**Separability** asks: does using this channel interfere with a viewer's ability to simultaneously and independently judge another channel applied to the same mark? Some channel pairs can be read independently; others perceptually "leak" into one another. *Original example:* encoding "delivery speed" via point **shape** and "customer region" via point **spatial position** in a scatterplot are likely separable — a viewer can judge shape-category counts and spatial clustering independently. But encoding "delivery speed" via point **size** and "customer satisfaction" via point **color saturation** on the *same* points risks low separability, since size and saturation can perceptually combine into a fused "prominence" impression, making it hard to cleanly read either value alone.

**Popout** asks: can a target with a specific channel value be detected almost instantly via fast, parallel pre-attentive processing, regardless of how many distractors surround it? *Original example:* a single bright orange dot encoding an "urgent" support ticket among hundreds of gray "normal" ticket dots on a dashboard will pop out near-instantly regardless of how many normal tickets are displayed, because color hue is a strong, isolated pre-attentive popout channel.

**(b) Tension between the properties:**

A realistic design tension arises when a designer tries to use a *single* highly popout-friendly channel (like color hue) to simultaneously encode **many** distinct categories, in pursuit of strong popout for each one. Suppose a network monitoring dashboard tries to encode 15 different *server types* using 15 distinct color hues, hoping that each server type will "pop out" instantly for an operator looking for it. This directly damages **discriminability**: the human visual system can only reliably discriminate a limited number of distinct hues at a glance (typically cited as well under 15 for fast, confident categorical separation) — beyond roughly 8–10 hues, adjacent colors become difficult to tell apart, meaning popout for any *individual* server type actually degrades as the total hue count grows, since "find the teal dot" becomes a much harder, slower task when teal is one of fifteen closely-spaced hues rather than one of three highly distinct ones. The same scenario can also strain **separability** if the designer additionally tries to encode a second attribute (say, CPU load) via size on the same dots: with 15 hues already competing for discriminability, adding a second channel increases the risk that size and hue differences begin to perceptually interact (e.g., larger dots of certain hues appearing more "salient" than their true CPU-load value alone would justify), undermining the assumption that hue and size can be read independently. This illustrates a general principle: pursuing one effectiveness property (popout via a single strong channel) to its limit, by overloading that channel with too many distinct values, can directly erode a different effectiveness property (discriminability) for that same channel — meaning a real design typically requires a *deliberate trade-off* across these four properties rather than independently maximizing each one.

---

### Essay Question 3 (20 marks)

The lecture states that "the perceptual system mostly operates with relative judgements, not absolute" judgements. Critically discuss this claim and its design implications, drawing on **Weber's Law**, **relative luminance judgments**, and **relative color judgments (color constancy)**. Your essay must:

**(a)** Explain each of the three phenomena in detail, with reference to the specific experimental/illustrative examples from the lecture (rectangle ratios, checkershadow illusion, illumination/color constancy demonstrations). **(12 marks)**

**(b)** Drawing a unifying conclusion across all three phenomena, propose THREE concrete, practical design guidelines a visualization designer should follow when using length, luminance, or color channels, to avoid being undermined by the relativity of human perception. **(8 marks)**

#### Model Answer — Essay Question 3

**(a) The three phenomena in detail:**

**Weber's Law and length/position judgments:** The lecture demonstrates that accuracy for length and position judgments is substantially improved when values share a **common scale and alignment**, allowing *relative* comparison rather than forcing viewers to make independent, *absolute* estimates of each value in isolation. This is formalized through Weber's Law, which states that perceptibility of a difference depends on the **ratio** of the increment to the background value, not the raw absolute difference. The lecture's worked example — filled rectangles differing by a 1:9 ratio being judged as "difficult," while white rectangles differing by a 1:2 ratio are judged as "easy" — concretely demonstrates that perceptual difficulty does not track the raw numeric magnitude of the difference; it tracks the *relative, contextual* framing of that difference, directly supporting the claim that judgment is fundamentally comparative rather than absolute.

**Relative luminance judgments and the checkershadow illusion:** The checkershadow illusion presents two tiles of objectively, measurably **identical** physical luminance, yet viewers reliably perceive one as darker than the other because one tile appears to sit within a cast shadow. This is a direct, dramatic demonstration that the visual system does not measure and report luminance as an absolute physical quantity — it interprets a tile's brightness *relative to* its surrounding visual context (in this case, inferring and "discounting" the presumed effect of a shadow), producing a perceived value that diverges sharply from ground truth.

**Relative color judgments and color constancy:** Color constancy describes how an object's perceived color remains relatively stable across a wide range of actual illumination conditions, even though the literal wavelengths of light reaching the eye from that object change substantially between, say, daylight and incandescent lighting. The visual system effectively "corrects for" the assumed color of the ambient light source, again prioritizing a stable, *contextually-adjusted* percept over a literal, absolute report of the raw physical input — directly paralleling the luminance case, but for hue/chroma rather than brightness.

**Unifying theme:** all three phenomena converge on the same underlying truth: human visual perception is fundamentally an *interpretive, contextual* process, not a passive, absolute measurement device — what a viewer perceives for any single channel value (length, luminance, or color) is always shaped by the surrounding visual context, comparison framing, and the relative relationships between elements, not simply by that element's own isolated physical/digital value.

**(b) Three concrete design guidelines:**

1. **Always align values to a common, shared scale/baseline when accurate comparison matters.** Since Weber's Law shows that relative, aligned comparisons are dramatically easier and more accurate than absolute, unaligned estimation, any chart intended to support precise value comparison (e.g., bar charts, dot plots) should share a single zero-aligned axis across all compared elements, rather than using small multiples with independently-scaled axes or scattering marks without a common reference line.

2. **Test color and luminance encodings within their actual final visual context, never in isolation.** Because both the checkershadow illusion and color constancy demonstrate that the *same* objective pixel value can be perceived very differently depending on surrounding colors/shading, a designer should never finalize a color-coding scheme by inspecting swatches in a legend alone — colors must be evaluated as they will actually appear, adjacent to the other colors, backgrounds, and apparent depth/shading cues present in the finished visualization, since the legend swatch's "true" appearance may not survive contextual placement.

3. **Avoid relying on luminance or saturation alone to convey small, precise quantitative differences in a visually "busy" or shadowed/textured background.** Since luminance perception is so strongly modulated by surrounding contrast, encoding subtle quantitative differences purely through brightness on top of a background with varying texture, shading, or surrounding colors risks the viewer's perceived ordering or magnitude diverging from the true underlying data — in high-precision contexts, a designer should prefer channels less susceptible to contextual distortion (such as aligned position/length) or provide a neutral, consistent background against which luminance differences can be judged more reliably.


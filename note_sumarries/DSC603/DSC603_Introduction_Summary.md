# Summary: DSC603 Data Mining – Introduction

## Course Objectives
- Introduces main **concepts and tasks** of data mining: data manipulation, cleaning techniques, representation of real-world information as data types.
- Explores approaches to **mine knowledge** from these data representations.

---

## 1. Why Data Mining?
- **Data explosion**: from terabytes to petabytes; automated collection (databases, Web, sensors).
- **Sources**: Business (Web, e-commerce, transactions, stocks), Science (remote sensing, bioinformatics, simulations), Society (news, digital cameras, YouTube).
- **Motive**: “We are drowning in data but starving for knowledge” → data mining = automated analysis of massive data.

**Evolution of science (brief):**
- Before 1600: empirical science.
- 1600–1950s: theoretical science.
- 1950s–1990s: computational science (simulation, no closed-form solutions).
- 1990–now: data science (flood of data, storage, Internet/grid, scaling of management and mining).

**Evolution of database technology:**
- 1960s: data collection, IMS, network DBMS.
- 1970s: relational model, RDBMS.
- 1980s: advanced models, application-oriented DBMS.
- 1990s: data mining, data warehousing, multimedia and Web DB.
- 2000s: stream data, data mining applications, Web (XML, integration), global information systems.

---

## 2. What Is Data Mining?
- **Definition**: Extraction of **interesting** (non-trivial, implicit, previously unknown, potentially useful) patterns or knowledge from huge amounts of data.
- **Other names**: KDD, knowledge extraction, data/pattern analysis, data archeology, information harvesting, business intelligence.
- **Not data mining**: simple search/query processing; (deductive) expert systems.

---

## 3. Examples (Included as in the Document)

### Example: KDD Process (Database/Warehousing View)
Steps: **Data cleaning** → **Data integration** → **Databases / Data warehouse** → **Task-relevant data selection** → **Data mining** → **Pattern evaluation**. Data mining is central in this process.

### Example: Web Mining Framework
Web mining usually involves: data cleaning, data integration from multiple sources, warehousing, data cube construction, data selection for mining, data mining, presentation of results, and storing/using patterns in a knowledge base.

### Example: Data Mining in Business Intelligence
Pyramid (bottom to top): **Data sources** (paper, files, Web, experiments, DBs) → **Data preprocessing/integration, data warehouses** → **Statistical summary, querying, reporting** → **Data mining (information discovery)** → **Data presentation / visualization** → **Decision making**. Roles: DBA, Data Analyst, Business Analyst, End User.

### Example: KDD from ML/Statistics View
- **Input data** → **Data preprocessing** (integration, normalization, feature selection, dimension reduction) → **Data mining** (pattern discovery: association & correlation, classification, clustering, outlier analysis, etc.) → **Post-processing** (pattern evaluation, selection, interpretation, visualization).

### Example: Association Rule
- **Diaper → Beer [0.5%, 75%]**: 0.5% support, 75% confidence. Used to illustrate that strongly associated items may or may not be strongly correlated; efficiency in large datasets and use for classification/clustering are discussed.

### Example: Classification
- **Countries** by climate; **cars** by gas mileage.
- Build models from training examples; predict unknown class labels.
- Methods: decision trees, naïve Bayes, SVM, neural networks, rule-based, pattern-based, logistic regression.
- Applications: fraud detection, direct marketing, classifying stars, diseases, web pages.

### Example: Cluster Analysis
- Unsupervised; group data into new categories (e.g. cluster houses for distribution patterns).
- Principle: maximize intra-class similarity, minimize inter-class similarity.

### Example: Outlier Analysis
- Outlier = object that does not comply with general behavior (noise vs. exception).
- “One person’s garbage could be another person’s treasure”; used in fraud detection and rare events.

### Example: Sequential / Trend Analysis
- Sequential pattern: e.g. first buy digital camera, then large SD memory cards.
- Also: trend/time-series, periodicity, motifs and biological sequences, similarity, mining data streams.

### Example: Structure and Network Analysis
- **Graph mining**: frequent subgraphs (e.g. chemical compounds), trees (XML), substructures.
- **Information networks**: social networks (e.g. author networks, terrorist networks); link mining; web mining (PageRank, Google); web community discovery, opinion mining, usage mining.

---

## 4. Multi-Dimensional View of Data Mining
- **Data**: DB (relational, OO, heterogeneous, legacy), warehouse, transactional, stream, spatiotemporal, time-series, sequence, text/web, multimedia, graphs and networks.
- **Knowledge (functions)**: characterization, discrimination, association, classification, clustering, trend/deviation, outlier analysis; descriptive vs. predictive; multiple functions and levels.
- **Techniques**: data-intensive, OLAP/warehouse, machine learning, statistics, pattern recognition, visualization, high-performance computing.
- **Applications**: retail, telecom, banking, fraud, bio, stock, text mining, web mining, etc.

---

## 5. Data That Can Be Mined
- **DB-oriented**: relational DB, data warehouse, transactional DB.
- **Advanced**: streams/sensor data; time-series, temporal, sequence (e.g. bio-sequences); structured data, graphs, social networks; object-relational, heterogeneous, legacy; spatial and spatiotemporal; multimedia; text; WWW.

---

## 6. Data Mining Functions (With Examples Above)
1. **Generalization**: data cleaning, transformation, integration; multidimensional model; data cubes; OLAP; characterization and discrimination (e.g. dry vs. wet region).
2. **Association and correlation**: frequent patterns/itemsets; association rules (e.g. Diaper → Beer); efficiency and use in classification/clustering.
3. **Classification**: model building from training data; prediction of class labels; methods and applications as in “Classification” example.
4. **Cluster analysis**: unsupervised grouping; principle as above.
5. **Outlier analysis**: definition and use as above.
6. **Time/ordering**: sequential patterns, trend, evolution, periodicity, motifs, streams (as above).
7. **Structure/network**: graph mining, information networks, web mining (as above).

---

## 7. Evaluation of Knowledge
- Not all mined knowledge is interesting (may be dimension-specific, non-representative, transient).
- Criteria: descriptive vs. predictive, coverage, typicality vs. novelty, accuracy, timeliness.

---

## 8. Confluence of Disciplines
Data mining sits at the intersection of: **database technology**, **machine learning**, **statistics**, **pattern recognition**, **algorithms**, **high-performance computing**, **visualization**, **applications**. Reasons: huge data (scalability), high dimensionality (e.g. microarrays), complex data types and new applications.

---

## 9. Applications (Examples from the Document)
- Web page analysis: classification, clustering, PageRank, HITS.
- Collaborative analysis and recommender systems.
- Basket data and targeted marketing.
- Biological and medical: classification, clustering (e.g. microarray), sequence and network analysis.
- Data mining and software engineering (e.g. IEEE Computer, Aug. 2009).
- From dedicated tools (SAS, MS SQL Server Analysis Manager, Oracle Data Mining) to “invisible” data mining.

---

## 10. Major Issues
- **Methodology**: new kinds of knowledge, multi-dimensional mining, interdisciplinary work, networked discovery, noise/uncertainty/incompleteness, pattern evaluation and constraint-guided mining.
- **User interaction**: interactive mining, background knowledge, presentation and visualization.
- **Efficiency and scalability**: algorithm efficiency; parallel, distributed, stream, and incremental mining.
- **Data diversity**: complex types, dynamic and global repositories.
- **Society**: social impact, privacy-preserving and invisible data mining.

---

## 11. History and Community
- 1989: IJCAI Workshop on KDD (Piatetsky-Shapiro, Frawley, 1991).
- 1991–1994: KDD workshops; “Advances in KDD and Data Mining” (Fayyad et al., 1996).
- 1995–1998: KDD conferences; Journal of Data Mining and Knowledge Discovery (1997).
- From 1998: ACM SIGKDD, SIGKDD Explorations; PAKDD, PKDD, SIAM-DM, IEEE ICDM, etc.; ACM Transactions on KDD (2007).

---

## 12. Conferences and Journals
- **KDD-related**: ACM SIGKDD (KDD), SIAM SDM, IEEE ICDM, ECML-PKDD, PAKDD, WSDM.
- **Related**: SIGMOD, VLDB, ICDE, EDBT; WWW, SIGIR; ICML, NIPS; CVPR; etc.
- **Journals**: Data Mining and Knowledge Discovery (DAMI/DMKD), IEEE TKDE, KDD Explorations, ACM Trans. KDD.

---

## 13. Where to Find References
- DBLP, CiteSeer, Google.
- SIGKDD CD-ROM; SIGMOD Anthology; ML, AAAI, IJCAI; SIGIR, WWW; statistics and visualization venues as in the slide.

---

## 14. Summary (From the Document)
- Data mining: discovering interesting patterns and knowledge from massive data.
- Natural evolution of DB technology; high demand; wide applications.
- KDD process: cleaning, integration, selection, transformation, mining, pattern evaluation, knowledge presentation.
- Many data types; functionalities: characterization, discrimination, association, classification, clustering, outlier and trend analysis, etc.
- Technologies and applications as above; major issues as above.

---

## 15. Recommended Reference Books (From the Document)
- Chakrabarti (Mining the Web); Duda, Hart, Stork (Pattern Classification); Dasu & Johnson (Exploratory Data Mining); Fayyad et al. (Advances in KDD); Fayyad, Grinstein, Wierse (Information Visualization); Han & Kamber (Data Mining: Concepts and Techniques, 3rd ed.); Hand, Mannila, Smyth (Principles of Data Mining); Hastie, Tibshirani, Friedman (Elements of Statistical Learning); Liu (Web Data Mining); Mitchell (Machine Learning); Piatetsky-Shapiro & Frawley (KDD); Tan, Steinbach, Kumar (Introduction to Data Mining); Weiss & Indurkhya (Predictive Data Mining); Witten & Frank (Data Mining: Practical Machine Learning Tools).

---

## Note on Exercises and Assignments
This PDF is a **42-slide introductory lecture** (DSC603 Data Mining – Introduction). It **does not contain** a separate section of numbered exercises or assignments with blank answers. The “answers” to “what does this course cover?” and “what do the examples mean?” are exactly what is summarized above: every example is included and explained in context. If you have another file (e.g. tutorial or problem set) with specific exercise or assignment questions, share its name or content and answers can be provided for those.

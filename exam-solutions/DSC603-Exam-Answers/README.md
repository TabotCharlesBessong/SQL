# DSC 603 – Data Mining Exam Solutions

Solutions for **DSC 603 Data Mining** exams (University of Buea).

## Contents

| File | Exam | Description |
|------|------|-------------|
| `DSC603-Data-Mining-Exam-Solutions.md` | 05 Jan 2023 (1h30) | Similarity measures, data warehousing (star schema, OLAP, bitmap), iceberg cube, aggregate cells |
| `DSC603-Exam-25Jan2023-Solutions.md` | 25 Jan 2023 (3h, 70 marks) | Data pre-processing, association rules (Apriori), decision tree, Naive Bayes, data warehouse & OLAP |

## Exam 1 (05 Jan 2023) — Coverage

- **Question 1 (Compulsory, 15 marks):** Similarity measures – rank 5 points by Euclidean distance and cosine similarity for a given query point.
- **Question 2 (Elective, 15 marks):** Data warehouse – star schema, OLAP operations for “total charge by students at GM Place in 2021”, bitmap indexing.
- **Bitmap indexing (5 marks):** Definition; advantages and problems.
- **Question 3 (Elective, 15 marks):** Curse of dimensionality – aggregate cell definition, count of nonempty aggregate cells, iceberg cube (min_support = 2).

## Exam 2 (25 Jan 2023) — Coverage

- **Question 1 (18 marks):** Data pre-processing – reasons for data cleaning; data integration (objective, redundant data categories, correlation/Chi-square); data reduction (need, dimensionality/numerosity reduction, curse of dimensionality, wavelet transforms, PCA).
- **Question 2 (20 marks):** Association rules – objective; Apriori property; step-by-step Apriori (Ck, Lk) with min_support 40%; all association rules and strong rules (min_confidence 70%).
- **Question 3 (18 marks):** Decision tree (Information Gain) for Oak vs Pine; classification rules; Bayesian classifier (X, Ci, naive assumption); Dogs vs Cats probabilities and classification of (Bark, Coarse, Brown).
- **Question 4 (20 marks):** Data warehouse vs database; warehouse schema and star schema; phases of warehouse architecture; bitmap vs B-tree indexing; OLAP and its use in data mining.

## Related course notes

See `note_sumarries/DSC603/` for summaries on data cubes, OLAP, cube technology, and data mining concepts.

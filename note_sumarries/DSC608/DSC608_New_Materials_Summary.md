# DSC608 New Materials Summary (Added Resources)

This summary consolidates the newly added DSC608 resources:
- Intro to Information Retrieval
- Queries and Interfaces
- DSC608 course outline (2023/2024)

## 1. Intro to Information Retrieval: Key Additions and Reinforcements

### 1.1 Core framing
- IR targets unstructured data (text, web pages, emails) and tries to satisfy an information need.
- RDBMS and IR differ in matching style:
  - RDBMS: exact matching over structured fields.
  - IR: approximate relevance ranking over free text.

### 1.2 Ad-hoc retrieval vs filtering
- Ad-hoc retrieval: relatively stable collection, changing query.
- Filtering: changing stream of documents, stable user profile.

### 1.3 Search engine architecture (two blocks)
- Indexing process:
  - Text acquisition (crawlers, feeds)
  - Text transformation (tokenization, stopping, stemming, extraction)
  - Index creation (dictionary + postings)
- Query process:
  - User interaction (query input, transformation, output)
  - Ranking (scoring and optimization)
  - Evaluation (logging, ranking analysis, performance analysis)

### 1.4 Why this matters for exams
- Typical exam prompts ask students to compare structured/unstructured search, explain architecture, and justify indexing choices.
- The architecture should always be tied to effectiveness + efficiency trade-offs.

## 2. Queries and Interfaces: High-Yield Concepts

### 2.1 Information need vs query quality
- A short keyword query is often an imperfect expression of a deeper information need.
- ASK (Anomalous State of Knowledge): users cannot fully describe what they do not yet know.

### 2.2 Query transformation pipeline
- Stopwords and stemming can be decided at query time for flexibility.
- Spell checking:
  - Edit distance (including Damerau-Levenshtein operations)
  - Context-sensitive correction via noisy channel model:
    - P(w|e) proportional to P(e|w)P(w)
  - Query logs improve correction quality and ranking of suggestions.

### 2.3 Query expansion and refinement
- Expansion can be based on:
  - Term association in collection
  - Top-ranked docs (pseudo-relevance feedback)
  - Query logs and session behavior
- Association measures commonly referenced:
  - Dice coefficient
  - Mutual information / expected mutual information
  - Chi-square-style dependence measures

### 2.4 Relevance feedback
- Explicit: user marks relevant documents.
- Pseudo feedback: assume top-k docs are relevant.
- Both can improve ranking, but pseudo feedback can drift when top results are noisy.

### 2.5 Context and personalization
- Important contextual signals:
  - session history
  - repeated/similar past queries
  - location (local search)
- Query intent can change with context even for identical keywords.

### 2.6 Result presentation
- Snippets and highlighting influence user judgments.
- Good snippet design:
  - readable text
  - meaningful context around query terms
  - avoid keyword soup
- Clustering and faceted classification support exploratory browsing.

### 2.7 Ads and retrieval
- Sponsored search ranks ads using relevance + bid + expected engagement.
- Vocabulary mismatch remains important, so expansion and reformulation still matter.

### 2.8 Cross-language retrieval
- Query translation and document translation are both used.
- Statistical translation models rely on aligned parallel corpora.

## 3. Course Outline Alignment (What to prioritize)

Based on the outline sequence, exam-prep priority should be:
1. Intro + architecture + indexing fundamentals
2. Text statistics and parsing (Zipf, Heaps, tokenization, stemming)
3. Ranking with indexes and query processing
4. Queries/interfaces and refinement methods
5. Retrieval models (Boolean, vector, probabilistic)
6. Evaluation metrics and testing approaches
7. Filtering and recommendation

## 4. Fast Revision Checklist

- Can you clearly distinguish information need from query?
- Can you draw and explain the indexing/query architecture blocks?
- Can you explain and apply Zipf and Heaps formulas?
- Can you contrast incidence matrix and inverted index in space terms?
- Can you compute one or two PageRank iterations from a directed graph?
- Can you explain when pseudo-relevance feedback helps or hurts?
- Can you compute/interpret P@k, AP, MAP, MRR, DCG, NDCG?

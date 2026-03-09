# DSC608 Information Retrieval — Essay Questions (50 marks total)

**Distribution:** 10 marks Easy (20%) | 15 marks Medium (30%) | 25 marks Hard (50%)

---

## EASY (10 marks total)

### Essay 1 [10 marks – EASY]

**Question:** Describe the main components of a search engine architecture. Explain the role of the **indexing process** and the **query process**, and name at least two sub-components of each.

**Model answer and marking guide:**

- **Overall architecture (2 marks):** A search engine is built from two main functions: (1) indexing process, and (2) query process. The indexing process prepares data structures from documents; the query process uses the query and these structures to produce a ranked list of results.

- **Indexing process (4 marks):**
  - **Text acquisition:** Identifies and stores documents (e.g. crawlers, feeds, conversion).
  - **Text transformation:** Converts documents into index terms (parsing, tokenization, stopping, stemming, link extraction, etc.).
  - **Index creation:** Builds data structures (e.g. inverted index) from index terms, possibly with weighting (e.g. TF-IDF) and document statistics.

- **Query process (4 marks):**
  - **User interaction:** Query input (UI, query language), query transformation (same normalisation as documents; spell check, expansion, relevance feedback), and results output (snippets, highlighting, clustering).
  - **Ranking:** Takes the query and index and produces a ranked list using a retrieval model (e.g. scoring with term weights).
  - **Evaluation:** Logging, ranking analysis, performance analysis to tune and improve the system.

**Explanation:** The notes present the architecture as indexing (acquisition → transformation → index creation) and query (user interaction, ranking, evaluation). A good answer names these and gives concrete sub-components with brief roles.

---

## MEDIUM (15 marks total)

### Essay 2 [8 marks – MEDIUM]

**Question:** Explain **Zipf’s law** and **Heaps’ law**. State each law, define the variables, and give one implication of each for the design or behaviour of an IR system.

**Model answer and marking guide:**

- **Zipf’s law (4 marks):**
  - **Statement:** The frequency *f* of a word is inversely proportional to its rank *r* (words ranked by decreasing frequency). Equivalently, *P(r)* ∝ 1/*r* (e.g. *P(r)* ≈ *c*/*r*, *c* ≈ 0.1 for English).
  - **Variables:** *f* = frequency of word, *r* = rank (1 = most frequent), *c* = corpus constant.
  - **Implication:** Few words are very frequent (e.g. “the,” “of”), many are rare. So: stopword lists target high-frequency words; IDF down-weights common terms; Zipf explains why term distributions are skewed. The law breaks down at very high and very low ranks.

- **Heaps’ law (4 marks):**
  - **Statement:** Vocabulary size *v* = *k*·*n*^β, where *n* is corpus size (total word tokens), *k* and β are parameters (often β ≈ 0.5, *k* in range ~10–100).
  - **Variables:** *v* = number of unique terms, *n* = total tokens, *k*, β = constants for the collection.
  - **Implication:** Vocabulary grows with corpus but at a decreasing rate. So: dictionary size can be predicted for scaling; new words keep appearing even in large corpora (e.g. web); index design must allow for growing vocabulary.

**Explanation:** Both laws are foundational text statistics in the notes. Full marks require the formula, variable definitions, and a clear IR implication for each.

---

### Essay 3 [7 marks – MEDIUM]

**Question:** Compare **Boolean retrieval** and the **vector space model** in terms of (a) how the query and documents are represented, (b) how results are produced, and (c) one main advantage and one main disadvantage of each.

**Model answer and marking guide:**

- **(a) Representation (2 marks):**
  - **Boolean:** Query is a Boolean expression over terms (AND, OR, NOT). Documents are treated as sets of terms (or term incidence). No weights.
  - **Vector space:** Query and documents are **vectors of term weights** (e.g. TF-IDF). Each dimension is a term in the vocabulary.

- **(b) How results are produced (2 marks):**
  - **Boolean:** For each document, evaluate the Boolean expression (membership in sets). Output is the **set** of matching documents; no ordering (or arbitrary, e.g. by date).
  - **Vector space:** Compute a **similarity** (e.g. cosine) between query vector and each document vector. Output is a **ranked list** by decreasing similarity.

- **(c) Advantage and disadvantage (3 marks):**
  - **Boolean:** Advantage: predictable, easy to explain; can include metadata (date, type); efficient (many docs eliminated). Disadvantage: no ranking; effectiveness depends on user’s query formulation; NOT often removes relevant docs; complex queries are hard.
  - **Vector space:** Advantage: natural ranking; simple framework; flexible (different similarity/weights). Disadvantage: assumes term independence; no explicit relevance model; long documents can dominate if not normalised (e.g. cosine addresses this).

**Explanation:** The notes contrast Boolean (exact match, set retrieval) with vector space (weights, similarity, ranking). A good answer covers representation, retrieval outcome, and trade-offs.

---

## HARD (25 marks total)

### Essay 4 [12 marks – HARD]

**Question:** (a) Describe the **inverted index** structure (dictionary and postings) and how it is built from a collection of documents. (b) Explain how it supports (i) Boolean conjunctive queries (AND), and (ii) ranked retrieval with TF-IDF-style scoring. (c) What is the benefit of storing **word positions** in postings, and what is one drawback of **precomputed scores** in the index?

**Model answer and marking guide:**

- **(a) Structure and building (4 marks):**
  - **Structure:** Inverted index has (1) **Dictionary:** sorted list of index terms (vocabulary). (2) **Postings:** for each term, a **postings list** of document IDs (and optionally term frequency, positions). Lists are typically sorted by document ID. Each (term, doc) pair is a “posting.”
  - **Building:** (1) Acquire documents. (2) For each document: tokenize, apply linguistic preprocessing (normalise, stop, stem) to get index terms. (3) Produce (term, docID) pairs; sort by term then docID; merge same (term, doc) and aggregate (e.g. counts, positions). (4) Split into dictionary (terms + maybe document frequency) and postings (lists of docIDs/counts/positions).

- **(b) Boolean AND and ranked retrieval (4 marks):**
  - **(i) Boolean AND:** For query *t*₁ AND *t*₂ AND … AND *t*ₖ, retrieve postings lists for *t*₁, …, *t*ₖ. **Intersect** the lists (e.g. merge-style: advance pointers, keep docIDs that appear in all lists). The result is the set of documents containing every query term.
  - **(ii) Ranked retrieval:** For each query term, get postings (with counts if available). For each document that contains at least one query term, **accumulate** a score, e.g. sum over query terms of (query_weight × document_weight), often TF-IDF. Sort documents by score and return top-*k*. Can be implemented term-at-a-time (accumulators) or document-at-a-time.

- **(c) Word positions and precomputed scores (4 marks):**
  - **Word positions:** Storing positions allows **proximity** and **phrase** queries: e.g. “tropical fish” or “tropical within 5 words of fish.” We align postings by doc and check position differences. Benefit: supports richer query features (phrases, proximity) and can improve relevance.
  - **Precomputed scores:** Storing per-document scores (or weights) in the index **speeds up** query-time scoring (less computation). **Drawback:** the scoring function is fixed at build time; changing the ranking formula (e.g. new weights or features) requires rebuilding the index, so **flexibility** is reduced.

**Explanation:** The question ties together index structure, construction, Boolean processing, and ranked retrieval from the notes. Full marks need clear description of dictionary/postings, build steps, AND via intersection, scoring idea, and trade-offs for positions and precomputed scores.

---

### Essay 5 [13 marks – HARD]

**Question:** (a) Define **precision** and **recall** and explain why they are both important in evaluating an IR system. (b) Explain the notions of **topical relevance** and **user relevance**, and why retrieval models often focus on topical relevance. (c) State the **Probability Ranking Principle (PRP)** and discuss how it relates to the goal of maximising effectiveness. (d) Briefly explain one way in which **relevance feedback** can improve results and where it fits in the search engine architecture.

**Model answer and marking guide:**

- **(a) Precision and recall (3 marks):**
  - **Precision** = (relevant retrieved) / (retrieved). Measures: of what we returned, how much was good. High precision means few non-relevant documents in the result list.
  - **Recall** = (relevant retrieved) / (relevant in collection). Measures: of all relevant documents, how much we got. High recall means we miss few relevant documents.
  - **Why both:** Improving one can hurt the other (e.g. returning everything boosts recall but kills precision). A system should balance them; the right balance depends on the application (e.g. legal discovery may emphasise recall; web search often emphasises precision at top ranks).

- **(b) Topical vs user relevance (3 marks):**
  - **Topical relevance:** Document is on the **same topic** as the query (subject match).
  - **User relevance:** The user would **actually find the document valuable** given context: novelty, language, audience, recency, etc.
  - **Why models focus on topical:** Topical relevance is easier to approximate from text (e.g. term overlap, TF-IDF, language models). User relevance depends on many factors that are hard to observe or model. So retrieval models typically model topical relevance, and ranking can add quality/context features (e.g. freshness, authority) to better approximate user relevance.

- **(c) PRP and effectiveness (4 marks):**
  - **PRP (Probability Ranking Principle):** A system should rank documents in **decreasing order of probability of relevance** to the user who submitted the request, where probabilities are estimated as well as possible from available data. Under this ordering, **overall effectiveness** is the best achievable given the data.
  - **Relation to effectiveness:** If we could know true relevance probabilities, following the PRP would maximise expected effectiveness (e.g. for binary relevance, ranking relevant docs first maximises precision at any cutoff and improves user experience). The challenge is **estimating** these probabilities; different retrieval models (Boolean, vector space, probabilistic) are different ways of approximating or encoding relevance.

- **(d) Relevance feedback and architecture (3 marks):**
  - **Idea:** Use the user’s relevance judgments (e.g. which retrieved documents are relevant) to **refine the query**: add terms from relevant documents, reweight terms, or remove terms from non-relevant documents. The refined query is then used to retrieve again (or to re-rank).
  - **Where it fits:** Relevance feedback is part of the **query transformation** (or user interaction) component. It happens **after** an initial ranking is shown and the user provides feedback; that feedback drives query expansion/reweighting for a follow-up retrieval. It addresses vocabulary mismatch and poor initial query formulation.

**Explanation:** This essay spans evaluation (precision/recall), relevance (topical vs user), the PRP, and relevance feedback as in the notes. Full marks require precise definitions and a clear link to effectiveness and architecture.

---

## Summary of mark allocation

| Question | Level  | Marks |
|----------|--------|-------|
| Essay 1  | Easy   | 10    |
| Essay 2  | Medium | 8     |
| Essay 3  | Medium | 7     |
| Essay 4  | Hard   | 12    |
| Essay 5  | Hard   | 13    |
| **Total**|        | **50**|

- Easy: 10/50 = 20%  
- Medium: 15/50 = 30%  
- Hard: 25/50 = 50%

---

# Set 2 — Essay Questions (50 marks total)

**Distribution:** 10 marks Easy (20%) | 15 marks Medium (30%) | 25 marks Hard (50%). Several questions are calculation-based with detailed step-by-step solutions.

---

## EASY (Set 2) — 10 marks

### Essay 6 [10 marks – EASY]

**Question:** (a) Define **precision** and **recall** with their formulas. (b) A system retrieves 20 documents for a query; 12 of them are relevant. There are 30 relevant documents in the collection. Compute precision and recall. (c) Why do we need both metrics?

**Model answer and marking guide:**

- **(a) Definitions (3 marks):**
  - **Precision** = (number of relevant documents retrieved) / (number of documents retrieved). Answers: “Of what we returned, how much was good?”
  - **Recall** = (number of relevant documents retrieved) / (number of relevant documents in the collection). Answers: “Of all that was good, how much did we get?”

- **(b) Calculation (4 marks):**
  - Relevant retrieved = 12, retrieved = 20, relevant in collection = 30.
  - **Precision** = 12/20 = **0.6** (60%).
  - **Recall** = 12/30 = **0.4** (40%).

- **(c) Why both (3 marks):** A system can have high precision by returning very few documents (e.g. only one, if that one is relevant) but then recall is low. Or it can have high recall by returning almost everything, but then precision drops. We need both to balance “quality of the list” (precision) and “coverage of the relevant set” (recall). The right balance depends on the application (e.g. web search often cares more about top-rank precision; legal discovery may care more about recall).

---

## MEDIUM (Set 2) — 15 marks

### Essay 7 [8 marks – MEDIUM] (Calculation-based)

**Question:** (a) State **Heaps’ law** and define every variable. (b) For a corpus with *k* = 50 and β = 0.5, compute the predicted vocabulary size when the corpus has 9,000,000 word tokens. Show each step. (c) If the corpus doubles to 18,000,000 tokens, what is the new predicted vocabulary? By what factor did vocabulary grow? (d) Give one implication of Heaps’ law for index design.

**Model answer and marking guide:**

- **(a) Heaps’ law (2 marks):** *v* = *k*·*n*^β. **Variables:** *v* = vocabulary size (number of unique words); *n* = total number of word tokens in the corpus; *k* and β are constants that depend on the collection (typically *k* in 10–100, β ≈ 0.5).

- **(b) Step-by-step for *n* = 9,000,000 (3 marks):**
  - *n*^β = *n*^0.5 = √9,000,000 = 3000 (since 3000² = 9,000,000).
  - *v* = *k*·*n*^0.5 = 50 × 3000 = **150,000** unique words.

- **(c) Doubling *n* (2 marks):**
  - New *n* = 18,000,000. *n*^0.5 = √18,000,000 ≈ 4242.6.
  - New *v* = 50 × 4242.6 ≈ **212,130**.
  - Factor: 212130/150000 ≈ **1.41** (i.e. √2). So when *n* doubles, *v* increases by √2 because *v* ∝ *n*^0.5.

- **(d) Implication (1 mark):** Dictionary size grows with corpus size but sublinearly; we can plan storage and scaling. On the web, vocabulary keeps growing (new words, typos, names), so index design must support large and growing dictionaries.

---

### Essay 8 [7 marks – MEDIUM] (Calculation-based)

**Question:** (a) Write the **cosine similarity** formula between query vector Q and document vector D. (b) For Q = (2, 2, 1) and D = (3, 0, 2), compute the dot product Q·D, the lengths |Q| and |D|, and the cosine similarity. Show every arithmetic step. (c) Why do we normalise by |Q| and |D|?

**Model answer and marking guide:**

- **(a) Formula (1 mark):** Cosine similarity = (Q·D) / (|Q|·|D|), where Q·D is the dot product Σᵢ *qᵢ*·*dᵢ* and |Q| = √(Σᵢ *qᵢ*²).

- **(b) Step-by-step (4 marks):**
  - **Dot product:** Q·D = 2×3 + 2×0 + 1×2 = 6 + 0 + 2 = **8**.
  - **|Q|** = √(2²+2²+1²) = √(4+4+1) = √9 = **3**.
  - **|D|** = √(3²+0²+2²) = √(9+0+4) = √13 ≈ **3.606**.
  - **Cosine** = 8/(3×√13) = 8/√117 ≈ 8/10.82 ≈ **0.739**.

- **(c) Why normalise (2 marks):** Without normalisation, long documents (with more terms and larger vector length) would tend to get higher dot products and dominate. Dividing by |Q| and |D| makes the score depend on the **direction** (angle) of the vectors rather than length, so we compare how similar the document is to the query in terms of relative term weights, not sheer size.

---

## HARD (Set 2) — 25 marks

### Essay 9 [12 marks – HARD] (Calculation-based)

**Question:** Consider a collection of *N* = 25,000 documents. For the query “information retrieval” we have: “information” appears in 5,000 documents; “retrieval” in 2,000 documents; both appear in 800 documents. (a) Under the **independence assumption**, what is the expected number of documents containing both terms? Show the formula and every step. (b) The actual co-occurrence is 800. Compare with your answer in (a) and explain the difference. (c) Using the **current result set** method: suppose we process 10% of the documents that contain “retrieval” and find 200 documents that contain both terms. Estimate the total number of documents containing both terms. Show the formula and steps. (d) Which estimate (independence or current result set) is more reliable here and why?

**Model answer and marking guide:**

- **(a) Independence estimate (4 marks):**
  - Under independence: *P*(“info” ∩ “retrieval”) = *P*(“info”)·*P*(“retrieval”) = (*f_info*/*N*)·(*f_ret*/*N*).
  - Expected count = *N* · *P*(both) = *N* · (*f_info*/*N*)·(*f_ret*/*N*) = (*f_info*·*f_ret*)/*N*.
  - Substitution: (5000 × 2000) / 25000 = 10,000,000 / 25,000 = **400** documents.
  - So the independence-based expected count is **400**.

- **(b) Comparison and explanation (2 marks):** Actual = 800, independence estimate = 400. So actual co-occurrence is **twice** the independence estimate. The words “information” and “retrieval” are **semantically related** and tend to appear together, so *P*(both) > *P*(“info”)·*P*(“retrieval”). Independence **underestimates** for related terms.

- **(c) Current result set estimate (3 marks):**
  - Formula: **Estimated total = *C* / *s***, where *C* = number of documents found so far that contain all query terms, *s* = proportion of the rarest-term postings processed.
  - Here *C* = 200, *s* = 0.10.
  - Estimate = 200 / 0.10 = **2,000** documents.
  - (Note: This estimates the number of docs containing both, under the assumption that we have processed 10% of docs containing “retrieval” and that matches are distributed uniformly. If the true count is 800, then in 10% we’d expect ~80, not 200—so the 200 might imply a higher total or a biased sample; the formula is still “estimate = C/s”.)

- **(d) Which is more reliable (3 marks):** The **current result set** method is often more reliable for this query because it does not assume independence; it uses the actual count *C* from the index and the known proportion *s* processed. The independence estimate is unreliable when terms are related (as here). The current result set method can be inaccurate if the sample (e.g. first 10% of postings) is not representative of the full set (e.g. if postings are ordered by doc ID and relevant docs are clustered). For “information retrieval,” current result set is typically preferred over independence.

---

### Essay 10 [13 marks – HARD] (Calculation-based)

**Question:** (a) Define **TF-IDF** weight: give the usual formulas for *tf*, *idf*, and the combined weight. (b) Collection: *N* = 10,000 documents. Term “search” has document frequency *df* = 400. In document D1 “search” appears 5 times; in D2 it appears 1 time. Use **tf** = 1+log(tf_raw) (natural log) and **idf** = log(*N*/*df*). Compute the TF-IDF weight for “search” in D1 and in D2. Show every step. (c) A query is “search engine.” “search” has the same idf as above; “engine” has *df* = 500. Query uses same tf-idf weighting with tf = 1+log(tf) for the single occurrence of each term. Compute the query weight for “search” and for “engine.” (d) For document D1 above, if “engine” appears 2 times (with same idf as in (c)), compute the score of D1 for this query as the sum of (query weight × document weight) for each term. Show the full calculation.

**Model answer and marking guide:**

- **(a) Formulas (2 marks):**
  - *tf* = 1 + log(tf_raw) (or similar normalised form); *idf* = log(*N*/*df*); **tf-idf** = *tf* × *idf*.
  - (Common variant: *tf_idf* = (1+log(tf_raw))·log(*N*/*df*).)

- **(b) TF-IDF for “search” in D1 and D2 (4 marks):**
  - **idf(“search”)** = log(10000/400) = log(25) ≈ **3.22** (natural log).
  - **D1:** tf_raw = 5 → tf = 1+log(5) ≈ 1+1.609 = **2.609**. tf-idf = 2.609 × 3.22 ≈ **8.40**.
  - **D2:** tf_raw = 1 → tf = 1+log(1) = 1+0 = **1**. tf-idf = 1 × 3.22 = **3.22**.

- **(c) Query weights (2 marks):**
  - “search”: one occurrence → tf = 1, idf = 3.22 → query weight ≈ **3.22**.
  - “engine”: idf = log(10000/500) = log(20) ≈ **3.00**. tf = 1 → query weight ≈ **3.00**.

- **(d) Score for D1 (5 marks):**
  - D1: “search” weight ≈ 8.40 (from (b)), “engine” weight: tf_raw = 2 → tf = 1+log(2) ≈ 1.693, idf = 3.00 → “engine” weight ≈ 1.693×3.00 ≈ **5.08**.
  - Score(D1) = (query weight “search” × doc weight “search”) + (query weight “engine” × doc weight “engine”) = 3.22×8.40 + 3.00×5.08 ≈ 27.05 + 15.24 ≈ **42.29**.
  - (Full step-by-step: 3.22×8.40 = 27.048; 3.00×5.08 = 15.24; total ≈ 42.29.)

---

## Set 2 summary of mark allocation

| Question  | Level  | Marks |
|-----------|--------|-------|
| Essay 6   | Easy   | 10    |
| Essay 7   | Medium | 8     |
| Essay 8   | Medium | 7     |
| Essay 9   | Hard   | 12    |
| Essay 10  | Hard   | 13    |
| **Total** |        | **50**|

- Easy: 10/50 = 20%  
- Medium: 15/50 = 30%  
- Hard: 25/50 = 50%

---

# Set 3 — Essay Questions: Missing Topics (50 marks total)

**Distribution:** 10 marks Easy (20%) | 15 marks Medium (30%) | 25 marks Hard (50%). Topics: Crawls & Feeds, Evaluation, Filtering & Recommendation.

---

## EASY (Set 3) — 10 marks

### Essay 11 [10 marks – EASY]

**Question:** (a) What are the three main components of a Cranfield-style test collection for evaluating an IR system? (b) Why do we need both precision and recall (or metrics that focus on the top, like P@k or MAP)? (c) Give one example of an **offline** evaluation metric and one example of an **online** evaluation metric.

**Model answer and marking guide:**

- **(a) Test collection (4 marks):** (1) **Document collection** — a fixed set of documents. (2) **Query set (topics)** — a set of test queries. (3) **Relevance judgments** — for (query, document) pairs, labels indicating relevance (binary or graded). These three together allow us to compute precision, recall, MAP, NDCG, etc.

- **(b) Why both / top-focused metrics (3 marks):** Precision alone can be maximised by returning very few documents; recall alone by returning almost everything. We need to balance quality of the list and coverage of relevant docs. For web search, users care most about the **top** results, so metrics like **P@k**, **MAP**, and **NDCG** focus on ranked quality at the top.

- **(c) Offline vs online (3 marks):** **Offline:** e.g. Precision, Recall, MAP, NDCG, P@10 — computed on a static test collection with relevance judgments. **Online:** e.g. Click-through rate (CTR), dwell time, session success rate, A/B test outcome — based on real user behaviour in production or an experiment.

---

## MEDIUM (Set 3) — 15 marks

### Essay 12 [8 marks – MEDIUM] (Calculation-based)

**Question:** (a) Define **Precision at k (P@k)**, **Average Precision (AP)**, and **Mean Average Precision (MAP)** with their formulas. (b) For a single query with 3 relevant documents, the system returns them at ranks 1, 2, and 5. Compute P@1, P@2, P@5 and then Average Precision. Show every step. (c) What is MAP if we have only this one query?

**Model answer and marking guide:**

- **(a) Definitions (3 marks):** P@k = (relevant in top k) / k. AP = (1 / number of relevant docs) × Σ (P@k at each rank k where the document is relevant). MAP = (1/Q) Σ_q AP(q).

- **(b) Calculation (4 marks):** P@1 = 1/1 = **1**. P@2 = 2/2 = **1**. P@5 = 3/5 = **0.6**. AP = (1/3)[1 + 1 + 0.6] = 2.6/3 ≈ **0.867**.

- **(c) MAP (1 mark):** If this is the only query, MAP = AP ≈ **0.867**.

---

### Essay 13 [7 marks – MEDIUM]

**Question:** (a) Describe the main components of a **web crawler** architecture (at least four). (b) What is the purpose of **duplicate** and **near-duplicate** detection? (c) Name two techniques for near-duplicate detection and briefly explain how each works.

**Model answer and marking guide:**

- **(a) Crawler components (3 marks):** (1) URL frontier — queue(s) of URLs to fetch. (2) Fetch module — retrieves pages (HTTP). (3) Parser — extracts links and content. (4) Duplicate / near-duplicate detection. (5) Document store. (Any four with brief roles.)

- **(b) Purpose (2 marks):** Duplicate detection avoids wasting resources on identical pages. Near-duplicate detection identifies almost-identical pages (e.g. same article with different ads), saving storage and improving quality.

- **(c) Two techniques (2 marks):** (1) **Shingles:** Document as set of overlapping word sequences; compare with Jaccard similarity; high Jaccard ⇒ near-duplicate. (2) **SimHash:** Document to bit fingerprint; compare with Hamming distance; small distance ⇒ near-duplicate.

---

## HARD (Set 3) — 25 marks

### Essay 14 [12 marks – HARD] (Calculation-based)

**Question:** (a) Define **DCG** and **NDCG** with formulas. Explain why we use a discount and why we normalise by IDCG. (b) For positions 1–5, relevance grades are [3, 2, 0, 1, 2]. Compute DCG_5 using DCG_p = Σ_{i=1..p} rel_i / log₂(i+1). (c) Compute IDCG_5 (ideal order: sort by relevance descending) and NDCG_5. Show all steps.

**Model answer and marking guide:**

- **(a) Definitions (4 marks):** DCG_p = Σ_{i=1..p} rel_i / log₂(i+1). Discount: lower ranks contribute less (users care about top). IDCG_p = DCG on ideal ranking (best first). NDCG_p = DCG_p / IDCG_p. Normalise so score in [0,1] and comparable across queries.

- **(b) DCG_5 (4 marks):** DCG_5 = 3/1 + 2/1.585 + 0 + 1/2.322 + 2/2.585 ≈ 3 + 1.26 + 0 + 0.43 + 0.77 ≈ **5.46**.

- **(c) IDCG_5 and NDCG_5 (4 marks):** Ideal order [3,2,2,1,0]. IDCG_5 ≈ 3 + 1.26 + 1 + 0.43 + 0 ≈ **5.69**. NDCG_5 = 5.46/5.69 ≈ **0.96**.

---

### Essay 15 [13 marks – HARD]

**Question:** (a) Explain the difference between **document filtering** and **ad-hoc retrieval** (what is fixed vs what changes). (b) Explain **content-based** and **collaborative filtering** for recommendations: main idea, one advantage, one disadvantage of each. (c) What is the **cold start** problem? How do content-based and collaborative each handle cold start for new users and new items? (d) Why might a **hybrid** recommendation system be used?

**Model answer and marking guide:**

- **(a) Filtering vs ad-hoc (3 marks):** Ad-hoc: collection **fixed**, query **changes**. Filtering: document stream **changes**, information need (profile) **stable**.

- **(b) Content-based vs collaborative (4 marks):** Content-based: recommend by **item features** similar to what user liked; advantage: no other users needed, new items OK if features exist; disadvantage: overspecialisation. Collaborative: recommend by **other users’** behaviour; advantage: discovers unexpected preferences; disadvantage: cold start, sparsity.

- **(c) Cold start (3 marks):** Cold start = little/no data for user or item. Collaborative: new user and new item both hard. Content-based: new item easier (use features); new user still hard (no profile). Hybrid can use content for cold start.

- **(d) Hybrid (3 marks):** Combines both to reduce cold start, increase diversity, and improve overall quality by using both content and behaviour signals.

---

## Set 3 summary of mark allocation

| Question  | Level  | Marks |
|-----------|--------|-------|
| Essay 11  | Easy   | 10    |
| Essay 12  | Medium | 8     |
| Essay 13  | Medium | 7     |
| Essay 14  | Hard   | 12    |
| Essay 15  | Hard   | 13    |
| **Total** |        | **50**|

- Easy: 10/50 = 20%  
- Medium: 15/50 = 30%  
- Hard: 25/50 = 50%

# DSC608 Information Retrieval — Short and Medium Structural Questions (30)

**Distribution:** 6 Easy (20%) | 9 Medium (30%) | 15 Hard (50%)

---

## EASY (6 questions)

### 1. [EASY] Define *information need* in the context of IR.

**Answer:** Information need is the topic or desire that leads a user to seek information—i.e. what they want to find out. It is distinct from the *query*, which is what they actually type or submit to the system.

---

### 2. [EASY] Name the two main parts of an inverted index.

**Answer:** (1) **Dictionary** (vocabulary/lexicon): the list of index terms. (2) **Postings**: for each term, a list of document IDs (and optionally counts or positions) indicating which documents contain that term.

---

### 3. [EASY] What is *precision* in IR evaluation?

**Answer:** Precision is the fraction of the **retrieved** documents that are relevant to the information need. So it answers: “Of what we returned, how much was good?”

---

### 4. [EASY] What is *recall* in IR evaluation?

**Answer:** Recall is the fraction of **all relevant documents in the collection** that were retrieved. So it answers: “Of all that was good, how much did we get?”

---

### 5. [EASY] Give one example of *structured* data and one of *unstructured* data.

**Answer:** Structured: e.g. relational database (account number, balance). Unstructured: e.g. email body, web page text, social media post. (Other valid examples acceptable.)

---

### 6. [EASY] What are the two possible outcomes of a Boolean retrieval query?

**Answer:** TRUE or FALSE for each document—i.e. the document either matches the Boolean expression or it does not. There is no ranking or score.

---

## MEDIUM (9 questions)

### 7. [MEDIUM] State Zipf’s law and give one implication for IR.

**Answer:** Zipf’s law: the frequency of a word is (approximately) inversely proportional to its rank when words are ordered by decreasing frequency. Implication: few words are very frequent (e.g. function words), many words are rare; this motivates stopword removal and affects term weighting (e.g. IDF for rare vs common terms).

---

### 8. [MEDIUM] State Heaps’ law. What do *v*, *n*, *k*, and β represent?

**Answer:** Heaps’ law: *v* = *k*·*n*^β. *v* = vocabulary size (number of unique words), *n* = total number of word tokens in the corpus, *k* and β are corpus-dependent constants (often β ≈ 0.5). It models how vocabulary grows as corpus size increases.

---

### 9. [MEDIUM] List three steps in building an inverted index from raw documents.

**Answer:** (1) Collect and acquire documents. (2) Tokenize and do linguistic preprocessing (e.g. normalise, stop, stem) to get index terms. (3) Build the index: sort by term, merge same-term occurrences, and form dictionary + postings (sorted by document ID).

---

### 10. [MEDIUM] What is the main advantage of the vector space model over Boolean retrieval?

**Answer:** The vector space model produces a **ranked** list of documents by similarity (e.g. cosine) to the query, so more relevant documents can be ranked higher. Boolean retrieval only returns a set with no notion of “more relevant.”

---

### 11. [MEDIUM] What do *tf* and *idf* stand for, and what does each capture?

**Answer:** *tf* = term frequency: how often the term appears in the document (or query); reflects importance in that document. *idf* = inverse document frequency: log(*N*/*df*) where *df* is the number of documents containing the term; reflects how discriminating the term is in the collection.

---

### 12. [MEDIUM] Describe the role of the *ranking component* in a search engine.

**Answer:** The ranking component takes the transformed query and, using the index and a retrieval model, computes a score for documents and produces a **ranked list**. It must be both effective (good results) and efficient (fast, high throughput).

---

### 13. [MEDIUM] What is *relevance feedback* and where is it used?

**Answer:** Relevance feedback is using the user’s relevance judgments (e.g. which results are relevant) to refine the query—e.g. by adding terms from relevant documents or reweighting. It is used in the **query transformation** part of the user interaction component to improve subsequent retrievals.

---

### 14. [MEDIUM] Why is the term–document incidence matrix impractical for very large collections?

**Answer:** The matrix has one row per term and one column per document, so it is huge (e.g. 500K × 1M). It is also very **sparse** (most entries 0). Storing it explicitly wastes memory; it is more efficient to store only the 1s (e.g. in an inverted index).

---

### 15. [MEDIUM] What is *anchor text* in web search and why is it useful?

**Answer:** Anchor text is the clickable text of a link pointing to a page (e.g. “Example Website” in \<a href="…">Example Website\</a>). It often describes the destination page and is short and query-like; using it as an additional “field” for the destination page can significantly improve retrieval effectiveness.

---

## HARD (15 questions)

### 16. [HARD] Explain the difference between *ad-hoc* retrieval and *filtering* in terms of what is stable and what changes.

**Answer:** In **ad-hoc** retrieval, the document collection is relatively stable and the **query** (information need) changes each time. In **filtering**, the document stream **changes** (e.g. new news) and the **information need** is stable, often represented as a user profile. So ad-hoc = fixed collection, varying query; filtering = varying collection, fixed need.

---

### 17. [HARD] When estimating result set size using the independence assumption *P(a∩b∩c) = P(a)P(b)P(c)*, why do we often get poor estimates? Give a concrete reason.

**Answer:** Words in documents are **not independent**; they co-occur (e.g. “fish” and “aquarium”). So the true *P(a∩b∩c)* is higher than the product of marginals. Using independence underestimates co-occurrence and gives poor result set size estimates, especially for multi-word queries.

---

### 18. [HARD] How can we estimate collection size *N* using two (approximately) independent words *a* and *b* and their document frequencies? Write the formula and state the assumption.

**Answer:** If *a* and *b* occur independently in documents, then *P(a∩b)* = *P(a)P(b)*, so *f_{a∩b}/N* = (*f_a/N*)(*f_b/N*), hence *N* = (*f_a*·*f_b*)/*f_{a∩b}*. The assumption is that the two words are (roughly) independent; we choose word pairs that are not strongly related (e.g. “tropical” and “lincoln”) to approximate this.

---

### 19. [HARD] What is the *vocabulary mismatch* problem, and how do retrieval models try to address it?

**Answer:** The same concept can be expressed with different words (e.g. “pipeline leak” vs “pipeline rupture”), so exact string match misses relevant documents. Retrieval models address it by: (1) text normalisation (stemming, stopping), (2) ranking by similarity or probability rather than exact match, (3) query expansion and relevance feedback, (4) using statistical properties of terms (e.g. TF-IDF, co-occurrence).

---

### 20. [HARD] In the abstract ranking model, what are *topical* features vs *non-topical* (quality) features? Give one example of each.

**Answer:** **Topical** features measure how much the document is *about* a subject (e.g. presence or weight of “tropical,” “fish”). **Non-topical** (quality) features do not directly represent topic, e.g. number of inlinks, last-update time. Both can be combined in the ranking function; non-topical features help prefer authoritative or fresh pages.

---

### 21. [HARD] Explain *term-at-a-time* vs *document-at-a-time* scoring in one sentence each.

**Answer:** **Term-at-a-time:** For each query term in turn, fetch its postings list and add that term’s contribution to the score of each document in the list (using accumulators). **Document-at-a-time:** Traverse the postings of all query terms in sync (e.g. by doc ID); for each document seen, compute its full score at once. Both are used in practice with different trade-offs and optimisations.

---

### 22. [HARD] Why might a search engine store *precomputed* scores in the inverted list? What is the main drawback?

**Answer:** Precomputed scores (e.g. per-term document weights) move scoring work to **indexing time**, so at query time we only combine precomputed values—faster. **Drawback:** the scoring formula is fixed at index build time; we cannot change the ranking function without rebuilding the index.

---

### 23. [HARD] What is the *Probability Ranking Principle* (PRP)? Does it tell us how to estimate probability of relevance?

**Answer:** The PRP states that to maximise effectiveness, the system should rank documents in **decreasing order of probability of relevance** to the user who submitted the request, where probabilities are estimated from available data. It **does not** specify how to estimate these probabilities; that is left to the retrieval model (e.g. probabilistic or classifier-based).

---

### 24. [HARD] In the vector space model, why do we often use 1+log(tf) instead of raw term count for the *tf* component?

**Answer:** Raw *tf* gives too much weight to documents with many repetitions of a term; a few terms can dominate. Using 1+log(tf) **subdues** the effect of very high frequencies so that going from 1 to 2 occurrences matters more than going from 100 to 101. This improves effectiveness in many retrieval experiments.

---

### 25. [HARD] Give two advantages and two disadvantages of Boolean retrieval.

**Answer:** **Advantages:** (1) Results are predictable and easy to explain; (2) many document features (e.g. metadata, date) can be included in the query; (3) processing can be efficient (many documents eliminated). **Disadvantages:** (1) Effectiveness depends heavily on the user’s ability to formulate queries; (2) no ranking—all matching documents are equivalent; (3) NOT often removes relevant documents; (4) complex queries are hard to write and may over-narrow (e.g. too many ANDs yield no results).

---

### 26. [HARD] What are *safe* and *unsafe* optimisations in ranking? Why might one use an unsafe optimisation?

**Answer:** **Safe** optimisations guarantee that computed scores (and hence ranking) are the same as without the optimisation. **Unsafe** optimisations do not guarantee this (e.g. approximate scores, early termination). One might use unsafe optimisations when they significantly **reduce response time** or resource use and the loss in effectiveness is acceptable or negligible in practice.

---

### 27. [HARD] How does an inverted index with *word positions* support phrase queries? Outline the idea.

**Answer:** Each posting stores (doc ID and) a list of positions where the term appears. For a phrase like “tropical fish,” we get postings for “tropical” and “fish,” then for each document that has both, we check if any “tropical” position is immediately (or within *k*) before a “fish” position. Only documents with such a proximity are returned for the phrase.

---

### 28. [HARD] What is *topical relevance* vs *user relevance*? Give an example where a document is topically relevant but may not be user-relevant.

**Answer:** **Topical relevance:** the document is on the same topic as the query. **User relevance:** the user would actually find the document valuable (considering novelty, language, audience, recency, etc.). Example: a list of all U.S. presidents is topically relevant to “Abraham Lincoln” but may not be user-relevant if the user wanted detailed biographical information about Lincoln.

---

### 29. [HARD] In PageRank, what are *B_u* and *L_v* in the formula *PR(u)* = (1−*d*)/*N* + *d* Σ_{v∈B_u} *PR(v)*/*L_v*?

**Answer:** *B_u* is the **set of pages that link to *u*** (inlinks). *L_v* is the **number of outgoing links** from page *v* (each link counted once). So *PR(v)/L_v* is the share of *v*’s PageRank passed to *u* along one link; *d* is the damping factor and (1−*d*)/*N* is the random-jump probability.

---

### 30. [HARD] Why is it important that tokenization (and stopping, stemming) applied to the query match what was applied at indexing time?

**Answer:** The index is built from **normalised** document terms (after tokenization, stopping, stemming). If the query is not processed the **same way**, query terms will not match the dictionary (e.g. “running” not stemmed won’t match “run” in the index). So we must apply the same text transformation to the query to ensure correct lookup and scoring.

---

# Set 2 — Short and Structural Questions (with numerical / step-by-step)

**Distribution:** 6 Easy | 9 Medium | 15 Hard (same as Set 1). Many items include calculations with detailed solutions.

---

## EASY (Set 2)

### 31. [EASY] For a query, a system retrieves 12 documents. Of these, 9 are relevant. There are 18 relevant documents in the collection. Compute precision and recall.

**Answer (step-by-step):**
- **Precision** = (relevant retrieved) / (retrieved) = 9/12 = **0.75** (or 75%).
- **Recall** = (relevant retrieved) / (relevant in collection) = 9/18 = **0.5** (or 50%).

---

### 32. [EASY] Write the formula for F1 (F-measure) in terms of precision *P* and recall *R*. If *P* = 0.8 and *R* = 0.2, compute F1.

**Answer (step-by-step):**
- **Formula:** F1 = 2·*P*·*R*/(*P*+*R*) (harmonic mean of P and R).
- **Substitute:** F1 = 2 × 0.8 × 0.2 / (0.8 + 0.2) = 0.32 / 1.0 = **0.32**.

---

### 33. [EASY] In Zipf’s law *P(r)* = *c*/*r* with *c* = 0.1, what is the probability of the word at rank 5?

**Answer (step-by-step):**
- *P*(5) = *c*/*r* = 0.1/5 = **0.02** (2% of all word occurrences).

---

### 34. [EASY] A corpus has 1,000,000 word tokens. Heaps’ law gives *v* = *k*·*n*^β. If *k* = 44 and β = 0.5, what is the predicted vocabulary size *v*?

**Answer (step-by-step):**
- *n* = 1,000,000, so *n*^β = *n*^0.5 = √1,000,000 = 1,000.
- *v* = *k*·*n*^β = 44 × 1,000 = **44,000** unique words.

---

### 35. [EASY] Compute the dot product of query Q = (2, 1, 0) and document D = (1, 0, 3).

**Answer (step-by-step):**
- Q·D = *q*₁*d*₁ + *q*₂*d*₂ + *q*₃*d*₃ = 2×1 + 1×0 + 0×3 = 2 + 0 + 0 = **2**.

---

### 36. [EASY] In a collection of *N* = 10,000 documents, a term appears in 200 documents. Compute IDF using idf = log(*N*/*df*). Use natural log.

**Answer (step-by-step):**
- *df* = 200, *N* = 10,000.
- idf = log(*N*/*df*) = log(10000/200) = log(50) ≈ **3.91** (ln) or log₁₀(50) ≈ 1.70.

---

## MEDIUM (Set 2)

### 37. [MEDIUM] A system returns 15 documents; 10 are relevant. There are 25 relevant documents in the collection. (a) Find precision and recall. (b) Find F1.

**Answer (step-by-step):**
- **(a)**  
  - Precision *P* = (relevant retrieved)/(retrieved) = 10/15 = **2/3 ≈ 0.667**.  
  - Recall *R* = (relevant retrieved)/(relevant in collection) = 10/25 = **2/5 = 0.4**.  
- **(b)**  
  - F1 = 2·*P*·*R*/(*P*+*R*) = 2·(10/15)·(10/25) / ((10/15)+(10/25)) = (200/375) / ((2/3)+(2/5)) = (8/15) / (10/15+6/15) = (8/15)/(16/15) = **8/16 = 0.5**.

---

### 38. [MEDIUM] Collection size *N* = 50,000. Word *a* appears in 2,000 documents, word *b* in 3,000 documents. Under the independence assumption, what is the expected number of documents containing both *a* and *b*? Show steps.

**Answer (step-by-step):**
- Under independence: *P(a∩b)* = *P(a)*·*P(b)* = (*f_a*/*N*)·(*f_b*/*N*) = (2000/50000)·(3000/50000).
- Expected count = *N* · *P(a∩b)* = *N* · (*f_a*/*N*)·(*f_b*/*N*) = (*f_a*·*f_b*)/*N*.
- So count = (2000 × 3000) / 50000 = 6,000,000 / 50,000 = **120** documents.

---

### 39. [MEDIUM] For a term that appears in 50 of 20,000 documents, compute idf = log(*N*/*df*). If the term appears 4 times in a document, compute tf = 1+log(tf_raw) (natural log) and then tf-idf weight for that document.

**Answer (step-by-step):**
- *N* = 20,000, *df* = 50.  
  idf = log(20000/50) = log(400) ≈ **6.00** (ln).  
- *tf_raw* = 4.  
  tf = 1+log(4) ≈ 1+1.386 ≈ **2.386**.  
- tf-idf = tf × idf ≈ 2.386 × 6.00 ≈ **14.32**.

---

### 40. [MEDIUM] Query Q = (3, 4, 0), Document D = (2, 2, 1). Compute (a) dot product Q·D, (b) |Q| and |D|, (c) cosine similarity.

**Answer (step-by-step):**
- **(a)** Q·D = 3×2 + 4×2 + 0×1 = 6+8+0 = **14**.  
- **(b)** |Q| = √(9+16+0) = √25 = **5**. |D| = √(4+4+1) = √9 = **3**.  
- **(c)** Cosine = (Q·D)/(|Q||D|) = 14/(5×3) = **14/15 ≈ 0.933**.

---

### 41. [MEDIUM] We want to estimate collection size *N*. Word “tropical” appears in 120,000 documents, “lincoln” in 770,000 documents, and both in 3,000 documents. Assuming approximate independence, estimate *N*. Show the formula and substitution.

**Answer (step-by-step):**
- Formula: *N* = (*f_a*·*f_b*)/*f_{a∩b}* (under *P(a∩b)* = *P(a)*·*P(b)*).  
- *f_tropical* = 120,000, *f_lincoln* = 770,000, *f_{tropical∩lincoln}* = 3,000.  
- *N* = (120,000 × 770,000) / 3,000 = 92,400,000,000 / 3,000 = **30,800,000** (about 30.8M documents).

---

### 42. [MEDIUM] After processing 25% of the documents that contain the rarest query term, the system has found 500 documents that contain all query terms. Estimate the total result set size. Show the formula.

**Answer (step-by-step):**
- Formula: **Estimated result size = *C* / *s***, where *C* = number of matching docs found so far, *s* = proportion of the “rarest-term” postings processed.  
- *C* = 500, *s* = 0.25.  
- Estimate = 500 / 0.25 = **2,000** documents.

---

### 43. [MEDIUM] Zipf’s law: *P(r)* = *c*/*r* with *c* = 0.1. (a) What is *P*(1)? (b) What is *P*(100)? (c) Verify that *r*·*P(r)* is constant.

**Answer (step-by-step):**
- **(a)** *P*(1) = 0.1/1 = **0.1**.  
- **(b)** *P*(100) = 0.1/100 = **0.001**.  
- **(c)** *r*·*P(r)* = *r*·(*c*/*r*) = *c* = 0.1 for any *r*. So the product is constant.

---

### 44. [MEDIUM] Heaps’ law *v* = *k*·*n*^β. For a corpus we have *k* = 60 and β = 0.45. Predict vocabulary size when *n* = 500,000 tokens. Show calculation.

**Answer (step-by-step):**
- *n*^β = 500,000^0.45. Using 500000^0.45 ≈ 369 (calculator: e^(0.45·ln(500000)) ≈ 369).  
- *v* = 60 × 369 ≈ **22,140** (or compute exactly: *v* = 60·500000^0.45).

---

### 45. [MEDIUM] Two documents D1 and D2 have cosine similarity to query Q of 0.7 and 0.3 respectively. Which is ranked higher? What does cosine measure?

**Answer:** D1 is ranked **higher** because 0.7 > 0.3; we rank by **decreasing** similarity. Cosine measures the angle between the two vectors (or equivalently, the similarity of their direction); it is length-normalised so document length does not dominate.

---

## HARD (Set 2)

### 46. [HARD] **Precision/Recall/F1 with contingency table.** For a query, the collection has 100 relevant documents. The system retrieves 40 documents, of which 20 are relevant. (a) Compute precision, recall, and F1. (b) If we retrieve the top 80 documents and 50 of them are relevant, what are P, R, and F1? Compare with (a).

**Answer (step-by-step):**
- **(a)**  
  - Retrieved = 40, relevant retrieved = 20, relevant in collection = 100.  
  - *P* = 20/40 = **0.5**. *R* = 20/100 = **0.2**.  
  - F1 = 2·0.5·0.2/(0.5+0.2) = 0.2/0.7 ≈ **0.286**.  
- **(b)**  
  - Retrieved = 80, relevant retrieved = 50.  
  - *P* = 50/80 = **0.625**. *R* = 50/100 = **0.5**.  
  - F1 = 2·0.625·0.5/1.125 = 0.625/1.125 ≈ **0.556**.  
- **Comparison:** Retrieving more (80 vs 40) increased recall (0.5 vs 0.2) and in this case also precision (0.625 vs 0.5), so F1 increased. In general, expanding the result list tends to increase recall and decrease precision; here the extra 40 docs included 30 more relevant, so both improved.

---

### 47. [HARD] **TF-IDF full calculation.** Collection: *N* = 5,000 documents. Term “retrieval” has *df* = 100. In document D1 it appears 6 times; in D2 it appears 2 times. Use tf = 1+log(tf_raw) (natural log) and idf = log(*N*/*df*). Compute tf-idf for “retrieval” in D1 and D2. Which document gets a higher weight and why?

**Answer (step-by-step):**
- idf = log(5000/100) = log(50) ≈ **3.91** (same for all docs).  
- **D1:** tf_raw = 6 → tf = 1+log(6) ≈ 1+1.79 = **2.79**. tf-idf = 2.79 × 3.91 ≈ **10.91**.  
- **D2:** tf_raw = 2 → tf = 1+log(2) ≈ 1+0.69 = **1.69**. tf-idf = 1.69 × 3.91 ≈ **6.61**.  
- **D1** gets the higher weight because the term appears more often in D1 (higher tf). Both use the same idf.

---

### 48. [HARD] **Cosine similarity from scratch.** Query Q = (1, 2, 2), D1 = (2, 1, 0), D2 = (1, 1, 1). Compute cosine similarity of Q with D1 and with D2. Which document ranks higher?

**Answer (step-by-step):**
- **|Q|** = √(1+4+4) = √9 = **3**.  
- **Q·D1** = 1×2 + 2×1 + 2×0 = 2+2+0 = **4**. **|D1|** = √(4+1+0) = √5.  
  sim(Q,D1) = 4/(3·√5) = 4/(3√5) ≈ **0.596**.  
- **Q·D2** = 1×1 + 2×1 + 2×1 = 1+2+2 = **5**. **|D2|** = √(1+1+1) = √3.  
  sim(Q,D2) = 5/(3·√3) = 5/(3√3) ≈ **0.962**.  
- **D2** ranks higher (0.962 > 0.596).

---

### 49. [HARD] **Result set size (independence vs actual).** Collection *N* = 100,000. For query “tropical fish aquarium”: *f_tropical* = 12,000, *f_fish* = 8,000, *f_aquarium* = 5,000. (a) Under full independence, estimate the number of documents containing all three terms. (b) If the actual count is 800, why might the independence estimate be wrong?

**Answer (step-by-step):**
- **(a)** Under independence, *P(a∩b∩c)* = *P(a)*·*P(b)*·*P(c)* = (*f_a*/*N*)·(*f_b*/*N*)·(*f_c*/*N*).  
  Expected count = *N* · (*f_a*/*N*)·(*f_b*/*N*)·(*f_c*/*N*) = (*f_a*·*f_b*·*f_c*)/*N*².  
  Count = (12000 × 8000 × 5000) / (100000)² = 480,000,000,000 / 10,000,000,000 = **48** documents.  
- **(b)** Actual 800 >> 48. The words “tropical,” “fish,” and “aquarium” **co-occur** (they are semantically related), so *P(a∩b∩c)* is much higher than the product of marginals. Independence **underestimates** result set size for related terms.

---

### 50. [HARD] **PageRank iteration.** Consider 3 pages A, B, C. Links: A→B, A→C, B→C, C→A. So B_u: B has {A}, C has {A,B}, A has {C}. L_v: L_A=2, L_B=1, L_C=1. Let *d* = 0.85, *N* = 3. (a) Write the PageRank equations. (b) Compute one iteration starting from PR(A)=PR(B)=PR(C)=1/3.

**Answer (step-by-step):**
- **(a)**  
  PR(A) = (1−*d*)/*N* + *d*·(PR(C)/*L_C*) = 0.15/3 + 0.85·PR(C)/1 = 0.05 + 0.85·PR(C).  
  PR(B) = 0.05 + 0.85·PR(A)/2.  
  PR(C) = 0.05 + 0.85·(PR(A)/2 + PR(B)/1).  
- **(b)** Initial: PR(A)=PR(B)=PR(C)=1/3 ≈ 0.333.  
  - PR(A) = 0.05 + 0.85×0.333 ≈ 0.333.  
  - PR(B) = 0.05 + 0.85×0.333/2 ≈ 0.192.  
  - PR(C) = 0.05 + 0.85×(0.333/2 + 0.333) = 0.05 + 0.85×0.5 ≈ 0.475.  
  After one iteration: PR(A)≈0.333, PR(B)≈0.192, PR(C)≈0.475. (Repeating would converge to the stationary distribution.)

---

### 51. [HARD] **Collection size estimation.** Words “apple” and “orange” have document frequencies 50,000 and 40,000 in a collection; they co-occur in 4,000 documents. (a) Estimate *N* using *N* = (*f_a*·*f_b*)/*f_{a∩b}*. (b) If the true *N* is 1,000,000, is the estimate reasonable? What does that suggest about independence?

**Answer (step-by-step):**
- **(a)** *N* = (50000 × 40000) / 4000 = 2,000,000,000 / 4000 = **500,000**.  
- **(b)** True *N* = 1,000,000, so our estimate (500,000) is **half** the true size. That suggests “apple” and “orange” **co-occur more** than independence would predict (e.g. fruit-related context), so *f_{a∩b}* is larger than *f_a*·*f_b*/*N*, leading to an **underestimate** of *N*. For a good *N* estimate we need word pairs that are roughly independent (e.g. unrelated words).

---

### 52. [HARD] **Heaps’ law and Zipf.** (a) Given *v* = *k*·*n*^β with *k* = 50, β = 0.5, find *v* when *n* = 4,000,000. (b) If we double *n* to 8,000,000, what is the new *v*? By what factor did *v* increase?

**Answer (step-by-step):**
- **(a)** *v* = 50·√4,000,000 = 50·2000 = **100,000**.  
- **(b)** New *v* = 50·√8,000,000 = 50·2828.4 ≈ **141,421**. Ratio = 141421/100000 ≈ **1.414** (i.e. √2). So when *n* doubles, *v* increases by factor √2 (because *n*^0.5 doubles when *n* quadruples; here *n* only doubled so *n*^0.5 multiplies by √2).

---

### 53. [HARD] **Boolean postings intersection.** Term “cat” has postings [1, 3, 5, 7, 9]; “dog” has postings [2, 3, 5, 8]. List the steps to compute the result of the query “cat AND dog” (intersection). Give the result list.

**Answer (step-by-step):**
- Use two pointers: one for “cat” list, one for “dog” list.  
- Compare 1 and 2: 1 < 2 → advance cat pointer.  
- Compare 3 and 2: 3 > 2 → advance dog pointer.  
- Compare 3 and 3: match → output 3, advance both.  
- Compare 5 and 5: match → output 5, advance both.  
- Compare 7 and 8: 7 < 8 → advance cat pointer.  
- Compare 9 and 8: 9 > 8 → advance dog pointer. One list exhausted → stop.  
- **Result:** [**3, 5**].

---

### 54. [HARD] **F1 and balance.** (a) If precision is 1.0 and recall is 0.2, compute F1. (b) What recall would we need (keeping P = 1) to get F1 = 0.5? Set 2·1·*R*/(1+*R*) = 0.5 and solve for *R*.

**Answer (step-by-step):**
- **(a)** F1 = 2·1·0.2/(1+0.2) = 0.4/1.2 ≈ **0.333**.  
- **(b)** 2*R*/(1+*R*) = 0.5 ⇒ 2*R* = 0.5(1+*R*) ⇒ 2*R* = 0.5 + 0.5*R* ⇒ 1.5*R* = 0.5 ⇒ *R* = **1/3 ≈ 0.333**. So we need recall 1/3 to get F1 = 0.5 when P = 1.

---

### 55. [HARD] **Combined: IDF and result set.** In a collection of 80,000 documents, term “python” appears in 1,600 documents, “programming” in 4,000, and both in 400. (a) Compute idf for “python” and for “programming” using idf = log(*N*/*df*). (b) Under independence, expected docs with both = (*f_a*·*f_b*)/*N*. Compute it. (c) Actual co-occurrence is 400. Is it above or below the independence estimate? Interpret.

**Answer (step-by-step):**
- **(a)** idf(“python”) = log(80000/1600) = log(50) ≈ 3.91. idf(“programming”) = log(80000/4000) = log(20) ≈ 3.00 (natural log).  
- **(b)** Expected = (1600×4000)/80000 = 6,400,000/80,000 = **80** documents.  
- **(c)** Actual = 400 > 80. So “python” and “programming” **co-occur more** than independence; they are related terms. Independence would **underestimate** the number of documents containing both.

---

# Set 3 — Missing Topics (Crawls, Evaluation, Filtering & Recommendation)

**Distribution:** 6 Easy | 9 Medium | 15 Hard. Includes numerical/calculation questions where applicable.

---

## EASY (Set 3)

### 56. [EASY] Name the three main components of a Cranfield-style test collection for IR evaluation.

**Answer:** (1) **Document collection** — a fixed set of documents. (2) **Query set (topics)** — a set of queries. (3) **Relevance judgments** — for (query, document) pairs, labels indicating whether the document is relevant (binary or graded).

---

### 57. [EASY] What is P@k? Give the formula.

**Answer:** **Precision at k**: the proportion of the top-k retrieved documents that are relevant. **Formula:** P@k = (number of relevant documents in the top k) / k.

---

### 58. [EASY] In one sentence, what is the difference between content-based and collaborative filtering for recommendations?

**Answer:** **Content-based** recommends items similar in **features** (e.g. text, genre) to what the user liked. **Collaborative** recommends items that **other users** with similar tastes liked, using user–item behaviour (e.g. ratings, clicks).

---

### 59. [EASY] List two main components of a web crawler architecture.

**Answer:** (1) **URL frontier** — queue of URLs to fetch. (2) **Fetch module** — retrieves pages (HTTP). (3) **Parser** — extracts links and content. (4) **Duplicate detection** — avoids re-fetching same or near-duplicate URLs. (Any two acceptable.)

---

### 60. [EASY] What does MAP stand for, and what is it the mean of?

**Answer:** **Mean Average Precision**. MAP is the **mean** of **Average Precision (AP)** scores over all queries in the test set. MAP = (1/Q) Σ_q AP(q).

---

### 61. [EASY] What is the purpose of "removing noise" in the crawler pipeline?

**Answer:** To strip **boilerplate** (ads, navigation, footers, scripts) from the page so that indexing and duplicate detection focus on **main content**. This improves relevance and makes hashing/fingerprinting more stable.

---

## MEDIUM (Set 3)

### 62. [MEDIUM] For a query, the system returns relevant documents at ranks 1, 2, and 5. There are 3 relevant documents in total. Compute Average Precision (AP). Use AP = (1/|rel|) Σ_{k: doc at k relevant} P@k.

**Answer (step-by-step):** P@1 = 1/1 = 1. P@2 = 2/2 = 1. P@5 = 3/5 = 0.6. AP = (1/3)[1 + 1 + 0.6] = (1/3)(2.6) ≈ **0.867**.

---

### 63. [MEDIUM] Define Mean Reciprocal Rank (MRR) and give the formula. When is it useful?

**Answer:** **MRR** = mean over queries of the **reciprocal** of the rank of the **first relevant** document. Formula: MRR = (1/Q) Σ_q 1/rank_q. **Useful for:** known-item or navigational queries where the user cares about finding the first correct result quickly.

---

### 64. [MEDIUM] What are shingles (e.g. 3-shingles) and how are they used in near-duplicate detection?

**Answer:** **Shingles** are overlapping sequences of w words. The document is represented as a **set of shingles**. Two documents are compared using **Jaccard similarity** (|A∩B|/|A∪B|); high Jaccard indicates near-duplicates. More robust than exact hash for small changes (e.g. ads, timestamps).

---

### 65. [MEDIUM] What is the difference between document filtering and ad-hoc retrieval in terms of what is fixed and what changes?

**Answer:** In **ad-hoc retrieval**, the **document collection** is relatively fixed and the **query** **changes** each time. In **document filtering**, the **document stream** **changes** and the **information need** is **stable** (user **profile**). So: ad-hoc = fixed collection, varying query; filtering = varying stream, fixed profile.

---

### 66. [MEDIUM] Write the formula for DCG at position p. What is the role of the denominator?

**Answer:** **DCG_p** = Σ_{i=1..p} rel_i / log₂(i+1). The **denominator** log₂(i+1) **discounts** lower ranks: relevant documents at the **top** contribute more. This reflects that users care more about top results.

---

### 67. [MEDIUM] What is NDCG and how is it obtained from DCG? Why normalise?

**Answer:** **NDCG_p** = DCG_p / IDCG_p, where **IDCG_p** is the DCG of the **ideal ranking** (documents sorted by relevance, best first). **Why normalise:** So that scores are in [0, 1] and **comparable across queries** that have different numbers of relevant documents.

---

### 68. [MEDIUM] What is the "conversion problem" in the context of crawls and feeds?

**Answer:** Documents come in **many formats** (HTML, PDF, Word, email, JSON). The **conversion problem** is turning each into a **normalised representation** (e.g. plain text + metadata) so that a single indexing pipeline can process them. This involves parsers or renderers per format.

---

### 69. [MEDIUM] Give two efficiency metrics commonly used when evaluating search engines.

**Answer:** (1) **Response time (latency)** — time from query submission to first/full result. (2) **Throughput** — queries per second (QPS). Others: indexing speed (docs/sec), CPU/memory/disk usage.

---

### 70. [MEDIUM] What is pooling in the context of building relevance judgments for a test collection?

**Answer:** **Pooling** means forming the set of documents to be judged by taking the **union of top-k results** from several retrieval systems for each query. Only documents in this pool get human relevance judgments. Documents not in the pool are usually treated as non-relevant, which can bias evaluation.

---

## HARD (Set 3)

### 71. [HARD] **AP calculation.** A query has 4 relevant documents. The system returns them at ranks 1, 3, 6, 10. Compute P@1, P@3, P@6, P@10 and then Average Precision. Show steps.

**Answer (step-by-step):** P@1 = 1/1 = **1**. P@3 = 2/3. P@6 = 3/6 = **0.5**. P@10 = 4/10 = **0.4**. AP = (1/4)[1 + 2/3 + 0.5 + 0.4] = (1/4)(2.567) ≈ **0.642**.

---

### 72. [HARD] **MRR calculation.** For three queries, the rank of the first relevant document is 2, 1, and 5 respectively. Compute MRR.

**Answer (step-by-step):** Reciprocal ranks: 1/2, 1/1, 1/5 = 0.5, 1, 0.2. MRR = (1/3)(0.5 + 1 + 0.2) = 1.7/3 ≈ **0.567**.

---

### 73. [HARD] **NDCG calculation.** For positions 1–4, relevance grades are [3, 2, 0, 1]. Compute DCG_4 using DCG_p = Σ rel_i / log₂(i+1). Then compute IDCG_4 (ideal order: 3, 2, 1, 0) and NDCG_4.

**Answer (step-by-step):** DCG_4 = 3/1 + 2/1.585 + 0 + 1/2.322 ≈ 4.69. IDCG_4 = 3/1 + 2/1.585 + 1/2 + 0 ≈ 4.76. NDCG_4 = DCG_4 / IDCG_4 ≈ **0.985**.

---

### 74. [HARD] Explain how SimHash is used for near-duplicate detection at scale. What is compared?

**Answer:** **SimHash** maps each document to a fixed-length **bit fingerprint** so that similar documents have **similar** fingerprints (few bit differences). We compare fingerprints using **Hamming distance** (number of differing bits). If the distance is below a threshold, the documents are near-duplicates. This allows fast comparison at scale.

---

### 75. [HARD] What is F_β? How does β affect the weight on precision vs recall? Give the formula.

**Answer:** **F_β** = (1+β²)·P·R / (β²·P + R). When **β > 1**, recall is weighted more than precision. When **β < 1**, precision is weighted more. β = 1 gives the balanced F1.

---

### 76. [HARD] Why is statistical significance important when comparing two IR systems? What do we typically report?

**Answer:** The observed difference in MAP might be due to **random variation** across queries. **Significance testing** (e.g. paired t-test, Wilcoxon) tests whether the difference is **statistically significant**. We report **p-values** or **confidence intervals**. A small p-value suggests the difference is unlikely due to chance.

---

### 77. [HARD] What is the cold start problem in recommendation? How does it differ between collaborative and content-based filtering?

**Answer:** **Cold start** = difficulty when there is little or no data for a user or item. **Collaborative:** New user (no history) and new item (no ratings) are both hard. **Content-based:** New item is easier if we have item features; new user is still hard (no profile). **Hybrid** approaches often address cold start.

---

### 78. [HARD] Describe the role of the URL frontier in a web crawler. What does "crawl budget" mean?

**Answer:** The **URL frontier** is the **queue** of URLs to be fetched. The crawler takes a URL, fetches the page, parses it, adds new URLs to the frontier. The frontier may be **prioritised**. **Crawl budget** is the limit on how many pages (or bandwidth) is allocated to a site or the whole crawl per time period.

---

### 79. [HARD] What are online evaluation and offline evaluation? Give one example metric for each.

**Answer:** **Offline evaluation** uses a **static test collection** (fixed documents, queries, relevance judgments). Metrics: **MAP, NDCG, P@k**. **Online evaluation** uses **real user traffic** (clicks, dwell time). Examples: **CTR**, **A/B test**. Online reflects actual user satisfaction but is noisier and requires deployment.

---

### 80. [HARD] What is R-precision? How is it different from P@10? When might R-precision be preferred?

**Answer:** **R-precision** = precision when the number of documents retrieved equals **R** (the number of relevant documents for that query); i.e. P@R, and R varies per query. **P@10** is at a **fixed** cutoff (10) for all queries. R-precision is query-dependent and often correlated with AP; preferred when we want a cutoff that adapts to each query's relevance set size.

---

# Set 4 — Exam-Aligned Practice (June 2023 Style)

## SHORT STRUCTURAL

### 81. [MEDIUM] State Zipf's law using both frequency and probability forms.

**Answer:** Frequency form: $f(r) \propto 1/r$. Probability form: $P(r)=c/r$, where $r$ is word rank and $c$ is a corpus-dependent constant.

### 82. [MEDIUM] What does a Zipf curve look like on normal axes and on log-log axes?

**Answer:** On normal axes, it is a steeply decreasing curve with a long tail. On log-log axes, it is approximately a straight line with negative slope.

### 83. [MEDIUM] Write Heaps' law and define all parameters.

**Answer:** Heaps' law is $v = k n^{\beta}$, where $v$ is vocabulary size, $n$ is number of tokens, and $k,\beta$ are corpus constants.

### 84. [HARD] Given $(n,v)=(10^3,10^3)$ and $(10^5,10^4)$, estimate $\beta$ in Heaps' law.

**Answer:** Divide equations: $10 = 100^{\beta}$, so $\beta = \log(10)/\log(100)=0.5$.

### 85. [HARD] If $\beta=0.5$ and $k=\sqrt{1000}$, estimate vocabulary when $n=10^9$.

**Answer:** $v=k n^{0.5}=\sqrt{1000}\cdot\sqrt{10^9}\approx 31.62\times31622.78\approx 10^6$ terms.

### 86. [MEDIUM] In PageRank, what do $B_u$, $L_v$, $N$, and $d$ represent?

**Answer:** $B_u$ is the set of pages linking to page $u$; $L_v$ is number of outgoing links from page $v$; $N$ is total number of pages; $d$ is damping factor.

### 87. [HARD] Why does PageRank divide incoming contribution by outdegree $L(v)$?

**Answer:** A page's rank vote is split among all pages it links to; more outlinks means less rank passed per link.

### 88. [HARD] Compare incidence matrix and inverted index in one sentence each.

**Answer:** Incidence matrix stores a full $M\times N$ binary grid of term-document presence. Inverted index stores only non-zero occurrences as postings lists per term.

### 89. [HARD] State space complexity for incidence matrix and inverted index.

**Answer:** Incidence matrix: $O(MN)$. Inverted index: $O(M+K)$ where $K$ is number of non-zero term-document incidences.

### 90. [HARD] Why is inverted indexing preferred in IR systems?

**Answer:** Real collections are sparse, so inverted index avoids storing massive zeros, giving large space savings and efficient query-time processing.

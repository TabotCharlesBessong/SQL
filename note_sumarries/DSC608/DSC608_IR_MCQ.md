# DSC608 Information Retrieval — Multiple Choice Questions (20)

**Distribution:** 4 Easy (20%) | 6 Medium (30%) | 10 Hard (50%)

---

## EASY (4 questions)

### 1. [EASY] What is information retrieval primarily concerned with?
- A) Querying structured databases with SQL  
- B) Finding unstructured material that satisfies an information need from large collections  
- C) Storing data in predefined formats  
- D) Exact matching of query strings in relational tables  

**Answer: B**  
**Explanation:** IR is defined as finding material (usually documents) of an unstructured nature that satisfies an information need from within large collections. Structured databases and exact matching are the domain of RDBMS, not IR.

---

### 2. [EASY] In the context of IR, which pair of metrics is commonly used to evaluate effectiveness?
- A) Throughput and response time  
- B) Precision and recall  
- C) Coverage and freshness  
- D) Index size and vocabulary size  

**Answer: B**  
**Explanation:** Precision (fraction of returned results that are relevant) and recall (fraction of relevant documents in the collection that were returned) are the two statistics commonly used to assess the quality of search results.

---

### 3. [EASY] The inverted index consists of two main parts. They are:
- A) Documents and queries  
- B) Dictionary and postings  
- C) Terms and stopwords  
- D) Crawler and indexer  

**Answer: B**  
**Explanation:** The inverted index has a dictionary (vocabulary/lexicon) of terms and postings (for each term, a list of document IDs or postings lists). Documents and queries are not parts of the index structure.

---

### 4. [EASY] In Boolean retrieval, the outcome of query processing is:
- A) A ranked list of documents  
- B) A set of documents (TRUE/FALSE match only)  
- C) A single best document  
- D) A relevance score for each document  

**Answer: B**  
**Explanation:** Boolean retrieval is “exact-match” retrieval with two outcomes: a document either matches the Boolean expression (TRUE) or not (FALSE). There is no ranking.

---

## MEDIUM (6 questions)

### 5. [MEDIUM] Zipf’s law states that word frequency in a corpus is:
- A) Proportional to vocabulary size  
- B) Inversely proportional to the word’s rank (by frequency)  
- C) Proportional to document length  
- D) Constant across all words  

**Answer: B**  
**Explanation:** Zipf’s law says the frequency *f* of a word is inversely proportional to its rank *r* (with words ranked by decreasing frequency). So few words occur very often and many words rarely.

---

### 6. [MEDIUM] Heaps’ law is used to model:
- A) Term frequency distribution  
- B) Vocabulary growth as corpus size increases  
- C) Precision and recall  
- D) PageRank scores  

**Answer: B**  
**Explanation:** Heaps’ law relates vocabulary size *v* to corpus size *n* (e.g. *v* = *k*·*n*^β). As the corpus grows, new words appear but at a decreasing rate. Zipf’s law models term frequency distribution.

---

### 7. [MEDIUM] In the vector space model, documents are typically ranked using:
- A) Boolean AND of query terms  
- B) Cosine similarity between query and document vectors  
- C) Number of query terms in the document  
- D) Length of the document  

**Answer: B**  
**Explanation:** In the vector space model, documents and the query are represented as term-weight vectors. Ranking is by similarity; cosine (dot product normalised by vector lengths) is a common and effective choice.

---

### 8. [MEDIUM] TF-IDF weighting assigns higher weight to a term when:
- A) The term appears in many documents  
- B) The term appears rarely in the collection (low document frequency) and/or often in the document  
- C) The document is long  
- D) The term is a stopword  

**Answer: B**  
**Explanation:** IDF is high when the term appears in few documents (discriminating). TF reflects importance within the document. So TF-IDF is high when the term is frequent in the document and rare in the collection.

---

### 9. [MEDIUM] PageRank of a page can be interpreted as:
- A) The number of outgoing links from the page  
- B) The probability that a random surfer is on that page  
- C) The number of terms in the page  
- D) The TF-IDF score of the page  

**Answer: B**  
**Explanation:** PageRank is defined as the probability that a “random surfer” following links (with possible random jumps) is viewing that page. Links from high-PageRank pages increase a page’s PageRank.

---

### 10. [MEDIUM] Which component of a search engine is responsible for tokenizing, stopping, and stemming?
- A) Ranking component  
- B) Text transformation (within indexing)  
- C) User interaction component  
- D) Evaluation component  

**Answer: B**  
**Explanation:** Text transformation takes raw text and produces index terms; it includes parsing, tokenization, stopping, and stemming. Ranking uses these terms to score documents; user interaction handles query input and results display.

---

## HARD (10 questions)

### 11. [HARD] Estimating result set size under the word-independence assumption often fails because:
- A) The collection is too small  
- B) Query terms tend to co-occur (not independent)  
- C) IDF is not used  
- D) Stopwords are removed  

**Answer: B**  
**Explanation:** Independence assumes *P(a∩b∩c)* = *P(a)P(b)P(c)*. In practice, if a document contains one query term (e.g. “fish”), another (e.g. “aquarium”) is more likely to appear, so estimates are poor. Better estimates use co-occurrence or the current result set.

---

### 12. [HARD] In the ranking formula Score(D,Q) = Σᵢ gᵢ(Q)·fᵢ(D), why is the sum in practice over only a small number of terms?
- A) Only positive weights are used  
- B) Query feature values gᵢ(Q) are non-zero only for terms that appear in the query  
- C) Document features are sparse  
- D) The formula is approximate  

**Answer: B**  
**Explanation:** For each query, only the terms in the query have non-zero query feature values gᵢ(Q). So the sum need only run over query terms, making scoring efficient even with millions of features.

---

### 13. [HARD] Term-at-a-time scoring and document-at-a-time scoring differ mainly in:
- A) Whether the index is compressed  
- B) Whether Boolean filters are applied  
- C) How the index is traversed to accumulate document scores (one term’s list at a time vs all terms’ lists together)  
- D) The use of TF-IDF  

**Answer: C**  
**Explanation:** Term-at-a-time: for each query term, traverse its postings, add that term’s contribution to each document’s score. Document-at-a-time: traverse all query terms’ postings in sync, computing each document’s full score when it is seen. Both can be optimised further.

---

### 14. [HARD] Topical relevance and user relevance differ in that:
- A) Topical relevance is binary, user relevance is multi-valued  
- B) Topical relevance is about same topic; user relevance includes novelty, language, audience, etc.  
- C) Only topical relevance is used in evaluation  
- D) User relevance does not depend on the query  

**Answer: B**  
**Explanation:** A document is topically relevant if it is on the same topic as the query. User relevance incorporates all factors that affect a user’s judgment (e.g. novelty, language, intended audience, recency). Both can be binary or multi-valued.

---

### 15. [HARD] The Probability Ranking Principle (PRP) states that:
- A) Documents should be ranked by TF-IDF score  
- B) Documents should be ranked by decreasing probability of relevance (given available data) to maximise effectiveness  
- C) Only relevant documents should be retrieved  
- D) Precision and recall should be equal  

**Answer: B**  
**Explanation:** PRP says that to maximise overall effectiveness, the system should rank documents in order of decreasing probability of relevance to the user who submitted the request, where probabilities are estimated from available data. It does not specify how to estimate those probabilities.

---

### 16. [HARD] Why might using NOT in a Boolean query (e.g. NOT automobile) be problematic?
- A) It slows down the query  
- B) It can remove relevant documents that mention the excluded term in a different context  
- C) It is not supported by inverted indexes  
- D) It increases recall  

**Answer: B**  
**Explanation:** NOT removes any document containing the term anywhere. Example: a relevant document about Lincoln’s funeral train (“nine-car funeral train”) would be excluded by NOT car, so NOT often removes relevant as well as non-relevant documents and is generally not recommended.

---

### 17. [HARD] An inverted index with “word positions” in postings is used primarily to support:
- A) Boolean AND queries  
- B) TF-IDF scoring  
- C) Proximity matches (e.g. phrases, “within k words”)  
- D) Stopping and stemming  

**Answer: C**  
**Explanation:** Storing positions allows the system to check whether query terms appear as a phrase or within a given window. Boolean AND and TF-IDF can be supported with document IDs and counts; positions are for proximity.

---

### 18. [HARD] Safe vs unsafe optimisations in ranking refer to:
- A) Encryption of indexes  
- B) Whether the optimisation guarantees the same scores as the unoptimised version (safe) or not (unsafe)  
- C) Whether compression is used  
- D) Use of cache  

**Answer: B**  
**Explanation:** Safe optimisations preserve the exact scores (e.g. same ranking). Unsafe optimisations may change scores or ranking but can be faster; their impact on effectiveness must be evaluated carefully.

---

### 19. [HARD] Anchor text is important in web search because:
- A) It replaces PageRank  
- B) It describes the destination page and is often short and query-like; experiments show it can have strong impact on effectiveness  
- C) It is always longer than the page content  
- D) It is used only for Boolean queries  

**Answer: B**  
**Explanation:** Anchor text from links pointing to a page describes that page and tends to be short and descriptive. Retrieval experiments show it can have significant impact on effectiveness, sometimes more than PageRank for some query types.

---

### 20. [HARD] In the vector space model, cosine similarity is often preferred over raw dot product because:
- A) It is faster to compute  
- B) It normalises by document and query length, reducing the bias toward long documents  
- C) It only considers binary term presence  
- D) It is required by the Probability Ranking Principle  

**Answer: B**  
**Explanation:** The denominator |Q||D| normalises by the lengths of the query and document vectors. Without this, long documents could get higher scores simply because they have more terms. Cosine focuses on the direction (relative weights) rather than length.

---

# Set 2 — Additional MCQs (20)

**Distribution:** 4 Easy | 6 Medium | 10 Hard

---

## EASY (Set 2)

### 21. [EASY] A system retrieves 10 documents; 4 are relevant. There are 20 relevant documents in the collection. What is precision?
- A) 4/20  
- B) 4/10  
- C) 10/20  
- D) 20/10  

**Answer: B**  
**Explanation:** Precision = (relevant retrieved) / (retrieved) = 4/10. Recall would be 4/20.

---

### 22. [EASY] In the formula *v* = *k*·*n*^β (Heaps’ law), *n* represents:
- A) Number of unique words  
- B) Total number of word tokens in the corpus  
- C) Number of documents  
- D) Rank of a word  

**Answer: B**  
**Explanation:** In Heaps’ law, *n* is the total number of word occurrences (tokens) in the corpus. *v* is the vocabulary size (number of unique words).

---

### 23. [EASY] Cosine similarity between two vectors is computed as:
- A) Sum of the two vectors  
- B) Dot product of the vectors divided by the product of their lengths  
- C) Difference of the vectors  
- D) Number of matching terms  

**Answer: B**  
**Explanation:** Cosine similarity = (Q·D)/(|Q||D|), i.e. dot product divided by the product of the Euclidean lengths of the two vectors.

---

### 24. [EASY] IDF for a term is high when:
- A) The term appears in many documents  
- B) The term appears in few documents  
- C) The term has high term frequency  
- D) The document is long  

**Answer: B**  
**Explanation:** IDF = log(*N*/*df*). When *df* (number of documents containing the term) is **low**, *N*/*df* is high, so IDF is high. Rare terms get high IDF.

---

## MEDIUM (Set 2)

### 25. [MEDIUM] A system retrieves 8 documents; 6 are relevant. There are 12 relevant documents in total. What is recall?
- A) 6/8  
- B) 6/12  
- C) 8/12  
- D) 12/8  

**Answer: B**  
**Explanation:** Recall = (relevant retrieved) / (relevant in collection) = 6/12 = 0.5. Precision = 6/8.

---

### 26. [MEDIUM] In a collection of 100,000 documents, term “algorithm” appears in 500 documents. What is idf(“algorithm”) using idf = log(*N*/*df*)?
- A) log(500)  
- B) log(100000/500) = log(200)  
- C) 100000/500  
- D) 500/100000  

**Answer: B**  
**Explanation:** *N* = 100,000, *df* = 500. idf = log(*N*/*df*) = log(100000/500) = log(200) ≈ 5.3 (if natural log) or ≈ 2.3 (if log₁₀).

---

### 27. [MEDIUM] For two words with document frequencies *f_a* = 1000 and *f_b* = 2000, and co-occurrence *f_{a∩b}* = 100, the independence-based estimate of collection size *N* is:
- A) 1000 + 2000  
- B) (1000 × 2000) / 100 = 20,000  
- C) 1000 × 2000  
- D) 100 / (1000 × 2000)  

**Answer: B**  
**Explanation:** Under independence, *N* = (*f_a*·*f_b*)/*f_{a∩b}* = (1000×2000)/100 = 20,000.

---

### 28. [MEDIUM] Query Q = (2, 1, 0), Document D = (1, 2, 1). The dot product Q·D is:
- A) 2+1+0 = 3  
- B) 2·1 + 1·2 + 0·1 = 4  
- C) (2+1+0)(1+2+1)  
- D) max(2,1,0) + max(1,2,1)  

**Answer: B**  
**Explanation:** Dot product = Σᵢ *qᵢ*·*dᵢ* = 2×1 + 1×2 + 0×1 = 2+2+0 = 4.

---

### 29. [MEDIUM] Zipf’s law says that the product *r*·*P(r)* is approximately constant. For English this constant *c* is about:
- A) 0.01  
- B) 0.1  
- C) 1  
- D) 10  

**Answer: B**  
**Explanation:** For English text, *c* ≈ 0.1, so *r*·*P(r)* is roughly 0.1 across medium ranks.

---

### 30. [MEDIUM] F-measure (F1) is the harmonic mean of precision and recall. If P = 0.5 and R = 0.5, F1 is:
- A) 0.5  
- B) 1.0  
- C) 0.25  
- D) 2.0  

**Answer: A**  
**Explanation:** F1 = 2·P·R/(P+R) = 2·0.5·0.5/(0.5+0.5) = 0.5/1 = 0.5. When P = R, F1 equals P (and R).

---

## HARD (Set 2)

### 31. [HARD] A document has term “fish” with raw count 5. Using tf = 1+log(tf_raw), the tf value is (log base e):
- A) 5  
- B) 1 + log(5) ≈ 2.61  
- C) log(5)  
- D) 1/5  

**Answer: B**  
**Explanation:** tf = 1+log(tf_raw) = 1+ln(5) ≈ 1+1.609 ≈ 2.61. The 1+ ensures that a single occurrence gets a positive weight.

---

### 32. [HARD] In a corpus of 50,000 documents, term A appears in 1,000 docs, term B in 2,000 docs, and both in 100 docs. Using independence, estimated number of docs containing both is:
- A) 100  
- B) 1000 + 2000 - 100  
- C) (1000 × 2000) / 50000 = 40  
- D) 1000 × 2000  

**Answer: C**  
**Explanation:** Under independence, *P(A∩B)* = *P(A)*·*P(B)* = (1000/50000)·(2000/50000). So expected count = 50000 · (1000/50000)·(2000/50000) = (1000×2000)/50000 = 40. Actual co-occurrence is 100, showing dependence.

---

### 33. [HARD] Query Q = (3, 0, 4) and Document D = (2, 2, 2). |Q| = 5, |D| = 2√3. Cosine similarity sim(Q,D) equals:
- A) (3·2 + 0·2 + 4·2) / (5 × 2√3) = 14/(10√3)  
- B) 3+2+4  
- C) 5 × 2√3  
- D) 14  

**Answer: A**  
**Explanation:** Q·D = 3×2 + 0×2 + 4×2 = 6+0+8 = 14. Cosine = (Q·D)/(|Q||D|) = 14/(5×2√3) = 14/(10√3).

---

### 34. [HARD] After processing 20% of the documents that contain the rarest query term, a system has found 400 documents containing all query terms. Estimated total result set size is:
- A) 400 × 0.2 = 80  
- B) 400 / 0.2 = 2000  
- C) 400  
- D) 400 + 0.2  

**Answer: B**  
**Explanation:** Estimate = *C*/*s* = 400/0.2 = 2000. We assume the 400 are a 20% sample of all matching documents.

---

### 35. [HARD] In PageRank, if page *u* has two inlinks from pages *v* and *w* with *PR(v)* = 0.2, *L_v* = 5, *PR(w)* = 0.1, *L_w* = 2, and *d* = 0.85, *N* = 4, the contribution from inlinks (before adding (1−*d*)/*N*) is *d*·(0.2/5 + 0.1/2) = 0.85×(0.04+0.05) = 0.85×0.09 = 0.0765. The random-jump term is:
- A) 0.85/4  
- B) (1−0.85)/4 = 0.0375  
- C) 0.15  
- D) 0.85  

**Answer: B**  
**Explanation:** Random-jump term = (1−*d*)/*N* = (1−0.85)/4 = 0.15/4 = 0.0375. So *PR(u)* = 0.0375 + 0.0765 = 0.114.

---

### 36. [HARD] Heaps’ law: *v* = *k*·*n*^β. If *k* = 50, β = 0.5, and *n* = 1,000,000, predicted vocabulary size *v* is:
- A) 50 × 10^6  
- B) 50 × 1000 = 50,000  
- C) 50 × √(10^6) = 50 × 1000 = 50,000  
- D) 10^6 / 50  

**Answer: C**  
**Explanation:** *v* = *k*·*n*^β = 50·(1,000,000)^0.5 = 50·1000 = 50,000. (n^0.5 = √n.)

---

### 37. [HARD] Precision is 0.6 and recall is 0.4. F1 (harmonic mean) is closest to:
- A) 0.5  
- B) 2·0.6·0.4/(0.6+0.4) = 0.48  
- C) (0.6+0.4)/2 = 0.5  
- D) 0.6 × 0.4  

**Answer: B**  
**Explanation:** F1 = 2·P·R/(P+R) = 2·0.6·0.4/1.0 = 0.48. The arithmetic mean would be 0.5; harmonic mean is lower when P ≠ R.

---

### 38. [HARD] A term appears in 10 documents; each of those documents has length 100 tokens. Raw tf in one doc is 8. With tf = 1+log(tf_raw) and idf = log(*N*/*df*), *N* = 1000. The tf-idf weight for that term in that document is:
- A) 8 × 10  
- B) (1+log 8) × log(1000/10) = (1+2.08) × 4.61 ≈ 14.2  
- C) 8 + log(100)  
- D) 1 + log(1000)  

**Answer: B**  
**Explanation:** tf = 1+log(8) ≈ 3.08; idf = log(1000/10) = log(100) ≈ 4.61 (ln) or 2 (log₁₀). tf-idf = tf × idf ≈ 3.08 × 4.61 ≈ 14.2 (if natural log). Step-by-step: (1+ln(8))·ln(100) ≈ 3.08·4.61.

---

### 39. [HARD] In Zipf’s law *P(r)* = *c*/*r* with *c* = 0.1, the probability of the word at rank 10 is:
- A) 0.1  
- B) 0.1/10 = 0.01  
- C) 10  
- D) 0.1 × 10  

**Answer: B**  
**Explanation:** *P*(10) = *c*/*r* = 0.1/10 = 0.01. So the 10th most frequent word has probability 0.01 (1% of tokens).

---

### 40. [HARD] Two documents D1 and D2 have cosine similarity 0.9 and 0.5 with query Q respectively. Which is ranked higher and why?
- A) D2, because 0.5 > 0.9 is false  
- B) D1, because higher cosine means more similar to Q  
- C) Both equal  
- D) Depends on document length  

**Answer: B**  
**Explanation:** In the vector space model we rank by **decreasing** similarity. Cosine 0.9 is higher than 0.5, so D1 is ranked higher. Cosine already accounts for length via the denominator.

---

# Set 3 — Missing Topics (Crawls, Evaluation, Filtering & Recommendation)

**Distribution:** 4 Easy | 6 Medium | 10 Hard

---

## EASY (Set 3 – Missing Topics)

### 41. [EASY] In a test collection for IR evaluation, what are the three main components?
- A) Crawler, index, query  
- B) Document collection, set of queries, relevance judgments  
- C) Precision, recall, F1  
- D) Dictionary, postings, crawler  

**Answer: B**  
**Explanation:** The Cranfield-style test collection has (1) a fixed document collection, (2) a set of queries (topics), and (3) relevance judgments for (query, document) pairs. Crawler/index are system components; precision/recall are metrics.

---

### 42. [EASY] Precision at 10 (P@10) is defined as:
- A) The 10th document’s relevance score  
- B) The proportion of the top 10 retrieved documents that are relevant  
- C) Recall when 10 documents are retrieved  
- D) The number of relevant documents in the collection  

**Answer: B**  
**Explanation:** P@k = (number of relevant documents in the top k) / k. So P@10 = (relevant in top 10) / 10. It focuses evaluation on the top results.

---

### 43. [EASY] Collaborative filtering recommends items based on:
- A) Only the content (text) of the items  
- B) The behaviour or preferences of other users  
- C) The number of clicks on the item  
- D) The length of the document  

**Answer: B**  
**Explanation:** Collaborative filtering uses “users like you” — it finds users with similar preferences and recommends what they liked. Content-based filtering uses item features (e.g. text); collaborative uses other users’ behaviour.

---

### 44. [EASY] Which component of a web crawler is responsible for deciding if a URL has already been fetched?
- A) Parser  
- B) Fetch module  
- C) Duplicate detection (or URL frontier / seen URLs)  
- D) Indexer  

**Answer: C**  
**Explanation:** Duplicate detection (or the URL frontier with a “seen” set) ensures we do not re-fetch the same or duplicate URLs. The fetch module retrieves pages; the parser extracts links and content.

---

## MEDIUM (Set 3)

### 45. [MEDIUM] Mean Average Precision (MAP) is:
- A) The average of precision and recall  
- B) The mean of Average Precision scores over all queries  
- C) Precision at the rank of the last relevant document  
- D) The maximum precision at any recall level  

**Answer: B**  
**Explanation:** MAP = (1/Q) Σ AP(q), where AP(q) is Average Precision for query q. So MAP is the mean of per-query AP values. It is a standard metric for ranked retrieval over multiple queries.

---

### 46. [MEDIUM] For near-duplicate detection, SimHash is used because:
- A) It gives the exact same hash for any two similar documents  
- B) Similar documents have similar hashes (small Hamming distance)  
- C) It is the same as MD5  
- D) It only works for exact duplicates  

**Answer: B**  
**Explanation:** SimHash produces a fingerprint so that similar documents get hashes that differ in few bits (small Hamming distance). So we can quickly filter near-duplicates by comparing hashes. Exact duplicates would use a content hash (e.g. SHA-256).

---

### 47. [MEDIUM] Document filtering differs from ad-hoc retrieval in that:
- A) Filtering uses Boolean queries only  
- B) In filtering the document stream changes and the information need (profile) is stable; in ad-hoc the collection is stable and the query changes  
- C) Filtering does not use an index  
- D) Ad-hoc retrieval has no ranking  

**Answer: B**  
**Explanation:** In filtering, we have a standing profile (fixed need) and a stream of new documents; we select documents matching the profile. In ad-hoc retrieval, the collection is relatively fixed and the user submits a new query each time.

---

### 48. [MEDIUM] NDCG (Normalized Discounted Cumulative Gain) is used when:
- A) Relevance is binary (relevant/not relevant) only  
- B) We have graded relevance (e.g. 0–3) and want to account for both relevance and rank position  
- C) We only care about the first result  
- D) There are no relevant documents  

**Answer: B**  
**Explanation:** NDCG uses graded relevance and discounts gains by position (lower ranks count less). So it rewards putting highly relevant documents at the top. It is normalised by the ideal DCG so scores are comparable across queries.

---

### 49. [MEDIUM] In the crawler pipeline, “removing noise” typically refers to:
- A) Deleting duplicate URLs  
- B) Stripping boilerplate (ads, navigation, scripts) from the page content before indexing or hashing  
- C) Removing stopwords only  
- D) Ignoring low PageRank pages  

**Answer: B**  
**Explanation:** Removing noise means cleaning the HTML/content to keep main content and drop boilerplate (headers, footers, ads, scripts). This improves indexing quality and makes duplicate/near-duplicate detection more stable. Duplicate URL handling is separate.

---

### 50. [MEDIUM] Mean Reciprocal Rank (MRR) is most useful for:
- A) Measuring precision over many documents  
- B) Queries where the user wants the first relevant result (e.g. known-item search)  
- C) Measuring recall  
- D) Collaborative filtering only  

**Answer: B**  
**Explanation:** MRR = mean over queries of 1/(rank of first relevant document). It focuses on how soon the first relevant result appears, which is important for known-item or navigational queries. It is not recall or precision over the full list.

---

## HARD (Set 3)

### 51. [HARD] For a query with 5 relevant documents, the system returns them at ranks 1, 3, 4, 7, 10. The Average Precision (AP) is computed as (1/5)[P@1 + P@3 + P@4 + P@7 + P@10]. What is P@1 and P@3?
- A) P@1 = 1, P@3 = 1  
- B) P@1 = 1/1 = 1, P@3 = 2/3 (two relevant in top 3)  
- C) P@1 = 5, P@3 = 5  
- D) P@1 = 0.2, P@3 = 0.2  

**Answer: B**  
**Explanation:** P@1 = (relevant in top 1)/1 = 1. P@3 = (relevant in top 3)/3 = 2/3 (ranks 1 and 3 are relevant). AP = (1/5)[1 + 2/3 + 3/4 + 4/7 + 5/10] ≈ (1/5)[1 + 0.667 + 0.75 + 0.571 + 0.5] ≈ 0.698.

---

### 52. [HARD] Shingles are used in duplicate detection to:
- A) Compress the document  
- B) Represent the document as a set of overlapping word sequences and compare similarity (e.g. Jaccard) to find near-duplicates  
- C) Compute PageRank  
- D) Build the inverted index  

**Answer: B**  
**Explanation:** W-shingles are overlapping sequences of w words. Two documents are compared by their shingle sets; high Jaccard similarity (|A∩B|/|A∪B|) indicates near-duplicates. This is more robust than exact hash for near-duplicate detection.

---

### 53. [HARD] F_β with β > 1 weights:
- A) Precision more than recall  
- B) Recall more than precision  
- C) Neither; F_β is constant  
- D) Only precision  

**Answer: B**  
**Explanation:** F_β = (1+β²)·P·R/(β²·P + R). With β > 1, the denominator has a larger coefficient on P, so recall is effectively weighted more. So F_2 weights recall twice as much as precision; F_0.5 weights precision more.

---

### 54. [HARD] Content-based filtering for recommendation suffers from:
- A) Cold start for new users only  
- B) Overspecialisation (recommending only items very similar to what the user already liked) and need for good item features  
- C) Not using any user data  
- D) Being slower than collaborative filtering  

**Answer: B**  
**Explanation:** Content-based filtering recommends items similar in features to what the user liked, so it can over-specialise (no diversity/serendipity). It also requires good item features. Cold start for new items is less of an issue (if features exist); collaborative filtering has cold start for new users and new items.

---

### 55. [HARD] DCG at position p is defined as DCG_p = Σ_{i=1..p} rel_i / log₂(i+1). The denominator log₂(i+1) is used to:
- A) Increase the weight of lower-ranked documents  
- B) Discount lower ranks so that relevant documents at the top contribute more  
- C) Normalise by query length  
- D) Compute recall  

**Answer: B**  
**Explanation:** The log term grows with rank i, so 1/log₂(i+1) decreases as i increases. So documents at rank 1 get full weight, and lower ranks are discounted. This reflects the user behaviour that results at the top matter more.

---

### 56. [HARD] A/B testing in search engines is an example of:
- A) Offline evaluation using a test collection  
- B) Online evaluation using real user traffic to compare two variants  
- C) Duplicate detection  
- D) Building a test collection  

**Answer: B**  
**Explanation:** A/B testing divides real user traffic between variant A and variant B (e.g. two ranking algorithms) and compares metrics (CTR, dwell time, success rate). It is online evaluation with real users, not offline evaluation on a static test collection.

---

### 57. [HARD] When using a test collection, “pooling” refers to:
- A) Merging multiple document collections  
- B) Forming the set of documents to be judged by taking the top-k results from several systems, then judging that pool; unjudged docs are often treated as non-relevant  
- C) Computing average precision  
- D) Collaborative filtering  

**Answer: B**  
**Explanation:** Pooling: run several retrieval systems, take the union of top-k results per query to form the pool of documents that get relevance judgments. This keeps judgment cost manageable. Documents not in the pool are typically assumed non-relevant for evaluation, which can bias metrics.

---

### 58. [HARD] R-precision is:
- A) Precision at a fixed rank (e.g. 10) for all queries  
- B) Precision when the number of documents retrieved equals the number of relevant documents for that query (i.e. P@R where R = number relevant)  
- C) Recall at k  
- D) The same as MAP  

**Answer: B**  
**Explanation:** R-precision uses R = number of relevant documents for the query, and computes precision when exactly R documents are retrieved (i.e. P@R). So it is query-dependent (R varies per query). It is often correlated with AP.

---

### 59. [HARD] Document feeds (e.g. RSS, sitemaps) compared to web crawling are typically:
- A) Slower and less efficient for getting new content  
- B) More efficient and timely for structured updates (e.g. news, blog posts) when publishers provide feeds  
- C) Only used for duplicate detection  
- D) Unrelated to indexing  

**Answer: B**  
**Explanation:** Feeds provide a direct stream of new or updated documents (e.g. RSS, Atom, sitemaps), so the system can index them without discovering URLs by crawling. This is often more efficient and timely for content that is published via feeds. Crawling is still used for general web discovery.

---

### 60. [HARD] Statistical significance testing when comparing two IR systems (e.g. System A vs B on MAP) is used to:
- A) Increase the MAP score  
- B) Determine whether the observed difference in a metric (e.g. MAP) could be due to chance; we report p-values or confidence intervals  
- C) Replace the need for a test collection  
- D) Compute P@k  

**Answer: B**  
**Explanation:** A difference in MAP (or other metric) between two systems might be due to random variation across queries. Significance tests (e.g. paired t-test, Wilcoxon) test whether the difference is statistically significant. We report p-values or confidence intervals; small p suggests the difference is unlikely due to chance.

---

# Set 4 — Exam-Aligned MCQs (Zipf, Heaps, PageRank, Index Structures)

**Distribution:** 4 Easy | 6 Medium | 10 Hard

## EASY (Set 4)

### 61. [EASY] Zipf's law primarily relates word frequency to:
- A) Document length  
- B) Word rank  
- C) Number of query terms  
- D) Number of documents in the corpus  

**Answer: B**  
**Explanation:** Zipf's law states frequency is inversely proportional to rank when words are ordered by decreasing frequency.

### 62. [EASY] Heaps' law models:
- A) Link popularity  
- B) Vocabulary growth with corpus size  
- C) Snippet quality  
- D) Precision-recall trade-off  

**Answer: B**  
**Explanation:** Heaps' law is $v = k n^\beta$, where vocabulary size grows sublinearly with total tokens.

### 63. [EASY] In PageRank, a hyperlink from page A to page B is treated as:
- A) A duplicate signal  
- B) A vote passed from A to B  
- C) A stemming rule  
- D) A stopword indicator  

**Answer: B**  
**Explanation:** PageRank interprets links as votes, weighted by source rank and source outdegree.

### 64. [EASY] Which structure is standard for large-scale text retrieval?
- A) Full incidence matrix  
- B) Inverted index  
- C) Dense tensor table  
- D) B-tree of snippets  

**Answer: B**  
**Explanation:** Inverted index stores only observed term-document occurrences and is efficient for sparse text data.

## MEDIUM (Set 4)

### 65. [MEDIUM] If $f(r) \propto 1/r$, then moving from rank 10 to rank 20 approximately changes frequency by:
- A) Doubles  
- B) Halves  
- C) Stays same  
- D) Quadruples  

**Answer: B**  
**Explanation:** Inverse proportionality means doubling rank roughly halves frequency.

### 66. [MEDIUM] Heaps' law is $v = k n^\beta$. If $\beta=0.5$, doubling $n$ multiplies $v$ by:
- A) 2  
- B) $\sqrt{2}$  
- C) 1/2  
- D) 4  

**Answer: B**  
**Explanation:** $v \propto n^{0.5}$ so doubling tokens scales vocabulary by $2^{0.5}$.

### 67. [MEDIUM] In $PR(u)=\frac{1-d}{N}+d\sum_{v\in B_u}\frac{PR(v)}{L(v)}$, $L(v)$ is:
- A) Number of inlinks to $v$  
- B) Number of outlinks from $v$  
- C) Number of terms on page $v$  
- D) Length of query $v$  

**Answer: B**  
**Explanation:** Page $v$ distributes its rank across its outgoing links; $L(v)$ is outdegree.

### 68. [MEDIUM] With $N=5$ and $d=0.85$, the random jump term in PageRank is:
- A) 0.85/5  
- B) 0.15/5  
- C) 1/5  
- D) 0.85  

**Answer: B**  
**Explanation:** Random component is $(1-d)/N = 0.15/5 = 0.03$.

### 69. [MEDIUM] Space for incidence matrix with $M$ terms and $N$ docs is best described as:
- A) $O(M+N)$  
- B) $O(MN)$  
- C) $O(\log MN)$  
- D) $O(K)$ only  

**Answer: B**  
**Explanation:** The full matrix stores every term-document cell, regardless of sparsity.

### 70. [MEDIUM] If $K$ is non-zero term-document entries, inverted index space is approximately:
- A) $O(MN)$  
- B) $O(M+K)$  
- C) $O(N^2)$  
- D) $O(M^2)$  

**Answer: B**  
**Explanation:** Dictionary plus postings scales with terms and observed incidences.

## HARD (Set 4)

### 71. [HARD] Given Heaps data points $(n,v)=(10^3,10^3)$ and $(10^5,10^4)$, which $\beta$ fits best?
- A) 0.25  
- B) 0.5  
- C) 0.75  
- D) 1.0  

**Answer: B**  
**Explanation:** $10=100^\beta$, so $\beta=\log(10)/\log(100)=0.5$.

### 72. [HARD] With $\beta=0.5$ and $k\approx31.62$, estimated vocabulary at $n=10^9$ is closest to:
- A) $10^4$  
- B) $10^5$  
- C) $10^6$  
- D) $10^7$  

**Answer: C**  
**Explanation:** $v=kn^{0.5}\approx31.62\times31622.78\approx10^6$.

### 73. [HARD] In PageRank, which change typically decreases rank passed along each outgoing edge from a page?
- A) Increasing damping factor  
- B) Increasing outdegree of source page  
- C) Decreasing corpus size  
- D) Increasing stopword list  

**Answer: B**  
**Explanation:** Rank share per edge is $PR(v)/L(v)$; higher $L(v)$ means less per outgoing link.

### 74. [HARD] Why is an incidence matrix often impractical for web-scale IR?
- A) It cannot represent Boolean queries  
- B) It is dense with ones  
- C) It is huge and mostly zeros  
- D) It cannot store document IDs  

**Answer: C**  
**Explanation:** For large vocabularies and corpora, the matrix is massive and sparse, wasting space.

### 75. [HARD] Which statement about inverted index postings is most accurate?
- A) They are usually sorted by term frequency only  
- B) They are usually sorted by document ID for efficient merging/intersection  
- C) They are unsorted for faster appends only  
- D) They cannot store positional information  

**Answer: B**  
**Explanation:** Sorted postings support efficient Boolean and ranked query processing.

### 76. [HARD] If a PageRank question has unclear edge direction in the diagram, the best exam strategy is to:
- A) Skip the question  
- B) Assume random directions and provide no explanation  
- C) State your adjacency assumption clearly and compute consistently  
- D) Use TF-IDF instead  

**Answer: C**  
**Explanation:** Clear assumptions with consistent math can still earn method marks.

### 77. [HARD] A no-damping PageRank variant differs from standard PageRank mainly by removing:
- A) Inlink contribution term  
- B) Outdegree normalization  
- C) Random jump term  
- D) Initialisation values  

**Answer: C**  
**Explanation:** Standard PageRank includes random jump $(1-d)/N$; no-damping forms omit it.

### 78. [HARD] Which pair are both empirical laws used in IR text statistics?
- A) Bayes and Markov  
- B) Zipf and Heaps  
- C) TF and IDF  
- D) AP and MAP  

**Answer: B**  
**Explanation:** Zipf models frequency-rank distribution; Heaps models vocabulary growth.

### 79. [HARD] If vocabulary growth is sublinear, then as corpus grows large, new-word discovery rate:
- A) Increases linearly  
- B) Stays constant  
- C) Decreases  
- D) Becomes negative  

**Answer: C**  
**Explanation:** Heaps law with $\beta<1$ implies diminishing marginal growth in vocabulary.

### 80. [HARD] In a sparse corpus, which representation directly stores only observed term-document matches?
- A) Dense incidence matrix  
- B) Inverted index postings  
- C) Euclidean distance matrix  
- D) Query log table  

**Answer: B**  
**Explanation:** Postings lists record only actual occurrences, avoiding zero storage overhead.

# DSC608 — Missing Topics Summary (from Course Outline)

This document covers topics from the DSC608 course outline that were not fully covered in the main IR notes: **Crawls and Feeds**, **Queries and Interfaces** (result presentation, advertising, clustering, cross-language), **Evaluating Search Engines** (effectiveness and efficiency metrics, test collections, significance, online testing), and **Filtering and Recommendation**.

---

## 1. Crawls and Feeds

### 1.1 Deciding What to Search
- **Crawl scope**: Choose what to index—whole web, a domain, specific sites, or document feeds (e.g. news, email).
- **Policies**: Respect *robots.txt* and crawl delay; prioritise important or fresh pages; allocate **crawl budget** (how many pages per site/time).

### 1.2 Crawling the Web
- **Web crawler (spider)**: A program that discovers and fetches web pages by following links, so that they can be stored and indexed.
- **Basic loop**: (1) Pick a URL from a **URL frontier** (queue of URLs to fetch). (2) Fetch the page (HTTP). (3) Parse the page to extract links and text. (4) Add new URLs to the frontier. (5) Store or pass the document for indexing. (6) **Duplicate detection**: avoid re-fetching the same or near-duplicate page.

**Crawler architecture (main components):**
- **URL frontier**: Queue(s) of URLs to be fetched; often prioritised (e.g. by PageRank, freshness).
- **Fetch module**: HTTP client; handles DNS, redirects, rate limiting.
- **Parser**: Extracts links (hrefs) and main content; may strip scripts/ads.
- **Duplicate / near-duplicate detection**: Decides if a URL or document is already seen or too similar to one already stored.

### 1.3 Crawling Documents and Email
- **Document crawlers**: Traverse file systems or document stores (e.g. shared drives, CMS) to find documents (PDF, Office, etc.) for indexing.
- **Email**: May be crawled from mail servers (IMAP, Exchange) or logs; need to handle folders, attachments, and privacy.

### 1.4 Document Feeds
- **Feeds**: Push or pull of documents (e.g. RSS/Atom, sitemaps, API feeds) instead of discovering by following links.
- **Use**: News, blogs, product catalogues; often more efficient and timely than crawling for structured updates.
- **Conversion**: Feeds may provide metadata (title, date, link); crawler output is raw HTML or other format—both need **conversion** to a common document representation for indexing.

### 1.5 The Conversion Problem
- **Heterogeneous formats**: HTML, PDF, Word, email, JSON, etc. must be converted to a **normalised form** (e.g. plain text + metadata) before text transformation and indexing.
- **Methods**: Parsers/renderers per format; sometimes OCR for images; extract title, author, date, body, links.

### 1.6 Storing the Documents
- **Document store**: Persist raw or processed documents for snippet generation, caching, and re-indexing. Often keyed by document ID; may be distributed (e.g. sharded by doc ID or URL).
- **Metadata**: Store URL, fetch time, content hash, content type, and other fields used by the index or duplicate detection.

### 1.7 Detecting Duplicates
- **Exact duplicates**: Same content → same **hash** (e.g. SHA-256 of normalised content). Store hashes of seen documents; skip if hash already exists.
- **Near-duplicates**: Pages that are almost identical (e.g. same article with different ads or timestamps). Detecting them saves storage and improves quality.

**Techniques:**
- **Shingles (w-shingles)**: Represent a document as a set of overlapping word sequences (e.g. 3-word shingles). Compare **Jaccard similarity** of shingle sets; high overlap ⇒ near-duplicate. **Example**: "the cat sat" → shingles {"the cat sat", "cat sat on", ...}. Two docs with high Jaccard are near-duplicates.
- **SimHash**: Compute a **fingerprint** of the document (e.g. from term weights or shingles) so that similar documents have similar hashes (few bit differences). Compare fingerprints with **Hamming distance**; small distance ⇒ near-duplicate. Used at scale for quick filtering.
- **MinHash**: Compact sketch of a set (e.g. shingles) that approximates Jaccard similarity; used for fast similarity estimation over many pairs.
- **Bloom filter**: Space-efficient structure to record “seen” URLs or hashes; may have false positives (say “seen” when not), but no false negatives; good for first-pass duplicate URL filtering.

**Pipeline**: Normalise HTML (remove boilerplate, scripts, ads) before hashing so that small changes do not change the hash; then apply fingerprinting (SimHash) or shingles for near-duplicate detection.

### 1.8 Removing Noise
- **Boilerplate**: Navigation, footers, headers, sidebars, ads—often removed so that indexing and duplicate detection focus on main content.
- **Methods**: Heuristics (e.g. strip script/style tags), DOM-based extraction (identify main content block), or learned models (classify which regions are content vs noise). Reduces index size and improves relevance.

---

## 2. Queries and Interfaces (Additional Detail)

### 2.1 Result Pages and Snippets
- **Snippet**: Short extract from a document shown with the search result (e.g. 2–3 lines). Helps the user judge relevance before clicking.
- **Snippet generation**: Often a window of text around the first (or best) match of query terms; may **highlight** query terms; sometimes use metadata (e.g. title, URL) or abstract/summary.
- **Result page**: Ordered list of (title, snippet, URL, sometimes date/site); may include facets, filters, and ads.

### 2.2 Advertising and Search
- **Sponsored results**: Ads shown alongside organic results; often triggered by query keywords (keyword advertising).
- **Ranking**: Ads may be ranked by bid × predicted click-through rate (CTR) or similar; relevance and policy filters apply.
- **Evaluation**: Click-through rate (CTR), revenue per query; must not confuse with organic effectiveness metrics.

### 2.3 Clustering the Results
- **Clustering**: Group retrieved documents into categories or themes (e.g. by topic, source, type) so users can browse by cluster.
- **Methods**: Cluster on document vectors (e.g. TF-IDF); use labels from taxonomy or key phrases; or use snippets/titles for fast grouping. Improves **diversity** and navigation when there are many results.

### 2.4 Cross-Language Search
- **Cross-language IR**: Query in one language, documents in another; or multilingual index with language detection.
- **Techniques**: Translate query to document language(s); translate documents to a common language; or use multilingual embeddings/representations. Evaluation must consider translation quality and retrieval quality.

---

## 3. Evaluating Search Engines

### 3.1 Why Evaluate?
- Compare systems (e.g. ranking algorithms, indexing choices).
- Tune parameters (e.g. weights, thresholds).
- Monitor quality over time (regression testing).
- Decide what to ship (A/B tests, offline metrics).

### 3.2 The Evaluation Corpus (Test Collection)
- **Cranfield paradigm**: Evaluation is based on a **test collection** consisting of:
  - **Document collection**: Fixed set of documents.
  - **Query set**: Set of queries (topics).
  - **Relevance judgments**: For (query, document) pairs, labels indicating relevance (binary or graded).
- **Relevance judgments**: Usually human-assessed; in practice only a subset of (query, doc) pairs is judged (e.g. pooling: judge docs that appear in top-*k* of several systems). Unjudged docs are often treated as non-relevant.
- **Limitations**: Judgments are incomplete and may be subjective; collection may not match production; cost of building and maintaining test collections.

### 3.3 Logging
- **Query logs**: Record queries, timestamps, user ID (if available), result list shown, clicks, dwell time.
- **Uses**: Analyse query distribution; train spell-check and suggestions; infer relevance from clicks (e.g. click-through rate, dwell time); A/B testing and online evaluation.
- **Privacy**: Logs are sensitive; anonymisation and retention policies are required.

### 3.4 Effectiveness Metrics (Recall and Precision)
- **Precision** = (relevant retrieved) / (retrieved) = *TP*/(*TP*+*FP*).
- **Recall** = (relevant retrieved) / (relevant in collection) = *TP*/(*TP*+*FN*).
- **F-measure (F1)** = 2·*P*·*R*/(*P*+*R*). **F_β** = (1+β²)·*P*·*R*/(β²·*P*+*R*); β > 1 weights recall more, β < 1 weights precision more.
- **Trade-off**: Returning more documents tends to increase recall and decrease precision. Single-value metrics (e.g. F1) combine both.

### 3.5 Focusing on the Top Documents
For web search, users care most about the top results. Metrics that focus on top-*k*:

- **Precision at k (P@k)**: Proportion of the top-*k* results that are relevant.  
  **P@k** = (number of relevant in top *k*) / *k*.  
  Example: Of top 10 results, 4 relevant ⇒ P@10 = 0.4. Does not consider rank order.

- **Average Precision (AP)**: For one query, average of precision values at each rank where a relevant document appears.  
  **AP** = (Σ_{k: doc at k is relevant} P@k) / (total number of relevant documents).  
  Equivalently: at each position *k*, if the doc at *k* is relevant, add P@k to the sum; then divide by the number of relevant docs. AP is between 0 and 1; higher when relevant docs are ranked higher.

- **Mean Average Precision (MAP)**: Mean of AP over all queries.  
  **MAP** = (1/*Q*) Σ_{q=1..Q} AP(q).  
  Standard metric for comparing systems over a set of queries.

- **R-precision**: For a query with *R* relevant documents, precision when exactly *R* documents are retrieved (i.e. P@R).  
  **R-precision** = (relevant in top *R*) / *R*.  
  Requires knowing *R*; often correlated with AP.

- **Mean Reciprocal Rank (MRR)**: For each query, **reciprocal rank** = 1/(rank of first relevant document). **MRR** = mean over queries of reciprocal rank.  
  **MRR** = (1/*Q*) Σ_q 1/rank_q.  
  Focuses on “first relevant hit”; good for known-item or navigational queries.

### 3.6 Graded Relevance and NDCG
When relevance is on a scale (e.g. 0–3 or 0–5), we can use gain-based metrics:

- **DCG at p (Discounted Cumulative Gain)**:  
  **DCG_p** = Σ_{i=1..p} *rel_i* / log₂(*i*+1).  
  *rel_i* = relevance of document at position *i*. The denominator log₂(*i*+1) **discounts** lower ranks.  
  Alternative (common in IR): **DCG_p** = Σ_{i=1..p} (2^{rel_i} − 1) / log₂(*i*+1), which emphasises highly relevant documents.

- **IDCG_p (Ideal DCG)**: DCG computed on the **ideal ranking** (all documents sorted by relevance, best first). So IDCG_p is the maximum possible DCG for that query up to position *p*.

- **NDCG at p (Normalised DCG)**:  
  **NDCG_p** = DCG_p / IDCG_p.  
  Value between 0 and 1; 1 means the ranking is ideal. NDCG is comparable across queries with different numbers of relevant documents. **Mean NDCG** = average of NDCG over queries.

### 3.7 Averaging and Interpolation
- **Averaging**: Report mean (or median) of a metric over queries (e.g. MAP, mean NDCG). Some use **geometric mean** (e.g. GMAP) to reduce impact of a few very bad queries.
- **Interpolation**: For precision-recall curves, **interpolated precision** at recall *r* is the maximum precision at any recall ≥ *r*. Smooths the curve; 11-point average is the average of interpolated precision at recall levels 0, 0.1, …, 1.0.

### 3.8 Using Preferences
- **Preference-based evaluation**: Instead of absolute relevance, use **preference judgments**: for two documents, which is better for the query? Can be easier and more reliable than grading. Metrics can be based on how often the system agrees with preferences (e.g. pairwise accuracy).

### 3.9 Efficiency Metrics
- **Response time (latency)**: Time from query submission to first result (or full result). Target: milliseconds to a few hundred ms for web search.
- **Throughput**: Queries per second (QPS) the system can handle.
- **Indexing speed**: Documents (or bytes) processed per second during indexing.
- **Resource use**: CPU, memory, disk I/O, network.

### 3.10 Training, Testing, and Statistics
- **Train/test split**: Use separate query sets (or temporal split) for tuning parameters vs reporting final metrics; avoid overfitting to the test set.
- **Cross-validation**: Rotate which part is test; average metrics.
- **Statistical significance**: When comparing two systems, the difference in MAP (or other metric) may be due to chance. Use **significance tests** (e.g. paired *t*-test on per-query scores, Wilcoxon signed-rank, bootstrap) to test whether the difference is significant. Report *p*-values or confidence intervals.

### 3.11 Setting Parameter Values
- **Parameter tuning**: Choose parameters (e.g. weights, *k* in P@k, BM25 parameters) by optimising a metric (e.g. MAP or NDCG) on a **development/validation** set. Avoid tuning on the test set.
- **Grid search** or **optimisation** (e.g. coordinate descent) over parameter space.

### 3.12 Online Testing
- **A/B testing**: Show variant A to a fraction of users and variant B to the rest; compare metrics (CTR, dwell time, success rate, revenue). Decide which variant wins.
- **Online metrics**: Click-through rate (CTR), zero-result rate, session success rate, abandonment rate, dwell time. Complement offline metrics (precision, recall, MAP, NDCG) with real user behaviour.

---

## 4. Filtering and Recommendation

### 4.1 Document Filtering
- **Filtering**: From a **stream** of incoming documents, **select** those that match a standing **profile** (information need). Unlike ad-hoc search, the query (profile) is fixed and the collection (stream) changes.
- **Profile**: Representation of the user’s interest (e.g. set of keywords with weights, classifier, or rule set). Updated over time (e.g. from feedback).
- **Methods**:
  - **Content-based filtering**: Score each incoming document against the profile (e.g. similarity to profile vector, or classifier). Retrieve or push documents above a threshold.
  - **Rule-based**: Hand-crafted rules (e.g. “contains term X and date after Y”).
- **Evaluation**: Precision/recall over the stream; delay to first relevant document; utility over time.
- **Challenges**: Profile drift (interest changes); cold start (new user, few examples); stream volume and latency.

### 4.2 Collaborative Filtering
- **Idea**: Use **other users’** behaviour (ratings, clicks, purchases) to predict what the **current user** will like. “Users who liked X also liked Y.”
- **Assumption**: Users with similar behaviour on some items will agree on others.
- **User–item matrix**: Rows = users, columns = items; entries = rating or interaction (e.g. 1 if clicked). Sparse.
- **Methods**:
  - **User-based**: Find users similar to the current user (e.g. by correlation or cosine on rating vectors); recommend items those similar users liked that the current user has not seen.
  - **Item-based**: Find items similar to items the user liked (e.g. similar users who bought both); recommend similar items.
  - **Matrix factorization**: Factor the user–item matrix (e.g. latent factors); predict missing entries; recommend items with high predicted score.
- **Metrics**: Precision/recall at *k*, NDCG, MRR, or rating prediction error (MAE, RMSE).
- **Cold start**: New user (no history) or new item (no ratings)—collaborative filtering cannot use them; content-based or hybrid helps.

### 4.3 Content-Based Filtering (Recommendation)
- **Idea**: Recommend items **similar** to those the user liked, based on **item features** (e.g. text, genre, attributes). No need for other users’ data.
- **Process**: Build a **user profile** from liked items (e.g. average vector of item features); score candidate items by similarity to profile; recommend top-*k*.
- **Pros**: No cold start for new items (if features exist); interpretable (same “content” as liked items). **Cons**: Overspecialisation (only similar to past); need good features.

### 4.4 Hybrid Recommendation
- **Hybrid**: Combine collaborative and content-based (e.g. weighted average of scores, or use content to fill in for cold start). Often used in practice to get both diversity and coverage.

---

## Key Formulae (Missing Topics)

| Topic | Formula |
|--------|---------|
| **P@k** | P@k = (relevant in top *k*) / *k* |
| **AP** | AP = (Σ_{k: rel at k} P@k) / (total relevant) |
| **MAP** | MAP = (1/*Q*) Σ_q AP(q) |
| **MRR** | MRR = (1/*Q*) Σ_q 1/(rank of 1st relevant) |
| **R-precision** | (relevant in top *R*) / *R*, *R* = number relevant |
| **DCG_p** | DCG_p = Σ_{i=1..p} *rel_i* / log₂(*i*+1) |
| **NDCG_p** | NDCG_p = DCG_p / IDCG_p |
| **F_β** | F_β = (1+β²)·*P*·*R*/(β²·*P*+*R*) |
| **Jaccard (shingles)** | |A∩B| / |A∪B| |
| **Duplicate (exact)** | hash(doc) in Seen → skip |

---

## References (concepts from course and standard IR sources)
- Croft, Metzler, Strohman. *Search Engines: Information Retrieval in Practice.*
- Manning, Raghavan, Schütze. *Introduction to Information Retrieval* (Ch. 8 Evaluation; crawler architecture).
- TREC/CLEF evaluation methodology; Wikipedia “Evaluation measures (information retrieval)”, “Collaborative filtering”, “Web crawler”.

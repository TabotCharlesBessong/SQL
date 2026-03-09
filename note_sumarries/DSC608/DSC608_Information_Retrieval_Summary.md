# DSC608 Introduction to Information Retrieval — Summary (Detailed)

## 1. Introduction to Information Retrieval

### 1.1 Structured vs Unstructured Data
- **Structured data**: Data stored in a predefined format (e.g. relational database with fixed schema). **Example:** A bank account record with fields like account number (six-digit integer) and balance (real with two decimals). Queries (e.g. “find balance > 50000”) are straightforward because semantics and format are well defined.
- **Unstructured data**: Data stored in its native form and not processed until use. **Examples:** Email body, web page text, social media posts, presentations. Most real-world data is unstructured. A news story about a bank merger might have a headline and source as attributes, but the main content is free text—so queries like “bank merger” or “bank takeover” cannot be answered by simple field comparison; we need IR to compare query text with document text.

### 1.2 What is Information Retrieval (IR)?
- **IR** is the task of finding material (usually documents) of an **unstructured** nature that satisfies an **information need** from within large collections (typically on computers).
- **Information need**: The user’s desire to locate and obtain information (the “topic” or goal). This is distinct from the **query**, which is what the user actually types—often an imperfect representation of the need.

### 1.3 IR vs RDBMS
| Aspect | RDBMS | IR |
|--------|--------|-----|
| Semantics | Well defined (schema) | Subjective (relevance) |
| Query | Complex (e.g. SQL), exact | Usually simple (keywords), approximate |
| Retrieval | Exact match to query | Best guess at relevance |
| Priority | Efficiency | Effectiveness first, then efficiency |

**Example:** In a DB we ask “accounts with balance > 5000” and get exact matches. In IR we ask “bank merger news” and the system must infer which documents are relevant; there is no single “correct” set.

### 1.4 Ad-hoc Retrieval
- **Ad-hoc retrieval**: The collection is relatively fixed; the user submits a **one-off query** that changes each time (e.g. web search). This is the main focus of the notes.
- **Information need vs query**: Need = what the user wants to know; query = the text (or other input) used to communicate that need. Queries are often short and ambiguous.
- **Filtering** (contrast): The **document stream** changes (e.g. new news), while the **information need** is stable and often represented as a **user profile**. The system filters incoming documents against the profile.

### 1.5 Classifying IR Systems (by scale)
- **Web search**: Billions of documents, millions of machines; the most visible IR application.
- **Personal IR**: e.g. search in email or personal files.
- **Vertical search**: Restricted to a domain (e.g. jobs, products).
- **Enterprise search**: Organisation’s internal documents (web, email, reports, DBs) on centralised or few machines.
- **Desktop search**: One user’s machine (files, email, browser history).
- **Peer-to-peer**: No central index; search over a network of nodes (e.g. file sharing).

### 1.6 Big Issues in IR
- **Relevance**: A document is relevant if the user finds it valuable for their need. **Vocabulary mismatch** means the same idea can be expressed in many ways (“pipeline leak” vs “pipeline rupture”), so exact text match is a poor guide to relevance.
- **Topical vs user relevance**: **Topical** = same topic as the query. **User relevance** includes other factors: novelty, language, audience, recency, etc. A document can be topically relevant but not user-relevant (e.g. already seen, wrong language).
- **Evaluation**: We need metrics to compare systems. **Precision** = fraction of **retrieved** documents that are relevant. **Recall** = fraction of **all relevant** documents that were retrieved. Trade-off: returning more documents can increase recall but often decreases precision.
- **Users**: Users judge quality; techniques like query suggestion, query expansion, and relevance feedback help them express and refine their need.

### 1.7 Search Engine
- A **search engine** is software that compares queries to documents and returns a **ranked** list of documents. Design concerns: relevance (and evaluation), performance (response time, throughput, indexing speed), coverage and freshness, scalability, adaptability, and specific problems (e.g. spam).

### 1.8 Search Engine Architecture
Two main blocks: **indexing process** (offline) and **query process** (at query time).

**Indexing process:**
1. **Text acquisition**: Identify and store documents (crawlers, feeds, conversion).
2. **Text transformation**: Turn raw text into **index terms** (parsing, tokenization, stopping, stemming, link extraction, etc.).
3. **Index creation**: Build search structures (e.g. inverted index) from terms, with optional weighting (e.g. TF-IDF) and statistics.

**Query process:**
1. **User interaction**: Accept query, transform it (same pipeline as documents), present results (snippets, highlighting, etc.).
2. **Ranking**: Use index and retrieval model to score and rank documents.
3. **Evaluation**: Logging, ranking analysis, performance analysis.

**Term–document incidence matrix**: Rows = terms, columns = documents; entry = 1 if term in document, else 0. For large collections (e.g. 500K terms × 1M docs) the matrix is huge and very sparse (>99% zeros), so we use an **inverted** representation: for each term, store only the list of documents containing it (the inverted index).

### 1.9 Inverted Index
- **Dictionary (lexicon)**: Sorted list of index terms; often kept in memory.
- **Postings**: For each term, a **postings list**—typically a sorted list of document IDs. Can be extended with term frequency per document and/or word positions.
- **Building**: Collect documents → tokenize → linguistic preprocessing (normalise, stop, stem) → produce (term, docID) pairs → sort by term then docID → merge and form dictionary + postings. Postings are usually stored on disk; each list is sorted by doc ID for efficient intersection and merging.

### 1.10 Query Process (detail)
- **Ranking formula**: Score(D,Q) = Σᵢ (query weight for term i × document weight for term i). Weights are often TF-IDF-like. Only terms that appear in the query contribute (other query weights are zero), so the sum is over a small number of terms.
- **Term-at-a-time scoring**: For each query term, fetch its postings and add that term’s contribution to each document’s score (accumulators). **Document-at-a-time**: Traverse all query terms’ postings in sync; for each document seen, compute its full score at once.
- **Safe vs unsafe optimisations**: Safe = same scores as unoptimised; unsafe = may change scores but can be faster—impact on effectiveness must be evaluated.

---

## 2. Processing Text (Text Transformation)

### 2.1 From Words to Terms
We convert many surface forms of words into consistent **index terms** so that “running,” “runs,” “run” can match. Issues: case, punctuation, morphology (stemming), tokenisation (what counts as a word), and that not all words are equally useful (e.g. “the” vs “algorithm”).

### 2.2 Text Statistics

#### Zipf’s Law
- **Statement**: The frequency *f* of a word is (approximately) **inversely proportional** to its rank *r* when words are ranked by decreasing frequency. So the 1st most frequent word appears much more often than the 2nd, and so on.
- **Formulae**: *f* ∝ 1/*r*; in probability form *P(r)* ≈ *c*/*r*, where *c* is a constant (for English, *c* ≈ 0.1). So *r*·*P(r)* ≈ *c*.
- **Example**: In many corpora, “the” and “of” account for ~10% of tokens; the top 6 words ~20%; top 50 ~40%. A large proportion of types (e.g. 70,000 in AP89) occur only once. The law fits medium ranks well but breaks down at very high and very low ranks.
- **IR use**: Explains why a few words are very common (stopwords) and many are rare (good discriminators); motivates IDF.

#### Heaps’ Law
- **Statement**: Vocabulary size *v* (number of unique words) grows with corpus size *n* (total word tokens) according to *v* = *k*·*n*^β.
- **Variables**: *n* = total tokens in corpus; *v* = number of unique terms; *k* and β are corpus-dependent (*k* often 10–100, β ≈ 0.5). So vocabulary grows quickly when the corpus is small and more slowly when it is large.
- **Example**: For AP89, *k* ≈ 62.95, β ≈ 0.455. After ~10.9M words, predicted *v* ≈ 100,151; actual ≈ 100,024. On the web, new words keep appearing even after tens of millions of tokens (typos, names, code, etc.).
- **IR use**: Predict dictionary size for scaling; plan for growing vocabulary.

#### Estimating Result Set Size
- **Independence assumption**: If words *a*, *b*, *c* occurred independently, *P(a∩b∩c)* = *P(a)*·*P(b)*·*P(c)*. So expected number of docs containing all three ≈ *N*·(*f_a*/*N*)·(*f_b*/*N*)·(*f_c*/*N*) = *f_a*·*f_b*·*f_c*/*N*². In practice words co-occur (e.g. “fish” and “aquarium”), so this **underestimates** for related terms.
- **Using current result set**: If we have processed a proportion *s* of the documents that contain the rarest query term and found *C* documents containing all query terms, we can estimate total result size as *C*/*s*. Assumes roughly uniform distribution of matches. **Example**: Query “tropical fish aquarium”; after processing 3000 of 26,480 docs containing “aquarium,” 258 contain all three → estimate 258/(3000/26480) ≈ 2277.

#### Estimating Collection Size
- If two words *a* and *b* are (roughly) independent, *P(a∩b)* = *P(a)*·*P(b)* ⇒ *f_{a∩b}*/*N* = (*f_a*/*N*)·(*f_b*/*N*) ⇒ **N = (*f_a*·*f_b*)/*f_{a∩b}***. We choose words that are not semantically related (e.g. “tropical” and “lincoln”) to approximate independence. **Example**: *f_lincoln* = 771,326, *f_tropical* = 120,990, *f_{lincoln∩tropical}* = 3,018 ⇒ *N* ≈ (120,990×771,326)/3,018 ≈ 30.9M (actual GOV2 ≈ 25.2M).

### 2.3 Document Parsing
- **Tokenization**: Split character stream into tokens (e.g. words). Tricky: short words (e.g. “el paso”), hyphens (e.g. “e-bay” vs “t-shirts”), apostrophes, numbers, abbreviations, case (e.g. “Bush” vs “bush”). Query tokenization must match indexing.
- **Stopping**: Remove function words (stopwords) to save space and time; can harm phrase queries (“to be or not to be”). Often we index everything and decide at query time which terms to use.
- **Stemming**: Map morphological variants to a common stem (e.g. “running” → “run”). **Porter stemmer**: Rule-based (e.g. replace *sses* by *ss*, delete *s* under conditions); effective but can create false positives (e.g. “ups” → “up”) and false negatives (“countries” → “countrie”).

### 2.4 Link Analysis
- **Anchor text**: The clickable text of a link (e.g. \<a href="…">Example Website\</a>). Often describes the destination page; used as an extra “field” for that page; can have strong impact on effectiveness.
- **PageRank**: Models a “random surfer” who follows links with probability *d* and jumps to a random page with probability 1−*d*. **Formula**: *PR(u)* = (1−*d*)/*N* + *d*·Σ_{v∈B_u} *PR(v)*/*L_v*, where *B_u* = pages linking to *u*, *L_v* = number of outgoing links from *v*. So a page’s score is the random-jump term plus a weighted sum of scores from pages that link to it. High-quality inlinks increase *PR*; susceptible to link spam.

---

## 3. Indexes

### 3.1–3.2 Ranking Model
- **Abstract**: Documents have **features** (topical + quality). A **ranking function** combines query and document features into a score; we sort by score.
- **Concrete**: Score(D,Q) = Σᵢ *gᵢ*(Q)·*fᵢ*(D). Topical *fᵢ*(D) might be term weights (e.g. “tropical,” “fish”); non-topical might be update count, inlink count. *gᵢ*(Q) encodes how important feature *i* is for this query. In practice only query terms have non-zero *gᵢ*(Q), so the sum is over few terms.

### 3.3 Inverted Index Variants
- **Simple**: Dictionary + postings (doc IDs only).
- **With counts**: Each posting stores (docID, tf) for better ranking (e.g. TF-IDF).
- **With positions**: Each posting stores (docID, list of positions) for **proximity** and phrase queries (e.g. “tropical fish”).
- **Fields/extents**: Restrict search to title, date, etc.; use separate lists or extent lists (contiguous regions).
- **Precomputed scores / score-ordered lists**: Store precomputed weights or scores for speed; reduces flexibility to change the ranking function later.

### 3.4 Compression
- Inverted lists are large; lossless compression saves space; we decompress when reading. Trade-off: compression ratio vs decompression speed.

---

## 4. Retrieval Models

### 4.1 Relevance
- **Topical relevance**: Document is on the same topic as the query. **User relevance**: User would find it valuable (all factors). Models often assume **binary** (relevant/not) or **multi-valued** relevance. Retrieval models simplify relevance to make ranking computable.

### 4.2 Boolean Retrieval
- Query = Boolean expression (AND, OR, NOT). Output = set of matching documents; **no ranking**. Pros: predictable, can use metadata, efficient. Cons: no ranking, NOT removes too many relevant docs, complex queries are hard.

### 4.3 Vector Space Model
- Documents and query = **vectors** of term weights (e.g. TF-IDF). **Cosine similarity**: *sim*(Q,D) = (Q·D)/(|Q||D|). Numerator = dot product (sum of products of weights for each term); denominator = product of vector lengths (normalisation). Ranking = sort by decreasing similarity. **Why cosine**: Reduces bias toward long documents (length normalisation).
- **TF-IDF**: *tf* = importance in document (e.g. 1+log(tf_raw) to dampen very high counts); *idf* = log(*N*/*df*) so rare terms get higher weight; weight = *tf*×*idf*. **Common form**: *tf_idf* = (1+log(tf))·log(*N*/*df*). Query and document weighted similarly.

### 4.4 Probabilistic Models
- **Probability Ranking Principle (PRP)**: Rank by **decreasing probability of relevance** (given available data) to maximise effectiveness. Does not say how to estimate that probability.
- **IR as classification**: We can treat retrieval as estimating *P(relevant | document, query)*; term presence/absence and weights contribute to this estimate.

---

## 5. Boolean Query Processing with Inverted Index
- **Conjunctive query** (e.g. Brutus AND Calpurnia): Get postings for Brutus and for Calpurnia; **intersect** the two sorted lists (e.g. merge-style). Result = docs in both lists.
- **(A OR B) AND NOT C**: Union postings for A and B, then remove any doc that appears in C’s postings. With term–document matrix, AND can be implemented as bitwise AND of row vectors.

---

## Key Formulae (with short explanations)

| Formula | Meaning |
|---------|---------|
| **Precision** = (relevant retrieved) / (retrieved) | Fraction of retrieved that are relevant. |
| **Recall** = (relevant retrieved) / (relevant in collection) | Fraction of all relevant that were retrieved. |
| **F-measure** (F1) = 2·P·R/(P+R) | Harmonic mean of P and R; balances both. |
| **Zipf** *P(r)* ≈ *c*/*r*, *c* ≈ 0.1 | Probability of word at rank *r*; few very frequent, many rare. |
| **Heaps** *v* = *k*·*n*^β | Vocabulary *v* vs corpus size *n*; β ≈ 0.5. |
| **Result set (indep.)** | Docs with all terms ≈ *f_a*·*f_b*·*f_c* / *N*² (3 terms). |
| **Collection size** *N* = (*f_a*·*f_b*)/*f_{a∩b}* | Under word independence. |
| **PageRank** *PR(u)* = (1−*d*)/*N* + *d* Σ_{v→u} *PR(v)*/*L_v* | Random surfer; *L_v* = outdegree of *v*. |
| **Cosine** *sim*(Q,D) = (Q·D)/(\|Q\|\|D\|) | Dot product / (|Q|·|D|). |
| **TF-IDF** *w* = (1+log tf)·log(*N*/*df*) | Term weight; *tf* in doc, *df* = docs containing term. |

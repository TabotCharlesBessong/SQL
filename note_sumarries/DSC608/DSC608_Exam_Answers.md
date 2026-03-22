# DSC608 Exam Answers (June 2023 Paper - Extracted Questions)

This answer sheet addresses the exam questions visible in the provided exam page image for DSC608 (Information Retrieval).

## Question 1: Zipf's Law and Heaps' Law

### 1(a)(i) State Zipf's law and write an expression

Zipf's law states that when words are ranked by decreasing frequency, the frequency of a word is inversely proportional to its rank.

Common forms:

$$
f(r) \propto \frac{1}{r}
$$

or

$$
P(r) = \frac{c}{r}
$$

where:
- $r$ is rank
- $f(r)$ is frequency
- $P(r)$ is probability of occurrence
- $c$ is a corpus-dependent constant (often about 0.1 for English text)

### 1(a)(ii) Sketch/describe the graph for Zipf's law

- If you plot frequency vs rank on normal axes, you get a steeply decreasing curve (few very frequent words, many rare words).
- If you plot on log-log axes, the relationship is approximately linear with negative slope.

### 1(a)(iii) Limitations / conditions where Zipf's law applies

Zipf's law is an empirical approximation, not an exact law. It works best when:
- corpus is sufficiently large and natural-language-like
- rank is in the middle range

Limitations:
- very high-frequency words can deviate
- very low-frequency tail (hapax words, typos, names) can deviate
- domain-specific corpora and short corpora may not fit well

### 1(b) Heaps' law expression

$$
v = k n^{\beta}
$$

where:
- $v$ = vocabulary size (unique terms)
- $n$ = total tokens in corpus
- $k,\beta$ = corpus-dependent constants

### 1(b)(i) What parameters mean

- $v$: number of distinct words observed
- $n$: total running words/tokens
- $k$: scaling constant
- $\beta$: growth exponent (typically around 0.4 to 0.6, often near 0.5)

### 1(b)(ii) Conditions where Heaps' law applies

Heaps' law generally applies to growing natural-language corpora where vocabulary growth is sublinear:
- as more text is added, new words keep appearing
- but growth rate slows over time

### 1(b)(iii) Estimate vocabulary for 10^9 tokens

Given in the question:
- first 1,000 tokens -> vocabulary 1,000
- first 100,000 tokens -> vocabulary 10,000

Use:

$$
v = k n^{\beta}
$$

From point 1:

$$
1000 = k(1000)^\beta
$$

From point 2:

$$
10000 = k(100000)^\beta
$$

Divide second by first:

$$
\frac{10000}{1000} = \left(\frac{100000}{1000}\right)^\beta \Rightarrow 10 = 100^\beta
$$

So:

$$
\beta = \frac{\log 10}{\log 100} = \frac{1}{2} = 0.5
$$

Now solve for $k$ using first point:

$$
1000 = k(1000)^{0.5} = k\sqrt{1000}
$$

$$
k = \frac{1000}{\sqrt{1000}} = \sqrt{1000} \approx 31.62
$$

Estimate vocabulary at $n=10^9$:

$$
v = 31.62 \times (10^9)^{0.5} = 31.62 \times 10^{4.5}
$$

$$
10^{4.5} \approx 31622.78
$$

$$
v \approx 31.62 \times 31622.78 \approx 1,000,000
$$

Estimated vocabulary size:

$$
\boxed{v \approx 10^6\text{ terms}}
$$

## Question 2: Link Analysis and Data Structures

## 2(a)(i) How PageRank classifies hyperlinks for importance

PageRank treats a hyperlink from page $u$ to page $v$ as a vote of importance from $u$ to $v$.
- Votes from highly ranked pages are stronger.
- A page's rank is shared among its outgoing links, so a page with many outlinks passes less weight per link.

## 2(a)(ii) Expression for page rank and parameter meanings

Standard PageRank form:

$$
PR(v) = \frac{1-d}{N} + d\sum_{u \in B_v}\frac{PR(u)}{L(u)}
$$

where:
- $PR(v)$: rank score of page $v$
- $d$: damping factor (typically 0.85)
- $N$: total number of pages
- $B_v$: set of pages linking into $v$
- $L(u)$: number of outgoing links from page $u$

## 2(a)(iii) Two PageRank iterations on the given graph

The exam image graph is slightly unclear in arrow direction on one diagonal edge, so below is a clean worked approach with explicit assumptions.

Assumed directed edges (consistent with the image structure):
- $1 \to 2$
- $3 \to 1,\;3 \to 2,\;3 \to 4,\;3 \to 5$
- $2 \to 5$
- $4 \to 5$
- $5 \to 4$

Total pages $N=5$, initial ranks:

$$
PR_0(1)=PR_0(2)=PR_0(3)=PR_0(4)=PR_0(5)=\frac{1}{5}=0.2
$$

Use $d=0.85$.

Outdegrees:
- $L(1)=1$, $L(2)=1$, $L(3)=4$, $L(4)=1$, $L(5)=1$

Constant term:

$$
\frac{1-d}{N}=\frac{0.15}{5}=0.03
$$

### Iteration 1

$$
PR_1(1)=0.03+0.85\left(\frac{PR_0(3)}{4}\right)=0.03+0.85(0.05)=0.0725
$$

$$
PR_1(2)=0.03+0.85\left(\frac{PR_0(1)}{1}+\frac{PR_0(3)}{4}\right)=0.03+0.85(0.25)=0.2425
$$

$$
PR_1(3)=0.03+0.85(0)=0.03
$$

$$
PR_1(4)=0.03+0.85\left(\frac{PR_0(3)}{4}+\frac{PR_0(5)}{1}\right)=0.03+0.85(0.25)=0.2425
$$

$$
PR_1(5)=0.03+0.85\left(\frac{PR_0(2)}{1}+\frac{PR_0(3)}{4}+\frac{PR_0(4)}{1}\right)=0.03+0.85(0.45)=0.4125
$$

### Iteration 2

$$
PR_2(1)=0.03+0.85\left(\frac{PR_1(3)}{4}\right)=0.03+0.85(0.0075)=0.036375
$$

$$
PR_2(2)=0.03+0.85\left(PR_1(1)+\frac{PR_1(3)}{4}\right)
$$

$$
=0.03+0.85(0.0725+0.0075)=0.098
$$

$$
PR_2(3)=0.03
$$

$$
PR_2(4)=0.03+0.85\left(\frac{PR_1(3)}{4}+PR_1(5)\right)
$$

$$
=0.03+0.85(0.0075+0.4125)=0.387
$$

$$
PR_2(5)=0.03+0.85\left(PR_1(2)+\frac{PR_1(3)}{4}+PR_1(4)\right)
$$

$$
=0.03+0.85(0.2425+0.0075+0.2425)=0.448625
$$

After two iterations, highest scores are pages 5 and 4 for this assumed graph.

Note:
- If your instructor expects a no-damping variant, use:

$$
PR(v)=\sum_{u\in B_v}\frac{PR(u)}{L(u)}
$$

- If one ambiguous diagonal edge in the image is in the opposite direction, recompute with that corrected adjacency list.

## 2(b) Incidence matrix vs inverted index (with example and space cost)

### What they are

Incidence matrix:
- Rows are terms, columns are documents.
- Entry is 1 if term appears in document, else 0.

Example for terms {fish, tank} and documents {D1, D2, D3}:

| Term\\Doc | D1 | D2 | D3 |
|---|---:|---:|---:|
| fish | 1 | 0 | 1 |
| tank | 1 | 1 | 0 |

Inverted index:
- Dictionary maps each term to postings list of documents containing it.

From table above:
- fish -> [D1, D3]
- tank -> [D1, D2]

### Space complexity comparison

Let:
- $M$ = number of terms
- $N$ = number of documents
- $K$ = number of non-zero term-document incidences

Incidence matrix space:

$$
O(MN)
$$

Inverted index space:

$$
O(M+K)
$$

Since real text collections are very sparse ($K \ll MN$), inverted indexes are vastly more space-efficient and are the standard structure for IR systems.

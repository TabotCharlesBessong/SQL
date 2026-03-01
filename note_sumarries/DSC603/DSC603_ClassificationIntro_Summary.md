# Summary: DSC603 Data Mining — Classification (Introduction)

## Document Outline

- Classification: Basic Concepts
- Decision Tree Induction
- Bayes Classification Methods
- Rule-Based Classification
- Model Evaluation and Selection
- Techniques to Improve Classification Accuracy: Ensemble Methods
- Summary

---

## 1. Classification: Basic Concepts

### Supervised vs. Unsupervised Learning

- **Classification** is a form of data analysis that extracts models describing important data classes and helps understand the data at large.
- **Classification** predicts **categorical (discrete, unordered) labels**; **prediction** models **continuous-valued** functions.
- **Supervised learning (classification):**
  - Training data are accompanied by **labels** (class of each observation).
  - New data is classified based on the training set.
- **Unsupervised learning (clustering):**
  - Class labels of training data are **unknown**.
  - Goal: establish the existence of classes or clusters in the data.

### Classification vs. Numeric Prediction

| | Classification | Numeric Prediction |
|---|----------------|---------------------|
| **Output** | Categorical class labels (discrete/nominal) | Continuous-valued functions |
| **Goal** | Classify data using a model built from a training set and a class label attribute | Predict unknown or missing numeric values |
| **Examples** | Credit/loan approval, medical diagnosis (cancer/benign), fraud detection, web page categorization | Forecasting sales, temperature, etc. |

### Classification: Two-Step Process

1. **Model construction**
   - Each tuple is assumed to belong to a **predefined class** (from class label attribute).
   - Set of tuples used: **training set**.
   - Model can be: classification rules, decision trees, or mathematical formulae.

2. **Model usage**
   - **Estimate accuracy:** compare known labels of a **test set** with model predictions.
   - **Accuracy rate** = percentage of test samples correctly classified.
   - Test set must be **independent** of the training set (to avoid overfitting).
   - If accuracy is acceptable, use the model to classify new data.
   - **Note:** If the test set is used to choose among models, it is called a **validation (test) set**.

---

## 2. Decision Tree Induction

### Idea

- Build a tree where each **internal node** tests an attribute, each **branch** is a value of that attribute, and each **leaf** assigns a class label.
- **Algorithm (greedy, top-down):**
  - Start with all training examples at the root.
  - Attributes are categorical (continuous ones are discretized first).
  - Recursively partition examples by a **selected attribute** (e.g., using information gain).
  - **Stopping:** (1) all samples at a node are same class, (2) no remaining attributes (use majority vote at leaf), or (3) no samples left.

### Brief Review of Entropy

- For a set $D$ with classes $C_1, \ldots, C_m$, let $p_i$ = proportion of $D$ in class $C_i$.
- **Entropy (expected information)** to classify a tuple in $D$:

  $$\mathrm{Info}(D) = -\sum_{i=1}^{m} p_i \log_2(p_i)$$

  (For binary: $m = 2$.)

### Attribute Selection: Information Gain (ID3/C4.5)

- $p_i$: probability that a tuple in $D$ belongs to class $C_i$, estimated by $|C_{i,D}|/|D|$.
- **Info(D):** expected information needed to classify a tuple in $D$ (entropy).
- **Info_A(D):** expected information needed to classify $D$ after splitting on attribute $A$ (with $v$ partitions):

  $$\mathrm{Info}_A(D) = \sum_{j=1}^{v} \frac{|D_j|}{|D|} \times \mathrm{Info}(D_j)$$

- **Information gain:**

  $$\mathrm{Gain}(A) = \mathrm{Info}(D) - \mathrm{Info}_A(D)$$
- **Rule:** Choose the attribute with the **highest information gain**.

### Solved Example 1: Information Gain (Buys_Computer)

**Training data:** 14 tuples; class **buys_computer**: **yes** (9), **no** (5).

**Step 1 — Compute Info(D)**

$$\mathrm{Info}(D) = I(9,5) = -\frac{9}{14}\log_2\frac{9}{14} - \frac{5}{14}\log_2\frac{5}{14} \approx 0.940$$

**Step 2 — Compute Info and Gain for each attribute**

- **Age** (≤30, 31…40, >40):
  - ≤30: 5 tuples (2 yes, 3 no) → $I(2,3) \approx 0.971$
  - 31…40: 4 tuples (4 yes, 0 no) → $I(4,0) = 0$
  - >40: 5 tuples (3 yes, 2 no) → $I(3,2) \approx 0.971$

  $$\mathrm{Info}_{\mathrm{age}}(D) = \frac{5}{14} I(2,3) + \frac{4}{14} I(4,0) + \frac{5}{14} I(3,2) = \frac{5}{14}(0.971) + 0 + \frac{5}{14}(0.971) \approx 0.694$$

  $$\mathrm{Gain}(\mathrm{age}) = \mathrm{Info}(D) - \mathrm{Info}_{\mathrm{age}}(D) \approx 0.940 - 0.694 = 0.246$$

- **Income:** $\mathrm{Gain}(\mathrm{income}) \approx 0.029$
- **Student:** $\mathrm{Gain}(\mathrm{student}) \approx 0.151$
- **Credit_rating:** $\mathrm{Gain}(\mathrm{credit\_rating}) \approx 0.048$

**Conclusion:** **Age** has the highest information gain (0.246), so it is chosen as the root split. The tree then continues recursively on the partitions.

### Continuous-Valued Attributes

- Sort values of attribute $A$, consider **midpoints** between adjacent values as candidate split points.
- Choose the split point that **minimizes** expected information requirement (or maximizes gain).
- Split: $D_1 = \{ A \leq \text{split-point} \}$, $D_2 = \{ A > \text{split-point} \}$.

### Gain Ratio (C4.5)

- Information gain is **biased toward attributes with many values**.
- **Gain ratio** normalizes by split information:

  $$\mathrm{SplitInfo}_A(D) = -\sum_{j=1}^{v} \frac{|D_j|}{|D|} \log_2 \frac{|D_j|}{|D|}, \qquad \mathrm{GainRatio}(A) = \frac{\mathrm{Gain}(A)}{\mathrm{SplitInfo}_A(D)}$$

- Example: $\mathrm{gain\_ratio}(\mathrm{income}) = 0.029/1.557 \approx 0.019$.
- Select the attribute with the **maximum gain ratio**.

### Gini Index (CART, IBM IntelligentMiner)

- **Gini index** for data set $D$ with $n$ classes:

  $$\mathrm{gini}(D) = 1 - \sum_{j=1}^{n} p_j^2$$

- If $D$ is split on $A$ into $D_1$ and $D_2$:

  $$\mathrm{gini}_A(D) = \frac{|D_1|}{|D|}\mathrm{gini}(D_1) + \frac{|D_2|}{|D|}\mathrm{gini}(D_2)$$

- **Reduction in impurity:** $\Delta\mathrm{gini}(A) = \mathrm{gini}(D) - \mathrm{gini}_A(D)$.
- Choose the attribute (and split) that **minimizes** $\mathrm{gini}_A(D)$ (or maximizes $\Delta\mathrm{gini}(A)$).

### Solved Example 2: Gini Index (Buys_Computer)

- $D$: 9 **yes**, 5 **no**.

  $$\mathrm{gini}(D) = 1 - \left(\frac{9}{14}\right)^2 - \left(\frac{5}{14}\right)^2 \approx 0.459$$

- **Income** partitions $D$ into: $D_1$ = {low, medium} (10 tuples), $D_2$ = {high} (4 tuples).

  $$\mathrm{gini}_{\mathrm{income}}(D) = \frac{10}{14}\mathrm{gini}(D_1) + \frac{4}{14}\mathrm{gini}(D_2)$$

  (With actual class counts in $D_1$ and $D_2$, you get the numeric value; the slide states $\mathrm{gini}_{\mathrm{low,medium}}$ is 0.458 and similar for other splits.)
- **Interpretation:** Among possible splits, the one with the **lowest** $\mathrm{gini}_A(D)$ is chosen (e.g., {low, medium} vs. {high}).

### Comparing Attribute Selection Measures

| Measure | Behavior |
|--------|----------|
| **Information gain** | Biased toward multivalued attributes |
| **Gain ratio** | Can prefer unbalanced splits (one partition much smaller) |
| **Gini index** | Biased toward multivalued attributes; can favor equal-sized, pure partitions; harder when # classes is large |

### Overfitting and Tree Pruning

- **Overfitting:** Tree fits training data (and noise) too closely → poor accuracy on unseen data.
- **Prepruning:** Stop splitting if the goodness measure falls below a threshold (threshold choice is tricky).
- **Postpruning:** Grow full tree, then remove branches using a **separate validation set** to choose the best pruned tree.

### Enhancements to Basic Induction

- **Continuous attributes:** Define discrete intervals (e.g., midpoints) for splitting.
- **Missing values:** Assign most common value, or assign probabilities to possible values.
- **Attribute construction:** New attributes from existing ones to reduce fragmentation/replication.

### Scalability: RainForest and BOAT

- **RainForest:** Builds **AVC-lists** (Attribute, Value, Class_label) so scalability is separated from tree quality; AVC-set = projection with class counts; AVC-group = set of AVC-sets at a node.
- **BOAT:** Uses **bootstrapping** to form smaller samples, builds trees from each, then constructs a tree $T'$ close to the one from the full data; **two scans**, incremental.

---

## 3. Bayes Classification Methods

### Why Bayesian Classification?

- **Statistical classifier:** predicts **class membership probabilities**.
- Based on **Bayes’ theorem**.
- **Naïve Bayesian classifier** often performs comparably to decision trees and some neural networks.
- **Incremental:** each training example can update hypothesis probabilities; prior knowledge can be combined with data.
- Provides an **optimal decision-making benchmark** even when full Bayesian inference is intractable.

### Bayes’ Theorem

- **Total probability:** $P(B) = \sum_{i=1}^{M} P(B \mid A_i) P(A_i)$.
- **Bayes’ theorem:**

  $$P(H \mid X) = \frac{P(X \mid H)\,P(H)}{P(X)}$$

  - $X$: data sample (evidence); class label unknown.
  - $H$: hypothesis that $X$ belongs to class $C$.
  - $P(H \mid X)$: **posterior** probability that the hypothesis holds given $X$.
  - $P(H)$: **prior** probability (e.g., “will buy computer” regardless of attributes).
  - $P(X)$: probability of observing $X$.
  - $P(X \mid H)$: **likelihood** of $X$ given $H$.

### Classification: Maximum a Posteriori (MAP)

- Given training set $D$, tuple $X = (x_1, x_2, \ldots, x_n)$, classes $C_1, \ldots, C_m$.
- **Goal:** assign $X$ to class $C_i$ with **maximum** $P(C_i \mid X)$.
- From Bayes: $P(C_i \mid X) = \frac{P(X \mid C_i)\,P(C_i)}{P(X)}$. Since $P(X)$ is constant for all classes, we only need to maximize:

  $$P(C_i \mid X) \propto P(X \mid C_i)\,P(C_i)$$

### Naïve Bayes Classifier

- **Assumption:** attributes are **conditionally independent** given the class:

  $$P(X \mid C_i) = \prod_{k=1}^{n} P(x_k \mid C_i)$$

- **Categorical $A_k$:** $P(x_k \mid C_i)$ = (number of tuples in $C_i$ with $A_k = x_k$) / $|C_{i,D}|$.
- **Continuous $A_k$:** typically use a **Gaussian** with mean $\mu$ and standard deviation $\sigma$:

  $$P(x_k \mid C_i) = g(x; \mu_{C_i}, \sigma_{C_i}) = \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

- **Decision:** $\mathrm{argmax}_{C_i} \, P(C_i) \prod_{k=1}^{n} P(x_k \mid C_i)$.

### Solved Example 3: Naïve Bayes (Buys_Computer)

**Training set:** 14 tuples; **C1:** buys_computer = **yes** (9), **C2:** buys_computer = **no** (5).

**To classify:**

$$X = (\mathrm{age}\leq30,\ \mathrm{income}=\mathrm{medium},\ \mathrm{student}=\mathrm{yes},\ \mathrm{credit\_rating}=\mathrm{fair})$$

**Step 1 — Priors**
- $P(\mathrm{yes}) = 9/14 \approx 0.643$, $P(\mathrm{no}) = 5/14 \approx 0.357$.

**Step 2 — Likelihoods (from counts in training set)**

| Attribute | $P(\cdot \mid \mathrm{yes})$ | $P(\cdot \mid \mathrm{no})$ |
|-----------|----------------------------|----------------------------|
| age = ≤30 | 2/9 ≈ 0.222 | 3/5 = 0.6 |
| income = medium | 4/9 ≈ 0.444 | 2/5 = 0.4 |
| student = yes | 6/9 ≈ 0.667 | 1/5 = 0.2 |
| credit_rating = fair | 6/9 ≈ 0.667 | 2/5 = 0.4 |

**Step 3 — $P(X \mid C_i)$ (product of the four probabilities)**
- $P(X \mid \mathrm{yes}) = 0.222 \times 0.444 \times 0.667 \times 0.667 \approx 0.044$.
- $P(X \mid \mathrm{no}) = 0.6 \times 0.4 \times 0.2 \times 0.4 = 0.019$.

**Step 4 — $P(X \mid C_i)\,P(C_i)$**
- $P(X \mid \mathrm{yes})\,P(\mathrm{yes}) \approx 0.044 \times 0.643 \approx 0.028$.
- $P(X \mid \mathrm{no})\,P(\mathrm{no}) \approx 0.019 \times 0.357 \approx 0.007$.

**Conclusion:** $0.028 > 0.007$ → **X is classified as buys_computer = yes**.

### Zero-Probability Problem and Laplace Correction

- If any $P(x_k \mid C_i) = 0$, then $P(X \mid C_i) = 0$ and the class gets zero posterior.
- **Laplace correction:** add 1 to each count (or add a small constant) so no probability is zero.
- Example: income = low (0), medium (990), high (10). Corrected: low = 1/1003, medium = 991/1003, high = 11/1003.

### Comments on Naïve Bayes

- **Pros:** Simple, fast, often good accuracy.
- **Cons:** Assumes conditional independence; loss of accuracy when attributes are dependent. Dependencies can be modeled with **Bayesian Belief Networks**.

---

## 4. Rule-Based Classification

### IF-THEN Rules

- **Form:** IF (antecedent conditions) THEN (class).
- **Assessment:**  
  - **Coverage(R)** = (tuples covered by R) / |D|.  
  - **Accuracy(R)** = (tuples correctly classified by R) / (tuples covered by R).
- **Conflict resolution** when several rules fire: **size ordering** (prefer “toughest” rule), **class-based ordering** (e.g., by prevalence or cost), or **rule-based ordering** (decision list by quality or expert order).

### Rule Extraction from a Decision Tree

- One rule per **path from root to leaf**.
- Antecedent = conjunction of attribute-value pairs along the path; consequent = leaf class.
- Rules are **mutually exclusive and exhaustive**.
- Example (from buys_computer tree):  
  IF age = young AND student = no THEN buys_computer = no;  
  IF age = young AND student = yes THEN buys_computer = yes;  
  IF age = mid-age THEN buys_computer = yes;  
  etc.

### Sequential Covering (FOIL, AQ, CN2, RIPPER)

- Learn rules **one at a time** for a class $C_i$.
- After learning a rule, **remove** the positive tuples it covers.
- Repeat on remaining tuples until a stopping condition (e.g., no more examples or rule quality below threshold).
- **Rule generation:** start with empty condition; repeatedly add the predicate that best improves rule quality (e.g., **FOIL-gain**); then **prune** using an independent set of test tuples (e.g., FOIL_Prune = pos/(pos+neg)).

---

## 5. Model Evaluation and Selection

### Confusion Matrix

- **Rows:** actual class; **columns:** predicted class.
- $\mathrm{CM}_{i,j}$: number of class $i$ tuples predicted as class $j$.
- For binary: **TP, FN, FP, TN** (actual \ predicted: C / ¬C).

### Accuracy, Error Rate, Sensitivity, Specificity

- **Accuracy** = (TP + TN) / All.
- **Error rate** = (FP + FN) / All = 1 − Accuracy.
- **Sensitivity (recall for positive class)** = TP / P.
- **Specificity** = TN / N.
- **Class imbalance:** one class rare (e.g., fraud, disease); accuracy can be misleading; sensitivity/specificity and precision/recall are important.

### Precision, Recall, F-Measure

- **Precision** = TP / (TP + FP): among predicted positives, how many are actually positive?
- **Recall** = TP / (TP + FN) = TP / P: among actual positives, how many did we predict?
- **F1 (F-score)** = harmonic mean of precision and recall:
  $$F_1 = \frac{2 \times \mathrm{precision} \times \mathrm{recall}}{\mathrm{precision} + \mathrm{recall}}$$
- **F_β:** weights recall $\beta$ times as much as precision.

### Solved Example 4: Classifier Evaluation (Cancer)

**Confusion matrix:**

| Actual \ Predicted | cancer = yes | cancer = no | Total | Recognition |
|--------------------|-------------|-------------|-------|-------------|
| cancer = yes       | 90 (TP)     | 210 (FN)    | 300 (P) | 30.00% (sensitivity) |
| cancer = no        | 140 (FP)    | 9560 (TN)   | 9700 (N) | 98.56% (specificity) |
| Total              | 230 (P')    | 9770 (N')   | 10000  | 96.40% (accuracy)   |

**Solution:**

- **Precision** = TP / (TP + FP) = 90 / 230 ≈ **39.13%**  
  Interpretation: Of all cases predicted as cancer, 39.13% actually have cancer.

- **Recall** = TP / (TP + FN) = TP / P = 90 / 300 = **30.00%**  
  Interpretation: Of all actual cancer cases, the classifier correctly identified 30%.

- **Accuracy** = (TP + TN) / All = (90 + 9560) / 10000 = **96.40%**.

- **Sensitivity** = TP / P = 90 / 300 = **30.00%** (same as recall for positive class).

- **Specificity** = TN / N = 9560 / 9700 ≈ **98.56%**.

Despite high accuracy, **precision and recall for the positive class (cancer) are low** — typical in **class-imbalanced** settings where the rare class matters most.

### Estimating Accuracy: Holdout, Cross-Validation, Bootstrap

- **Holdout:** Random split into training set (e.g., 2/3) and test set (e.g., 1/3). **Random subsampling:** repeat holdout $k$ times and average accuracies.
- **k-fold cross-validation:** Partition data into $k$ folds; each fold in turn is the test set, rest training; average accuracy. **Stratified:** keep class distribution in each fold similar to the full data. **Leave-one-out:** $k$ = number of tuples.
- **Bootstrap:** Sample $d$ tuples **with replacement** $d$ times → training set; unseen tuples → test set. About 63.2% of data in bootstrap sample, 36.8% in test. Repeat $k$ times and combine (e.g., .632 bootstrap).

### Comparing Classifiers: Confidence Intervals and t-Test

- Use **k-fold cross-validation** to get error rates for models M1 and M2.
- **Null hypothesis:** M1 and M2 have the same error rate.
- **Paired t-test** (same partitioning for both): compute $t$-statistic with $k-1$ degrees of freedom; if we reject the null, the difference is statistically significant and we prefer the model with lower error.
- **Non-paired t-test** when two different test sets are used (with $k_1$ and $k_2$ samples).

### ROC Curves

- **ROC (Receiver Operating Characteristics):** plot **True Positive Rate (sensitivity)** vs. **False Positive Rate (1 − specificity)**.
- **Area under the curve (AUC):** measure of model accuracy; perfect model has AUC = 1; random classifier close to 0.5.
- Rank test tuples by predicted probability of positive class; then build curve by varying threshold.

### Issues in Model Selection

- **Accuracy** (and precision, recall, F, sensitivity, specificity when relevant).
- **Speed:** training time and classification/prediction time.
- **Robustness** to noise and missing values.
- **Scalability** on large databases.
- **Interpretability** (e.g., tree size, rule compactness).

---

## 6. Ensemble Methods

### Goal

- Combine $k$ models $M_1, \ldots, M_k$ to form an improved model $M^*$ and **increase accuracy**.

### Bagging (Bootstrap Aggregation)

- **Training:** From dataset $D$ of size $d$, at each iteration $i$, sample $d$ tuples **with replacement** → $D_i$; train classifier $M_i$ on $D_i$.
- **Classification:** For unknown $X$, each $M_i$ votes; **majority class** is the final prediction. For regression, average the predictions.
- **Effect:** Often better and more robust than a single classifier; especially helpful with noise.

### Boosting

- **Idea:** Weight training tuples; iteratively train classifiers and **increase weights** for misclassified tuples so next classifier focuses on them.
- **Prediction:** Weighted vote of the $k$ classifiers (weights based on accuracy).
- **Effect:** Often higher accuracy than bagging, but higher risk of **overfitting** to misclassified examples.

### AdaBoost (Freund and Schapire, 1997)

- Start with equal weights $1/d$ for all tuples.
- For each round $i$: sample $D_i$ **with replacement** according to current weights; train $M_i$; compute error as **sum of weights** of misclassified tuples.
- **Classifier vote weight:** $\log((1 - \mathrm{error}(M_i))/\mathrm{error}(M_i))$.
- **Update tuple weights:** increase if misclassified, decrease if correct.

### Random Forest (Breiman 2001)

- **Construction:** Each model is a **decision tree**; at each node, use a **random subset of attributes** (e.g., Forest-RI: $F$ random attributes; Forest-RC: random linear combinations of attributes) to choose the split; grow to maximum size.
- **Classification:** Each tree votes; **majority class** is returned.
- **Properties:** Accuracy often comparable to AdaBoost; **robust** to errors and outliers; relatively **insensitive** to number of attributes per split; can be **faster** than bagging/boosting.

### Class-Imbalanced Data

- **Problem:** Rare positive class (e.g., fraud, disease), many negatives.
- **Methods:**  
  - **Oversampling:** duplicate or resample positive examples.  
  - **Under-sampling:** reduce negative examples.  
  - **Threshold-moving:** shift decision threshold so positive class is easier to predict (reduce false negatives).  
  - **Ensemble techniques:** combine with the methods above.  
- Multiclass imbalance remains difficult.

---

## 7. Summary

- **Classification** extracts models that describe data classes; effective and scalable methods exist for **decision trees**, **Naïve Bayes**, **rule-based** classifiers, and others.
- **Evaluation:** accuracy, sensitivity, specificity, precision, recall, F and $F_\beta$; **stratified k-fold cross-validation** is recommended for estimating accuracy.
- **Ensembles** (e.g., **bagging**, **boosting**, **Random Forest**) can improve accuracy by combining multiple models.
- **Model selection:** significance tests and **ROC curves**; no single method is best for all datasets; trade-offs involve accuracy, training time, robustness, scalability, and interpretability.

---

## Quick Reference: Formulas

| Concept | Formula |
|--------|---------|
| Entropy | $\mathrm{Info}(D) = -\sum_i p_i \log_2 p_i$ |
| Info after split on A | $\mathrm{Info}_A(D) = \sum_j \frac{\|D_j\|}{\|D\|} \mathrm{Info}(D_j)$ |
| Information gain | $\mathrm{Gain}(A) = \mathrm{Info}(D) - \mathrm{Info}_A(D)$ |
| Gini | $\mathrm{gini}(D) = 1 - \sum_j p_j^2$ |
| Bayes | $P(C_i \mid X) \propto P(X \mid C_i) P(C_i)$, Naïve: $P(X \mid C_i) = \prod_k P(x_k \mid C_i)$ |
| Accuracy | (TP + TN) / All |
| Precision | TP / (TP + FP) |
| Recall (sensitivity for positive) | TP / (TP + FN) = TP / P |
| F1 | $F_1 = \frac{2 \cdot \mathrm{precision} \cdot \mathrm{recall}}{\mathrm{precision} + \mathrm{recall}}$ |

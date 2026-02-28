# IST691: Hypothesis Testing — Summary

Summary of the course material **Hypothesis Testing** (Research Methodology and Scientific Writing).

---

## 1. Outline

- Data collection (sample size, procedure, approval, consent, debriefing)
- Statistics: review of fundamental concepts (central tendency, variance, normal distribution, z-scores)
- Inferential statistics (descriptive vs inferential, confidence intervals, regression)
- Hypothesis testing (critical values, significance, errors, rejection regions, p-values, t-test, ANOVA)

---

## 2. Data Collection Issues

### 2.1 Sample Size

- **Important** for accurate, statistically meaningful results.
- **Too small:** Outliers and anomalies can be overrepresented → skewed results, poor picture of the population.
- **Too large:** Study becomes complex, expensive, and time-consuming; gains in accuracy may not justify the cost.

**Computing sample size (known population):** Need (1) **population size** *N* (if very large and unknown, 100,000 is often used); (2) **margin of error** (confidence interval) — smaller margin = higher accuracy; (3) **confidence level** (e.g. 90%, 95%, 99%) — how sure we are the true value falls within the margin; (4) **standard deviation** — spread of data (0.5 often used as a conservative choice); (5) **sample proportion** *p* (from prior studies or pilot; if unsure, 0.5 gives largest sample). Use **z-scores** for the chosen confidence level (e.g. 95% two-tailed → 1.96) and the appropriate **formula** for sample size.

**Unknown population:** Use a formula that relies on confidence level, margin of error, and standard deviation (e.g. 0.5) without *N*.

### 2.2 Procedure

- **Pilot study:** A small run-through of the experiment. **Benefits:** Reveals poorly worded instructions; suggests whether the IV manipulation works as intended; gives the researcher practice.

### 2.3 Institutional Approval

- Studies involving **humans** or **animals** often require approval.
- **IACUC** (Institutional Animal Care and Use Committee): Reviews use of animals (e.g. minimizing pain, appropriate surgical care).
- **IRB** (Institutional Review Board): Reviews human-subject research; primary concern is **welfare** of participants (informed consent, avoidance of harm).

### 2.4 Participant Consent

- Participants must **consent** except when the study is **exempt** (e.g. anonymous surveys, observation of public behaviour).
- **Consent form:** Gives full information so participants can make an **informed** choice.

### 2.5 Debriefing (Post-experimental Interview)

- Interview **after** the experiment in which the study is **explained** and the participant can **comment**.

---

## 3. Statistics: Fundamental Concepts

### 3.1 Central Tendency

- **Mean:** Arithmetic average.  
- **Median:** Middle value; splits the data in half.  
- **Mode:** Most frequently occurring value.

### 3.2 Variance and Standard Deviation

- **Variance (σ² or s²):** Measure of how **spread out** data are from the mean. Population σ², sample s².  
- **Standard deviation (σ or s):** Spread of data; deviation from the mean. In **original units** (variance is in squared units). SD is often used to describe variability; variance is often used in formulas.

### 3.3 Normal Distribution

- **Importance:** Describes many natural phenomena (heights, blood pressure, measurement error, IQ). Symmetric around the mean; most values near the centre; probabilities decrease equally in both tails.
- **Properties:** Bell-shaped; mean = median = mode at the peak; half of values below and half above the mean.
- **Empirical rule:** ~68% within ±1 SD; ~95.4% within ±2 SD; ~99.7% within ±3 SD. Values beyond ±3 SD are rare.

### 3.4 Standard Normal Curve (Z-Distribution)

- Normal distribution with **mean = 0** and **SD = 1**. Any normal distribution can be converted to it using **z-scores**.
- **Z-score (standard score):** Number of **standard deviations** a value is from the mean. Formula: **z = (X − μ) / σ**.  
  - z &lt; 0: below mean; z &gt; 0: above mean; z = 1: 1 SD above mean; etc.  
  - About 68% of values between −1 and 1; ~95% between −2 and 2; ~99% between −3 and 3.
- **Uses:** Find probability above/below a value; compare sample mean to population mean; compare scores across different distributions.

---

## 4. Descriptive vs Inferential Statistics

| | Descriptive | Inferential |
|--|-------------|-------------|
| **Goal** | Summarize and graph **the data you have** (e.g. one sample). | Use **sample** data to make conclusions about the **population**. |
| **Uncertainty** | No inference; you describe only what you measured. | Incorporates **sampling error**; results are uncertain. |
| **Tools** | Central tendency, dispersion (range, SD), skewness, 5-number summary, correlation, scatter plots. | Hypothesis tests, confidence intervals, regression. |

**Inferential statistics:** Define the population; draw a **representative sample** (e.g. random); use methods that account for **sampling error**. **Confidence interval (CI):** A range of values that is likely to contain the unknown **population parameter**; built from sample data and a chosen **confidence level**; provides a margin of error around the estimate. **Regression:** Describes the relationship between independent and dependent variables and often includes hypothesis tests for whether relationships hold in the population.

---

## 5. Hypothesis Testing: Core Ideas

### 5.1 Critical Values

- **Critical value:** A boundary in the **sampling distribution** of the test statistic. Defines how different the sample result must be from the null hypothesis to be **statistically significant**. Used in both hypothesis tests and confidence intervals to handle uncertainty.

### 5.2 Significance Level (α)

- **α (alpha):** Set **before** the study. Probability of **rejecting the null when it is true** (Type I error).  
- Example: α = 0.05 → 5% risk of concluding a difference exists when there is none.  
- **Lower α** → need **stronger evidence** to reject the null.

### 5.3 Type I and Type II Errors

| | Null true | Null false |
|--|-----------|------------|
| **Reject null** | **Type I error** (α) — false positive | Correct (power) |
| **Do not reject null** | Correct | **Type II error** (β) — false negative |

- **Type I:** Support the alternative when the null is true (e.g. convict innocent person). **α = P(Type I)**.  
- **Type II:** Fail to support the alternative when it is true (e.g. let guilty person go). **β = P(Type II)**.

### 5.4 Rejection Region (Critical Region)

- **Rejection region:** Range of values of the test statistic for which we **reject the null** (and accept the alternative).  
- **One-tailed test:** One rejection region — either “greater than” (right-tailed) or “less than” (left-tailed). Used when the hypothesis is **directional**.  
- **Two-tailed test:** Two rejection regions — “different from” in either direction. Used when we care about **any** difference.  
- **Rejection region and α:** For 95% confidence, α = 0.05. That 5% is the total rejection region (all in one tail for one-tailed; split across two tails for two-tailed).

### 5.5 P-Value and Critical Value Methods

- **P-value:** Probability of obtaining the **observed effect (or larger)** in the sample **if the null hypothesis is true**. Lower p-value = stronger evidence against the null.  
- **Decision:** If **p ≤ α** → reject the null (statistically significant). If p &gt; α → do not reject.  
- **Critical value method:** Compare the **test statistic** to the **critical value(s)**. If the test statistic falls in the rejection region (e.g. |z| ≥ 1.96 for α = 0.05 two-tailed), reject the null.  
- **Two-tailed (α = 0.05):** Reject if z ≤ −1.96 or z ≥ 1.96 (α/2 in each tail). **One-tailed:** One critical value; full α in one tail.

---

## 6. Selecting a Statistical Test

- The **experimental design** determines **which test** to use. Data are analyzed to see whether group differences are **too large to be due to chance**.  
- **Design the study with the planned analysis in mind** so the design (and test) **answers the research question**.

### 6.1 When to Use Z-Score vs T-Score

| Use **z** when | Use **t** when |
|----------------|----------------|
| **Population SD (σ) is known** and | **Population SD is unknown** (use sample SD *s*), or |
| Sample size is **large** (e.g. &gt; 30) | Sample size is **small** (e.g. &lt; 30) |

- **Rule of thumb:** In many studies σ is unknown → use **t**.  
- **z = (X − μ) / σ** (population). **t** uses sample SD: e.g. **t = (X − μ) / [s/√n]**.
- For large *n*, *t* and *z* are similar. Use the **t-table** (or software) for critical values when using *t*.

---

## 7. Independent Samples t-Test

- **Purpose:** Compare **means of two independent groups** to see if the difference is **too large to attribute to chance**.
- **Example (document):** Two groups of rats (0.5 vs 1.0 mg/kg cocaine); outcome = number of lever presses. **H₀:** No increase in abuse as access increases. **Hₐ:** Abuse increases as access increases.  
- **Design:** One IV (dose), two levels, different participants → **independent-samples t-test** (parametric comparison of means).  
- **Steps:** Compute **t-statistic** (difference in means relative to variability). Choose **α** (e.g. 0.05). **Degrees of freedom** = N − 2 (total number of scores minus 2). Compare computed *t* to **critical value** from t-table (one- or two-tailed). If |t| &gt; critical value → reject H₀.  
- **Document example:** t = 3.39, df = 22, one-tailed α = 0.05, critical t = 1.717. 3.39 &gt; 1.717 → reject H₀; the difference is statistically significant. (Descriptively, lower dose had higher mean presses in that example.)

---

## 8. Analysis of Variance (ANOVA)

### 8.1 Role and One-Way ANOVA

- **ANOVA** extends the t-test when there are **more than two groups** or **more than one IV**.
- **One-way ANOVA:** One IV with **two or more levels**; appropriate for **simple randomized** (between-participants) designs.
- **Key ideas:**  
  - **Total variation** = **between-groups** (SSbet) + **within-groups** (SSwithin).  
  - **Between-groups:** Variation due to the IV and chance.  
  - **Within-groups:** Variation within each group (chance/error).  
  - **Mean square (MS):** SS divided by its degrees of freedom (MSbet, MSwithin).  
  - **F-ratio:** **F = MSbet / MSwithin.** Large F → group means differ more than expected by chance.
- **Decision:** Compare **computed F** to **critical F** (from F-table using df for between and within, and α). If F &gt; critical F → reject H₀; conclude there are significant differences among groups. Then use **descriptive statistics** (e.g. group means) to see which groups differ.

### 8.2 Two-Way ANOVA

- Used for **factorial designs** with **two (or more) IVs** to study **main effects** and **interaction**.
- **Example (document):** Caffeine pretreatment (yes/no) × cocaine dose (0.1, 0.5, 1.0 mg/kg).  
- **Summary table:** Gives F-ratios for each main effect and for the interaction. Compare each to the appropriate **critical F** (using df for that effect and for error).  
- **Interpretation:** Significant **main effect** of A (or B) → that factor affects the DV. Significant **interaction** → the effect of one factor **depends on** the level of the other. If interaction is significant, interpret it rather than main effects alone.

---

## 9. Potential Errors in the Statistical Decision-Making Process

- The main **decision errors** in hypothesis testing are **Type I** (reject true null; controlled by α) and **Type II** (fail to reject false null; related to power and sample size).  
- Researchers choose **α** to limit Type I error; **sample size** and **effect size** influence Type II error and **power** (probability of correctly rejecting a false null).

---

*End of summary.*

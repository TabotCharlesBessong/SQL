# IST691: Research Methodology and Scientific Writing — Summary & Practice

This document summarizes two course materials: **Introduction** (science, research, scientific method) and **Control in Experimentation**, and provides practice questions with answers and explanations.

---

## Part 1: Summary of “Introduction” (Research Methodology)

### 1.1 What is Science?

- **Science** is a systematic way of building and organizing knowledge through testable explanations and predictions.
- It studies the structure and behaviour of the physical and natural world via **observation**, **experimentation**, and **testing theories** against evidence.
- **Computer Science** is the systematic study of computing systems and computation, including theories, design methods, algorithms, testing, analysis, verification, and knowledge representation.

### 1.2 What is Research?

- **Research** is intellectual activity aimed at **discovering**, **interpreting**, and **revising** knowledge about the world.
- It is often (but not always) based on the scientific method.
- Purposes: discover something new, interpret the unexplained, or revise what is wrong or incomplete.
- **Computer Science Research** applies scientific methods to topics such as algorithms, AI, databases, networking, ML, NLP, IoT, etc., with the goal of advancing knowledge, developing technologies, and solving problems through hypotheses, experiments/simulations, and evidence-based conclusions.

### 1.3 Methods of Acquiring Knowledge (Non-Scientific vs Scientific)

There are several ways people gain knowledge; only one is the **scientific method**. The others can still play a role in daily life or in generating ideas, but they do not by themselves build reliable scientific knowledge:

| Method        | Description | Main problem |
|---------------|-------------|--------------|
| **Tenacity**  | Holding to habit or superstition; “we’ve always believed it.” | No way to correct errors when evidence contradicts the belief. |
| **Intuition** | Relying on gut, emotion, or instinct rather than facts or logic. | Can be wrong due to cognitive and motivational biases; sometimes useful when analysis is paralyzing. |
| **Authority** | Accepting claims because an authority says they are true. | The authority may be wrong; we can still evaluate their credentials and methods. |
| **Rationalism** | Using logic and reasoning from stated premises. | If premises are wrong or logic is flawed, conclusions are invalid; easy to make logical errors without training. |
| **Empiricism** | Gaining knowledge through observation and experience. | Observations and experience can be wrong (e.g. flat earth, optical illusions, experimenter expectations). |

The **scientific method** combines **systematic empiricism** (careful, controlled observations) with **rationalism** (logical conclusions), making it the most reliable way to produce valid knowledge. Limitations: not always feasible, can be costly and time-consuming, and applies only to **empirical** questions.

### 1.4 The Scientific Method

- **Definition:** A process for experimentation used to explore observations and answer questions; the goal is to discover cause–effect relationships by asking questions, gathering and examining evidence, and combining information into a logical answer.
- **Steps:** (1) Identify the problem and formulate a hypothesis, (2) Design the experiment, (3) Conduct the experiment, (4) Test the hypothesis, (5) Communicate the results.
- Scientists may use intuition, authority, rationalism, or empiricism to *generate* ideas, but they *test* those ideas through systematic, controlled observation and logic.
- The process can be iterative: new information may require going back and repeating steps.

### 1.5 Characteristics of the Scientific Approach

- **Control:** Eliminating or holding constant extraneous variables so that causes of observations can be identified; central to the scientific method.
- **Operational definition:** Defining concepts by the steps or operations used to measure or produce them (e.g. “hunger” = 8 hours of food deprivation) to avoid ambiguity.
- **Replication:** Results must be reproducible; the same findings should be obtainable if the study is repeated.

### 1.6 Objectives of Science

Science aims to **understand** the world. Understanding is taken to include:

- **Description:** Accurately portraying a phenomenon and the degree to which variables exist.
- **Explanation:** Determining the cause(s) of a phenomenon.
- **Prediction:** Anticipating when an event will occur.
- **Control:** Manipulating the conditions that determine a phenomenon.

### 1.7 Basic Assumptions Underlying Science

- **Uniformity in nature:** There are order, regularities, and lawful relations among events; without this, understanding, theories, and facts would not be possible.
- **Determinism:** Behaviour and events are caused by specific factors; science seeks those determinants.
- **Axioms** supporting inquiry:
  - **Reality:** What we perceive is real and has substance.
  - **Rationality:** Events have a rational basis and can be understood through logic.
  - **Regularity:** The same laws apply across times and places.
  - **Discoverability:** It is possible to discover these uniformities.

### 1.8 Method vs Technique

- **Method** refers to the common logic of inquiry (the scientific method).
- **Technique** is the specific tool or procedure (e.g. telescope, microscope, one-way mirror) used depending on the subject, problem, and stage of inquiry.

---

## Part 2: Summary of “Control in Experimentation”

### 2.1 Internal Validity and Confounding

- **Internal validity** is the extent to which we can accurately say that the **independent variable (IV)** produced the observed effect on the **dependent variable (DV)** — i.e. that the effect is due to the experimental treatment, not other factors.
- **Extraneous variable:** Any variable other than the IV that can influence the DV.
- **Confounding:** When a variable systematically varies with the IV and also affects the DV. A **confounding variable** can distort or hide the true effect of the IV and lead to wrong cause–effect conclusions (e.g. in “coffee and heart disease,” smoking can be the confounder).
- **Ways to address confounders:** Randomization, blinding (single/double), stratification, and statistical adjustment.

### 2.2 Threats to Internal Validity (Extraneous Variables to Control)

| Threat | Description |
|--------|-------------|
| **History** | External events during the study that affect participants (e.g. a new health campaign during a diet study). |
| **Maturation** | Internal changes in participants over time (e.g. aging, fatigue, learning) that affect outcomes. |
| **Testing** | Pre-test effects (e.g. familiarity or sensitization) affecting post-test scores. |
| **Instrumentation** | Changes in measurement tools or procedures between measurements (e.g. different interviewers, worn equipment). |
| **Statistical regression** | Extreme pre-test scores tending to move toward the mean on post-test, so “improvement” may be regression, not treatment. |
| **Selection (selection bias)** | Pre-existing differences between groups due to non-random assignment (e.g. one group more capable or motivated). |
| **Experimental mortality** | Differential drop-out across groups, so remaining participants no longer represent the original sample. |

### 2.3 Constancy

- Even when extraneous variables cannot be **eliminated**, we can try to **hold their influence constant** across all levels of the IV.
- **Constancy:** The influence of an extraneous variable is the same in all treatment conditions, so it does not differentially affect the comparison.

### 2.4 Techniques for Achieving Constancy

1. **Randomization**
   - **Random sampling:** Each member of the population has an equal chance of being selected; helps obtain a representative sample.
   - **Random assignment:** Participants are randomly assigned to treatment groups so that extraneous variables are distributed similarly across groups; maximizes group equivalence but does not eliminate extraneous variables.
   - Variants: simple random sampling, stratified random sampling, systematic random sampling, cluster sampling (single- or multi-stage).
   - Randomization does not guarantee perfect balance; other techniques (matching, counterbalancing, etc.) may still be needed.

2. **Matching**
   - Equating participants across groups on variables thought to be related to the IV or to confound the effect.
   - **Blocking:** Building the extraneous variable into the design as another IV (use when the effect of that variable is of interest).
   - **Equating participants:** Forming equivalent groups by matching on the control variable; group size is typically a multiple of the number of levels of the IV.
   - Increases sensitivity and controls for the matched variables.

3. **Counterbalancing**
   - Controls **sequencing effects** when participants experience multiple conditions.
   - **Order effects:** Due to position (e.g. practice, fatigue).
   - **Carry-over effects:** Performance in one condition affecting the next.
   - Procedures: randomized counterbalancing (random order per participant), intra-subject (e.g. ABBA), intra-group (different groups get different orders), incomplete counterbalancing (subset of sequences so each condition appears in each position and, if possible, each condition precedes/follows every other equally).

4. **Control of Participant Effects**
   - Participants may try to present themselves in a favourable way or react to their beliefs about the study.
   - **Double-blind placebo:** Neither participant nor experimenter knows who receives treatment vs placebo.
   - **Deception:** Providing a cover story or false rationale unrelated to the real hypothesis; must be justified ethically and kept constant for all participants.

5. **Control of Experimenter Effects**
   - **Recording errors:** Reduced by training, multiple recorders/observers, or automated recording (e.g. computers, video).
   - **Attribute errors:** Experimenter attributes (e.g. age, gender) can interact with treatment; sometimes the same experimenter is used in all conditions, unless that would create an interaction.
   - **Expectancy effects:** **Blind technique** — experimenter does not know each participant’s condition, so they cannot treat groups differently; **partial blind** when full blind is impossible; **automation** (written/recorded instructions, automated response collection) to remove experimenter–participant interaction.

---

## Part 3: Practice Questions

**Distribution:** Easy 25%, Normal 40%, Hard 35%.  
**Types:** Multiple choice (MCQ), short/structural, and complete-the-statement.  
**Note:** Correct answers for MCQs are deliberately placed in different positions (A, B, C, D) to avoid bias.

---

### Section A: Easy (25% — 5 questions)

**1. [MCQ — Easy]**  
A researcher defines “anxiety” as “a score above 30 on the State-Trait Anxiety Inventory.” This is an example of:

- A) A theoretical definition  
- **B) An operational definition**  
- C) A confounding variable  
- D) Replication  

**Answer: B**  
**Explanation:** An operational definition specifies how a concept is measured or produced (the steps or operations). Here, anxiety is defined by the instrument and the cutoff score, which removes ambiguity and supports replication.

---

**2. [MCQ — Easy]**  
Which of the following best describes “internal validity”?

- A) The extent to which a measure is consistent over time  
- B) The extent to which participants are randomly selected  
- C) The extent to which results apply to other populations or settings  
- **D) The extent to which the observed effect can be attributed to the independent variable**  

**Answer: D**  
**Explanation:** Internal validity concerns whether the IV actually caused the change in the DV, rather than extraneous or confounding variables. The other options refer to external validity, reliability, or sampling.

---

**3. [Structural — Easy]**  
Name two methods of acquiring knowledge that are *not* the scientific method, and state one limitation of each.

**Answer (example):**  
- **Authority:** Limitation — the authority may be wrong.  
- **Intuition:** Limitation — can be wrong due to cognitive or motivational biases.  
(Other pairs such as tenacity, rationalism, empiricism are also acceptable with correct limitations.)

---

**4. [Complete — Easy]**  
In the scientific method, ________ is considered the most important element because it allows researchers to eliminate or hold constant ________ that could otherwise affect the observations.

**Answer:** control; extraneous variables  
**Explanation:** Control is the central feature that allows cause–effect conclusions by removing or holding constant extraneous influences.

---

**5. [MCQ — Easy]**  
“Events in nature follow the same laws at all times and places.” This assumption is called:

- **A) Regularity**  
- B) Determinism  
- C) Discoverability  
- D) Rationality  

**Answer: A**  
**Explanation:** Regularity is the assumption that natural laws are consistent across time and place. Determinism refers to causes of behaviour; discoverability to the possibility of finding uniformities; rationality to understanding through logic.

---

### Section B: Normal (40% — 8 questions)

**6. [MCQ — Normal]**  
In a study on tutoring and grades, if tutored students are on average brighter than non-tutored students, then intelligence in this context is best described as:

- A) The dependent variable  
- B) The independent variable  
- C) A controlled variable  
- **D) An extraneous (or confounding) variable**  

**Answer: D**  
**Explanation:** The IV is tutoring; the DV is grades. Intelligence is another factor that could explain differences in grades and is correlated with who gets tutoring, so it is an extraneous/confounding variable that threatens internal validity.

---

**7. [MCQ — Normal]**  
Which threat to internal validity is best described as “extreme pre-test scores tending to move toward the mean on post-test”?

- A) History  
- B) Maturation  
- **C) Statistical regression (regression to the mean)**  
- D) Instrumentation  

**Answer: C**  
**Explanation:** Statistical regression (regression to the mean) occurs when individuals selected for extreme scores later show less extreme scores even without any treatment. History is external events; maturation is internal change over time; instrumentation is change in measurement.

---

**8. [MCQ — Normal]**  
Random assignment of participants to treatment groups primarily:

- **A) Distributes extraneous variables roughly equally across groups**  
- B) Ensures the sample is representative of the population  
- C) Eliminates all extraneous variables  
- D) Guarantees that groups will be identical on every variable  

**Answer: A**  
**Explanation:** Random assignment aims to equate groups by distributing known and unknown extraneous variables across conditions. It does not eliminate them, guarantee equality on every variable, or by itself ensure a representative sample (that is the role of random sampling).

---

**9. [Structural — Normal]**  
List the five main steps of the scientific method in order.

**Answer:**  
(1) Identify the problem and formulate a hypothesis  
(2) Design the experiment  
(3) Conduct the experiment  
(4) Test the hypothesis  
(5) Communicate the research results  

---

**10. [MCQ — Normal]**  
Counterbalancing is used mainly to control for:

- A) Experimenter expectations  
- B) Selection bias  
- C) Differences between participants in different groups  
- **D) Sequencing effects (e.g. order and carry-over effects)**  

**Answer: D**  
**Explanation:** Counterbalancing addresses the order in which conditions are presented and carry-over from one condition to another. The other options are addressed by randomization, blinding, or matching.

---

**11. [Complete — Normal]**  
In the double-blind placebo design, neither the ________ nor the ________ knows which participants receive the actual treatment versus the placebo, which helps control both participant and ________ effects.

**Answer:** participant; experimenter (or researcher); experimenter (or expectancy)  
**Explanation:** Double-blind keeps both participants and experimenters unaware of condition to reduce placebo and expectancy effects.

---

**12. [Structural — Normal]**  
Give one difference between “matching by building the extraneous variable into the design” (blocking) and “matching by equating participants.” When would you use blocking?

**Answer (example):**  
- Blocking turns the extraneous variable into an additional independent variable with levels (e.g. low/medium/high IQ); equating creates groups that are similar on the control variable without making it a factor in the design.  
- Use blocking when you are interested in the effect of the extraneous variable (e.g. whether IQ moderates the effect of the treatment).

---

**13. [MCQ — Normal]**  
Which of the following is *not* an axiom underlying scientific inquiry as discussed in the course?

- **A) Replication**  
- B) Reality  
- C) Rationality  
- D) Discoverability  

**Answer: A**  
**Explanation:** The four axioms are Reality, Rationality, Regularity, and Discoverability. Replication is a characteristic of the scientific approach (reproducibility of results), not one of these foundational axioms.

---

### Section C: Hard (35% — 7 questions)

**14. [MCQ — Hard]**  
A researcher runs an experiment where all participants receive condition A then B. Participants perform better in B. Which of the following is *most* likely to threaten internal validity here?

- A) Experimental mortality  
- B) History  
- **C) Order or carry-over effects (e.g. practice)**  
- D) Selection bias  

**Answer: C**  
**Explanation:** When everyone gets A then B, improvement in B could be due to practice or carry-over from A, not the treatment itself. Counterbalancing or randomizing order would address this. The other options are less directly tied to the fixed order of conditions.

---

**15. [MCQ — Hard]**  
“Systematic empiricism” in the scientific method refers to:

- **A) Making careful, controlled observations to test ideas**  
- B) Using only logic and deduction to reach conclusions  
- C) Accepting the views of expert authorities  
- D) Relying on personal experience and intuition  

**Answer: A**  
**Explanation:** Systematic empiricism means gathering evidence through structured, controlled observation rather than casual experience. Logic is used to interpret that evidence; authority and intuition are not the defining features of systematic empiricism here.

---

**16. [MCQ — Hard]**  
Stratified random sampling is most useful when:

- A) The population is very small  
- B) You want to minimize the number of participants  
- C) All participants must receive every treatment condition  
- **D) You need the sample to represent specific subgroups (strata) in the population**  

**Answer: D**  
**Explanation:** Stratified sampling divides the population into strata (e.g. by age, gender) and samples from each to ensure representation of those subgroups. It is not primarily about small populations, minimizing N, or within-subjects designs.

---

**17. [Structural — Hard]**  
Explain why “empiricism alone” is considered insufficient for science, and how the scientific method addresses this.

**Answer (example):**  
Empiricism (relying on observation and experience) can be wrong because of illusions, expectations, or limited conditions (e.g. “backwards satanic messages” or flat earth). The scientific method uses *systematic* empiricism: controlled conditions, operational definitions, and replication, and combines it with rational interpretation of evidence. So science does not rely on raw experience alone but on structured observation and logic.

---

**18. [Complete — Hard]**  
If the number of treatment conditions in an incomplete counterbalancing design is **odd**, a common remedy is to add a second set of sequences that are the ________ of the first set, so that each condition precedes and follows every other condition the same number of times.

**Answer:** reverse  
**Explanation:** With an odd number of conditions, the standard incomplete counterbalancing pattern does not satisfy the “each condition precedes and follows every other equally” rule. Adding the reverse sequences fixes this.

---

**19. [MCQ — Hard]**  
Control of “experimenter expectancies” is best achieved by:

- A) Using the same experimenter in all conditions  
- B) Training the experimenter to record data carefully  
- **C) Keeping the experimenter blind to each participant’s treatment condition**  
- D) Using a very large sample size  

**Answer: C**  
**Explanation:** Expectancy effects occur when the experimenter’s knowledge of condition influences participant behaviour or recording. The blind technique (experimenter does not know who is in which condition) directly addresses this. Same experimenter, training, and sample size do not by themselves prevent expectancies.

---

**20. [Structural — Hard]**  
In the “coffee and heart disease” example, smoking is a confounding variable. Explain in one or two sentences why randomization of participants to “high” vs “low” coffee consumption groups would not remove this confound, and what design or analysis strategy could help instead.

**Answer (example):**  
Randomization would assign people to different *levels of coffee consumption*, but coffee consumption is a behaviour, not a randomly assigned treatment — so we cannot randomly assign who drinks more coffee. Randomization therefore cannot equalize smoking across “coffee groups.” Instead, we could measure smoking and use stratification (e.g. compare coffee and heart disease within smokers and within non-smokers separately) or statistical adjustment (e.g. regression controlling for smoking) to reduce confounding.

---

## Quick Reference: MCQ Answer Key (by position)

| Q  | Correct option |
|----|-----------------|
| 1  | B               |
| 2  | D               |
| 5  | A               |
| 6  | D               |
| 7  | C               |
| 8  | A               |
| 10 | D               |
| 13 | A               |
| 14 | C               |
| 15 | A               |
| 16 | D               |
| 19 | C               |

*(Distribution: A = 4, B = 1, C = 4, D = 4 — spread across options to avoid positional bias.)*

---

*End of summary and practice questions.*

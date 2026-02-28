# IST691: Control in Experimentation — Summary

Summary of the course material **Control in Experimentation** (Research Methodology and Scientific Writing).

---

## 1. Outline

- Introduction (internal validity, extraneous and confounding variables)
- Control of extraneous variables (constancy)
- Techniques for achieving constancy (randomization, matching, counterbalancing, participant effects, experimenter effects)

---

## 2. Introduction

### 2.1 Internal Validity

- A major goal in any experiment is **internal validity**.
- **Internal validity:** The extent to which we can accurately state that the **independent variable** produced the observed effect — i.e. the extent to which the observed effect is caused **only** by the experimental treatment condition.

### 2.2 Why Control Matters

- The **dependent variable** can be influenced by variables **other than** the independent variable.
- **Example:** Studying the effect of **tutoring** (IV) on **grades** (DV). If tutored students are on average brighter than non-tutored students, the improvement in grades might be due to **intelligence**, not tutoring. Intelligence is an **extraneous variable** that threatens internal validity.

### 2.3 Key Definitions

| Term | Definition |
|------|------------|
| **Extraneous variable** | Any variable **other than the IV** that influences the dependent variable. |
| **Confounding** | Occurs when a variable **systematically varies with** the independent variable and also affects the DV. |
| **Confounding variable** | A variable not included (or not controlled) in the experiment that affects the relationship between the IV and DV; it can affect **both**, causing unexpected results and **unreliable** conclusions. |

### 2.4 Confounding Variable: Characteristics and Example

- **Key characteristics:** (1) **Correlated with the IV** (e.g. coffee drinking); (2) **Causally related to the DV** (e.g. heart disease).
- **Example — Coffee and heart disease:** If we hypothesize that coffee causes heart disease (IV = coffee consumption, DV = heart disease), **smoking** can be a confounder: smokers often drink more coffee, and smoking causes heart disease. The confounder can make it seem as if coffee causes heart disease when **smoking** may be the real cause.

**Why confounders matter:** They **distort** results (hide or exaggerate the true effect of the IV) and can **invalidate** cause-and-effect conclusions.

**How to control confounders:** Randomization, blinding (single or double), stratification (analyze within groups defined by the confounder), and statistical adjustment.

---

## 3. Control of Extraneous Variables: Constancy

- Some extraneous variables can be **eliminated** (especially in the lab), but many **cannot**.
- Even when elimination is not possible, we can **eliminate the differential influence** of such variables across the **levels of the IV** — i.e. keep their influence **constant** across all treatment conditions.
- **Constancy:** Stability (absence of change) in the influence exerted by an extraneous variable in **all** treatment conditions.

---

## 4. Extraneous Variables to Be Controlled (Threats to Internal Validity)

| Threat | Description | Example / note |
|--------|-------------|----------------|
| **History** | External events during the study that affect participants, unrelated to the treatment. | A new public health campaign during a diet study. |
| **Maturation** | Natural, internal changes in participants over time (e.g. aging, fatigue, learning) that might alter behaviour. | In a long project, participants may improve regardless of treatment. |
| **Testing** | The effect of taking a **pre-test** on the **post-test** (e.g. familiarity, sensitization). | Pre-test influences post-test scores. |
| **Instrumentation** | Changes in the **measurement tool or procedure** between measurements (e.g. worn scale, different interviewers). | What is being assessed changes. |
| **Statistical regression (regression to the mean)** | Extreme pre-test scores tend to move toward the population mean on post-test. | If participants are selected for extreme scores (e.g. lowest performers), “improvement” may be regression, not the program. |
| **Selection (selection bias)** | Pre-existing differences between groups, often due to **non-random assignment**. | One group more motivated or capable; outcome differences may be due to selection, not treatment. **Control:** Random assignment, matching. |
| **Experimental mortality** | **Drop-out** from the study, especially if **unequal** across groups. | Remaining participants may not represent the original sample (e.g. more motivated stay), skewing results. |

---

## 5. Techniques for Achieving Constancy

Five main categories: **Randomization**, **Matching**, **Counterbalancing**, **Control of Participant Effects**, **Control of Experimenter Effects**.

---

## 6. Randomization

### 6.1 Role

- A control technique that **equates groups** by ensuring every member has an **equal chance** of being assigned to any group.
- **Random sampling** from a population helps ensure no **systematic bias** in selection and that the sample is **representative** of the population.
- **Representative sample:** Participants have the same characteristics (on relevant dimensions) as the population.
- A representative sample is obtained by **random sampling**.
- **Random sample:** Each person has an **equal chance** of being selected, and the selection of one does **not** affect the selection of another.
- **Random assignment:** Randomly selected participants are **randomly assigned** to as many groups as there are experimental treatment conditions.

### 6.2 What Random Assignment Does

- Provides strong assurance that groups are **equal** (on average).
- **Eliminates systematic differences** between groups.
- **Does not eliminate** extraneous variables but **randomly distributes** them across groups, so their influence is **held constant** across conditions.

### 6.3 Variants of Randomization

| Type | Description |
|------|-------------|
| **Simple random sampling** | Each member of the population is equally likely to be chosen. Purest and most straightforward; considered the most unbiased representation of the population. |
| **Stratified random sampling** | Population divided into **strata** (subgroups) by one or more attributes (e.g. sex, age, income, education); subjects selected from each stratum in a **proportionate** manner. Goal: guarantee representation of specific subgroups. |
| **Systematic random sampling** | (Referenced in outline; typically selecting every *k*th unit from an ordered list after a random start.) |
| **Cluster sampling** | Population subdivided into **clusters** (natural groups); a **few clusters** are chosen randomly. Clusters are **externally homogeneous** (shared characteristic) and **internally heterogeneous** (different compositions within). **Single-stage:** all members of selected clusters are included. **Multistage:** further sampling within selected clusters. Examples: cities, areas, organizations, universities. |

### 6.4 Simple Random Sample: Example

- **Population:** 600 employees of company ABC.
- **Steps:** (1) List all 600 and assign numbers 1–600. (2) Choose sample size (e.g. 150). (3) Use a random number generator to get 150 numbers from 1 to 600. (4) The 150 employees with those numbers form the sample.

### 6.5 Example: Assigning Participants to Groups (Learning Study)

- **Context:** Study on learning; **intelligence** is correlated with learning and must be controlled.
- **Bad approach:** Assign first 10 participants to Group A, next 10 to Group B (e.g. by arrival time). If Group B learns faster, we cannot tell if it is due to **treatment** or to **higher average IQ** in Group B. Intelligence is a **confounding variable** and a **rival hypothesis**.
- **Good approach:** **Random assignment** to the two treatment groups. The difference in average IQ between groups becomes much smaller (e.g. 0.2 vs 1.6). Both groups have similar IQ, so the biasing effect of IQ is controlled. Random assignment **distributes** variables to be controlled in roughly the same way across groups, **holding the effect of the extraneous variable constant**.

### 6.6 Limitations of Randomization

- Randomization **does not guarantee** equal distribution of variables in every run; by **chance**, they may still be uneven.
- Some extraneous variables are **not** well controlled by randomization alone.
- **Other techniques** (matching, counterbalancing, control of participant and experimenter effects) are used **together with** randomization.

---

## 7. Matching

- **Definition:** Use of techniques to **equate** participants in the treatment groups on **specific variables** (those thought to be related to the IV or to confound it).
- **Advantages:** Controls for the matched variables; **increases the sensitivity** of the experiment.

### 7.1 Matching by Building the Extraneous Variable into the Design (Blocking)

- The extraneous variable is turned into **another independent variable** (e.g. different levels of IQ).
- **Use** when you are **interested in the effect** of that variable (e.g. how DV scores differ across IQ levels).

### 7.2 Matching by Equating Participants

- Similar goal: **equivalent groups** on the control variable.
- **Difference:** Instead of creating a new IV from categories of the extraneous variable, participants are **matched** on the variable to be controlled. The number of participants is typically a **multiple** of the number of levels of the IV.

---

## 8. Counterbalancing

### 8.1 Purpose

- Technique to control **sequencing effects**.
- **Sequencing effects:** When the **order** of experimental treatments **interacts** (e.g. one condition affects performance in another). Common when **all participants** experience **each** condition.

### 8.2 Two Types of Sequencing Effects

| Type | Description | Example |
|------|-------------|--------|
| **Order effects** | Due to the **order** in which conditions are given. | Practice, fatigue. |
| **Carry-over effects** | Performance in **one** condition **affects** performance in a **later** condition. | Effect of Treatment A still present when the participant does Treatment B. |

### 8.3 Counterbalancing Procedures

| Procedure | Description | Example |
|-----------|-------------|--------|
| **Randomized counterbalancing** | The **sequence** of conditions is **randomly determined** for each participant. | IV with three levels A, B, C → six sequences (ABC, ACB, BAC, BCA, CAB, CBA); each participant randomly assigned to one. |
| **Intra-subject: ABBA** | Each participant gets conditions in **one order**, then the **reverse**. | Taste Cola A then B, assess; then B then A, assess → ABBA. To allow for differential order effects, use another group with **BAAB**. |
| **Intra-group counterbalancing** | **Groups** of participants (not individuals) are counterbalanced — different groups get different orders. Used when each participant cannot take all sequences (e.g. too many conditions). | — |
| **Incomplete counterbalancing** | A **subset** of all possible sequences is used (most common form of intra-group). **Even number of conditions:** Use as many sequences as conditions. First sequence: 1, 2, *n*, 3, (*n*−1), 4, (*n*−2), 5, … (e.g. 4 conditions → ABDC i.e. 1,2,4,3; 6 conditions → ABFCED). Remaining sequences: **increment each value by 1** in the previous sequence. Each condition then **precedes and follows** every other condition the **same number of times**. **Odd number of conditions:** This rule is not fully satisfied (e.g. A may be preceded by C twice but never by B). **Remedy:** Add the **reverse** of each of the first set of sequences (e.g. five more sequences that are the reverses of the first five). |

---

## 9. Control of Participant Effects

- Participants’ behaviour can be influenced by **perceptions and motives** (e.g. presenting themselves in the best light).

### 9.1 Double-Blind Placebo Model

- **Neither** the experimenter **nor** the participant knows which treatment condition (e.g. drug vs placebo) the participant received.
- One of the best techniques for controlling **participant and experimenter** effects.

### 9.2 Deception

- Giving participants a **false rationale** for the experiment (e.g. a cover story).
- Provide a hypothesis **unrelated** (orthogonal) to the real hypothesis.
- **Ethics:** The risk of the false information must not outweigh the benefit; the false information must be **constant** for all participants.

---

## 10. Control of Experimenter Effects

- **Experimenter effects:** Unintentional **biasing** influence from the experimenter.

### 10.1 Three Approaches

| Approach | Description |
|----------|-------------|
| **Control of recording errors** | Train researchers; use **multiple** recorders/observers or equipment (e.g. video, computers); have participants respond on a computer to remove human recording errors. |
| **Control of attribute errors** | Use the **same** experimenter in all treatment conditions — unless the treatment **interacts** with experimenter attributes (e.g. gender, age), in which case this may not be appropriate. |
| **Blind technique (control of experimenter expectancies)** | **Knowledge of each participant’s treatment condition is kept from the experimenter** so they cannot treat groups differently. This is the **experimenter** part of the double-blind design. The experimenter may know the hypothesis but is **blind** to which condition each participant is in. **Partial blind:** Keep condition hidden from the experimenter for **as many stages** as possible when full blind is not feasible. **Automation:** Fully automate procedures (written/recorded/filmed/computer-presented instructions; responses via timers, counters, computers, etc.) so that **no experimenter–participant interaction** is required. |

---

*End of summary.*

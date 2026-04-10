# IST606 Security Management – Detailed Lecture Summary

Source lecture: IST606_SecurityManagement_4_093206.pdf (Dr Nyamsi, 06/06/2023)

## 1. Executive Overview

This lecture frames security management as a continuous governance process, not a one-time technical activity. The central argument is that information security only works when organizations:

1. Define business and asset objectives clearly.
2. Set explicit risk tolerance levels.
3. Design controls based on risk mitigation (not guesswork).
4. Implement controls in a usable and sustainable way.
5. Review and continuously monitor control effectiveness.
6. Periodically perform active assessments to validate real-world resilience.

The lecture therefore links three themes into one system:

1. Information Security Life Cycle.
2. Information Security Risk Management.
3. Active Security Assessment (ASA).

---

## 2. Information Security Life Cycle

The lecture explains security as a phase-based life cycle around each information asset.

### 2.1 Security Design

Security design is the phase where controls are devised to meet previously defined security objectives.

The lecturer identifies five core design tasks:

1. Security design for confidentiality.
2. Security design for integrity.
3. Security design for availability.
4. Security design for authentication.
5. Security design for non-repudiation.

A key message is that these are not abstract ideals; each objective must be operationalized through concrete controls tied to risk mitigation.

#### Security design steps highlighted in the lecture

1. Risk mitigation planning:
- Aim is to reduce risk down to acceptable levels stated in policy.

2. Security training program design:
- Training should target the security maintenance team.
- Content should match the asset definition and policy requirements.

3. Security planning program design:
- A security plan for upcoming years (lecture references a 3-year planning horizon).
- A business continuity plan defining actions during disasters.

4. Design of a risk-driven security program:
- Controls are selected and organized as an actionable security program guided by risk priorities.

### 2.2 Security Implementation

Implementation is the phase that operationalizes the risk-driven security program.

Lecture emphasis:

1. Implementation must ensure usability and sustainability.
2. Verification/testing is required to check practical adequacy.
3. If controls are incomplete or vulnerable, the implementation process may be paused or discontinued for correction.
4. Security complexity should be hidden from users where possible, but policy-compliant configurations must still be enforced.

This implies a practical trade-off: strong security must coexist with operational usability.

### 2.3 Security Review and Certification Preparation

Purpose: ensure that key authorities agree with the proposed security program before formal control certification assessment starts.

Two major review activities:

1. Security review for authorization.
2. Security auditing.

The lecture states that certification then evaluates whether controls are:

1. Implemented correctly.
2. Operating as intended.
3. Producing desired outcomes.

### 2.4 Continual Service (Continuous Security)

Security is presented as ongoing service management, not project closure.

Core continual steps:

1. Configuration management and control.
2. Monitoring security controls.
3. Monitoring computing-environment changes.
4. Reporting and documenting changes.

Additional recurring activities:

1. Periodic risk assessments.
2. Periodic policy and procedure review.
3. Security awareness training.
4. Periodic effectiveness testing of policies, procedures, practices, and controls.
5. Formal remedial-action process (plan, implement, evaluate, document).
6. Incident detection, reporting, and response procedures.

The lifecycle message is explicit: monitoring and correction continue throughout the asset lifecycle.

### 2.5 Practice Orientation in the Lecture

The lecture includes practical tasks:

1. Class workshop:
- Apply full security lifecycle to a small business website hosted by the business itself.
- Assume existing security plan and continuity plan.

2. Homework matrix exercise:
- Build a 5x6 matrix: computing environment components (people, activities, data, technology, network) versus lifecycle phases.
- In each cell, prioritize CIA objective(s) most critical in that context.

This reinforces context-dependent security planning instead of one-size-fits-all controls.

---

## 3. Information Security Risk Management

This section defines risk management as the decision system that drives security investment and control selection.

### 3.1 Risk Definition and Core Components

Lecture definition: risk is a measure of potential inability to meet objectives within cost, schedule, and technical constraints.

Two components are mandatory in risk reasoning:

1. Probability (likelihood of occurrence).
2. Consequence (impact/severity if occurrence happens).

Risk events should be defined at a level that makes impacts and causes understandable and actionable.

### 3.2 Multi-Layer Control Perspective

Risk exists across assets, threats, vulnerabilities, and existing controls. Controls can target different architecture layers:

1. Physical security:
- Barriers and protections against unauthorized physical access.

2. Network security:
- Secure, highly available, scalable, manageable, reliable network architecture.

3. Application security:
- Applications must be secured in the context of the full system, not in isolation.

4. Data security:
- Data is a high-value resource.
- Common controls include cryptography and backup.

### 3.3 Risk Management Life Cycle Phases

The lecture describes risk management as recurrent and documented:

1. Risk planning.
2. Risk analysis.
3. Risk assessment.
4. Risk treatment.
5. Risk monitoring.
6. Risk documentation.

#### Risk planning

Develop and document a comprehensive strategy for identifying and tracking risks, treatment planning, continuous reassessment, and resource assignment.

#### Risk analysis

Refine each identified risk area by clarifying description, causes, and effects; then rate and prioritize by probability, severity, and interdependencies.

#### Risk assessment

Measure likelihood and impact to determine risk levels; prioritize treatment; compare assessed risk against expected treatment benefits before approval.

#### Risk treatment

Define/select/implement controls to bring risk to acceptable levels. Should include what will be done, by whom, by when, at what cost.

#### Risk monitoring

Track treatment effectiveness using metrics; revisit planning, analysis, and treatment when changes occur.

#### Risk documentation

Record all risk-management-phase information for governance, traceability, and accountability.

### 3.4 Business Value and Risk Tolerance

The lecture links CIA loss directly to business harm:

1. Loss of business value.
2. Reputational damage.
3. Loss of partner/customer trust.
4. Broader undesirable social outcomes.

Therefore:

1. Asset owners must understand exposure conditions.
2. Owners must define tolerated risk levels.
3. Asset policy should state tolerated risk.
4. Organization-wide policy should consolidate tolerated levels across systems.
5. Divisions/units should maintain policy manuals with clear objectives and constraints.

### 3.5 Accepted vs Unacceptable Risk States

Lecture decision logic:

1. If risk is below tolerated level:
- Risk may be accepted; no immediate additional controls needed.

2. If risk is above tolerated level:
- Immediate security investment/treatment is required to move risk back to acceptable range.

### 3.6 Recovery and Management Levels

Recovery planning is a security-management responsibility.

Corrective action modes:

1. Compromised productivity mode.
2. Full unavailability mode.

Risk exists at all management levels:

1. Strategic risks (planning-level).
2. Functional risks (function performance).
3. Operational risks (day-to-day operations).

The organization must identify, assess, and mitigate risks at each level.

### 3.7 Security Culture as Risk Control

The lecture strongly stresses a sustainable security culture:

1. Awareness.
2. Literacy.
3. Training.
4. Education.

Two control-action classes are distinguished:

1. Preventive actions:
- Reduce chance that intolerable losses occur.

2. Mitigation actions:
- Reduce vulnerability severity against known threats.

---

## 4. Active Security Assessment (ASA)

ASA is presented as a practical validation mechanism for security posture.

### 4.1 Why Active Assessment is Needed

Security management includes planning, intrusion detection, risk management, and auditing. These activities require testing support.

Literature uses different terms (vulnerability assessment, penetration testing, ethical hacking), but the lecture adopts ASA to emphasize broad and structured active testing.

### 4.2 ASA Definition in the Lecture

ASA is an active assessment conducted under:

1. Well-defined objective.
2. Well-defined scope.
3. Well-defined security policy.

Required ASA actions:

1. Discover access information.
2. Identify vulnerabilities.
3. Exploit vulnerabilities in controlled manner to evaluate resilience.
4. Generate recommendations and act within policy constraints.

The lecture insists assessment must be comprehensive across people, activities, data, infrastructure, and technology.

### 4.3 Relevant Standards and Guidance Mentioned

Examples listed for planning and guidance:

1. ISO 17799.
2. ISO 27001-05.
3. BS 25277.
4. NIST Security Plan Guidelines.
5. OSSTMM.

### 4.4 Ethical Testers vs Real Hackers

The lecture draws clear distinctions:

1. Testers have defined objective/scope/policy; attackers do not.
2. Testers are method-limited and accountability-driven; attackers are unrestricted.
3. Testers document all steps and findings; attackers hide traces.
4. Testers seek risk reduction; attackers seek destructive or unauthorized outcomes.

ASA therefore simulates attacker behavior for defensive learning and mitigation.

### 4.5 Simulated Attack Coverage by Component

#### People

- Social engineering against critical personnel to extract useful access information.

#### Infrastructure/Physical and Network

Examples discussed:

1. Lower-layer link attacks causing downtime.
2. Generic router DoS via overload.
3. Cryptographic exhaustion-style attack paths.
4. Unauthorized neighbor/routing adjacency attacks.
5. TCP RST session-reset attacks.
6. ICMP-based hard-error/disruption attacks.

#### Technology (OS and Applications)

- Exploit known OS vulnerabilities.
- Attack common services/protocols/applications (e.g., HTTP, SMTP, FTP, VoIP).
- Use proxies to obscure source and complicate forensics.

#### Data

- Data corruption can cascade into major output/system damage.
- DoS can delay/deny timely access to information.
- Poorly protected critical files are high-risk.
- Database-heavy web systems create target-rich surfaces and performance-related constraints.

#### Activities (Processes/Policies/Procedures)

- Insider abuse can corrupt procedures and rules.
- Activity security includes process adherence and infrastructure dependencies.

### 4.6 Ethics Rules for ASA

The lecture highlights four baseline ethical requirements:

1. Stay inside objective, scope, and project policy.
2. Respect privacy.
3. Avoid destructive effects.
4. Report ethics violations within the test team.

### 4.7 ASA as a Managed Project

ASA should be planned and run as a formal IT project with top-management approval.

Planning phase should establish:

1. Team composition.
2. Project objectives.
3. Scope boundaries.
4. Security policy.

Operational note in lecture:
- Users are often not informed to avoid altered behavior that invalidates realism.

### 4.8 Scope Elements that Must Be Explicitly Defined

1. Target system and included/excluded components.
2. Timing of major test steps.
3. Risks accepted during assessment.
4. Strategy (visibility, place, direction).
5. Deliverables and delivery dates.
6. Response activities and testing limitations.

#### Timing governance

- Some tests should avoid active production windows.
- Performance-impacting tests are often scheduled at night/weekends/early morning.

#### Accepted-risk governance during ASA

Lecture asks practical questions:

1. What if testers discover immediate danger?
2. Should they wait for final report only?
3. What limited immediate actions are permitted to reduce exposure?

This points to pre-approved emergency response boundaries in project policy.

### 4.9 Strategy Model: Visibility, Place, Direction

#### Place

- External vs internal tester position.

#### Visibility

Based on two variables:

1. Whether testers receive partial access information from owners before testing.
2. Whether users/management are informed before testing.

Named visibility modes in lecture:

1. Visible.
2. Double Visible.
3. Blind.
4. Double Blind.

#### Direction

- One-way or two-way.
- Two-way can involve controlled “warring” between testers and security staff.
- Warring may be synchronous or asynchronous:
1. Synchronous: testers attack and defenders respond in same period.
2. Asynchronous: testers attack in one period; defenders analyze/respond in later period.

Rules of engagement must be set in ASA policy.

### 4.10 Closing Position of the Lecture

The conclusion ties all sections together:

1. Good security design depends on good security analysis.
2. Good analysis requires effectiveness assessment and requirement refinement.
3. Security assessment can be passive or active.
4. Active assessment uses guided, policy-driven penetration methods.

---

## 5. Integrated Study Takeaways (What to Remember for Exams)

1. Security management is lifecycle-based, risk-driven, and continuous.
2. CIA + authentication + non-repudiation must be translated into implementable controls.
3. Risk tolerance must be explicitly documented at asset and organizational levels.
4. Risk treatment is not complete without monitoring and documentation.
5. Security culture (awareness/training/literacy) is a control mechanism, not just HR activity.
6. ASA is ethical, scoped, policy-bound attacker simulation for improving defense.
7. ASA scope design (timing, visibility, place, direction, response limits) determines test validity and safety.
8. Continuous service is mandatory because environment, threats, and control effectiveness change over time.

---

## 6. Quick Revision Map

If you need a 60-second recall chain, use this flow:

Business objectives -> Risk tolerance -> Security analysis -> Security design (CIA + auth + non-repudiation) -> Implementation (usable + sustainable) -> Review/audit/certification readiness -> Continuous monitoring/remediation -> Active assessment validation -> Updated risk picture -> Repeat.

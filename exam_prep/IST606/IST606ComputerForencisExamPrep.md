# IST 606: Security Management and Computer Forensics
## Exam Practice Question Bank — Full Answer Key

This answer key provides model answers for **Section A (MCQs)**, **Section B (Structural Questions)**, and **Section C (Essay Questions)** across all four practice sets. Use it to check your own answers, not as a substitute for writing them out yourself under timed conditions.

---

# SET 1 — Crimes Against Persons (Identity Theft, SIM Fraud & Phishing)

## Section A — MCQ Answers

| # | Answer | Quick Justification |
|---|--------|---------------------|
| 1 | B | Crime against persons = digital harm to an individual's identity, privacy, safety, or wellbeing |
| 2 | C | SIM fraud directly targets an individual's identity |
| 3 | B | SIM swap's goal is intercepting 2FA codes via number takeover |
| 4 | B | Law No. 2010/012 of 21 December 2010 governs cybercrime in Cameroon |
| 5 | A | ANTIC (National Agency for ICT) handles monitoring/investigation |
| 6 | B | Cellebrite UFED extracts data directly from seized mobile devices |
| 7 | B | FTK Imager's defining function is hash-verified, unaltered bit-for-bit copying |
| 8 | C | Election database hacking is a crime against society/government, not the person |
| 9 | B | Hash values prove the copy matches the original exactly |
| 10 | B | GPS metadata in a forged ID photo is classic metadata evidence |

---

## Section B — Structural Answers (Marie's SIM Fraud Case)

**1) Why is this a cybercrime against persons rather than property? (4 marks)**

This case is classified as a cybercrime against persons because the central harm is directed at Marie's *identity* — her National ID was misused without consent — rather than at a physical or organisational asset. The consequences (unauthorized account access, financial loss, impersonation risk, psychological distress) all attach to her personally rather than to a company or institution. While the money taken is a "property" element, the *mechanism* of the crime — exploiting personal identity documents — is what defines it as a person-centred offence under Cameroon's cybercrime framework, since cybercrime against persons is defined as illegal digital activity that directly harms an individual's identity, privacy, safety, or psychological wellbeing.

**2) Three vulnerabilities that enabled the fraud (6 marks — 2 marks each)**

- **Weak identity verification at registration agents:** Agents often fail to rigorously cross-check the photocopy of an ID against the person physically presenting it, allowing a previously submitted ID copy to be reused fraudulently.
- **Lack of document destruction/retention policy:** The agent who received Marie's ID copy six months earlier should have securely destroyed or restricted access to it; its reuse suggests poor data handling and storage practices.
- **Absence of secondary verification for new SIM activations:** There was no biometric re-confirmation or SMS/call-back verification to the legitimate ID holder before the new SIM was activated and linked to mobile money services.

**3) Four categories of digital evidence + sources (10 marks — 2.5 each)**

| Category | Example Evidence | Source |
|---|---|---|
| Registration records | The submitted ID photocopy, registration timestamp, agent ID | Telecom operator's SIM registration database |
| Mobile money transaction records | Withdrawal amount, timestamp, agent cash-out point | MTN Mobile Money transaction servers/logs |
| Device evidence | Calls, messages, and locations linked to the fraudulent SIM | Seized phone (via Cellebrite UFED extraction) |
| CCTV/witness evidence | Footage of the person who physically registered the SIM and the person who withdrew the funds | Camera systems at the registration kiosk and mobile money agent shop |

**4) How Cellebrite UFED is used at each stage (6 marks)**

1. **Seizure & isolation:** The suspect's phone is placed in airplane mode immediately to prevent remote wipe, then connected to the UFED unit.
2. **Extraction mode selection:** Physical extraction is chosen to recover deleted data (e.g. deleted SMS confirming the fraud), not just visible data.
3. **SIM data extraction:** UFED pulls the ICCID/IMSI directly from the SIM, linking the device to the fraudulent registration.
4. **Deleted message recovery:** Recovers deleted texts that may contain mobile money PINs or coordination with accomplices.
5. **Report generation:** Produces a timestamped, hash-verified PDF/HTML report admissible in court.

**5) Roles of key stakeholders (6 marks — 2 each)**

- **(a) ANTIC:** Monitors ICT activity, coordinates the technical investigation, and may formally flag the registration agent's compliance failure to telecom regulators.
- **(b) Mobile money agent:** Provides testimonial evidence on how the withdrawal was processed, supplies transaction logbooks, and may be investigated for possible collusion or negligence.
- **(c) Forensic examiner:** Extracts, analyses, and documents digital evidence from the phone, registration systems, and transaction logs, producing a report that withstands legal scrutiny.

**6) Why jurisdiction complicates the case (4 marks)**

If the suspect operates from outside Cameroon, investigators face cross-border legal barriers: Cameroonian law enforcement has no direct authority to compel evidence or extradite suspects from another country. This requires mutual legal assistance treaties (MLATs) or international cooperation channels, which are often slow, and differing national laws on data privacy and cybercrime may restrict what evidence can legally be shared or obtained.

**7) Four rules for preserving evidence admissibility (4 marks — 1 each)**

- Maintain a documented chain of custody for the seized device at every handoff.
- Use write-blockers/forensic imaging tools so the original device is never directly altered.
- Compute and record hash values (MD5/SHA-1) immediately after imaging to prove integrity.
- Ensure all collection is properly authorised (e.g. court order/warrant) to avoid evidence being ruled inadmissible.

---

## Section C — Essay Answer Guides

**1) Cybercrime against persons / SIM fraud case study (17 marks)**

A strong answer should: define cybercrime against persons with reference to Cameroon's Law No. 2010/012; explain that SIM registration was introduced to improve accountability but that weak enforcement at the verification stage (agent negligence, inadequate training, document reuse, lack of biometric checks) creates exploitable gaps; discuss how this enables anonymity for mobile money fraud, identity theft, and harassment; and propose three concrete measures — e.g., mandatory biometric verification at registration, real-time ID-database cross-checking, and audit trails with agent accountability penalties.

**2) Spear phishing investigation (17 marks)**

Explain that spear phishing targets specific individuals/institutions with personalised, convincing emails (unlike generic phishing), exploiting human trust and routine email behaviour rather than purely technical flaws. Vulnerabilities include weak spam filtering, absence of multi-factor authentication, and low staff awareness. Investigation tools: Wireshark (network traffic linked to phishing infrastructure), Gophish (simulating attacks to measure susceptibility), MxToolbox (verifying sender domains/headers), Splunk (log analysis for suspicious logins), and Autopsy (recovering malicious attachments/browser history from affected devices).

**3) Human error vs technical sophistication (16 marks)**

Argue both sides: cybercriminals exploit predictable human behaviours (trust in authority, urgency, routine clicking) more than novel exploits — supported by the fact that SIM fraud and phishing succeed primarily through social engineering and procedural laxity, not advanced hacking. However, acknowledge that some attacks (e.g. SIM swapping via telecom system manipulation) do require technical knowledge of telecom infrastructure. Conclude that most successful cybercrimes against persons are a *combination*, but the entry point is overwhelmingly human/procedural failure.

**4) Investigation process applied to identity theft (17 marks)**

Walk through: **Identification** (recognising the incident and scope), **Preservation** (securing devices/accounts, preventing further tampering), **Collection** (gathering device data, transaction logs, registration records), **Examination** (running tools like Cellebrite/Autopsy), **Analysis** (correlating timestamps, identifying patterns), **Presentation** (structured report for court). Throughout, emphasise chain-of-custody documentation, hash verification, and legal authorisation at every step.

**5) Skills/prerequisites for digital forensic investigators (16 marks)**

Technical: knowledge of operating systems, networking, file systems, and forensic tools (Autopsy, FTK Imager, Cellebrite). Legal: understanding of Cameroon's cybercrime law, evidentiary standards, and chain-of-custody requirements. Analytical: pattern recognition, attention to detail, logical reasoning under ambiguity. Ethical: integrity, confidentiality, objectivity (investigators must not contaminate or selectively present evidence), and respect for privacy/consent boundaries.

---
---

# SET 2 — Crimes Against Society (Election Interference & Ponzi Schemes)

## Section A — MCQ Answers

| # | Answer | Quick Justification |
|---|--------|---------------------|
| 1 | B | Society-level harm = collective democratic legitimacy and trust, not one individual |
| 2 | B | Disinformation/deepfakes are coordinated attacks on the collective electorate |
| 3 | B | Ponzi schemes harm the public collectively (society) and their finances (property) |
| 4 | B | Metadata can reveal post-deadline tampering with official documents |
| 5 | A | Wireshark captures/analyses network traffic to fraudulent platforms |
| 6 | C | Turnout anomalies are statistical/data forensic evidence |
| 7 | A | Registry Explorer examines USB-related registry keys |
| 8 | B | Jurisdiction/cross-border issues are the central challenge |
| 9 | B | Real government/classified systems are legally/ethically inaccessible to students |
| 10 | B | Mobile money data reveals suspicious payment patterns and fund flows |

---

## Section B — Structural Answers (Election Interference Case)

**1) Why is this a crime against society? (4 marks)**

The harm here is not confined to one victim — it threatens the legitimacy of the election process itself, public trust in democratic institutions, and social cohesion across multiple regions (evidenced by the protests). Crimes against society are defined by their effect on the collective political rights and stability of the nation, rather than an individual's personal data or finances, which distinguishes this from crimes against persons or property.

**2) Four categories of evidence (8 marks — 2 each)**

- **Result anomaly evidence:** Statistical records showing turnout exceeding registered voter counts, found in the electoral commission's result databases/spreadsheets.
- **Deepfake video evidence:** The video file itself, its metadata (creation tool, device, timestamps), found via forensic analysis of the file and its upload history on social platforms.
- **Social media coordination evidence:** Patterns of simultaneous/bot-like posting, found through platform APIs, OSINT tools, and account creation date analysis.
- **System/network access evidence:** Logs showing unauthorized access attempts to electoral databases, found in server and firewall logs.

**3) Statistical anomaly detection techniques (6 marks)**

Cross-referencing reported turnout against the registered voter population per polling station to flag percentages exceeding 100%; checking for duplicate entries across polling stations; comparing historical turnout trends to detect statistically implausible spikes; and using simple variance/outlier analysis to flag stations whose figures deviate sharply from regional averages.

**4) Metadata analysis of the deepfake video (6 marks)**

Forensic metadata tools (e.g. ExifTool) can reveal the software used to create or edit the video (commonly AI-generation or editing suites leave signature metadata tags), the device identifier of the originating equipment, creation and last-modified timestamps, and sometimes GPS data — all of which can corroborate or contradict claims about when and where the video was produced, helping establish whether it is fabricated and by whom.

**5) Tracing the disinformation campaign (8 marks)**

Steps: (1) Identify the first known appearance of the content using platform search/OSINT tools; (2) map the accounts that shared/amplified it using link-analysis tools like Maltego; (3) examine account creation dates, posting frequency, and behavioural patterns to detect bot/inauthentic activity; (4) correlate timestamps across accounts to detect coordinated (non-organic) posting; (5) request platform cooperation for backend metadata (IP logs, device fingerprints) through legal channels; (6) document the full spread timeline for presentation.

**6) Roles of stakeholders (6 marks — 2 each)**

- **(a) ANTIC:** Leads technical investigation into the cyberattack on electoral systems and disinformation infrastructure.
- **(b) Electoral commission IT department:** Provides system access logs, confirms which systems were affected, and assists in technical remediation.
- **(c) Social media platforms:** Cooperate (where legally compelled) by providing account metadata, removing confirmed disinformation, and assisting attribution.

**7) Two ethical/legal constraints (2 marks)**

Investigators must avoid any appearance of political bias or partisan interference in a highly sensitive case, and must obtain proper legal authorisation before accessing private platform data or account information.

---

## Section C — Essay Answer Guides

**1) Cybercrime against society vs. persons vs. property (17 marks)**

Define each category clearly: persons (individual identity/privacy harm), property (financial/physical/digital assets), society (collective democratic, social, and institutional harm). Use election interference to show how a single attack (e.g., a hacked results database) can simultaneously have elements of multiple categories, but is classified as "against society" when its primary harm is to collective trust and national stability rather than one victim's pocket.

**2) SUNRUN Ponzi scheme investigation methodology (17 marks)**

Explain the scheme's mechanics (using social media virality and mobile money to recruit victims, paying early investors with new investors' funds), then walk through the five-phase investigation: identification (recognising the fraud pattern), collection (mobile money records, social media account data, domain/hosting records), preservation (forensic imaging of any seized devices, hash verification), analysis (correlating fund flows, identifying organiser accounts via Maltego-style link analysis), and presentation (structured report reconstructing the scheme for prosecution) — noting the added difficulty that organisers have disappeared and infrastructure may be abandoned.

**3) Disinformation/deepfakes vs. hacking electoral systems (16 marks)**

A balanced argument: deepfakes/disinformation are harder to legally classify and attribute (free speech tensions, distributed responsibility, viral spread beyond any single actor's control), while direct hacking leaves clearer technical evidence trails (logs, intrusion signatures). Conclude that disinformation may be *more socially corrosive* due to scale and difficulty of correction, even if hacking is more technically traceable — both require updated legal and forensic frameworks.

**4) Five-phase methodology illustrated with an election scenario (17 marks)**

Use a chosen scenario (e.g. a hacked results database) and explicitly walk through identification, collection, preservation, analysis, and presentation with concrete actions and tools at each stage, mirroring the structural answer in Section B but in full essay form with justification for each phase's necessity.

**5) Challenges with evidence in crimes against society (16 marks)**

Discuss jurisdiction (perpetrators/servers often abroad), attribution (anonymous accounts, VPNs, bot networks make identifying real actors difficult), and the sheer scale/speed of social media spread which often outpaces investigative capacity — concluding that international cooperation frameworks and platform transparency agreements are essential complements to domestic forensic work.

---
---

# SET 3 — Crimes Against Property (Website Cloning & Digital Asset Theft)

## Section A — MCQ Answers

| # | Answer | Quick Justification |
|---|--------|---------------------|
| 1 | B | Property crimes target money, files, IP, websites, organisational info |
| 2 | B | The fake domain mimics the real one to deceive applicants into paying |
| 3 | B | Copying unique code/design/content without authorization = IP theft |
| 4 | B | Crime requires lack of authorization + intent to profit/harm + deception |
| 5 | B | ICANN Lookup retrieves domain registration/ownership data |
| 6 | B | WinMerge compares source code between two websites |
| 7 | A | VirusTotal scans URLs/files for malicious classification |
| 8 | B | Maltego performs OSINT/link analysis for attribution |
| 9 | B | Typo-squatting = deceptive domain registration resembling the original |
| 10 | B | Splunk analyses logs to trace attacker access patterns |

---

## Section B — Structural Answers (AfriMart Website Cloning Case)

**1) Why is this a crime against property? Which property types? (4 marks)**

This is a crime against property because it targets AfriMart's *intangible and financial assets*: its intellectual property (unique website design, logo, source code, product catalogue), its brand reputation/domain identity, and indirectly its customers' financial property (payments made for undelivered goods). Unlike a crime against persons, the primary target is the company's digital and commercial assets, not an individual's personal identity.

**2) Four evidence indicators confirming cloning (8 marks — 2 each)**

- **Identical source code patterns:** Same file structures, coding comments, or tracking script IDs as AfriMart's real site.
- **Duplicate visual design:** Near-identical layout, graphics, and copyrighted product images.
- **Domain similarity:** "afrimart-cm.shop" is a typo-squatted variant of "afrimart.cm".
- **Matching embedded metadata:** Identical metadata in product images on both sites, proving direct copying rather than independent creation.

**3) Domain and DNS investigation procedure (8 marks)**

(1) Perform a WHOIS lookup via ICANN Lookup on "afrimart-cm.shop" to identify the registrant and registration date; (2) check DNS records to identify the hosting provider and associated IP address; (3) compare the registration date to AfriMart's legitimate domain to establish a suspicious timing pattern; (4) cross-reference the hosting IP against known malicious hosting ranges; (5) document all findings with timestamps for the forensic report.

**4) WinMerge and browser developer tools (6 marks)**

WinMerge performs a line-by-line comparison of the downloaded HTML/CSS/JS source code from both sites, highlighting identical or near-identical blocks — strong evidence of direct copying. Browser developer tools allow investigators to inspect live rendered HTML, CSS, and JavaScript in real time, check for identical analytics/tracking IDs, and capture network requests that may reveal where form data (e.g. fraudulent payment details) is being sent.

**5) Server log analysis linking CMS logins to clone appearance (8 marks)**

Using Splunk, investigators would: import AfriMart's web/CMS server logs; filter for login attempts and failed authentication events around the period the clone appeared; correlate IP addresses and timestamps of suspicious logins with the clone's domain registration date; check for unusual access patterns (e.g. bulk downloads of product images/descriptions shortly before the clone went live); and build a timeline showing the breach preceded the clone's launch, suggesting the attacker scraped data directly from the compromised CMS.

**6) Evidence preservation steps (6 marks)**

Create forensic images (e.g. via FTK Imager) of any seized servers/devices; compute and record hash values immediately to prove integrity; take timestamped screenshots of the cloned website before it can be taken down; preserve WHOIS/DNS records through official export functions; maintain a documented chain of custody for every piece of evidence; and store all evidence in read-only/access-controlled storage.

---

## Section C — Essay Answer Guides

**1) Cybercrime against property / website cloning (17 marks)**

Define cybercrime against property broadly (money, systems, files, IP, websites, organisational data), then narrow to website cloning specifically: unauthorized duplication of design, code, content, and branding to deceive users. Explain the infringed property types (visual design, source code, brand identity, domain reputation) and typical objectives (credential theft, banking fraud, malware distribution, reputational exploitation).

**2) Full investigation of the passport cloning case (17 marks)**

Walk through: identification (comparing original vs. suspected clone via Httrack and browser dev tools), domain/DNS investigation (ICANN Lookup), source code analysis (WinMerge), malware/phishing analysis (VirusTotal), log analysis (Splunk), attribution (Maltego for OSINT/link analysis), and evidence preservation (Autopsy, hashing, chain of custody) — explicitly naming each tool's role at its respective stage.

**3) Website cloning vs. database/backend theft (16 marks)**

Compare: website cloning evidence is largely *visible/external* (domain records, visual design, source code) and easier to detect quickly through public comparison; database/backend theft evidence is *internal* (server logs, SQL dumps, backup files) and requires privileged access or cooperation from the victim organisation, making it slower to detect but often more financially damaging since it involves customer data exposure.

**4) Domain similarity: easy to detect, hard to prosecute (17 marks)**

Argue that typo-squatting is visually/technically obvious (easy WHOIS/DNS checks confirm it), but prosecution is difficult because: the registrant may use privacy-shielded WHOIS registration; servers/registrars may be in jurisdictions with weak cybercrime cooperation; proving *intent to deceive* (rather than coincidence or parody) requires demonstrating deliberate visual/functional mimicry; and suspects can simply abandon one domain and register another, evading enforcement.

**5) Evidence preservation in property crimes (16 marks)**

Discuss hashing (MD5/SHA-1) as proof of unaltered evidence, forensic imaging (FTK Imager) as the standard first step before analysis, and chain of custody as the documented trail proving evidence wasn't tampered with between collection and court presentation. Explain consequences of failure: evidence becomes inadmissible, cases collapse on technical objections, and legitimate prosecutions fail even when the underlying crime is proven to have occurred.

---
---

# SET 4 — Crimes Against Government & General Forensic Principles

## Section A — MCQ Answers

| # | Answer | Quick Justification |
|---|--------|---------------------|
| 1 | A | DFRWS paradigm: Identification → Preservation → Collection → Examination → Analysis → Presentation |
| 2 | B | Disk imaging = exact bit-for-bit copy without altering the original |
| 3 | A | Attack on state-owned telecom's admin systems = crime against government |
| 4 | B | The natural environment is not one of the four standard categories |
| 5 | B | Chain of custody = documented handling trail proving evidence integrity |
| 6 | B | Forensic investigators need technical + legal + analytical skills combined |
| 7 | B | Autopsy analyses disk images/file systems, recovers deleted files |
| 8 | B | Digital evidence is fragile/volatile, unlike most physical evidence |
| 9 | A | Cross-border nature of cybercrime creates jurisdictional conflict |
| 10 | C | "People" actor category covers human-related vulnerability causes |

---

## Section B — Structural Answers

### Question 1 (Exam Board Server Breach)

**1) What is cybercrime, and why is this against government/institutional infrastructure? (4 marks)**

Cybercrime is illegal activity conducted using computers and the internet, including hacking, fraud, and unauthorized data manipulation. This scenario qualifies as a crime against government/institutional infrastructure because the examination board is a public institutional body responsible for managing nationally significant academic records; an attack on its servers threatens the integrity and availability of a public service that affects many citizens collectively, not just one individual.

**2) Three possible motivations (6 marks — 2 each)**

- **Financial gain:** Selling altered results or holding the board to ransom for restoring access.
- **Disruption/sabotage:** Causing chaos for political, competitive, or personal-grievance reasons (e.g. a disgruntled former employee).
- **Vandalism/reputation damage:** Defacing or corrupting the system simply to demonstrate capability or embarrass the institution.

**3) Methods and tools used in the attack (8 marks)**

Possible methods include malware (to gain persistent unauthorized access), phishing (to obtain administrator credentials), SQL injection (to manipulate the results database directly), DDoS attacks (to overwhelm and disrupt server availability), and exploitation of unpatched vulnerabilities in the server software.

**4) Roles of stakeholders (10 marks — 2 each)**

- **(a) Law enforcement:** Investigates the crime, secures the scene, collects evidence, and coordinates with other agencies to identify and apprehend suspects.
- **(b) Legal department/state counsel:** Advises on legal procedure, represents the state in any proceedings, and ensures investigative steps remain lawful.
- **(c) Judge:** Oversees judicial proceedings impartially and delivers a verdict based on presented evidence.
- **(d) Forensic expert:** Analyses digital evidence, determines the attack method, assesses the extent of damage, and assists in data recovery.
- **(e) Lawyer:** Represents the examination board's interests, provides counsel, and protects the client's rights throughout the process.

**5) Steps in the forensic investigation (10 marks)**

Identification (determine scope/affected systems) → Preservation (secure evidence against tampering) → Collection (gather logs, files, network traffic) → Examination (analyse data for patterns/anomalies) → Analysis (determine attack methods and damage extent) → Documentation (record all findings and methods) → Reporting (present findings to stakeholders) → Recovery (restore systems and implement preventive measures).

**6) Why jurisdiction is a problem here (2 marks)**

If the attacker operates from outside Cameroon, differing national cybercrime laws, the difficulty of cross-border evidence requests, and complex extradition processes can significantly slow or block prosecution.

---

### Question 2 (School Information System Breach)

**1) Causes of vulnerabilities by actor (12 marks — 2 each)**

- **(a) People:** Human error or insufficient training among staff managing accounts; lack of awareness about safe access practices.
- **(b) Activities:** Password sharing or weak session management practices allowed one parent to view another's child's profile.
- **(c) Data:** Improper validation/access control on stored grade and profile data allowed unauthorized viewing and modification.
- **(d) Network:** Weak network segmentation or unsecured access points may have allowed unauthorized reach into the system.
- **(e) Technology:** Outdated or misconfigured server/database technology may not have enforced proper access boundaries.
- **(f) Software:** Bugs or flawed access-control logic in the school's information system likely allowed the cross-account profile view.

**2) Confidentiality/integrity/availability/authentication issues for three actors (9 marks — 3 each)**

- **People:** *Confidentiality* — need training to prevent accidental disclosure; *Integrity* — monitoring to prevent unauthorized changes; *Authentication* — strong identity verification for all users.
- **Data:** *Confidentiality* — encrypt stored grades/personal data; *Integrity* — checksums/validation to detect tampering; *Availability* — regular backups to prevent loss.
- **Software:** *Confidentiality* — built-in access restrictions per user role; *Integrity* — prevent unauthorized data alteration through validated input; *Authentication* — software should only grant access to verified, authorized users.

**3) Risk-driven security program (5 marks)**

A concise five-part program: (1) Risk assessment to identify threat likelihood/impact; (2) Role-based access control (RBAC) with multi-factor authentication; (3) Continuous monitoring and logging of system activity; (4) Regular security patching/updates; (5) Staff, student, and parent training on safe access practices, paired with a documented incident response plan.

---

## Section C — Essay Answer Guides

**1) The DFRWS investigative paradigm (17 marks)**

Explain each phase in turn — identification (recognising and scoping an incident), preservation (securing evidence against loss/tampering), collection (gathering relevant data using forensically sound methods), examination (technical processing of collected data), analysis (interpreting findings to answer investigative questions), and presentation (communicating results clearly and defensibly) — and argue that skipping or rushing any phase risks evidence being challenged or ruled inadmissible in court, undermining the entire investigation's legal value.

**2) Disk imaging as a forensic technique (17 marks)**

Define disk imaging as creating an exact, bit-for-bit copy of storage media. Discuss tools (FTK Imager, dd, Autopsy ingestion of images) and the centrality of hash verification (MD5/SHA-1) in proving the image matches the original exactly. Explain risks of skipping proper imaging: working directly on the original device risks altering timestamps/metadata, potentially destroying the very evidence being sought and rendering findings legally indefensible.

**3) Four crime categories compared (16 marks)**

Use one Cameroonian example each: persons (SIM card registration fraud), society (election interference via disinformation), government (spear phishing attack on Camtel's email infrastructure), property (cloning of the passport pre-enrollment website). Discuss how investigative focus shifts: person-crimes emphasise individual device/account forensics; society-crimes emphasise scale, social media analysis, and statistical anomaly detection; government-crimes emphasise infrastructure/network forensics and national security coordination; property-crimes emphasise domain/source-code comparison and IP attribution.

**4) Skills/qualifications for forensic investigators (17 marks)**

As in Set 1 Essay 5, but expand on professional conduct: investigators must maintain objectivity (presenting all findings, not just supportive ones), confidentiality (protecting sensitive case details), and procedural discipline (following legally mandated steps exactly) — since a forensic expert's credibility and the case's admissibility depend equally on technical skill and ethical rigour.

**5) Proving evidence hasn't been tampered with (16 marks)**

Argue that raw evidence collection is often the "easy" part technically, while the harder, legally decisive challenge is *proving* integrity: chain of custody documents every person who handled evidence and when; hashing provides mathematical proof that a copy is identical to the original; write-blockers prevent any modification during collection. Without these, even genuine, damning evidence can be thrown out in court — meaning forensic rigour in preservation is just as important as technical skill in analysis.

---

*End of Answer Key.*

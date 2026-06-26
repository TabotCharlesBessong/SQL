# IST 606: Security Management and Computer Forensics
## Section C (Restructured) — Scenario-Based Questions in the Exact University of Buea Exam Format

**Important note on this revision:** Looking again at the two past exam papers, the questions are **not** generic "discuss/critically evaluate" essay prompts. They follow one consistent pattern: a single detailed case scenario, followed by a numbered list of direct, specific questions — "What is cybercrime?", "What could be the motivation?", "If the servers are affected, what methods/tools were used?", "What role would [X] play?", "What are the steps in the investigation?", "Why is jurisdiction a problem?" — each carrying its own mark allocation (ranging from 2 to 10 marks per question).

This document rebuilds **Section C for all four practice sets** in that exact format, replacing the previous "essay" style. Each set now has **one full scenario with 6 direct questions worth 50 marks total**, matching the structure and mark distribution of your two sample papers as closely as possible, followed by complete, detailed model answers.

---
---

# SET 1 — Crimes Against Persons
## Section C (50 marks)

### Case Scenario

A Western Union transfer case involving the theft of money sent to Tabot Ndip, a final-year Computer Science student at the University of Buea, by his elder sister based in Belgium. Tabot had been receiving threatening messages on WhatsApp from an unknown number demanding FCFA 1,500,000, threatening to leak compromising photos allegedly taken from his hacked laptop camera if he did not pay. In panic, and without informing his family, Tabot asked his sister to urgently send him FCFA 800,000 through Western Union to "settle an emergency," intending to pay the blackmailer. Before Tabot could collect the money, investigators discovered that the Western Union transfer had already been fraudulently collected at a branch in Douala using a forged national ID card bearing Tabot's name but a different photograph. Tabot's sister, devastated at the double loss — her brother still being blackmailed and the money she sent now stolen — reported the matter to the police. During preliminary investigation, it was discovered that the threatening messages had originated from a SIM card registered using a stolen identity, and that the same phone number had previously been linked to two similar blackmail attempts reported in Buea and Limbe.

### Questions

**1) Why will this be treated as a cybercrime case? (3 marks)**

**2) What could be the motivation behind this attack? (4 marks)**

**3) If the laptop camera was indeed compromised, what could be the methods and tools used in this attack? (6 marks)**

**4) What will be the role of the following persons in handling this case? (3,3,3 marks)**
   - a. Law enforcement
   - b. Legal department (state counsel)
   - c. Forensic Expert

**5) What are some of the steps that will be used in the forensic investigation of the case above? State clearly how each step will be executed. (10 marks)**

**6) Why is jurisdiction a problem in this digital forensics case? (3 marks)**

---

### Detailed Answers

**1) Why will this be treated as a cybercrime case? (3 marks)**

This case qualifies as a cybercrime because it involves multiple illegal acts carried out through digital technologies and networks. First, the blackmail itself was conducted via WhatsApp, a digital communication platform, using threats tied to allegedly unauthorized access to Tabot's laptop camera — meaning the offence began with a suspected computer intrusion (1 mark). Second, the SIM card used to send the threatening messages was registered using a stolen identity, making this a case of digital identity fraud compounding the offence (1 mark). Third, the fraudulent collection of the Western Union transfer using a forged ID, while partly a physical-world deception, was enabled by and connected to the broader digital extortion scheme, and the use of electronic funds transfer systems and mobile communication to orchestrate and benefit from the crime brings it squarely within the definition of cybercrime as illegal activity conducted using computers, networks, and digital technologies (1 mark).

**2) What could be the motivation behind this attack? (4 marks)**

Several motivations are evident or inferable from the scenario:
- **Financial gain** — the primary and most obvious motivation, as the attacker demanded FCFA 1,500,000 directly from Tabot, and the linked SIM number was tied to two prior, similar blackmail attempts, suggesting this is a repeated, deliberate financial extortion scheme (1 mark).
- **Exploitation of fear and shame** — by threatening to leak compromising photos, the attacker is exploiting psychological vulnerability and the victim's fear of reputational and social harm, a common tactic in "sextortion"-style cybercrime designed to pressure victims into paying quickly without involving authorities (1 mark).
- **Opportunistic targeting of vulnerable victims** — the choice of a university student, who may have limited financial resources but family members abroad able to send money quickly via Western Union, suggests calculated victim selection based on perceived ability to pay under pressure (1 mark).
- **Possible organised or repeat criminal activity** — the fact that the same number was linked to two earlier blackmail attempts in Buea and Limbe suggests the motivation is not a one-off act of personal grievance but a sustained, profit-driven criminal pattern, possibly run by an individual or small group operating a deliberate extortion scheme across multiple victims (1 mark).

**3) If the laptop camera was indeed compromised, what could be the methods and tools used in this attack? (6 marks)**

If Tabot's laptop camera was genuinely compromised (as opposed to the threat being a bluff with no real access), several methods and tools could plausibly have been used:
- **Remote Access Trojans (RATs):** Malicious software such as njRAT, DarkComet, or similar tools that, once installed on a victim's device (often via a disguised download, malicious email attachment, or infected USB drive), allow an attacker to remotely activate the webcam, microphone, and access files without the victim's knowledge (2 marks).
- **Phishing or social engineering for initial access:** The attacker may have sent Tabot a deceptive link or file (disguised as a school document, software crack, or game) that, once opened, silently installed the RAT or spyware on his system (1 mark).
- **Spyware/stalkerware applications:** Commercially available spyware tools, sometimes marketed under the guise of parental control or device-tracking software, can be misused to covertly access a device's camera and files if installed directly or remotely (1 mark).
- **Exploitation of unpatched software vulnerabilities:** If Tabot's operating system or webcam driver software had unpatched security flaws, an attacker with sufficient technical skill could exploit these vulnerabilities to gain unauthorized remote access without requiring the victim to click on anything (1 mark).
- **Webcam indicator bypass techniques:** More sophisticated attackers may use techniques to suppress the webcam's activity light (the small LED that typically indicates when a camera is recording), allowing covert recording without alerting the victim that the camera is active (1 mark).

**4) Roles of key persons (3,3,3 marks)**

- **(a) Law enforcement (3 marks):** Law enforcement officers would be responsible for receiving and formally registering Tabot's sister's complaint, coordinating the physical investigation at the Western Union branch in Douala where the fraudulent collection occurred (including reviewing CCTV footage and staff testimony), tracing the phone number used for the blackmail messages through the telecom operator, and working with ANTIC or a forensic expert to handle the digital evidence. They would also be responsible for identifying and apprehending the suspect(s), particularly given the pattern linking this case to two prior incidents in Buea and Limbe, which suggests a coordinated, multi-victim investigation.

- **(b) Legal department (state counsel) (3 marks):** The state counsel would provide legal guidance on how to properly classify the offence(s) — extortion, fraud, identity theft, and unauthorized computer access — under Cameroon's Law No. 2010/012 on Cybersecurity and Cybercriminality and the Penal Code. They would ensure that evidence collection by law enforcement and forensic experts follows legally defensible procedures (proper authorisation for any data requests to the telecom operator or Western Union), advise on how to handle the cross-victim pattern (whether the three incidents should be prosecuted as a single, connected case), and represent the state in any subsequent court proceedings.

- **(c) Forensic Expert (3 marks):** The forensic expert would be responsible for examining Tabot's laptop to determine whether it was genuinely compromised (checking for installed RATs, spyware, or signs of remote access), extracting and analysing the WhatsApp messages and the metadata of the SIM card used for the threats, and tracing any digital trail connecting the SIM registration, the blackmail messages, and the fraudulent Western Union collection. They would also assist in establishing whether the same device, SIM, or digital fingerprint links this case to the two prior reported incidents in Buea and Limbe.

**5) Steps in the forensic investigation, with execution detail (10 marks)**

- **Identification (2 marks):** The investigator first defines the scope of the case: confirming that it involves (i) the alleged laptop compromise, (ii) the blackmail messages sent via a fraudulently registered SIM, and (iii) the fraudulent Western Union collection. This step is executed by interviewing Tabot and his sister, reviewing the WhatsApp messages, and obtaining an initial incident report from the Western Union branch.

- **Preservation (2 marks):** Once the scope is defined, the investigator ensures no evidence is lost: Tabot's laptop is taken offline and not used further to prevent the attacker from remotely wiping evidence of the intrusion; a formal request is sent to the telecom operator to preserve (not delete) the call/message records and registration data tied to the suspect SIM; and Western Union is requested to preserve CCTV footage and transaction records from the Douala branch before they are routinely overwritten.

- **Collection (2 marks):** The investigator then formally gathers the preserved evidence: a forensic image of Tabot's laptop hard drive is created (using a tool such as FTK Imager) so that all subsequent analysis is performed on a copy rather than the original; certified records of the SIM registration and message logs are obtained from the telecom operator; and the Western Union branch's CCTV footage and the forged ID card used for collection are formally seized as physical/digital evidence.

- **Examination (2 marks):** The collected evidence is then processed: the laptop image is examined (using a tool such as Autopsy) for traces of RAT or spyware installation, unusual outbound network connections, or recently executed unfamiliar files; the SIM registration record is examined to determine what identity document was used and whether it matches the previous two reported cases; and the CCTV footage is reviewed to identify the individual who collected the fraudulent transfer.

- **Analysis (1 mark):** The investigator interprets the findings collectively — correlating the timeline of the blackmail messages, the SIM registration date, and the Western Union collection to establish a coherent sequence of events, and cross-referencing the suspect SIM number and any identifiable patterns (writing style, demand amount, method) against the Buea and Limbe cases to assess whether they were committed by the same individual or group.

- **Presentation (1 mark):** Finally, the investigator compiles all findings into a clear, structured report for use by the state counsel and the court, explaining in accessible terms what evidence was found, how it was obtained, and what conclusions (e.g., identity of the suspect, confirmation of a repeat offending pattern) it supports.

**6) Why is jurisdiction a problem in this digital forensics case? (3 marks)**

Jurisdiction could become a significant problem in this case for several reasons: if the attacker is found to be operating from outside Cameroon (for instance, using a foreign-based messaging service or VPN to mask their location), Cameroonian law enforcement would have no direct authority to compel evidence or arrest the suspect without engaging international legal cooperation mechanisms (1 mark). Even within Cameroon, if the three linked cases (Tabot's, Buea, and Limbe) fall under different local police jurisdictions or judicial districts, coordinating a single unified investigation and prosecution across these boundaries can introduce procedural delays and administrative complexity (1 mark). Additionally, if Western Union's transaction data or the telecom operator's records are stored on servers located outside Cameroon, obtaining timely access to that data may require navigating the foreign jurisdiction's own data protection and disclosure laws, further slowing the investigation (1 mark).

---
---

# SET 2 — Crimes Against Society
## Section C (50 marks)

### Case Scenario

During the build-up to a regional council election in the South West Region of Cameroon, the regional electoral commission's IT office detects unusual activity on the online voter pre-registration portal. Simultaneously, a series of WhatsApp voice notes — purportedly from a well-known local politician making derogatory remarks about a rival ethnic community — begins circulating rapidly across community WhatsApp groups, sparking tension and small-scale unrest in two neighbourhoods. The politician publicly denies ever making the statements, claiming the voice note is fabricated. Days later, technical staff discover that the voter pre-registration portal's database shows over 3,000 duplicate registration entries created within a single overnight period, all using sequentially generated fake national ID numbers. The regional government, alarmed by both the database anomaly and the unrest caused by the voice note, refers the matter to ANTIC and requests a full forensic investigation.

### Questions

**1) What is cybercrime, in the context of this case? (3 marks)**

**2) What could be the motivation behind this combined attack? (5 marks)**

**3) If the voter registration servers were affected, what methods and tools could have been used to create the duplicate entries? (6 marks)**

**4) What will be the role of the following persons in handling this case? (3,3,3,3 marks)**
   - a. ANTIC
   - b. Law enforcement
   - c. The regional electoral commission's IT department
   - d. Forensic Expert

**5) What are some of the steps that will be used in the forensic investigation of the case above, and how will each be executed? (8 marks)**

**6) Why is jurisdiction a problem in this case, especially regarding the voice note? (3 marks)**

**7) What rules/regulations could be considered violated by the actors in this case? (4 marks)**

---

### Detailed Answers

**1) What is cybercrime, in the context of this case? (3 marks)**

Cybercrime refers to illegal activities carried out using computers, networks, or digital technologies (1 mark). In this case, two distinct cyber-enabled offences are present: the unauthorized creation of thousands of fraudulent duplicate entries on the electoral commission's digital registration system, which constitutes unauthorized computer system access and data manipulation (1 mark); and the creation and/or deliberate circulation of a fabricated voice recording designed to deceive the public and incite unrest, which constitutes a form of digital disinformation and potential defamation conducted through electronic communication networks (1 mark).

**2) What could be the motivation behind this combined attack? (5 marks)**

- **Electoral manipulation:** The creation of 3,000 duplicate fake registrations suggests an attempt to artificially inflate voter rolls, potentially to enable later fraudulent voting or to undermine confidence in the electoral roll's integrity (1 mark).
- **Political sabotage:** The fabricated voice note targeting a specific politician suggests a motivation to damage that individual's reputation and electoral prospects, possibly orchestrated by a rival political faction (1 mark).
- **Incitement of social/ethnic division:** By specifically fabricating derogatory remarks about an ethnic community, the perpetrator(s) may be motivated by a desire to deliberately provoke inter-communal tension, potentially to disrupt the election process itself or distract from the database manipulation (1 mark).
- **Distraction/diversion tactic:** It is plausible the two incidents are connected, with the viral voice note deliberately timed to draw public and media attention away from the simultaneous, more technical manipulation of the voter database (1 mark).
- **Undermining public trust in democratic institutions:** Beyond any specific political outcome, a broader motivation may be to erode general public confidence in the fairness and security of the electoral process itself, a goal sometimes pursued by actors seeking to destabilise the region regardless of who specifically benefits electorally (1 mark).

**3) Methods and tools for creating duplicate database entries (6 marks)**

- **SQL Injection:** If the registration portal's input fields were not properly secured, an attacker could inject malicious SQL code to directly insert thousands of fake records into the database, explaining both the volume and the suspiciously sequential nature of the fake ID numbers (2 marks).
- **Automated scripting/bots:** A script (e.g., written in Python) could be used to repeatedly submit the online registration form automatically, generating fake entries with sequentially incremented ID numbers far faster than any human could manually input them, consistent with thousands of entries appearing "within a single overnight period" (2 marks).
- **Exploitation of weak input validation:** If the portal did not properly verify that submitted national ID numbers actually existed in the national identity database before accepting a registration, this vulnerability would allow fabricated ID numbers to be accepted without rejection (1 mark).
- **Compromised administrator credentials:** Alternatively, the attacker may have obtained legitimate administrative access credentials (through phishing or credential theft) and used a direct database management tool to bulk-insert the fraudulent records, which would also explain why the activity could occur without triggering normal user-facing security alerts (1 mark).

**4) Roles of key persons (3,3,3,3 marks)**

- **(a) ANTIC (3 marks):** As Cameroon's national ICT security agency, ANTIC would lead the technical investigation into both the database breach and the voice note's authenticity, coordinating directly with the regional electoral commission's IT staff, potentially deploying its own forensic specialists to analyse server logs and the audio file, and providing an authoritative technical assessment to support any subsequent legal action.

- **(b) Law enforcement (3 marks):** Law enforcement would investigate the unrest triggered by the voice note (taking statements from affected community members, documenting any property damage or violence), coordinate with ANTIC on tracing the technical origin of both incidents, and pursue identification and apprehension of those responsible for both the database manipulation and the disinformation campaign.

- **(c) Regional electoral commission's IT department (3 marks):** This department would provide first-line technical support by supplying server access logs, identifying exactly which accounts or IP addresses were used to create the duplicate entries, assisting forensic investigators in understanding the portal's normal versus abnormal traffic patterns, and implementing immediate containment measures (such as freezing further registrations) to prevent additional fraudulent entries while the investigation proceeds.

- **(d) Forensic Expert (3 marks):** The forensic expert would conduct the detailed technical analysis: examining server logs to trace the exact method used to insert the duplicate records, performing audio forensic analysis on the voice note to assess whether it shows signs of digital splicing, AI voice synthesis, or manipulation, and presenting findings on both fronts in a single coordinated forensic report given the suspected connection between the two incidents.

**5) Steps in forensic investigation and execution (8 marks)**

- **Identification (1.5 marks):** Investigators define the scope as covering both the database anomaly (3,000 duplicate entries) and the voice note's authenticity, executed by reviewing the IT department's initial anomaly report and collecting the circulating voice note files from affected WhatsApp groups.

- **Preservation (1.5 marks):** The electoral commission's database is backed up and frozen from further write access to prevent additional tampering or accidental overwriting of the evidence of fraudulent entries, while the original voice note file(s), along with their associated WhatsApp metadata (sender numbers, group names, timestamps of first appearance), are preserved before they can be deleted by users or groups.

- **Collection (1.5 marks):** Server access logs covering the overnight period of the anomaly are formally collected, along with the complete set of 3,000 duplicate records for pattern analysis, and the voice note is collected directly from its earliest identifiable source (the first WhatsApp group or account where it appeared) along with the file's available metadata.

- **Examination (1.5 marks):** The server logs are examined to identify the specific IP addresses, timestamps, and method (e.g., SQL injection signatures or automated submission patterns) used to create the fake entries, while the voice note is examined using audio forensic techniques to detect splicing artefacts, inconsistent background noise, or signs of AI-based voice cloning.

- **Analysis (1 mark):** Findings from both strands are correlated — for instance, checking whether the timing of the database manipulation aligns with or precedes the voice note's release, which would support the theory that the two incidents are part of a single coordinated operation.

- **Presentation (1 mark):** A consolidated report is prepared for ANTIC, law enforcement, and the regional government, clearly explaining the technical findings on both the database manipulation and the voice note's authenticity, and the evidentiary basis for any conclusions about coordination between the two incidents.

**6) Why is jurisdiction a problem, especially regarding the voice note? (3 marks)**

The voice note was circulated via WhatsApp, a platform owned by Meta and operating under international data governance policies; if investigators need backend data (such as the account that originally uploaded or first sent the voice note, or its associated phone number and IP address) directly from WhatsApp/Meta, this requires a formal legal request to a foreign company governed by foreign law, which can be slow and is not guaranteed to succeed (1 mark). If the voice note's creator used a VPN or a phone number registered in a different country, tracing the true point of origin becomes significantly more difficult and may extend the investigation beyond Cameroon's direct legal authority (1 mark). Additionally, if the voice note (or the database attack) is found to have originated from individuals outside Cameroon, prosecuting them would require international cooperation mechanisms that may not exist or may be slow to engage, particularly given the urgency created by the ongoing community unrest (1 mark).

**7) What rules/regulations could be considered violated? (4 marks)**

- Cameroon's **Law No. 2010/012 of 21 December 2010 on Cybersecurity and Cybercriminality**, specifically provisions criminalising unauthorized access to and manipulation of computer systems (covering the database intrusion) (1 mark).
- Provisions of the **Penal Code relating to defamation and incitement to public disorder/hate**, given the fabricated voice note's role in sparking inter-communal tension (1 mark).
- **Electoral law provisions** governing the integrity of voter registration, since deliberately falsifying voter roll entries constitutes electoral fraud under Cameroonian electoral legislation (1 mark).
- Potentially, provisions concerning **identity-related offences**, since the fraudulent entries used fabricated national ID numbers, implicating laws protecting the integrity of national identification systems (1 mark).

---
---

# SET 3 — Crimes Against Property
## Section C (50 marks)

### Case Scenario

A medium-sized agricultural cooperative based in Bafoussam, COOPAGRI, operates an online platform allowing farmers across the West Region to register, list their produce, and connect with buyers, including several export companies. COOPAGRI's manager receives complaints from three buyers stating that they had paid deposits totalling FCFA 3,200,000 through a "COOPAGRI" website that turned out to be a near-identical clone, hosted at "coopagri-officiel.shop" instead of the real "coopagri.cm". Upon investigation, COOPAGRI's IT contractor discovers that the cloned site contains the exact same farmer listings, photos, and cooperative logo as the real platform, and that the real platform's admin panel shows three suspicious login attempts from an unfamiliar IP address two weeks before the clone appeared online. The cooperative's board, fearing further financial damage to its reputation and member farmers, demands an urgent investigation and wants to know whether their own staff may have been involved in leaking the website's data.

### Questions

**1) Why will this be treated as a cybercrime against property? (3 marks)**

**2) What could be the motivation behind cloning COOPAGRI's website? (4 marks)**

**3) Given the suspicious admin panel login attempts, what methods and tools could the attacker have used to gain the data needed to build the clone? (6 marks)**

**4) What will be the role of the following persons in resolving this case? (3,3,3 marks)**
   - a. Law enforcement
   - b. COOPAGRI's IT contractor
   - c. Forensic Expert

**5) What are the steps that will be used in the forensic investigation of this case, and how will each be executed? (10 marks)**

**6) Why might it be difficult to determine whether an insider (COOPAGRI staff) was involved? (4 marks)**

**7) Why is jurisdiction potentially a problem in this case? (3 marks)**

---

### Detailed Answers

**1) Why will this be treated as a cybercrime against property? (3 marks)**

This case is a cybercrime against property because it directly targets COOPAGRI's digital and intellectual assets: its website design, farmer listings, photographs, and cooperative logo were copied without authorization (1 mark). It also targets the financial property of the three buyers who paid deposits to the fraudulent clone, money which was never received by the legitimate cooperative (1 mark). Additionally, COOPAGRI's brand reputation and the trust relationship with its buyers and member farmers — itself a form of valuable intangible business property — has been damaged by the existence of a convincing fraudulent clone bearing its identity (1 mark).

**2) What could be the motivation behind cloning COOPAGRI's website? (4 marks)**

- **Direct financial fraud:** The clear and immediate motivation is collecting deposit payments from buyers who believe they are dealing with the legitimate cooperative, as evidenced by the FCFA 3,200,000 already collected (1 mark).
- **Exploitation of an established trust relationship:** By copying real farmer listings, photos, and the cooperative's logo, the attacker leverages the credibility and existing buyer relationships that COOPAGRI had already built, making the fraud more convincing than a generic scam site (1 mark).
- **Targeting a sector with limited digital literacy/verification habits:** Agricultural buyers and cooperative members in the region may have lower familiarity with verifying domain authenticity before making payments, making this an attractive, lower-risk target compared to more digitally sophisticated sectors (1 mark).
- **Possible reputational sabotage by a competitor:** It is also possible that a rival cooperative or competing business interest orchestrated the clone specifically to damage COOPAGRI's reputation among its export buyers, beyond pure direct financial gain (1 mark).

**3) Methods and tools for obtaining the data needed to build the clone (6 marks)**

- **Unauthorized admin panel access via the suspicious login attempts:** The three suspicious login attempts from an unfamiliar IP address two weeks before the clone appeared strongly suggest the attacker attempted (and may have succeeded) in gaining direct administrative access to COOPAGRI's real platform, which would have given them full access to farmer listings, photos, and design files directly from the source (2 marks).
- **Credential theft via phishing:** The attacker may have obtained valid admin login credentials by sending a phishing email or message to a COOPAGRI staff member with administrative access, tricking them into revealing their username and password (1 mark).
- **Brute-force or credential-stuffing attacks:** Automated tools could have been used to repeatedly attempt login combinations (brute-force) or to test username/password pairs leaked from unrelated data breaches (credential stuffing) against the admin panel, consistent with multiple login attempts from one IP address (1 mark).
- **Web scraping tools:** Even without admin access, simpler tools such as Httrack could have been used to systematically download and copy all publicly visible content from the legitimate site — listings, photos, and design — without needing to breach the admin panel at all, meaning the suspicious login attempts and the cloning could potentially be two related but technically separate aspects of the same operation (1 mark).
- **Source code inspection via browser developer tools:** The attacker could have used standard browser developer tools to inspect and copy the HTML, CSS, and JavaScript structure of the legitimate site's publicly accessible pages, replicating its design without needing any unauthorized backend access (1 mark).

**4) Roles of key persons (3,3,3 marks)**

- **(a) Law enforcement (3 marks):** Law enforcement would formally register the complaint from the affected buyers and COOPAGRI's management, coordinate with the forensic expert to gather evidence from both the legitimate and cloned websites, investigate the domain registration details of the fraudulent site to identify the registrant, and pursue identification and prosecution of the individual(s) responsible once sufficient evidence is gathered.

- **(b) COOPAGRI's IT contractor (3 marks):** The IT contractor would provide critical first-hand technical information, including the server access logs showing the suspicious login attempts (IP addresses, timestamps, which accounts were targeted), assist in confirming exactly which data (listings, images, design files) may have been accessed or downloaded during those login attempts, and support the forensic expert by providing necessary system access and documentation of the platform's normal operation for comparison purposes.

- **(c) Forensic Expert (3 marks):** The forensic expert would conduct the technical investigation comparing the legitimate and cloned websites' source code and content, analyse the suspicious login attempt logs to determine whether they succeeded and what data was potentially exposed, investigate the cloned domain's registration details, and assess whether the evidence points toward an external attacker, an insider, or some combination of both.

**5) Steps in forensic investigation and execution (10 marks)**

- **Identification (1.5 marks):** Investigators confirm and scope the incident by comparing the real and cloned websites side by side (layout, listings, logo) and reviewing the buyer complaints to establish the financial scope of harm, and reviewing the admin panel's suspicious login alert to determine if it is connected.

- **Preservation (1.5 marks):** The legitimate platform's server logs covering the period of the suspicious login attempts are immediately preserved (backed up) before any automatic log rotation could delete them; the cloned website is captured (screenshots, full page downloads) before it can be taken down by the perpetrator once they realise an investigation is underway.

- **Collection (2 marks):** A complete copy of both websites is collected using a tool such as Httrack for offline comparison; the domain registration record for "coopagri-officiel.shop" is collected via an ICANN Lookup WHOIS query; and the server access logs, including the three suspicious login attempts' IP addresses and timestamps, are formally collected from COOPAGRI's hosting provider.

- **Examination (2 marks):** The two websites' source code is examined using a tool such as WinMerge to confirm identical or near-identical code, layout, and content, providing strong technical proof of copying; the suspicious login attempts are examined to determine whether they originated from a known COOPAGRI staff device/network or an entirely external, unrecognised source.

- **Analysis (1.5 marks):** The investigator correlates the timing of the suspicious login attempts (two weeks prior) with the appearance of the clone, supporting the theory that data obtained through that access was used to build the fraudulent site, and cross-references the buyers' payment records with the clone's payment collection mechanism to trace where the FCFA 3,200,000 was ultimately transferred.

- **Presentation (1.5 marks):** A final report is compiled for COOPAGRI's board and law enforcement, clearly setting out the evidence linking the suspicious admin access to the website cloning, the financial harm to identified victims, and recommendations for both prosecution and improved platform security going forward.

**6) Why might it be difficult to determine whether an insider was involved? (4 marks)**

Determining insider involvement is difficult for several reasons: legitimate staff members with authorised admin access would generate login records that look procedurally similar to the suspicious unauthorized attempts, making it hard to distinguish a staff member acting maliciously from a genuine external attacker who has merely stolen or guessed valid credentials (1 mark). If the suspicious IP address happens to resolve to a shared or dynamic IP range (such as a public Wi-Fi network or mobile data connection also used by legitimate staff), this could create ambiguity rather than a clear external/internal distinction (1 mark). Staff members under suspicion may have both the motive to deny involvement and sufficient legitimate access to potentially cover their tracks more effectively than an external attacker unfamiliar with the system's internal logging and monitoring setup (1 mark). Finally, without comprehensive baseline logging of normal staff access patterns prior to the incident, it may be impossible to establish what "unusual" insider behaviour would even look like, since the investigation may lack a clear point of comparison (1 mark).

**7) Why is jurisdiction potentially a problem in this case? (3 marks)**

If the fraudulent domain "coopagri-officiel.shop" was registered through a foreign registrar or is hosted on servers outside Cameroon, COOPAGRI and Cameroonian law enforcement would need to navigate that country's legal processes to obtain registrant information or request a takedown, which can be slow and uncertain (1 mark). If the suspicious login attempts originated from an IP address that traces to a location outside Cameroon, pursuing the responsible individual would require international cooperation that may not be readily available for a case of this financial scale (1 mark). Even if the perpetrator is eventually identified as being based outside Cameroon, extraditing them or compelling their cooperation with a Cameroonian investigation would depend on bilateral or international legal frameworks that may not exist or may not prioritise a case of this size (1 mark).

---
---

# SET 4 — Crimes Against Government & General Forensic Principles
## Section C (50 marks)

### Case Scenario

The Ministry of Public Health's regional vaccination data management system, used to track immunisation records and supply chain data for the North West Region, suddenly becomes inaccessible to all regional health centres on a Monday morning. IT staff at the regional health delegation discover a ransom note displayed on the main server's login screen, demanding payment in cryptocurrency within 72 hours, threatening to permanently delete all vaccination records if payment is not made. With over 200,000 children's immunisation records at risk and several ongoing vaccination campaigns dependent on the system, the regional delegate of public health declares the situation a national health data emergency and requests urgent support from ANTIC and the Ministry of Defence's cyber unit, given the system's classification as critical government health infrastructure.

### Questions

**1) What is cybercrime, and why does this scenario qualify as a cybercrime against government infrastructure? (4 marks)**

**2) What could be the motivation behind this attack? (4 marks)**

**3) Given that this appears to be a ransomware attack, what methods and tools were likely used to carry it out? (8 marks)**

**4) What will be the role of the following persons/bodies in handling this case? (2,2,2,2,2 marks)**
   - a. ANTIC
   - b. Ministry of Defence's cyber unit
   - c. Regional health delegation's IT staff
   - d. Legal department (state counsel)
   - e. Forensic Expert

**5) What are the steps that will be used in the forensic investigation of this case, and how will each be executed? (10 marks)**

**6) Why is jurisdiction a problem in ransomware cases such as this one? (4 marks)**

**7) Should the ransom be paid? Justify your answer with reference to forensic and risk considerations. (4 marks)**

---

### Detailed Answers

**1) What is cybercrime, and why does this qualify as a crime against government infrastructure? (4 marks)**

Cybercrime is illegal activity conducted using computers, networks, or digital technologies, encompassing offences such as hacking, ransomware deployment, data theft, and system sabotage (2 marks). This scenario qualifies specifically as a cybercrime against government infrastructure because the targeted system — the regional vaccination data management system — is a critical, state-operated public health asset, and the attack's impact extends beyond any single individual to threaten a core government function (public health service delivery) affecting an entire region and over 200,000 citizens' health records, which is precisely the defining characteristic of crimes against government/critical infrastructure as opposed to crimes against an individual person or a private company's property (2 marks).

**2) What could be the motivation behind this attack? (4 marks)**

- **Financial gain (extortion):** The explicit ransom demand in cryptocurrency is the most direct evidence of financial motivation, exploiting the urgency and high stakes of healthcare data to pressure rapid payment (1 mark).
- **Disruption of public services:** Beyond pure financial motive, the attacker may also be motivated by a desire to disrupt government health operations specifically, possibly to embarrass the government or demonstrate the vulnerability of public infrastructure (1 mark).
- **Opportunistic targeting of under-resourced systems:** Government health systems in many regions may have lower cybersecurity investment relative to their criticality, making them attractive, comparatively low-effort targets for ransomware groups seeking reliable payouts from victims who cannot afford prolonged downtime (1 mark).
- **Possible political or ideological motivation:** Depending on further investigation, it is also possible (though not yet confirmed in this scenario) that the timing — disrupting active vaccination campaigns — suggests an additional motivation of undermining public health initiatives or government credibility, beyond simple financial extortion (1 mark).

**3) Methods and tools likely used in the ransomware attack (8 marks)**

- **Initial access via phishing email:** Most ransomware campaigns begin when an employee opens a malicious email attachment or clicks a malicious link, which silently installs the initial malware payload onto the network (2 marks).
- **Exploitation of unpatched vulnerabilities:** Alternatively or additionally, the attacker may have exploited a known but unpatched vulnerability in the server's operating system or remote access software (such as an exposed Remote Desktop Protocol service with weak credentials) to gain initial network access without needing any user interaction (2 marks).
- **Lateral movement tools:** Once inside the network, attackers commonly use tools such as Mimikatz (to harvest additional credentials from memory) or built-in administrative tools (like PsExec) to move from the initially compromised machine to the critical server hosting the vaccination database, escalating their access and reach (1 mark).
- **Ransomware encryption payload:** A specific ransomware strain (such as variants similar to LockBit, Conti, or other known ransomware families) would then be deployed to encrypt the database and associated files, rendering them inaccessible and displaying the ransom note observed on the login screen (2 marks).
- **Command-and-control infrastructure:** The ransomware would typically communicate with an external command-and-control server to receive encryption keys or confirm successful deployment, and analysing any captured network traffic (using a tool like Wireshark) could help identify this infrastructure (1 mark).

**4) Roles of key persons/bodies (2,2,2,2,2 marks)**

- **(a) ANTIC (2 marks):** ANTIC would lead the national-level technical coordination of the response, providing specialised ransomware incident response expertise, advising on whether decryption is possible without paying the ransom, and coordinating communication between the regional health delegation and other national bodies.

- **(b) Ministry of Defence's cyber unit (2 marks):** Given the classification of this system as critical government infrastructure, the Ministry of Defence's cyber unit would assess whether the attack has any national security dimensions, support network-level containment and threat-actor attribution (particularly if there is any suspicion of a state-sponsored or organised criminal group with a known pattern), and provide additional technical resources beyond what civilian agencies alone could mobilise given the emergency declaration.

- **(c) Regional health delegation's IT staff (2 marks):** The IT staff would provide the first-line technical response, including isolating affected systems from the network to prevent further spread, supplying system logs and technical details of the ransom note and affected servers to forensic investigators, and supporting any recovery efforts (such as restoring from backups, if available) once the investigation permits.

- **(d) Legal department (state counsel) (2 marks):** State counsel would advise on the legal and policy implications of the ransom demand (including any government policy on whether ransoms may be paid), ensure that the emergency response actions remain within legal bounds, and prepare for potential prosecution once the attacker(s) are identified, including coordination with international legal mechanisms if the attacker is based abroad.

- **(e) Forensic Expert (2 marks):** The forensic expert would conduct the technical investigation into how the ransomware gained access, what data was actually affected or exfiltrated (as opposed to merely encrypted), and would assist in determining whether decryption without payment is feasible, while documenting all findings for both the immediate recovery effort and any future prosecution.

**5) Steps in forensic investigation and execution (10 marks)**

- **Identification (1.5 marks):** Investigators confirm the scope of affected systems by reviewing the ransom note, determining which servers and databases are encrypted versus still accessible, and establishing the likely point of initial compromise based on IT staff's account of recent unusual activity.

- **Preservation (2 marks):** Critically, the affected server(s) must be isolated from the network immediately (disconnected, not powered off, to preserve volatile memory evidence) to prevent further spread of the ransomware to other connected systems, while any available system logs from before the encryption occurred are preserved before they can be overwritten or further compromised.

- **Collection (2 marks):** A forensic image of the affected server's storage (and, where possible, a memory/RAM capture before any shutdown, since ransomware encryption keys may sometimes be recoverable from memory) is created using appropriate forensic imaging tools; network logs and firewall records covering the period leading up to the attack are also collected to trace the initial intrusion point.

- **Examination (2 marks):** The forensic image is examined for indicators of compromise — the specific ransomware strain's file signatures, any phishing email or malicious attachment that may have served as the entry point, and evidence of lateral movement tools used to reach the critical database server.

- **Analysis (1.5 marks):** Investigators analyse the complete timeline from initial compromise through to encryption, identify whether any data was exfiltrated before encryption (common in modern "double extortion" ransomware tactics), and assess whether the specific ransomware variant has any known weaknesses that might allow decryption without paying the ransom.

- **Presentation (1 mark):** A comprehensive report is prepared for ANTIC, the Ministry of Defence's cyber unit, and the regional health delegation, detailing how the attack occurred, its full scope and impact, and recommendations for both immediate recovery and future prevention.

**6) Why is jurisdiction a problem in ransomware cases such as this? (4 marks)**

Ransomware groups frequently operate from jurisdictions with limited cooperation with Cameroonian or even broader African and Western law enforcement, making identification and prosecution of the actual perpetrators extremely difficult even when their technical methods are well understood (1 mark). The cryptocurrency payment demanded is itself designed to be difficult to trace across borders, often routed through mixing services and exchanges in multiple countries before any funds could potentially be recovered or traced to a real identity (1 mark). The command-and-control infrastructure used to manage the ransomware is typically hosted across multiple countries specifically to complicate any single jurisdiction's ability to investigate or take down the infrastructure unilaterally (1 mark). Even if specific individuals are eventually identified, many ransomware operations are based in countries without extradition treaties with Cameroon, meaning that even a fully successful technical investigation may not result in the perpetrators ever facing prosecution (1 mark).

**7) Should the ransom be paid? Justify your answer with reference to forensic and risk considerations. (4 marks)**

Generally, the recommended position — consistent with international cybersecurity guidance and law enforcement advice — is that the ransom should **not** be paid, for several justified reasons. First, paying the ransom provides no guarantee that the attacker will actually provide a working decryption key or that all data will be restored, since the attacker has no binding obligation to honour the demand once paid (1 mark). Second, paying directly funds and incentivises further criminal ransomware activity, both by this specific group against future victims and by signalling to the broader criminal ecosystem that government health systems are a viable, profitable target (1 mark). Third, from a forensic standpoint, the priority should instead be determining whether secure backups exist that can restore the system independently of the attacker, and whether the specific ransomware variant has any publicly known decryption tools developed by cybersecurity researchers (a forensic expert's analysis of the ransomware's specific signature is essential to answering this) (1 mark). Fourth, given that this is a government system, paying a ransom may also raise broader policy concerns about whether public funds should ever be used to reward cyber-extortion, an issue the legal department and government leadership would need to weigh alongside the urgent practical need to restore critical vaccination records — meaning a final decision would balance the immediate humanitarian risk to the vaccination campaign against these broader strategic and ethical considerations (1 mark).

---

*End of Restructured Section C.*

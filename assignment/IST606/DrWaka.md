# IST606 Theoretical Research Assignment

## Deep Dive Into Malware Theory: Viruses, Trojan Horses, and Worms

### Student Note
This report is written as a **defensive academic analysis**. It explains malware behavior, impact, and manifestation patterns, and includes only a **safe, benign simulation** for educational demonstration. It does not include harmful code, exploit logic, or offensive deployment steps.

---

## 1. Definitions and Taxonomy (Virus, Worm, Trojan Horse)

Malware (malicious software) is any code intentionally designed to compromise confidentiality, integrity, or availability of systems and data. Three foundational malware families in cybersecurity theory are **viruses**, **worms**, and **trojan horses**.

### 1.1 Virus
A **virus** is malware that requires a host object (for example, an executable, macro-enabled document, script, or boot sector) and spreads when the host is executed or shared.

Core characteristics:
- Host-dependent (cannot usually spread as a truly standalone agent).
- Often modifies legitimate files by injecting malicious payloads.
- Spread is commonly assisted by user action (opening files, sharing USB, email attachments).

Typical stages:
1. Attachment to host file.
2. Dormancy (optional waiting trigger).
3. Replication and infection of additional files.
4. Payload activation (for example, data corruption, ransomware behavior, sabotage).

### 1.2 Worm
A **worm** is a self-contained, self-propagating malware that spreads across networks without requiring a host file in the classic sense.

Core characteristics:
- Standalone propagation logic.
- Uses network weaknesses, weak credentials, exposed services, or software vulnerabilities.
- Can spread at high speed, producing large-scale operational disruption.

Typical stages:
1. Scanning for reachable targets.
2. Exploitation or unauthorized access.
3. Self-copying to remote systems.
4. Optional secondary payload (botnet enrollment, data theft, cryptomining).

### 1.3 Trojan Horse
A **trojan horse** is malware disguised as legitimate software or an apparently harmless file. Unlike worms, trojans generally do not self-replicate aggressively by default.

Core characteristics:
- Relies on deception and social engineering.
- Appears useful or trustworthy (fake updates, cracked software, malicious installers).
- Opens backdoors, steals credentials, or downloads additional malware after execution.

Typical stages:
1. Social engineering delivery.
2. User execution.
3. Installation of hidden functionality.
4. Command-and-control communication or local abuse.

### 1.4 Comparative Summary

| Property | Virus | Worm | Trojan Horse |
|---|---|---|---|
| Needs host file | Yes | No (usually standalone) | No strict host requirement, but often disguised installer |
| Self-propagation | Limited, host-mediated | Strong network propagation | Usually limited; propagation mostly via social spread |
| Main enabler | File sharing / execution | Network exposure / vulnerabilities | Human trust and deception |
| Typical impact | File infection, corruption | Rapid spread, service disruption | Backdoor, spying, credential theft |

---

## 2. Lifecycle and Propagation Theory

Although malware families differ, many follow a common kill-chain style lifecycle:

### 2.1 Initial Access
Common entry vectors:
- Phishing attachments or links.
- Drive-by browser downloads.
- Infected USB devices.
- Compromised software updates (supply-chain).
- Exposed remote access services (RDP/SSH) with weak credentials.

### 2.2 Execution
The malicious code gains execution context:
- User-level process launch.
- Script engines (PowerShell, WScript, macros).
- Exploit-triggered shellcode or loader behavior.

### 2.3 Persistence
To survive reboot or user logout, malware may create persistence artifacts:
- Scheduled tasks or startup entries.
- Service creation.
- Registry run keys (Windows).
- Login scripts or cron jobs (Unix-like systems).

### 2.4 Privilege Escalation and Defense Evasion
Advanced samples attempt to:
- Elevate rights from standard user to admin/root.
- Disable logging and security tools.
- Obfuscate payloads to evade signature detection.

### 2.5 Lateral Movement and Command/Control
More mature campaigns move inside a network:
- Credential reuse or token theft.
- Remote service abuse.
- Beaconing to external command-and-control servers.

### 2.6 Actions on Objectives
Final goals include:
- Data theft and exfiltration.
- File encryption for ransom.
- Botnet coordination.
- Fraud, sabotage, or intelligence collection.

---

## 3. Technical Manifestation in Systems (How Malware Appears in Real Environments)

Malware manifestation means the observable changes it creates in endpoints, servers, and network telemetry.

### 3.1 Endpoint Indicators
- Unexpected process trees (for example, office app spawning shell process).
- New autorun entries or scheduled tasks not tied to approved software.
- Sudden creation of similarly named files across many directories.
- Unusual CPU, memory, or disk I/O spikes without business workload explanation.

### 3.2 File System Indicators
- Unauthorized modification of executables or scripts.
- Hash mismatch against known-good baselines.
- Hidden files or suspicious extensions.
- Mass file rename/encrypt patterns.

### 3.3 Network Indicators
- Repeated outbound calls to unknown IP/domain destinations.
- Unusual protocol usage from non-network tools.
- Rapid internal scanning behavior (many connection attempts across ports/hosts).
- Data transfer anomalies (e.g., exfiltration bursts at odd hours).

### 3.4 Identity and Access Indicators
- Login attempts from impossible travel patterns.
- Privilege changes outside normal admin windows.
- Creation of unexpected service accounts.
- Repeated authentication failures followed by successful access.

### 3.5 Mapping to Defensive Frameworks
Using frameworks like MITRE ATT&CK helps categorize behavior by tactics:
- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Defense Evasion
- Credential Access
- Lateral Movement
- Exfiltration
- Impact

This behavior-based framing is critical because modern variants mutate code quickly, but behavior patterns often remain detectable.

---

## 4. Historical Case Studies and Lessons

### 4.1 Virus Case: Melissa (1999)
What happened:
- Macro virus delivered through infected Word document attachments.
- Leveraged email clients to send itself to contact lists.

Why it mattered:
- Demonstrated how user productivity tools can become malware vectors.
- Showed that social trust and macro execution settings are major risks.

Lesson:
- Macro controls, attachment filtering, and least-privileged execution reduce risk significantly.

### 4.2 Worm Case: WannaCry (2017)
What happened:
- Ransomware worm that spread using an SMB vulnerability.
- Impacted hospitals, enterprises, and public infrastructure globally.

Why it mattered:
- Combined worm-speed propagation with ransomware impact.
- Revealed the operational cost of delayed patch management.

Lesson:
- Aggressive patching, network segmentation, and tested backup strategy are essential.

### 4.3 Trojan Case: Zeus / Zbot Family
What happened:
- Banking trojan focused on credential theft and financial fraud.
- Used keylogging and web-injection techniques on infected hosts.

Why it mattered:
- Demonstrated long-term monetization through silent credential abuse.
- Highlighted the role of social engineering and downloader chains.

Lesson:
- Multi-factor authentication, browser hardening, and endpoint monitoring are key controls.

---

## 5. Safe Simulation Demonstration (Benign and Non-Destructive)

### 5.1 Purpose of the Simulation
To academically demonstrate malware-like **spread patterns and detection logic** without creating real malware.

The simulation below:
- Creates harmless marker text files named `SIMULATED_INFECTION.txt`.
- Copies those marker files through a controlled test directory.
- Logs every action with timestamp.
- Never executes arbitrary payloads.
- Never modifies system settings.
- Never transmits data over the internet.

### 5.2 Ethical Safety Constraints
This simulation is safe because it avoids all harmful characteristics:
- No persistence mechanism.
- No privilege escalation.
- No code injection.
- No network exploitation.
- No deletion or encryption of user data.

### 5.3 Benign Python Simulation Code

```python
from pathlib import Path
from datetime import datetime
import shutil


def log_event(log_file: Path, message: str) -> None:
	 timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	 with log_file.open("a", encoding="utf-8") as f:
		  f.write(f"[{timestamp}] {message}\n")


def setup_demo_environment(base_dir: Path) -> list[Path]:
	 """Create isolated folders for a harmless spread-pattern demo."""
	 targets = [
		  base_dir / "department_a",
		  base_dir / "department_b",
		  base_dir / "department_c" / "subfolder_1",
		  base_dir / "department_c" / "subfolder_2",
	 ]
	 for folder in targets:
		  folder.mkdir(parents=True, exist_ok=True)
	 return targets


def benign_spread_simulation(base_dir: Path) -> None:
	 base_dir.mkdir(parents=True, exist_ok=True)
	 log_file = base_dir / "simulation.log"
	 quarantine_dir = base_dir / "quarantine"
	 quarantine_dir.mkdir(exist_ok=True)

	 log_event(log_file, "Simulation started")
	 targets = setup_demo_environment(base_dir)

	 # Create a harmless marker file to represent an "infected artifact".
	 seed_file = base_dir / "seed" / "SIMULATED_INFECTION.txt"
	 seed_file.parent.mkdir(parents=True, exist_ok=True)
	 seed_file.write_text(
		  "This is a harmless training marker file. No malware behavior.\n",
		  encoding="utf-8",
	 )
	 log_event(log_file, f"Seed marker created: {seed_file}")

	 # Simulate spread by copying the marker to test folders.
	 created_markers = []
	 for target in targets:
		  marker = target / "SIMULATED_INFECTION.txt"
		  shutil.copy2(seed_file, marker)
		  created_markers.append(marker)
		  log_event(log_file, f"Marker copied to: {marker}")

	 # Detection heuristic: flag if marker count exceeds threshold.
	 threshold = 3
	 if len(created_markers) > threshold:
		  log_event(
				log_file,
				f"ALERT: marker burst detected ({len(created_markers)} > {threshold})",
		  )

		  # Mock quarantine operation (safe file move).
		  for marker in created_markers:
				quarantined_path = quarantine_dir / marker.name
				marker.replace(quarantined_path)
				log_event(log_file, f"Quarantined: {quarantined_path}")

	 log_event(log_file, "Simulation finished successfully")


if __name__ == "__main__":
	 demo_root = Path("./safe_malware_simulation_lab")
	 benign_spread_simulation(demo_root)
	 print("Safe simulation complete. Check simulation.log for details.")
```

### 5.4 How to Explain This in Your Report
In your write-up, describe the simulation as follows:
- The code models **propagation pattern only**, not malicious capability.
- Marker-file spread approximates how infections can scale through shared resources.
- Log analysis demonstrates how defenders detect anomalies using thresholds.
- Mock quarantine represents incident response containment in production SOC workflows.

---

## 6. Prevention, Detection, and Incident Response Strategy

### 6.1 Preventive Controls
1. Patch and vulnerability management:
	Close known software vulnerabilities rapidly.
2. Least privilege:
	Limit admin access and enforce role-based permissions.
3. Email and web filtering:
	Block malicious attachments, links, and known bad domains.
4. Application allowlisting:
	Permit execution only for approved binaries/scripts.
5. Security awareness training:
	Reduce social engineering success rates.

### 6.2 Detective Controls
1. Endpoint Detection and Response (EDR):
	Monitor process creation, script execution, and persistence artifacts.
2. SIEM correlation:
	Combine logs from endpoints, identity systems, and firewalls.
3. File integrity monitoring:
	Detect unauthorized changes and hash deviations.
4. Network behavior analytics:
	Identify unusual scanning, beaconing, and data transfer patterns.

### 6.3 Corrective and Recovery Controls
1. Isolate infected hosts immediately.
2. Revoke compromised credentials and tokens.
3. Remove persistence artifacts and malicious binaries.
4. Restore from verified clean backups.
5. Conduct root-cause and gap analysis to prevent recurrence.

### 6.4 Incident Response Lifecycle (Practical View)
1. Preparation:
	Playbooks, backup testing, monitoring design.
2. Identification:
	Confirm suspicious behavior and classify severity.
3. Containment:
	Segment and isolate affected systems.
4. Eradication:
	Remove malware artifacts and entry vectors.
5. Recovery:
	Rebuild/restore systems and validate normal operations.
6. Lessons learned:
	Update controls, training, and architecture.

---

## 7. Practical Demonstration: Vulnerable Program, Controlled Abuse, and Malware-Behavior Simulation

This section documents a separate implementation folder used to support the theoretical research with safe, non-destructive experiments.

### 7.1 Lab Location and Structure
The practical work is implemented in:

- [assignment/IST606/safe-malware-theory-lab](safe-malware-theory-lab)

Core files:

- Vulnerable toy program: [assignment/IST606/safe-malware-theory-lab/src/vulnerable_app.py](safe-malware-theory-lab/src/vulnerable_app.py)
- Controlled abuse demonstration: [assignment/IST606/safe-malware-theory-lab/src/safe_exploit_demo.py](safe-malware-theory-lab/src/safe_exploit_demo.py)
- Virus-style simulator: [assignment/IST606/safe-malware-theory-lab/src/sim_virus.py](safe-malware-theory-lab/src/sim_virus.py)
- Trojan-style simulator: [assignment/IST606/safe-malware-theory-lab/src/sim_trojan.py](safe-malware-theory-lab/src/sim_trojan.py)
- Worm-style simulator: [assignment/IST606/safe-malware-theory-lab/src/sim_worm.py](safe-malware-theory-lab/src/sim_worm.py)
- Detection and quarantine monitor: [assignment/IST606/safe-malware-theory-lab/src/monitor.py](safe-malware-theory-lab/src/monitor.py)
- One-command runner: [assignment/IST606/safe-malware-theory-lab/src/run_all.py](safe-malware-theory-lab/src/run_all.py)

### 7.2 Vulnerability Model in the Toy Program
The vulnerable application intentionally includes insecure patterns that are academically relevant:

1. Unsanitized path handling:
	The app accepts user-controlled file names and writes them directly, illustrating path traversal-style risk.
2. Weak hardcoded authentication token:
	The app uses a simplistic fixed token, demonstrating poor authentication design.
3. Unsafe expression execution pattern:
	The app uses a dangerous pattern in privileged logic to illustrate why this design is forbidden in secure software engineering.

These weaknesses are intentionally introduced to create observable abuse scenarios for learning purposes.

### 7.3 Controlled Abuse Demonstration (Safe "Exploit" Concept)
The controlled abuse script demonstrates policy violation without harmful payloads:

1. File path abuse simulation:
	Shows how insecure path handling can produce writes outside expected paths in a controlled local folder.
2. Authentication weakness simulation:
	Shows how weak token design enables unauthorized privileged action.
3. Unsafe execution path reachability:
	Demonstrates execution of harmless mathematical expressions only, used to explain why this pattern is dangerous.

No destructive actions, no persistence, and no external communication are performed.

### 7.4 Malware Family Behavior Mapping
The three family simulators model behavior signatures only:

1. Virus-style model:
	Creates host-adjacent marker files to mimic file-bound replication behavior.
2. Trojan-style model:
	Displays a benign utility message while performing a hidden harmless marker write, demonstrating deception mechanics.
3. Worm-style model:
	Autonomously traverses a mock network list and writes markers for vulnerable nodes only, demonstrating self-propagation logic.

### 7.5 Detection and Containment
The monitor script demonstrates defensive operations:

1. Detects marker artifacts as indicators of compromise (IOCs).
2. Logs event counts and locations.
3. Quarantines marker files into an isolated folder.

This maps directly to incident response theory in Section 6 (Identification, Containment, Eradication).

### 7.6 Execution Evidence
The full safe workflow was executed successfully using:

python .\assignment\IST606\safe-malware-theory-lab\src\run_all.py

Observed outcomes:

1. Vulnerable app executed and logged normal plus denied/allowed privileged flow.
2. Controlled abuse simulation completed.
3. Virus, trojan, and worm behavior simulators completed.
4. Monitor quarantined marker artifacts and logged the actions.

Evidence artifacts can be inspected in the lab output folder and logs:

- [assignment/IST606/safe-malware-theory-lab/lab_output](safe-malware-theory-lab/lab_output)
- [assignment/IST606/safe-malware-theory-lab/lab_output/events.log](safe-malware-theory-lab/lab_output/events.log)

### 7.7 Screenshot Checklist for Submission
For a complete graded submission, include screenshots of:

1. Terminal output after running the one-command script.
2. Folder tree showing generated marker files and quarantine folder.
3. Excerpts from events.log showing detection and quarantine entries.
4. One short snippet from each simulator file to show behavior mapping.

### 7.8 Academic Integrity and Safety Statement
This practical section does not create malware. It is a constrained educational simulation designed to teach:

1. How vulnerabilities emerge from insecure coding decisions.
2. How malware families differ in propagation and manifestation.
3. How defenders detect, contain, and recover from suspicious behavior.

No harmful payloads or offensive exploitation techniques are included.

---

## Conclusion

Viruses, worms, and trojan horses remain foundational categories in malware theory because they represent distinct propagation and deception models: host infection, autonomous spread, and social-engineered delivery. Their manifestation can be systematically observed through endpoint telemetry, identity events, and network anomalies. The most reliable defense is layered: proactive prevention, real-time detection, disciplined containment, and resilient recovery through tested backups and incident response procedures.

The benign simulation included in this report demonstrates that students can study malware dynamics responsibly by modeling spread and defensive response without creating harmful software. This aligns with ethical cybersecurity practice and supports learning outcomes in threat analysis, detection engineering, and secure system operations.

---

## Optional References (Add in your preferred citation style)

- MITRE ATT&CK knowledge base
- CISA ransomware and malware advisories
- NIST SP 800-61 (Computer Security Incident Handling Guide)
- Academic papers on malware taxonomy and propagation models
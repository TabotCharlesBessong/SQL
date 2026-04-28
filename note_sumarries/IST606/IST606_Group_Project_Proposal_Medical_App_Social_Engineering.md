# IST 606 Group Project Proposal
## Topic: Securing a Medical Appointment Application Against Social Engineering Attacks

## 1. Project Information
- **Course:** IST 606 - Security Management
- **Team Size:** 3 Students
- **Proposed Team Members:**
  - Member 1: [Add Name]
  - Member 2: [Add Name]
  - Member 3: [Add Name]
- **Submission Date:** April 22, 2026

## 2. Proposed Project Title
**MediGuard: Social Engineering Attack Simulation and Defense for a Medical Appointment Platform**

## 3. Background and Rationale
Healthcare systems handle highly sensitive personal and medical information, making them attractive targets for attackers. While many systems focus on technical vulnerabilities, social engineering remains one of the most effective attack methods because it targets human behavior.

Our project focuses on a **medical appointment web application** and demonstrates how social engineering attacks can be used to compromise users and administrators. We will then design and implement practical controls to reduce this risk.

This topic aligns with IST 606 because it connects security management principles with real-world risk assessment, human factors, policy, technical controls, and incident response.

## 4. Problem Statement
Medical applications are vulnerable to social engineering techniques such as phishing, impersonation, and malicious links. Users may unknowingly disclose credentials or execute unsafe actions, leading to unauthorized access, data exposure, and operational disruption.

There is a need for an integrated approach that:
- Simulates realistic social engineering attacks,
- Measures user/system susceptibility,
- Implements and evaluates layered protections.

## 5. Project Goal
To design, implement, and evaluate a medical appointment application prototype that can be tested against social engineering attacks and strengthened through security controls, awareness mechanisms, and policy enforcement.

## 6. Objectives
1. Build a prototype medical appointment platform with core roles and workflows.
2. Define realistic social engineering attack scenarios targeting patients, doctors, and administrators.
3. Execute controlled attack simulations in a safe lab environment.
4. Implement preventive and detective controls to reduce attack success.
5. Measure and compare security outcomes before and after implementing protections.
6. Produce recommendations for secure deployment and user awareness.

## 7. Scope of the Application
### In Scope
- User roles: Patient, Doctor, Admin
- Core modules:
  - User registration and login
  - Appointment booking/cancellation
  - Basic profile and contact details
  - Admin dashboard for user/account management
- Social engineering attack simulations
- Defensive features and security awareness components

### Out of Scope
- Integration with real hospital systems
- Real medical diagnosis or treatment features
- Storage of real patient medical records
- Production deployment on live healthcare infrastructure

## 8. Threat Model and Social Engineering Scenarios
We will test the system against selected scenarios, including:

1. **Phishing Login Page Attack**
   - Users receive a fake login link claiming account verification is required.
   - Goal: steal credentials and attempt account takeover.

2. **Helpdesk/Administrator Impersonation**
   - Attacker sends messages requesting urgent password reset or MFA code.
   - Goal: bypass authentication through social pressure.

3. **Malicious Appointment Confirmation Link**
   - Users receive a fake appointment confirmation email with a malicious URL.
   - Goal: trigger unsafe action or credential capture.

4. **Pretexting for Account Recovery**
   - Attacker pretends to be a patient and requests account changes.
   - Goal: manipulate support/admin workflow.

## 9. Proposed Security Controls
We will implement and evaluate controls such as:

- **Multi-Factor Authentication (MFA)** for sensitive actions and admin logins.
- **Phishing-resistant UI warnings** for suspicious links and unusual requests.
- **Role-Based Access Control (RBAC)** with strict privilege separation.
- **Rate limiting and login anomaly detection** (failed attempts, unusual IPs).
- **Secure password policy** and account lockout thresholds.
- **Verified support workflow** (identity checks before account recovery).
- **Security awareness prompts** integrated into user flows.
- **Audit logging and incident flags** for suspicious behavior.

## 10. Methodology
### Phase 1: Requirements and Design
- Define functional requirements for the medical app.
- Identify assets, actors, and attack surfaces.
- Document threat scenarios and expected impact.

### Phase 2: Prototype Development
- Build the application with baseline functionality.
- Prepare a controlled test environment.

### Phase 3: Attack Simulation (Baseline)
- Run social engineering scenarios against the baseline prototype.
- Record metrics (credential capture attempts, unauthorized actions, user response patterns).

### Phase 4: Defense Implementation
- Add selected technical and procedural controls.
- Include policy and awareness components.

### Phase 5: Re-Test and Evaluation
- Re-run attack scenarios under the same conditions.
- Compare pre-control vs post-control outcomes.
- Analyze what improved and what risks remain.

## 11. Evaluation Metrics
We will assess project success using measurable indicators:

- Attack success rate before and after controls
- Number of blocked suspicious attempts
- Number of unauthorized access events
- User interaction with warning prompts (ignored vs followed)
- Mean time to detect suspicious activity
- Mean time to contain/recover from simulated incidents

## 12. Deliverables
1. **Project Report** (problem, method, results, lessons learned)
2. **Working Prototype** of the medical appointment application
3. **Attack Simulation Scripts/Playbook** for social engineering tests
4. **Security Control Implementation Documentation**
5. **Evaluation Results Dashboard/Table** (before vs after)
6. **Class Presentation Slides and Demo**

## 13. Team Role Distribution (Proposed)
- **Member 1 - Application Development Lead**
  - Build core app modules and role-based workflows.

- **Member 2 - Security & Attack Simulation Lead**
  - Design and execute social engineering scenarios.

- **Member 3 - Defense, Logging, and Evaluation Lead**
  - Implement controls, collect metrics, and prepare analysis.

All members contribute to testing, documentation, and presentation.

## 14. Proposed Timeline (Short Academic Schedule)
- **Week 1:** Finalize requirements, architecture, and scenarios
- **Week 2:** Build baseline prototype
- **Week 3:** Conduct baseline social engineering tests
- **Week 4:** Implement controls and awareness mechanisms
- **Week 5:** Re-test, analyze outcomes, and prepare report/demo

## 15. Risks and Mitigation
- **Risk:** Limited development time  
  **Mitigation:** Keep scope focused on core modules and 3-4 high-value scenarios.

- **Risk:** Inconsistent simulation results  
  **Mitigation:** Use standardized test scripts and fixed test conditions.

- **Risk:** Ethical concerns in social engineering simulation  
  **Mitigation:** Conduct all tests in a controlled environment with informed participants and no real patient data.

## 16. Ethical and Legal Considerations
- No real patient health data will be used.
- All demonstrations use synthetic/sample data.
- No real phishing campaigns will be executed outside the classroom/lab environment.
- The project is for educational and defensive cybersecurity purposes only.

## 17. Expected Outcomes
By the end of this project, we expect to:
- Demonstrate how social engineering can compromise a medical application,
- Show measurable risk reduction after implementing controls,
- Provide practical, security-management-oriented recommendations for healthcare app teams.

## 18. Approval Request
We respectfully submit this proposal for instructor approval and feedback. We are prepared to present the concept, architecture, test plan, and expected deliverables in class.

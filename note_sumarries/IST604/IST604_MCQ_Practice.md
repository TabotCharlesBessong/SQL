# IST604 – Web Services & Distributed Computing
## Chapter 2: Practice MCQ Questions

> **Instructions:** Select the best answer for each question. Answers are provided at the end.

---

### Section A: Fundamentals of Web Services

**1.** Which of the following best defines a web service?

- A) A website accessible through a browser
- B) A standards-based, language-agnostic software entity that communicates over a network using standardized protocols
- C) A local API library bundled within an operating system
- D) A database accessible through SQL over the internet

---

**2.** Which statement correctly distinguishes a web service from an API?

- A) APIs must operate over a network; web services do not
- B) All APIs are web services, but not all web services are APIs
- C) All web services are APIs, but not all APIs are web services
- D) Web services and APIs are functionally identical

---

**3.** Which of the following is NOT a key characteristic of a web service?

- A) Language-agnostic
- B) Vendor-neutral
- C) Requires a shared database
- D) Standards-based

---

**4.** A web service that enables a Java application on a Linux server to communicate with a .NET application on a Windows machine is demonstrating which core capability?

- A) Loose coupling
- B) Service reuse
- C) Interoperability
- D) Transport neutrality

---

### Section B: SOA and Architecture

**5.** In a Service-Oriented Architecture (SOA), which role is responsible for registering and discovering web services?

- A) Service Provider
- B) Service Requester
- C) Service Broker / Registry
- D) Service Consumer

---

**6.** What is the correct relationship between SOA and web services?

- A) SOA is the technical implementation; web services are the blueprint
- B) SOA is the architectural blueprint; web services are the technical implementation
- C) SOA and web services are the same concept
- D) Web services replace the need for SOA

---

**7.** In the SOA model, which protocol/standard is typically used by the service broker for service registration?

- A) SOAP
- B) REST
- C) UDDI
- D) WSDL

---

**8.** Which communication model requires the client to wait for a response before continuing execution?

- A) Messaging-based asynchronous model
- B) Document-based model
- C) RPC-based synchronous model
- D) Fire-and-forget model

---

**9.** Which statement best describes the messaging-based communication model?

- A) The client sends parameters and immediately receives return values
- B) The client sends an entire document and does not wait for a response
- C) The client and server share the same memory space
- D) Communication is always bidirectional and synchronous

---

### Section C: Web Services Standards

**10.** SOAP is best described as:

- A) An architectural style for building lightweight APIs
- B) A W3C-accepted XML-based messaging protocol transported over HTTP, SMTP, or FTP
- C) A registry for discovering and integrating web services
- D) A language for describing the interface of a web service

---

**11.** Which element of a SOAP message is **required**?

- A) Header
- B) Fault
- C) Attachment
- D) Body

---

**12.** What is the role of WSDL in a web services ecosystem?

- A) It transports messages between service providers and consumers
- B) It registers web services in a global directory
- C) It defines the formal interface contract describing a service's operations, data types, and endpoint location
- D) It handles authentication and security for SOAP messages

---

**13.** Which WSDL element is considered the most critical and groups the abstract operations of a service?

- A) `<types>`
- B) `<binding>`
- C) `<portType>` / `<interface>`
- D) `<service>`

---

**14.** UDDI querying returns which artifact describing the corresponding service interface?

- A) A SOAP Envelope
- B) A WSDL description
- C) A REST endpoint URL
- D) An OpenAPI specification

---

**15.** Which of the following correctly describes REST?

- A) A strict, XML-only messaging protocol
- B) A lightweight architectural style using standard HTTP methods and JSON/XML
- C) A registry for discovering RESTful services
- D) A security standard for encrypting web service messages

---

**16.** JSON and XML are both used for data interchange. Which statement is accurate?

- A) XML uses key-value pairs; JSON uses tag-based markup
- B) JSON is a W3C-recommended markup language; XML is a scripting language
- C) JSON is a lightweight, text-based alternative to XML, using key-value pairs and arrays
- D) XML is exclusively used by REST; JSON is exclusively used by SOAP

---

### Section D: SOAP vs. REST

**17.** Which of the following is an advantage of REST over SOAP?

- A) Built-in message-level security via WS-Security
- B) Support for multiple transport protocols (SMTP, JMS, TCP)
- C) Faster performance due to lightweight JSON payloads and HTTP caching
- D) Standardized Fault elements for detailed error reporting

---

**18.** In which scenario would SOAP be the more appropriate choice over REST?

- A) Building a public-facing mobile app API
- B) Designing a microservices architecture for a startup
- C) Processing financial transactions requiring ACID compliance and end-to-end encryption
- D) Creating a lightweight social media feed API

---

**19.** A SOAP request for retrieving a user must be sent using which HTTP method, regardless of the operation type?

- A) GET
- B) PUT
- C) POST
- D) DELETE

---

**20.** Which of the following is a key design philosophy difference between SOAP and REST?

- A) SOAP is resource-based; REST is operation-based
- B) SOAP is operation-based (e.g., `GetUserInfo`); REST is resource-based (e.g., `GET /users/123`)
- C) Both use identical design philosophies but differ only in transport protocol
- D) REST requires a formal WSDL contract; SOAP does not

---

### Section E: WSDL and Implementation

**21.** Which WSDL development approach starts with existing code and auto-generates the WSDL file?

- A) Top-Down (Contract-First)
- B) Bottom-Up (Code-First)
- C) Middle-Out
- D) Schema-First

---

**22.** In WSDL 2.0, the `<portType>` element was renamed to:

- A) `<endpoint>`
- B) `<description>`
- C) `<interface>`
- D) `<binding>`

---

**23.** Which WSDL operational pattern describes a service that sends a message to a client without expecting any response?

- A) Request-Response
- B) One-way
- C) Solicit-Response
- D) Notification

---

**24.** Which Java API is used specifically for building SOAP-based web services?

- A) JAX-RS
- B) Spring Boot
- C) JAX-WS
- D) RESTeasy

---

**25.** Which of the following tools would a developer use to test REST and SOAP web service endpoints?

- A) wsimport and WSDL2Java
- B) Postman and SoapUI
- C) wsgen and Java2WSDL
- D) Jersey and RESTeasy

---

## Answer Key

| Q | Answer | Q | Answer | Q | Answer |
|---|---|---|---|---|---|
| 1 | B | 10 | B | 19 | C |
| 2 | C | 11 | D | 20 | B |
| 3 | C | 12 | C | 21 | B |
| 4 | C | 13 | C | 22 | C |
| 5 | C | 14 | B | 23 | D |
| 6 | B | 15 | B | 24 | C |
| 7 | C | 16 | C | 25 | B |
| 8 | C | 17 | C | | |
| 9 | B | 18 | C | | |

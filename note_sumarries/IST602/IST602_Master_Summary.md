# IST602 Master Summary (Web Essentials + Markup Languages)

## Scope
This master note combines:
- IST602 1: Web Essentials (clients, servers, protocols, HTTP, TCP/UDP)
- IST602 2: Document Markup Languages (SGML, HTML, XML, XHTML, HTML evolution)

## Part A: Web Essentials

### WWW Core Components
- **Server**: hosts and delivers resources/services.
- **Client**: requests resources (usually a web browser).
- **Web Server**: serves web pages/resources using HTTP.
- **Web Page**: a single web document/resource.
- **Website**: collection of related pages under a domain.
- **URL**: unique locator/address for a resource.

### Internet Protocol Fundamentals
- A **protocol** is a formal set of communication rules.
- Protocols define: error checking, data handling, message boundaries, acknowledgments.

### Protocols to Know
- **FTP**: file transfer.
- **SMTP**: email transfer.
- **TCP/IP**: foundational Internet communication suite.

### TCP/IP Role Split
- **TCP**: breaks data into packets, ensures reliable ordered delivery, reassembles at destination.
- **IP**: handles packet addressing and routing (source/destination).

### TCP vs UDP
- **TCP**: connection-oriented, reliable, ordered, higher overhead.
- **UDP**: connectionless, faster/lower overhead, no delivery/order guarantees.
- Use rule of thumb:
  - reliability/data integrity needed -> TCP
  - low-latency streaming/real-time preferred -> UDP

### HTTP Essentials
- Application protocol for web request/response communication.
- Runs over TCP/IP.
- Typical sequence:
  1. Client sends request.
  2. Connection established via TCP.
  3. Server returns response.
  4. Connection may close or persist.
- Connection styles: **non-persistent** and **persistent**.

## Part B: Markup Languages

### What is a Markup Language?
- Tag/symbol based text encoding used to describe document structure and meaning.
- Separates content from presentation for portability and automation.

### SGML
- Meta-standard that defines how markup languages are structured.
- Introduced **DTD** for validating document types/structure.
- Relationship:
  - XML is a simplified subset of SGML.
  - HTML is an SGML application.

### HTML
- Dominant language for web page structure/presentation.
- Optimized for browser rendering.
- Can be extended by scripting (e.g., JavaScript).

### XML
- Extensible, generic language for structured data representation/exchange.
- Supports custom tags and strict syntax constraints.
- Main purpose: describe data/content semantics.

### XHTML
- HTML expressed with XML-style strict rules.
- Intended to reduce ambiguity and improve consistency.
- Adoption challenge: strict error handling was less practical for typical web workflows.

## HTML/XHTML Evolution Snapshot
- **HTML 4.0 (1997)**: feature-rich release.
- **HTML 4.01 (1999)**: cleanup; still loose syntax and inconsistent error handling.
- **XHTML 1.0 (2000)**: HTML 4.01 under XML syntax.
- **XHTML 1.1 (2001)**: stricter modularization.
- **XHTML 2.0 direction**: stricter path, limited practical adoption.
- **HTML5 (2009 trajectory)**: practical standardization, broader adoption; W3C aligned with HTML5 development.

## High-Value Comparisons

### HTML vs XML
- **HTML**: predefined tags; web page structure/presentation.
- **XML**: user-defined tags; data description and interchange.

### Strictness vs Practicality (Theme)
- Strict validation (XHTML/XML philosophy) improves consistency.
- Forgiving parsing (HTML/browser reality) improves usability/adoption.
- Modern web standards evolved to balance both concerns.

## Integrated Quick Revision Table
| Concept | One-line Meaning |
|---|---|
| Client-Server | Client requests, server responds with services/resources |
| URL | Unique Internet resource locator |
| Protocol | Communication rulebook between systems |
| TCP | Reliable, ordered, connection-oriented delivery |
| UDP | Fast, connectionless, best-effort delivery |
| HTTP | Web request/response protocol over TCP/IP |
| SGML | Parent standard/meta-language for markup systems |
| HTML | Web page markup for browser rendering |
| XML | Extensible structured data markup language |
| XHTML | HTML constrained by XML-style strict syntax |

## Exam Checklist
- Define and distinguish client, server, web server, webpage, website, URL.
- Explain what protocols do and why they are required.
- Describe TCP/IP responsibilities clearly.
- Compare TCP and UDP with use-case examples.
- Explain HTTP request-response flow and connection behavior.
- Define SGML, HTML, XML, XHTML and show their relationships.
- Explain HTML vs XML and why XHTML strictness faced adoption issues.
- Recall version evolution from HTML 4.x through XHTML phases to HTML5.

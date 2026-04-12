# IST602 1 Web Essentials (2024-2025) - Summary

## Overview
This lecture introduces foundational web concepts: the major elements of the World Wide Web, core Internet protocols, the client-server model, and the idea of markup languages.

## Key Concepts

### 1. Elements of the WWW
- **Server**: software/machine that stores and delivers information.
- **Client**: software (typically a browser) that initiates requests, receives responses, and displays content.
- **Web server**: delivers web pages/resources over HTTP.
- **Web page**: a single web-accessible document/resource.
- **Website**: a collection of related web pages, usually under one domain/URL base.
- **URL (Uniform Resource Locator)**: unique address used to identify and locate resources on the Internet.

### 2. Internet Protocol Basics
- A **protocol** is a formal rule set for communication between systems.
- Protocols define behaviors such as:
  - error checking
  - compression rules
  - message boundaries
  - acknowledgment/receipt signaling

### 3. Common Internet Protocols Mentioned
- **FTP**: file transfer.
- **SMTP**: email transfer.
- **TCP/IP**: core communication stack for host-to-host communication across and within networks.

### 4. How TCP/IP Works (High Level)
- **TCP** handles segmentation and reliable reassembly of messages.
- **IP** handles addressing/routing information for each packet (source/destination).
- Together they enable end-to-end data delivery across networks.

### 5. TCP vs UDP
- **TCP**:
  - connection-oriented
  - reliable and ordered delivery
  - error checking and recovery
  - suitable for web pages, files, and data integrity needs
- **UDP**:
  - connectionless and lightweight
  - no guaranteed delivery/order or built-in recovery
  - lower overhead
  - suitable for real-time or streaming-style communication where speed is favored over reliability

### 6. HTTP (Hypertext Transfer Protocol)
- Protocol used for transferring hypertext/resources between browser (client) and web server.
- Runs on top of TCP/IP.
- Defines request/response behavior.
- Typical flow:
  1. Browser requests a resource.
  2. HTTP over TCP establishes connection.
  3. Server processes request and sends response.
  4. Connection may close (or persist depending on connection type).
- Mentions **non-persistent** and **persistent** HTTP connections.

### 7. Intro to Markup Languages
- Lecture closes by introducing markup languages as a bridge to the next topic.

## Exam-Focused Takeaways
- Be able to distinguish **client vs server** roles.
- Understand why protocols are needed and what they standardize.
- Know the division of labor in **TCP/IP**.
- Clearly compare **TCP** and **UDP** by reliability, ordering, overhead, and use case.
- Explain the HTTP request-response lifecycle in a client-server setting.

## Quick Revision Table
| Topic | Core Idea |
|---|---|
| Client-Server | Client initiates requests; server provides resources/services |
| URL | Unique locator for Internet resources |
| Protocol | Rules governing communication between systems |
| TCP | Reliable, ordered, connection-oriented transport |
| UDP | Fast, connectionless, best-effort transport |
| HTTP | Web request/response protocol over TCP/IP |

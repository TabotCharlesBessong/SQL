# IST602 2 Markup Languages (2025-2026) - Summary

## Overview
This lecture explains document markup languages, focusing on SGML, HTML, XML, and XHTML, and traces HTML's historical evolution toward HTML5.

## Key Concepts

### 1. What is a Markup Language?
- A text-encoding approach that uses tags/symbols to define:
  - structure
  - formatting
  - relationships in documents
- It separates **content** from **presentation**, enabling reusable processing across systems.
- Core examples in this lecture: **SGML, HTML, XML, XHTML**.

### 2. SGML (Standard Generalized Markup Language)
- Parent standard for many markup languages.
- Defines how markup languages should be structured.
- Introduced **DTD (Document Type Definition)** for validating document structure.
- Important relationships:
  - **XML** is a simplified subset of SGML.
  - **HTML** is an SGML application.

### 3. HTML (HyperText Markup Language)
- Main language for structuring web pages.
- Browser-oriented presentation/structure language.
- Supports integration with scripting (e.g., JavaScript) for richer behavior.

### 4. XML (Extensible Markup Language)
- Designed to represent and exchange structured data.
- More generic and extensible than HTML.
- You can define custom tags, element relationships, and processing rules.
- Strict syntax expectations: invalid XML should be rejected by XML processors.
- Key distinction:
  - **HTML describes presentation/structure for web pages**.
  - **XML describes data/content and custom data formats**.

### 5. XHTML (Extensible HyperText Markup Language)
- HTML reformulated with XML rules.
- Goal: reduce ambiguity and enforce stricter syntax.
- Intended to improve interoperability with XML ecosystems.
- Practical issue: strict error handling was unpopular; many developers continued favoring forgiving HTML behavior.

## HTML Evolution Timeline (As Covered)
- **HTML 4.0 (1997)**: many new features; some old features deprecated.
- **HTML 4.01 (1999)**: cleanup release, but still loose syntax and inconsistent browser error recovery.
- **XHTML 1.0 (2000)**: HTML 4.01 in XML form; strict syntax model, but included compatibility loopholes.
- **XHTML 1.1 (2001)**: modular and stricter; moved toward stronger rejection of invalid syntax.
- **XHTML 2.0 (planned direction)**: reflected push for stricter standards but lost momentum.
- **HTML5 (2009 path consolidation)**:
  - WHATWG advanced practical web standards.
  - W3C shifted from XHTML 2.0 effort and adopted HTML5 development path.

## Major Theme from the Lecture
A long-standing tension exists between:
- strict, coherent syntax validation (XHTML/XML-style), and
- practical, user-friendly browser behavior that tolerates malformed markup.

Modern web adoption favored the more practical HTML5 direction.

## Exam-Focused Takeaways
- Define each markup language and explain their relationships.
- Differentiate **HTML vs XML** by purpose and extensibility.
- Explain why XHTML emerged and why strict adoption struggled.
- Know major milestones in HTML/XHTML version history and why HTML5 prevailed.

## Quick Comparison Table
| Language | Primary Purpose | Strictness | Notes |
|---|---|---|---|
| SGML | Meta-standard for markup languages | High/formal | Foundation for HTML and XML |
| HTML | Web page structure/presentation | Historically forgiving | Dominant for web authoring |
| XML | Structured data representation/exchange | Strict | User-defined tags and data models |
| XHTML | HTML + XML rules | Strict by design | Intended to remove HTML ambiguity |

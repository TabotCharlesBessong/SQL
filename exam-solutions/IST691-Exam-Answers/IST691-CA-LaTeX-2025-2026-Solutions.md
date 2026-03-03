# IST691 CA 2025/2026 — LaTeX (Research Methodology and Scientific Writing)

**University of Buea, Faculty of Science, Department of Computer Science**  
**Date:** 12/02/2025 | **Time:** 07:10–08:00 | **Total: 30 marks**

---

## Section A: Theoretical & Syntax Basics (10 marks)

### Question 1: Role of the preamble and three essential packages (4 marks)

**Role of the preamble**  
The **preamble** is the part of a LaTeX document **before** `\begin{document}`. It is used to:

- Set the **document class** (e.g. `\documentclass{article}`).
- Load **packages** that add features (math, figures, encoding, etc.).
- Define **global settings** (title, author, date, margins, etc.).

Nothing in the preamble is printed in the body; it only configures how the document is built.

**Three essential packages (examples)**

1. **`amsmath`** — Mathematical typesetting (equations, matrices, integrals, alignments).
2. **`graphicx`** — Include and scale images (`\includegraphics`).
3. **`inputenc`** (e.g. `\usepackage[utf8]{inputenc}`) — Input encoding so accents and special characters work correctly.

*(Other valid examples: `geometry`, `booktabs`, `hyperref`, `babel`.)*

---

### Question 2: Differentiate between a command and an environment (with examples) (3 marks)

| | **Command** | **Environment** |
|---|-------------|------------------|
| **Form** | Starts with `\`; often takes arguments in `{}` or `[]`. | Surrounded by `\begin{name}` and `\end{name}`. |
| **Scope** | Usually affects a **short piece** of text or a single object. | Affects **everything between** `\begin` and `\end`. |
| **Example** | `\textbf{bold}`, `\textit{italic}`, `\frac{1}{2}`. | `\begin{equation} ... \end{equation}`, `\begin{table} ... \end{table}`. |

**Examples**

- **Command:** `\textbf{Important}` produces **Important**; `\includegraphics{file}` inserts an image.
- **Environment:** `\begin{center} ... \end{center}` centres a block; `\begin{itemize} \item A \item B \end{itemize}` produces a bullet list.

---

### Question 3: Manage a bibliography — BibTeX vs embedded environment (3 marks)

**BibTeX (external .bib file)**  
- References are stored in a **separate `.bib` file** (e.g. `references.bib`) with entries such as `@article{key, author={...}, title={...}, ...}`.  
- In the document you cite with `\cite{key}` and put `\bibliography{references}` and `\bibliographystyle{plain}` where the list should appear.  
- You **compile**: LaTeX → BibTeX → LaTeX → LaTeX.  
- **Advantages:** Reuse the same references in many documents; consistent formatting; easy to share and edit.

**Embedded (thebibliography environment)**  
- References are written **inside the document** in a `\begin{thebibliography}{99} ... \end{thebibliography}` block.  
- Each entry is something like `\bibitem{key} Author. Title. Journal, year.`  
- You cite with `\cite{key}`.  
- **Advantages:** Single file; no extra compilation step; simple for few references.  
- **Disadvantages:** No automatic formatting; tedious for many references; harder to reuse.

**Summary:** Use **BibTeX** for larger or reusable bibliographies; use **embedded** for short, one-off lists.

#### Code examples

**1. BibTeX approach**

Create a file `references.bib` in the same folder as your `.tex` file:

```bibtex
@article{smith2020,
  author  = {Smith, J. and Doe, A.},
  title   = {Research Methods in Computer Science},
  journal = {Journal of Computing},
  year    = {2020},
  volume  = {10},
  number  = {2},
  pages   = {45--67}
}

@book{jones2019,
  author    = {Jones, M.},
  title     = {Scientific Writing},
  publisher = {Academic Press},
  year      = {2019},
  address   = {London}
}
```

In your main document (e.g. `main.tex`):

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{My Paper}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle

As shown in Smith et al.~\cite{smith2020}, and in Jones~\cite{jones2019}, we use citations.

\bibliographystyle{plain}
\bibliography{references}
\end{document}
```

**Compilation order:** `pdflatex main` → `bibtex main` → `pdflatex main` → `pdflatex main`.

---

**2. Embedded (thebibliography) approach**

Everything stays in one `.tex` file:

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{My Paper}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle

As shown in Smith et al.~\cite{smith2020}, and in Jones~\cite{jones2019}, we use citations.

\begin{thebibliography}{99}
\bibitem{smith2020}
Smith, J. and Doe, A. (2020). Research Methods in Computer Science. \textit{Journal of Computing}, 10(2), 45--67.

\bibitem{jones2019}
Jones, M. (2019). \textit{Scientific Writing}. Academic Press, London.
\end{thebibliography}
\end{document}
```

**Compilation:** Run `pdflatex main` twice (no BibTeX step). The `{99}` in `\begin{thebibliography}{99}` is used for label width (e.g. use `{9}` for up to 9 references, `{99}` for more).

---

## Section B: Practical Implementation Tasks (20 marks)

Below is **one complete LaTeX document** that fulfils all four tasks. Replace `Your Name` and `YourMatriculationNumber` with your details, and `screen.png` with your screen-capture filename (in the same folder as the .tex file).

### Full document (compile as a single file)

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{graphicx}
\graphicspath{{./}}
\usepackage{array}
\usepackage{booktabs}
\usepackage{caption}
\usepackage{ulem}
\usepackage{enumitem}

% ========== Task 1: Document setup (4 marks) ==========
\title{IST691: Research Methodology and Scientific Writing}
\author{Your Name \\ YourMatriculationNumber}
\date{12 February 2025}

\begin{document}
\maketitle

% ========== Task 2: Mathematical typesetting (6 marks) ==========
\section*{Task 2: Complex Formulas}

\subsection*{3x3 Matrix}

A 3x3 matrix example:
\begin{equation}
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
\end{equation}

\subsection*{Definite Integral with Limits}

A definite integral example:
\begin{equation}
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
\end{equation}

% ========== Task 3: Tables and graphics (6 marks) ==========
\section*{Task 3: Tables and Graphics}

\subsection*{3x3 Table with Centered Text}

Table~\ref{tab:example} shows a 3x3 table with centered text.

\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|}
\hline
\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
\hline
Cell 1,1 & Cell 1,2 & Cell 1,3 \\
\hline
Cell 2,1 & Cell 2,2 & Cell 2,3 \\
\hline
Cell 3,1 & Cell 3,2 & Cell 3,3 \\
\hline
\end{tabular}
\caption{Example of a 3x3 table with centered text}
\label{tab:example}
\end{table}

\subsection*{Image with Caption and Cross-Reference}

Figure~\ref{fig:screenshot} shows the screen capture.

\begin{figure}[h]
\centering
\includegraphics[width=0.85\textwidth,keepaspectratio]{screen.png}
\caption{Screen capture image}
\label{fig:screenshot}
\end{figure}

As shown in Figure~\ref{fig:screenshot}, the image is included with a caption and cross-reference.

% ========== Task 4: Nested list and formatting (4 marks) ==========
\section*{Task 4: Nested Lists and Text Formatting}

\subsection*{Nested Numbered List}

\begin{enumerate}
\item \textbf{First Main Item} — This uses \textbf{bold text}.
    \begin{enumerate}
    \item \textit{First sub-item} — This uses \textit{italic text}.
    \item \uline{Second sub-item} — This uses \uline{underlined text}.
    \end{enumerate}
\item \textit{Second Main Item} — This uses \textit{italic text}.
\item \uline{Third Main Item} — This uses \uline{underlined text}.
\end{enumerate}

\subsection*{Bulleted List with Formatting}

\begin{itemize}
\item \textbf{Bold item}
\item \textit{Italic item}
\item \uline{Underlined item}
\end{itemize}

\end{document}
```

---

### Checklist for submission

- [ ] Replace `Your Name` and `YourMatriculationNumber` in `\author{}`.  
- [ ] Add `\date{}` or keep the date as above.  
- [ ] Save your screen capture as `screen.png` in the same folder as the .tex file (or change the filename in `\includegraphics{...}`).  
- [ ] Compile the full document (pdfLaTeX or similar) and submit the **single PDF** to **n.bernard7@ubuea.cm**.

---

**End of solutions**

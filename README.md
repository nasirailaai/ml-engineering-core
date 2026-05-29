# ml-engineering-core

> Structured notes, experiments, and implementations from an ongoing study of machine learning engineering — written for clarity, built for reference.

---

## Overview

This repository documents my progression through ML engineering fundamentals. It is not a tutorial mirror or a collection of copied exercises. Every file here is written from scratch, with the goal of understanding *why* things work — not just *that* they work.

The structure follows a deliberate learning architecture: syntax → functions → control flow → lists → loops → strings → external libraries → then into ML-specific tooling (NumPy, pandas, scikit-learn). Each module builds on the last.

---

## Repository Structure

```
ml-engineering-core/
│
├── 01_python_syntax/
│   └── arithmetic_and_variables.py
│
├── 02_functions_and_scope/
│   └── functions_core.py
│
├── 03_control_flow/
│   └── booleans_and_conditionals.py
│
├── 04_lists_and_indexing/
│   └── lists_core.py
│
├── 05_loops_and_comprehensions/
│   └── loops_and_comprehensions.py
│
├── 06_strings_and_dicts/
│   └── strings_and_dicts.py
│
├── 07_external_libraries/
│   └── external_libraries.py
│
├── kaggle_notebooks/
│   ├── ex1-syntax-variables-complete.ipynb
│   ├── ex2-functions-getting-help.ipynb
│   ├── ex3-booleans-conditionals-complete.ipynb
│   ├── ex4-lists-complete.ipynb
│   ├── ex5-loops-list-comprehensions.ipynb
│   ├── ex6-strings-dictionaries-complete.ipynb
│   └── ex7-external-libraries-complete.ipynb
│
└── README.md
```

---

## Modules

### `01_python_syntax` — Complete
Core Python syntax through an ML engineering lens. Arithmetic operators, type behavior, and variable assignment — studied for how these primitives appear inside real training loops and data pipelines.

Key concepts: floor division for batch index computation, modulo in epoch logic, dynamic typing implications for production code.

### `02_functions_and_scope` — Complete
Functions as the primary unit of abstraction in ML pipelines. Docstrings, default arguments, error reading, and writing functions that are easy to test and compose.

Key concepts: default parameters as design decisions, docstrings as contracts, bug pattern recognition across typos, scope errors, and indentation issues.

### `03_control_flow` — Complete
Boolean logic and conditional branching — the decision layer of any ML system. Studied operator precedence, boolean algebra, and how if/elif/else structures appear in model evaluation and data filtering.

Key concepts: operator precedence bugs, int(bool) pattern for one-hot logic, threshold-based model deployment decisions.

### `04_lists_and_indexing` — Complete
Lists as foundational data structures. Indexing, slicing, mutation, and nested list access — mapped to their ML equivalents in batched datasets and feature vectors.

Key concepts: negative indexing for dataset access, slicing for train/test splits, in-place mutation patterns.

### `05_loops_and_comprehensions` — Complete
Iteration patterns that appear throughout ML code. For loops, while loops, list comprehensions, and Monte Carlo estimation.

Key concepts: return placement in loops, list comprehensions as NumPy-style filtering, Monte Carlo method for average value estimation.

### `06_strings_and_dicts` — Complete
String processing and dictionary operations — the backbone of NLP preprocessing and ML configuration management.

Key concepts: string validation for data cleaning, word search as tokenization, dictionary comprehensions as inverted indexes, dicts as hyperparameter configs.

### `07_external_libraries` — Complete
Working with external libraries, operator overloading, and the import system. The bridge from raw Python to NumPy, pandas, and scikit-learn.

Key concepts: variable shadowing bugs in nested loops, matplotlib graph object methods, blackjack hand evaluation as conditional logic, standard ML import conventions.

---

## Kaggle Notebooks

| Notebook | Module | Topics | Status |
|---|---|---|---|
| `ex1-syntax-variables-complete.ipynb` | 01 — Python Syntax | Arithmetic, types, variables | Complete |
| `ex2-functions-getting-help.ipynb` | 02 — Functions | Docstrings, default args, bug fixes | Complete |
| `ex3-booleans-conditionals-complete.ipynb` | 03 — Control Flow | Boolean logic, conditionals | Complete |
| `ex4-lists-complete.ipynb` | 04 — Lists | Indexing, slicing, mutation | Complete |
| `ex5-loops-list-comprehensions.ipynb` | 05 — Loops | Iteration, comprehensions, Monte Carlo | Complete |
| `ex6-strings-dictionaries-complete.ipynb` | 06 — Strings and Dicts | NLP preprocessing, configs | Complete |
| `ex7-external-libraries-complete.ipynb` | 07 — External Libraries | Imports, matplotlib, bug fixing | Complete |

All notebooks completed as part of the **Kaggle Python Course** — with added engineering context, ML-relevant examples, and documented reasoning beyond the original exercises.

---

## Engineering Principles Followed

**Hypothesis before execution.** Every code cell includes a comment predicting the output before running. This builds the ability to read code, not just run it.

**ML-relevant naming from day one.** Variables are named after real ML concepts (`learning_rate`, `batch_size`, `num_epochs`) rather than placeholder names (`x`, `a`, `val`).

**Structured before committed.** Files are organized before being pushed. No flat dumps of loose scripts.

**Context over completion.** Each module includes an ML context section connecting the syntax to real pipeline behavior — not just exercise solutions.

---

## Tech Stack

```
Language     Python 3.11+
Environment  Kaggle Notebooks
Libraries    NumPy · pandas · scikit-learn (next phase)
Version      Git with conventional commit messages
```

---

## Roadmap

- [x] Python syntax fundamentals
- [x] Functions and scope
- [x] Booleans and control flow
- [x] Lists and indexing
- [x] Loops and list comprehensions
- [x] Strings and dictionaries
- [x] External libraries and imports
- [ ] NumPy — arrays and vectorized operations
- [ ] pandas — tabular data engineering
- [ ] scikit-learn — classification and regression workflows
- [ ] First Kaggle competition submission with documented methodology

---

## Contact

**GitHub** — [github.com/ailanasirai](https://github.com/ailanasirai)
**LinkedIn** — [linkedin.com/in/aila-nasir](https://www.linkedin.com/in/aila-nasir/)
**Kaggle** — [kaggle.com/ailanasirai](https://www.kaggle.com/ailanasirai/code)

---

*This repository is actively maintained. Structure and content evolve as learning progresses.*

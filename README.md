# ml-engineering-core

> Structured notes, experiments, and implementations from an ongoing study of machine learning engineering — written for clarity, built for reference.

---

## Overview

This repository documents my progression through ML engineering fundamentals. It is not a tutorial mirror or a collection of copied exercises. Every file here is written from scratch, with the goal of understanding *why* things work — not just *that* they work.

The structure follows a deliberate learning architecture: syntax → functions → data structures → control flow → then into ML-specific tooling (NumPy, pandas, scikit-learn). Each module builds on the last.

---

## Repository Structure

```
ml-engineering-core/
│
├── 01_python_syntax/
│   └── arithmetic_and_variables.py  # Operators, types, ML-relevant naming
│
├── 02_functions_and_scope/
│   └── functions_core.py            # Docstrings, default args, bug fixes, ML context
│
├── 03_data_structures/              # upcoming
│
├── 04_control_flow/                 # upcoming
│
├── 05_numpy_foundations/            # upcoming
│
├── 06_pandas_core/                  # upcoming
│
├── kaggle_notebooks/
│   ├── ex1-syntax-variables-complete.ipynb
│   └── ex2-functions-getting-help.ipynb
│
└── assets/
    └── diagrams/
```

---

## Modules

### `01_python_syntax` — Complete
Core Python syntax through an ML engineering lens. Covers arithmetic operators, type behavior, and variable assignment — with focus on how these primitives appear inside real training loops and data pipelines.

Key concepts documented:
- Floor division (`//`) vs true division (`/`) — critical for batch index computation
- Modulo (`%`) in epoch logic and positional encoding patterns
- Dynamic typing implications for production ML code

### `02_functions_and_scope` — Complete
Functions as the primary unit of abstraction in ML pipelines. Covers docstrings, default arguments, error reading, and writing functions that are easy to test and compose.

Key concepts documented:
- `round()` with negative `ndigits` — rounding large numerical values
- Default parameters — optional arguments with sensible fallbacks
- Bug pattern recognition — typos, scope errors, indentation issues
- ML context — `normalize()` and `batch_count()` as pipeline functions

### `03_data_structures` — In Progress
Python's built-in structures mapped to their ML equivalents — lists as feature vectors, dicts as configuration objects, sets for vocabulary deduplication.

### `04_control_flow` — Upcoming
Loops, conditionals, and iteration patterns that appear repeatedly in training loops, data loaders, and preprocessing pipelines.

### `05_numpy_foundations` — Upcoming
The numerical backbone of ML. Vectorization, broadcasting, axis operations, and linear algebra from first principles.

### `06_pandas_core` — Upcoming
Tabular data manipulation: loading, cleaning, transforming, and preparing datasets for model input.

---

## Kaggle Notebooks

| Notebook | Module | Topics | Status |
|---|---|---|---|
| `ex1-syntax-variables-complete.ipynb` | 01 — Python Syntax | Arithmetic, types, variables, modulo logic | Complete |
| `ex2-functions-getting-help.ipynb` | 02 — Functions | Docstrings, default args, round(), bug fixes | Complete |

Notebooks here are exercise completions with added engineering context — hypothesis comments, ML-relevant examples, and documented reasoning beyond the original prompts.

---

## Engineering Principles Followed

**Hypothesis before execution.** Every code cell includes a comment predicting the output before running. This builds the ability to read code, not just run it.

**ML-relevant naming from day one.** Variables are named after real ML concepts (`learning_rate`, `batch_size`, `num_epochs`) rather than placeholder names (`x`, `a`, `val`). This builds vocabulary while building syntax.

**Structured before committed.** Files are organized before being pushed. No flat dumps of loose scripts.

---

## Tech Stack

```
Language     Python 3.11+
Environment  Kaggle Notebooks / local Jupyter
Libraries    NumPy · pandas · scikit-learn (progressive introduction)
Version      Git with conventional commit messages
```

---

## Roadmap

- [x] Python syntax fundamentals
- [x] Functions and scope
- [ ] Data structures
- [ ] Control flow
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

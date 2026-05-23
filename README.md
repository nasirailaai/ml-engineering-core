# ml-engineering-core

> Structured notes, experiments, and implementations from an ongoing study of machine learning engineering — written for clarity, built for reference.

---

## Overview

This repository documents my progression through ML engineering fundamentals. It is not a tutorial mirror or a collection of copied exercises. Every file here is written from scratch, with the goal of understanding *why* things work — not just *that* they work.

The structure follows a deliberate learning architecture: syntax → data structures → control flow → functions → then into ML-specific tooling (NumPy, pandas, scikit-learn). Each module builds on the last.

---

## Repository Structure

```
ml-engineering-core/
│
├── 01_python_syntax/
│   ├── notes.md                    # Conceptual notes on Python primitives
│   ├── arithmetic_operators.py     # Operator behavior, precedence, type implications
│   └── variable_types.py           # Dynamic typing, type inspection, ML-relevant naming
│
├── 02_functions_and_scope/
│   ├── notes.md
│   ├── function_design.py          # Parameters, return values, default args
│   └── scope_and_closures.py       # LEGB rule, closures, practical examples
│
├── 03_data_structures/
│   ├── notes.md
│   ├── lists_and_indexing.py       # Slicing, mutation, list comprehensions
│   ├── dicts_and_sets.py           # Key-value patterns common in ML configs
│   └── tuples_and_immutability.py
│
├── 04_control_flow/
│   ├── notes.md
│   ├── conditionals.py
│   └── loops_and_iteration.py      # for/while patterns, enumerate, zip
│
├── 05_numpy_foundations/
│   ├── notes.md
│   ├── array_operations.py         # Broadcasting, vectorization, axis logic
│   └── linear_algebra_basics.py    # Dot products, matrix ops, shapes
│
├── 06_pandas_core/
│   ├── notes.md
│   ├── dataframe_operations.py
│   └── data_cleaning_patterns.py
│
├── kaggle_notebooks/
│   ├── hello_python_extended.ipynb
│   └── README.md                   # Index of notebooks and what each covers
│
└── assets/
    └── diagrams/                   # Architecture sketches, concept maps
```

---

## Modules

### `01_python_syntax`
Core Python syntax studied through the lens of ML engineering. Covers arithmetic operators, type behavior, and variable assignment — with a focus on how these primitives appear inside real training loops and data pipelines.

Key observations documented:
- Floor division (`//`) vs true division (`/`) — critical for batch index computation
- Modulo (`%`) in epoch logic and positional encoding patterns
- Dynamic typing implications for production ML code

### `02_functions_and_scope` *(in progress)*
Functions as the primary unit of abstraction in ML pipelines. Covers parameter design, scope rules, and writing functions that are easy to test and compose.

### `03_data_structures` *(upcoming)*
Python's built-in structures mapped to their ML equivalents — lists as feature vectors, dicts as configuration objects, sets for vocabulary deduplication.

### `04_control_flow` *(upcoming)*
Loops, conditionals, and iteration patterns that appear repeatedly in training loops, data loaders, and preprocessing pipelines.

### `05_numpy_foundations` *(upcoming)*
The numerical backbone of ML. Vectorization, broadcasting, axis operations, and linear algebra implemented from first principles before reaching for higher-level libraries.

### `06_pandas_core` *(upcoming)*
Tabular data manipulation: loading, cleaning, transforming, and preparing datasets for model input.

---

## Kaggle Notebooks

| Notebook | Course | Topics | Status |
|---|---|---|---|
| `hello_python_extended.ipynb` | Kaggle — Python | Arithmetic, types, variables, f-strings | Complete |

Notebooks in this repository are extended versions of course material — not submissions. Each adds additional experiments, hypothesis testing, and engineering context beyond the original exercises.

---

## Engineering Principles Followed

**Hypothesis before execution.** Every code cell includes a comment predicting the output before running. This builds the ability to read code, not just run it.

**ML-relevant naming from day one.** Variables are named after real ML concepts (`learning_rate`, `batch_size`, `num_epochs`) rather than placeholder names (`x`, `a`, `val`). This builds vocabulary while building syntax.

**Notes over comments.** Each module has a `notes.md` that explains the *why* behind behavior — not a line-by-line description of what the code does.

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
- [ ] Functions and scope
- [ ] Data structures
- [ ] Control flow
- [ ] NumPy — arrays and vectorized operations
- [ ] pandas — tabular data engineering
- [ ] scikit-learn — classification and regression workflows
- [ ] First Kaggle competition submission with documented methodology

---

## Contact

**GitHub** — (https://github.com/nasirailaai/)  
**LinkedIn** — (https://www.linkedin.com/in/aila-nasir/)  
**Kaggle** — (kaggle.com/code/ailanasirai/ex1-syntax-variables-complete)

---

*This repository is actively maintained. Structure and content evolve as learning progresses.*

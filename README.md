# DSA0302: Natural Language Processing (NLP)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/Verification-100%25%20PASSED%20(26%2F26)-brightgreen?style=for-the-badge&logo=checkmarx" alt="Verification" />
  <img src="https://img.shields.io/badge/Course%20Code-DSA0302-purple?style=for-the-badge" alt="Course Code" />
  <img src="https://img.shields.io/badge/Theme-Tokyo%20Night-informational?style=for-the-badge" alt="Tokyo Night Theme" />
  <img src="https://img.shields.io/badge/Institution-SIMATS%20Engineering-red?style=for-the-badge" alt="Institution" />
</p>

---

## 📖 Overview

Welcome to the **DSA0302: Natural Language Processing** laboratory repository by **Ravilla Bhanu Prakash**. This repository contains the complete, verified computational linguistics curriculum covering 26 distinct experiments—from formal language theory and finite-state automata to context-free parsing, vector space information retrieval, discourse pragmatics, and modern neural sequence-to-sequence transformer models.

### Highlights
- **100% Automated Verification:** All 26 experiments include an automated test harness (`Lab/test_all_experiments.py`) achieving zero failures and complete test transcripts.
- **Tokyo Night Terminal Visuals:** Every experiment includes high-resolution, dark-mode terminal window screenshots generated programmatically via PIL (`Lab/generate_screenshots.py`).
- **Graceful Dual-Mode Engines:** Complex deep-learning and cloud API experiments (Exp 25 GPT-3 and Exp 26 MarianMT) feature high-fidelity offline academic emulators to guarantee test stability in restricted or offline lab environments.
- **Viva Voce Academic Preparation:** Comprehensive theoretical explanations and 15 complete viva voce questions and answers featuring LaTeX formulations.

---

## 📂 Repository Architecture

```text
DSA0302-NLP/
├── README.md                              # Master Repository Portfolio Landing Page (this file)
├── .gitignore                             # Python, Jupyter, & VirtualEnv exclusions
│
└── Lab/                                   # Complete Laboratory Coursework Suite
    ├── README.md                          # Master Laboratory Coursework Manual & Viva Prep Guide
    ├── test_all_experiments.py            # Automated Master Test Harness
    ├── generate_screenshots.py            # Custom Tokyo Night Dark-Mode Screenshot Engine
    │
    ├── Programs/                          # 26 Modular Experiment Folders
    │   ├── 01_Regex_Pattern_Matching/     # (main.py, README.md, sample_text.txt)
    │   ├── 02_Finite_State_Automaton/     # (main.py, README.md)
    │   ├── 03_Morphological_Analysis/     # (main.py, README.md)
    │   ├── 04_FSM_Morphological_Parsing/  # (main.py, README.md)
    │   ├── 05_Porter_Stemmer/             # (main.py, README.md)
    │   ├── 06_Ngram_Text_Generation/      # (main.py, README.md)
    │   ├── 07_POS_Tagging_NLTK/           # (main.py, README.md)
    │   ├── 08_Stochastic_POS_Tagger/      # (main.py, README.md)
    │   ├── 09_Rule_Based_POS_Tagger/      # (main.py, README.md)
    │   ├── 10_Transformation_Based_Tagger/# (main.py, README.md)
    │   ├── 11_Top_Down_CFG_Parser/        # (main.py, README.md)
    │   ├── 12_Earley_Parser/              # (main.py, README.md)
    │   ├── 13_Parse_Tree_Generation/      # (main.py, README.md)
    │   ├── 14_Agreement_Checking/         # (main.py, README.md)
    │   ├── 15_PCFG_Parsing/               # (main.py, README.md)
    │   ├── 16_SpaCy_NER/                  # (main.py, README.md)
    │   ├── 17_WordNet_Exploration/        # (main.py, README.md)
    │   ├── 18_FOPC_Parser/                # (main.py, README.md)
    │   ├── 19_Lesk_WSD/                   # (main.py, README.md)
    │   ├── 20_TFIDF_IR_System/            # (main.py, README.md, documents/)
    │   ├── 21_Syntax_Driven_Semantics/    # (main.py, README.md)
    │   ├── 22_Reference_Resolution/       # (main.py, README.md)
    │   ├── 23_Text_Coherence_Evaluation/  # (main.py, README.md)
    │   ├── 24_Dialog_Act_Recognition/     # (main.py, README.md)
    │   ├── 25_GPT3_Text_Generation/       # (main.py, README.md)
    │   └── 26_HuggingFace_Translation/    # (main.py, README.md)
    │
    └── outputs/                           # Verified Execution Logs & Visual Showroom
        ├── README.md                      # Visual Markdown Gallery of all screenshots
        ├── Exp01_Output.txt ... Exp26_Output.txt   # Complete Execution Transcripts
        └── Exp01_*.png ... Exp26_*.png             # Tokyo Night Terminal Window PNGs
```

---

## 📑 Curriculum & Experiment Index

| Exp # | Experiment Title | Module | Source Code | Terminal Output |
| :---: | :--- | :--- | :---: | :---: |
| **01** | Pattern Matching using Regular Expressions | M1: Automata & Morphology | [Code](./Lab/Programs/01_Regex_Pattern_Matching/) | [Screenshot](./Lab/outputs/Exp01_01_Regex_Pattern_Matching.png) |
| **02** | Finite State Automaton Ending in 'ab' | M1: Automata & Morphology | [Code](./Lab/Programs/02_Finite_State_Automaton/) | [Screenshot](./Lab/outputs/Exp02_02_Finite_State_Automaton.png) |
| **03** | Morphological Analysis using NLTK | M1: Automata & Morphology | [Code](./Lab/Programs/03_Morphological_Analysis/) | [Screenshot](./Lab/outputs/Exp03_03_Morphological_Analysis.png) |
| **04** | FSM for Morphological Parsing (Plurals) | M1: Automata & Morphology | [Code](./Lab/Programs/04_FSM_Morphological_Parsing/) | [Screenshot](./Lab/outputs/Exp04_04_FSM_Morphological_Parsing.png) |
| **05** | Word Stemming with Porter Stemmer | M1: Automata & Morphology | [Code](./Lab/Programs/05_Porter_Stemmer/) | [Screenshot](./Lab/outputs/Exp05_05_Porter_Stemmer.png) |
| **06** | N-gram Model for Text Generation | M2: Language Modeling | [Code](./Lab/Programs/06_Ngram_Text_Generation/) | [Screenshot](./Lab/outputs/Exp06_06_Ngram_Text_Generation.png) |
| **07** | POS Tagging using NLTK Library | M3: Part-of-Speech Tagging | [Code](./Lab/Programs/07_POS_Tagging_NLTK/) | [Screenshot](./Lab/outputs/Exp07_07_POS_Tagging_NLTK.png) |
| **08** | Stochastic (Probabilistic) POS Tagging | M3: Part-of-Speech Tagging | [Code](./Lab/Programs/08_Stochastic_POS_Tagger/) | [Screenshot](./Lab/outputs/Exp08_08_Stochastic_POS_Tagger.png) |
| **09** | Rule-Based POS Tagging using Regex | M3: Part-of-Speech Tagging | [Code](./Lab/Programs/09_Rule_Based_POS_Tagger/) | [Screenshot](./Lab/outputs/Exp09_09_Rule_Based_POS_Tagger.png) |
| **10** | Transformation-Based Tagging (Brill) | M3: Part-of-Speech Tagging | [Code](./Lab/Programs/10_Transformation_Based_Tagger/) | [Screenshot](./Lab/outputs/Exp10_10_Transformation_Based_Tagger.png) |
| **11** | Top-Down Parser for CFGs | M4: Syntactic Parsing | [Code](./Lab/Programs/11_Top_Down_CFG_Parser/) | [Screenshot](./Lab/outputs/Exp11_11_Top_Down_CFG_Parser.png) |
| **12** | Earley Chart Parser for CFGs | M4: Syntactic Parsing | [Code](./Lab/Programs/12_Earley_Parser/) | [Screenshot](./Lab/outputs/Exp12_12_Earley_Parser.png) |
| **13** | Parse Tree Generation for CFGs | M4: Syntactic Parsing | [Code](./Lab/Programs/13_Parse_Tree_Generation/) | [Screenshot](./Lab/outputs/Exp13_13_Parse_Tree_Generation.png) |
| **14** | Subject-Verb & Number Agreement Checking | M4: Syntactic Parsing | [Code](./Lab/Programs/14_Agreement_Checking/) | [Screenshot](./Lab/outputs/Exp14_14_Agreement_Checking.png) |
| **15** | Probabilistic CFG (PCFG) Parsing | M4: Syntactic Parsing | [Code](./Lab/Programs/15_PCFG_Parsing/) | [Screenshot](./Lab/outputs/Exp15_15_PCFG_Parsing.png) |
| **16** | Named Entity Recognition (NER) with SpaCy | M5: Lexical & Formal Semantics | [Code](./Lab/Programs/16_SpaCy_NER/) | [Screenshot](./Lab/outputs/Exp16_16_SpaCy_NER.png) |
| **17** | Lexical Database Exploration (WordNet) | M5: Lexical & Formal Semantics | [Code](./Lab/Programs/17_WordNet_Exploration/) | [Screenshot](./Lab/outputs/Exp17_17_WordNet_Exploration.png) |
| **18** | First-Order Predicate Calculus (FOPC) Parser | M5: Lexical & Formal Semantics | [Code](./Lab/Programs/18_FOPC_Parser/) | [Screenshot](./Lab/outputs/Exp18_18_FOPC_Parser.png) |
| **19** | Word Sense Disambiguation (Lesk Algorithm) | M5: Lexical & Formal Semantics | [Code](./Lab/Programs/19_Lesk_WSD/) | [Screenshot](./Lab/outputs/Exp19_19_Lesk_WSD.png) |
| **20** | Information Retrieval using TF-IDF | M6: Information Retrieval | [Code](./Lab/Programs/20_TFIDF_IR_System/) | [Screenshot](./Lab/outputs/Exp20_20_TFIDF_IR_System.png) |
| **21** | Syntax-Driven Semantic Analysis | M5: Lexical & Formal Semantics | [Code](./Lab/Programs/21_Syntax_Driven_Semantics/) | [Screenshot](./Lab/outputs/Exp21_21_Syntax_Driven_Semantics.png) |
| **22** | Reference & Anaphora Resolution | M7: Discourse & Pragmatics | [Code](./Lab/Programs/22_Reference_Resolution/) | [Screenshot](./Lab/outputs/Exp22_22_Reference_Resolution.png) |
| **23** | Text Coherence & Cohesion Evaluation | M7: Discourse & Pragmatics | [Code](./Lab/Programs/23_Text_Coherence_Evaluation/) | [Screenshot](./Lab/outputs/Exp23_23_Text_Coherence_Evaluation.png) |
| **24** | Dialogue Act Recognition in Conversations | M7: Discourse & Pragmatics | [Code](./Lab/Programs/24_Dialog_Act_Recognition/) | [Screenshot](./Lab/outputs/Exp24_24_Dialog_Act_Recognition.png) |
| **25** | Text Generation using OpenAI GPT-3 | M8: Deep Learning & Generative AI | [Code](./Lab/Programs/25_GPT3_Text_Generation/) | [Screenshot](./Lab/outputs/Exp25_25_GPT3_Text_Generation.png) |
| **26** | Machine Translation using Transformers | M8: Deep Learning & Generative AI | [Code](./Lab/Programs/26_HuggingFace_Translation/) | [Screenshot](./Lab/outputs/Exp26_26_HuggingFace_Translation.png) |

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Ravilla-Bhanu-prakash/DSA0302-NLP.git
cd DSA0302-NLP
```

### 2. Run an Individual Experiment
```bash
cd Lab/Programs/01_Regex_Pattern_Matching
python main.py
```

### 3. Run the Automated Master Test Suite
```bash
cd ../../
python test_all_experiments.py
```

### 4. Re-generate Terminal Screenshots
```bash
python generate_screenshots.py
```

---

## 👤 Author & Attribution

- **Developer:** [Ravilla Bhanu Prakash](https://github.com/Ravilla-Bhanu-prakash)
- **Institution:** SIMATS Engineering
- **Department:** Computer Science and Engineering / Artificial Intelligence & Data Science
- **Course Code:** `DSA0302` — Natural Language Processing
- **License:** MIT License

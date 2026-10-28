# DSA0302: Natural Language Processing — Laboratory Coursework Manual

**Institution:** SIMATS Engineering  
**Department:** Computer Science and Engineering / Artificial Intelligence & Data Science  
**Course Code:** `DSA0302`  
**Course Title:** Natural Language Processing (NLP)  
**Student:** Ravilla Bhanu Prakash  
**Target Environment:** Python 3.10+ (Windows / Linux / macOS)  
**Repository:** [Ravilla-Bhanu-prakash/DSA0302-NLP](https://github.com/Ravilla-Bhanu-prakash/DSA0302-NLP)  

---

## 1. Laboratory Coursework Overview

This repository houses the complete, verified laboratory coursework implementation for **DSA0302: Natural Language Processing**. The curriculum covers the computational foundations of natural language processing—ranging from deterministic finite-state automata and rule-based morphological transducers to context-free parsers, vector space retrieval engines, pragmatic discourse analyzers, and neural sequence-to-sequence transformer architectures.

### Directory Architecture
```text
Lab/
├── Programs/                          # 26 Modular, self-contained experiment folders
│   ├── 01_Regex_Pattern_Matching/
│   ├── 02_Finite_State_Automaton/
│   ├── 03_Morphological_Analysis/
│   ├── ...
│   └── 26_HuggingFace_Translation/
├── outputs/                           # Raw console transcripts and visual showroom
│   ├── Exp01_Output.txt ... Exp26_Output.txt
│   ├── Exp01_01_Regex_Pattern_Matching.png ... Exp26_26_HuggingFace_Translation.png
│   └── README.md                      # Visual gallery of all Tokyo Night screenshots
├── test_all_experiments.py            # Master automated verification test harness
├── generate_screenshots.py            # Custom Tokyo Night screenshot generator
└── README.md                          # Master documentation (this file)
```

---

## 2. Complete 26-Experiment Curriculum Index

| Exp # | Experiment Title | Module | Source Code | Output Screenshot | Raw Log |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **01** | Pattern Matching using Regular Expressions | M1: Automata & Morphology | [Code](./Programs/01_Regex_Pattern_Matching/) | [Screenshot](./outputs/Exp01_01_Regex_Pattern_Matching.png) | [Log](./outputs/Exp01_Output.txt) |
| **02** | Finite State Automaton Ending in 'ab' | M1: Automata & Morphology | [Code](./Programs/02_Finite_State_Automaton/) | [Screenshot](./outputs/Exp02_02_Finite_State_Automaton.png) | [Log](./outputs/Exp02_Output.txt) |
| **03** | Morphological Analysis using NLTK | M1: Automata & Morphology | [Code](./Programs/03_Morphological_Analysis/) | [Screenshot](./outputs/Exp03_03_Morphological_Analysis.png) | [Log](./outputs/Exp03_Output.txt) |
| **04** | FSM for Morphological Parsing (Plurals) | M1: Automata & Morphology | [Code](./Programs/04_FSM_Morphological_Parsing/) | [Screenshot](./outputs/Exp04_04_FSM_Morphological_Parsing.png) | [Log](./outputs/Exp04_Output.txt) |
| **05** | Word Stemming with Porter Stemmer | M1: Automata & Morphology | [Code](./Programs/05_Porter_Stemmer/) | [Screenshot](./outputs/Exp05_05_Porter_Stemmer.png) | [Log](./outputs/Exp05_Output.txt) |
| **06** | N-gram Model for Text Generation | M2: Language Modeling | [Code](./Programs/06_Ngram_Text_Generation/) | [Screenshot](./outputs/Exp06_06_Ngram_Text_Generation.png) | [Log](./outputs/Exp06_Output.txt) |
| **07** | POS Tagging using NLTK Library | M3: Part-of-Speech Tagging | [Code](./Programs/07_POS_Tagging_NLTK/) | [Screenshot](./outputs/Exp07_07_POS_Tagging_NLTK.png) | [Log](./outputs/Exp07_Output.txt) |
| **08** | Stochastic (Probabilistic) POS Tagging | M3: Part-of-Speech Tagging | [Code](./Programs/08_Stochastic_POS_Tagger/) | [Screenshot](./outputs/Exp08_08_Stochastic_POS_Tagger.png) | [Log](./outputs/Exp08_Output.txt) |
| **09** | Rule-Based POS Tagging using Regex | M3: Part-of-Speech Tagging | [Code](./Programs/09_Rule_Based_POS_Tagger/) | [Screenshot](./outputs/Exp09_09_Rule_Based_POS_Tagger.png) | [Log](./outputs/Exp09_Output.txt) |
| **10** | Transformation-Based Tagging (Brill) | M3: Part-of-Speech Tagging | [Code](./Programs/10_Transformation_Based_Tagger/) | [Screenshot](./outputs/Exp10_10_Transformation_Based_Tagger.png) | [Log](./outputs/Exp10_Output.txt) |
| **11** | Top-Down Parser for CFGs | M4: Syntactic Parsing | [Code](./Programs/11_Top_Down_CFG_Parser/) | [Screenshot](./outputs/Exp11_11_Top_Down_CFG_Parser.png) | [Log](./outputs/Exp11_Output.txt) |
| **12** | Earley Chart Parser for CFGs | M4: Syntactic Parsing | [Code](./Programs/12_Earley_Parser/) | [Screenshot](./outputs/Exp12_12_Earley_Parser.png) | [Log](./outputs/Exp12_Output.txt) |
| **13** | Parse Tree Generation for CFGs | M4: Syntactic Parsing | [Code](./Programs/13_Parse_Tree_Generation/) | [Screenshot](./outputs/Exp13_13_Parse_Tree_Generation.png) | [Log](./outputs/Exp13_Output.txt) |
| **14** | Subject-Verb & Number Agreement Checking | M4: Syntactic Parsing | [Code](./Programs/14_Agreement_Checking/) | [Screenshot](./outputs/Exp14_14_Agreement_Checking.png) | [Log](./outputs/Exp14_Output.txt) |
| **15** | Probabilistic CFG (PCFG) Parsing | M4: Syntactic Parsing | [Code](./Programs/15_PCFG_Parsing/) | [Screenshot](./outputs/Exp15_15_PCFG_Parsing.png) | [Log](./outputs/Exp15_Output.txt) |
| **16** | Named Entity Recognition (NER) with SpaCy | M5: Lexical & Formal Semantics | [Code](./Programs/16_SpaCy_NER/) | [Screenshot](./outputs/Exp16_16_SpaCy_NER.png) | [Log](./outputs/Exp16_Output.txt) |
| **17** | Lexical Database Exploration (WordNet) | M5: Lexical & Formal Semantics | [Code](./Programs/17_WordNet_Exploration/) | [Screenshot](./outputs/Exp17_17_WordNet_Exploration.png) | [Log](./outputs/Exp17_Output.txt) |
| **18** | First-Order Predicate Calculus (FOPC) Parser | M5: Lexical & Formal Semantics | [Code](./Programs/18_FOPC_Parser/) | [Screenshot](./outputs/Exp18_18_FOPC_Parser.png) | [Log](./outputs/Exp18_Output.txt) |
| **19** | Word Sense Disambiguation (Lesk Algorithm) | M5: Lexical & Formal Semantics | [Code](./Programs/19_Lesk_WSD/) | [Screenshot](./outputs/Exp19_19_Lesk_WSD.png) | [Log](./outputs/Exp19_Output.txt) |
| **20** | Information Retrieval using TF-IDF | M6: Information Retrieval | [Code](./Programs/20_TFIDF_IR_System/) | [Screenshot](./outputs/Exp20_20_TFIDF_IR_System.png) | [Log](./outputs/Exp20_Output.txt) |
| **21** | Syntax-Driven Semantic Analysis | M5: Lexical & Formal Semantics | [Code](./Programs/21_Syntax_Driven_Semantics/) | [Screenshot](./outputs/Exp21_21_Syntax_Driven_Semantics.png) | [Log](./outputs/Exp21_Output.txt) |
| **22** | Reference & Anaphora Resolution | M7: Discourse & Pragmatics | [Code](./Programs/22_Reference_Resolution/) | [Screenshot](./outputs/Exp22_22_Reference_Resolution.png) | [Log](./outputs/Exp22_Output.txt) |
| **23** | Text Coherence & Cohesion Evaluation | M7: Discourse & Pragmatics | [Code](./Programs/23_Text_Coherence_Evaluation/) | [Screenshot](./outputs/Exp23_23_Text_Coherence_Evaluation.png) | [Log](./outputs/Exp23_Output.txt) |
| **24** | Dialogue Act Recognition in Conversations | M7: Discourse & Pragmatics | [Code](./Programs/24_Dialog_Act_Recognition/) | [Screenshot](./outputs/Exp24_24_Dialog_Act_Recognition.png) | [Log](./outputs/Exp24_Output.txt) |
| **25** | Text Generation using OpenAI GPT-3 | M8: Deep Learning & Generative AI | [Code](./Programs/25_GPT3_Text_Generation/) | [Screenshot](./outputs/Exp25_25_GPT3_Text_Generation.png) | [Log](./outputs/Exp25_Output.txt) |
| **26** | Machine Translation using Transformers | M8: Deep Learning & Generative AI | [Code](./Programs/26_HuggingFace_Translation/) | [Screenshot](./outputs/Exp26_26_HuggingFace_Translation.png) | [Log](./outputs/Exp26_Output.txt) |

---

## 3. Automated Verification & Testing

Every experiment is systematically validated via the automated test harness [`Lab/test_all_experiments.py`](./test_all_experiments.py).

### How to Run the Verification Suite
```powershell
# Navigate into the Lab directory
cd "Lab"

# Run all 26 experiments and generate transcripts
python test_all_experiments.py

# Re-generate Tokyo Night screenshots
python generate_screenshots.py
```

### Verification Result
- **Total Experiments:** 26
- **Passed:** 26
- **Failed:** 0
- **Success Rate:** **100.0%**

---

## 4. Comprehensive Viva Voce Questions & Answers

### Q1: What is the fundamental difference between Stemming and Lemmatization?
**Answer:**  
- **Stemming** is a rule-based heuristic process that strips inflectional prefixes and suffixes from words (e.g., Porter Stemmer reducing *running* $\to$ *run*, but *crying* $\to$ *cri*). It does not take Part-of-Speech or context into account and often produces non-lexical stems.
- **Lemmatization** uses morphological analysis along with a lexical knowledge base (such as WordNet) to return the base dictionary headword, known as the *lemma* (e.g., *better* with adjective POS $\to$ *good*, *wolves* with noun POS $\to$ *wolf*).

### Q2: What is the formal mathematical specification of a Deterministic Finite Automaton (DFA)?
**Answer:**  
A DFA is formally defined as a 5-tuple $M = (Q, \Sigma, \delta, q_0, F)$ where:
1. $Q$ is a finite set of internal states.
2. $\Sigma$ is a finite input alphabet.
3. $\delta: Q \times \Sigma \to Q$ is the deterministic state transition function.
4. $q_0 \in Q$ is the designated start state.
5. $F \subseteq Q$ is the set of final/accepting states.

### Q3: Explain the Markov Assumption in N-gram Language Modeling.
**Answer:**  
The Markov assumption simplifies conditional joint probabilities by postulating that the occurrence of the current token $w_n$ depends exclusively on the preceding $N-1$ tokens rather than the arbitrary historical prefix:
$$P(w_n \mid w_1, w_2, \dots, w_{n-1}) \approx P(w_n \mid w_{n-1}, \dots, w_{n-N+1})$$
For a Bigram language model ($N=2$), this simplifies to:
$$P(w_i \mid w_{1 \dots i-1}) \approx P(w_i \mid w_{i-1})$$

### Q4: How does a Hidden Markov Model (HMM) execute Part-of-Speech Tagging?
**Answer:**  
An HMM models surface words as observed emissions and grammatical tags as hidden states. The most probable tag sequence $\hat{T}$ is decoded via:
$$\hat{T} = \arg\max_T \prod_{i=1}^n P(w_i \mid t_i) P(t_i \mid t_{i-1})$$
Where:
- $P(w_i \mid t_i)$ is the **Emission Probability** (likelihood of observing word $w_i$ given state $t_i$).
- $P(t_i \mid t_{i-1})$ is the **Transition Probability** (likelihood of moving from tag $t_{i-1}$ to $t_i$).
- Decoding across all possible paths is solved in polynomial time $O(T \cdot |S|^2)$ via the **Viterbi Algorithm**.

### Q5: How does Brill's Transformation-Based Tagging (TBL) algorithm operate?
**Answer:**  
Brill's tagger operates in two discrete phases:
1. **Initial State Annotator:** Each word is assigned its most frequent unigram tag in isolation from the lexicon.
2. **Error-Driven Transformation:** Iterative rewrite templates (e.g., *Change tag from NN to VB if preceding token is TO*) are scored against a reference gold standard. The transformation yielding the maximal net error reduction is greedily appended to the rule sequence until convergence.

### Q6: What are the three core operations of the Earley Chart Parser?
**Answer:**  
1. **Predictor:** When the scanning dot precedes a non-terminal $B$ ($A \to \alpha \cdot B \beta$), introduce top-down expectations by generating states for all production rules expanding $B$.
2. **Scanner:** When the scanning dot precedes a terminal token matching the current input symbol ($A \to \alpha \cdot a \beta$), advance the dot past the terminal into the next state chart.
3. **Completer:** When a production rule is fully recognized ($B \to \gamma \cdot$), look back at the chart where this rule originated and advance the dot for all waiting rules ($A \to \alpha \cdot B \beta \to A \to \alpha B \cdot \beta$).

### Q7: What causes Prepositional Phrase (PP) attachment ambiguity in CFGs?
**Answer:**  
In sentences such as *"The astronomer saw the star with a telescope"*, the prepositional phrase *with a telescope* can syntactically attach either to the Noun Phrase ($NP \to NP\ PP$: the star had a telescope) or to the Verb Phrase ($VP \to VP\ PP$: the act of seeing used a telescope). CFGs lack semantic grounding and consequently generate multiple structurally valid parse trees.

### Q8: What is a Probabilistic Context-Free Grammar (PCFG)?
**Answer:**  
A PCFG augments standard CFGs by assigning probabilities to production rules such that for every non-terminal $A$, the sum of probabilities of all expansions is unitary: $\sum_\beta P(A \to \beta) = 1.0$. The total probability of a parse tree $T$ is the joint product of all production probabilities in its derivation. The probabilistic Cocke-Younger-Kasami (CYK) or Viterbi algorithm identifies the single derivation with maximal probability.

### Q9: Define WordNet Synsets and their primary semantic relations.
**Answer:**  
In WordNet, the core atomic concept is the **Synset** (synonym set)—a group of unordered lemmas that share a distinct cognitive sense, accompanied by a definitional gloss and usage examples. Key semantic relations include:
- **Hypernymy (is-a):** Generalization ($canine \to dog$).
- **Hyponymy (sub-type):** Specialization ($poodle \to dog$).
- **Meronymy (part-of):** Component relationship ($wheel \to car$).
- **Antonymy:** Direct semantic opposition ($hot \leftrightarrow cold$).

### Q10: How does the Simplified Lesk Algorithm perform Word Sense Disambiguation?
**Answer:**  
The Lesk algorithm operates on the **context overlap hypothesis**: the correct dictionary sense of an ambiguous word in context will share the highest lexical overlap (vocabulary intersection) between its dictionary definition/examples and the words in the surrounding sentence window.

### Q11: How are Term Frequency (TF) and Inverse Document Frequency (IDF) calculated?
**Answer:**  
$$\text{TF}(t, d) = \frac{f_{t, d}}{\sum_{t' \in d} f_{t', d}}, \quad \text{IDF}(t, D) = \log\left(\frac{1 + |D|}{1 + |\{d \in D : t \in d\}|}\right) + 1$$
$$\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t, D)$$
The product measures term importance: words appearing frequently in a specific document but rarely across the general corpus receive high weights, serving as discriminative retrieval keys.

### Q12: Differentiate between Anaphora and Cataphora in Reference Resolution.
**Answer:**  
- **Anaphora:** A referring expression points back to an entity introduced earlier in discourse (*"Alan Turing conceived the machine. **He** changed computing forever"*).
- **Cataphora:** A referring expression points forward to an entity introduced later (*"Although **he** was tired, Alan continued his mathematical proof"*).

### Q13: Contrast Discourse Cohesion with Discourse Coherence.
**Answer:**  
- **Cohesion** pertains to surface-level grammatical and lexical connections linking sentences (e.g., cohesive ties like *moreover*, *consequently*, pronoun bindings).
- **Coherence** pertains to the underlying cognitive and semantic structure that ensures the discourse forms a meaningful, logically unified whole.

### Q14: What is a Dialogue Act (Speech Act)?
**Answer:**  
A Dialogue Act represents the pragmatic communicative function of an utterance in conversation (e.g., *Greeting*, *Statement-Opinion*, *Yes-No-Question*, *Directive/Command*, *Apology*). It models intentionality and speaker goals rather than surface syntax.

### Q15: Explain the Sequence-to-Sequence MarianMT Transformer architecture.
**Answer:**  
MarianMT utilizes an Encoder-Decoder multi-head self-attention architecture:
1. **Encoder:** Transforms input source tokens into continuous contextual vector embeddings via bidirectional self-attention and position-wise feedforward networks.
2. **Decoder:** Generates target translation tokens auto-regressively using causal masked self-attention over previous target tokens and cross-attention over the encoder representations, decoded using Beam Search.

---

## 5. Course Record Verification Sign-off

- **Student Name:** Ravilla Bhanu Prakash
- **Course Code:** `DSA0302`
- **Course Title:** Natural Language Processing
- **Institution:** SIMATS Engineering
- **Status:** Complete 26-Experiment Laboratory Practicum verified with 100% automated test compliance.

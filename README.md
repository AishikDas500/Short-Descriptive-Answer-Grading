# Automated Short Answer Grading System using Semantic Similarity

## Overview

This project is a lightweight Automated Short Answer Grading (ASAG) system designed for CBSE-style descriptive answers. It evaluates student responses by comparing them with a teacher-provided model answer using semantic similarity and concept coverage.

The goal is to support partial marking similar to real teacher evaluation instead of simple right-or-wrong checking.

Unlike traditional keyword-only systems, this project combines Sentence-BERT (SBERT) embeddings with weighted concept matching to better handle paraphrased answers where meaning matters more than exact wording.

The system is also evaluated against human teacher scores using Mean Absolute Error (MAE) and Pearson Correlation, and compared with a TF-IDF baseline model.

---

## Problem Statement

Manual grading of short descriptive answers is time-consuming, inconsistent, and difficult to scale, especially in school environments with large class sizes.

Most existing automated grading systems are designed for Western university-level datasets and objective answer formats. There is limited evaluation specifically for CBSE-style short answers in Indian classrooms.

This project aims to build a lightweight and explainable grading system better suited for short factual and descriptive answers commonly found in CBSE examinations.

---

## Objectives

* Build an automated grading system for short descriptive answers
* Use semantic similarity instead of exact word matching
* Support partial marking similar to human teachers
* Detect matched and missing concepts
* Compare performance with a TF-IDF baseline
* Evaluate system quality using teacher-assigned marks

---

## Tech Stack

### Backend

* FastAPI

### NLP / Machine Learning

* Sentence Transformers (all-MiniLM-L6-v2)
* scikit-learn
* pandas
* SciPy
* NLTK

### Frontend

* HTML
* CSS
* JavaScript

---

## Project Structure

```text
app/
│
├── preprocessor.py
├── similarity.py
├── grader.py
│
main.py
baseline.py
evaluate.py
evaluation_data.csv
index.html
requirements.txt
README.md
.gitignore
```

---

## Methodology

The system consists of three main components:

### 1. Text Preprocessing

Both student and model answers are cleaned before comparison using:

* lowercase conversion
* punctuation removal
* stopword removal

This reduces noise and improves grading quality.

---

### 2. Semantic Similarity

The preprocessed answers are converted into dense vector representations using SBERT (Sentence-BERT).

Cosine similarity is then used to measure how semantically similar the student answer is to the model answer.

This helps detect correct answers even when students use different wording.

### Example

**Model Answer:**
Plants use sunlight to make food.

**Student Answer:**
Plants prepare food using solar energy.

Even with different wording, semantic similarity remains high.

---

### 3. Concept Coverage

Important concepts are extracted from the model answer using keyword filtering.

The system checks:

* matched concepts
* missing concepts

Longer and more meaningful concepts are assigned higher weights to improve partial marking quality.

---

### 4. Final Grading

Final score is calculated using:

```text
Final Score = 0.5 × Semantic Similarity + 0.5 × Concept Coverage
```

This score is then scaled using `question_marks` and mapped into grade labels such as:

* Excellent
* Good
* Average
* Needs Improvement

---

## Baseline Comparison

To validate improvement, a TF-IDF baseline model is implemented.

### Baseline Method

* TF-IDF Vectorization
* Cosine Similarity
* Score-to-Marks conversion

This acts as the traditional keyword-based grading benchmark.

The goal is to prove that semantic similarity performs better than lexical matching alone.

---

## Evaluation Metrics

### Mean Absolute Error (MAE)

MAE measures the average difference between:

* teacher-assigned marks
* system-predicted marks

Lower MAE indicates better grading accuracy.

---

### Pearson Correlation

Pearson Correlation measures how strongly the system grading aligns with teacher grading patterns.

Higher correlation indicates stronger agreement with human evaluation.

Range:

* +1 = perfect agreement
* 0 = no relationship
* -1 = opposite grading logic

---

## Experimental Results

| Method                            | MAE ↓ | Pearson ↑ |
| --------------------------------- | ----: | --------: |
| TF-IDF Baseline                   |  0.87 |         — |
| Proposed SBERT + Concept Coverage |  0.66 |      0.53 |

### Key Result

The proposed system reduced Mean Absolute Error by approximately 24% compared to the TF-IDF baseline while achieving strong alignment with teacher-assigned scores.

This demonstrates that combining semantic similarity with concept-level analysis provides more reliable grading than traditional lexical matching.

---

## Research Contribution

This project focuses specifically on CBSE-style short descriptive answers, an area that remains underexplored compared to Western educational datasets.

The main contributions include:

1. A lightweight hybrid grading approach using semantic similarity and concept scoring
2. A CBSE-specific evaluation dataset
3. A baseline comparison against TF-IDF grading
4. An explainable grading system with matched and missing concept feedback

---

## Future Improvements

* Expand dataset using larger CBSE answer sheets
* Add subject-specific grading rubrics
* Improve concept detection using semantic keyword matching
* Add teacher dashboard for bulk evaluation
* Extend support for multilingual answers
* Deploy as a production-ready web platform

---

## Author

Aishik
Class 12 Student
Research Project on Automated Short Answer Grading System

---

## License

This project is developed for academic, educational, and research purposes only.

It is intended as a research prototype for studying automated short answer grading using semantic similarity and concept coverage.

This repository is not licensed for commercial use without prior permission from the author.

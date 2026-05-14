# Automated Short Answer Grading System using Semantic Similarity

## Overview

This project is an Automated Short Answer Grading System designed to evaluate descriptive student answers using semantic similarity and concept coverage.

The system compares a student's answer with the teacher’s model answer, calculates semantic similarity using SBERT (Sentence-BERT), checks important concept coverage using keyword matching, and assigns partial marks similar to real teacher grading.

Unlike simple keyword-based systems, this project focuses on CBSE-style subjective answers where meaning matters more than exact wording.

The project also includes a TF-IDF baseline comparison and evaluation metrics such as Mean Absolute Error (MAE) and Pearson Correlation to validate grading performance against teacher-assigned scores.

---

## Problem Statement 

Traditional short answer grading is time-consuming, subjective, and difficult to scale for large classrooms.

Most existing automated grading systems are designed for Western educational datasets and objective answer formats. There is limited evaluation for CBSE-style descriptive answers in Indian classrooms.

This project aims to build a grading system better suited for short descriptive answers commonly found in CBSE examinations.

---

## Objectives

- Build an automated grading system for short descriptive answers
- Use semantic similarity instead of exact word matching
- Detect missing and matched concepts
- Support partial marking similar to human teachers
- Compare performance with a TF-IDF baseline
- Evaluate grading quality using teacher-assigned marks

---

## How it works

### Text Processing
Both student and model answers are cleaned using:

- lowercase conversion
- punctuation removal
- stopword removal

This improves grading quality by removing unnecessary noise.

### Semantic Similarity
SBERT converts both answers into sentence embeddings.

Cosine similarity is then used to measure how semantically similar both answers are.

This helps detect correct answers even when wording is different.

### Concept Coverage 
Important keywords are extracted from the model answer.

The system checks:

matched concepts
missing concepts

Longer and more meaningful concepts are given higher weights.

This improves partial marking quality.

### Final Grading 
Final score is calculated using:

Final Score = 0.5 × Semantic Similarity + 0.5 × Concept Coverage

This score is converted into marks based on question_marks and mapped to grade labels

---

## Experimental Results

| Method                            | MAE   | Pearson   |
| --------------------------------- | ----: | --------: |
| TF-IDF Baseline                   |  0.83 |         — |
| Proposed SBERT + Concept Coverage |  0.65 |      0.44 |

### Key Improvements 

The proposed system reduced Mean Absolute Error by approximately 22% compared to the TF-IDF baseline, while achieving strong alignment with teacher-assigned scores.

## Tech Stack

### Backend
- FastAPI

### Natural Language Processing (NLP)
- Sentence Transformers (all-MiniLM-L6-v2)
- scikit-learn
- pandas
- SciPy
- NLTK

### Frontend 
- HTML
- CSS
- JavaScript

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

## Future Improvement 
- Expand dataset using larger CBSE exam answer sheets with different language imputs
- Add subject-specific grading rubrics
- Improve concept detection using semantic keyword matching
- Add teacher dashboard for bulk answer evaluation
- Deploy as a production-ready web platform

## Research Contriution 
This project focuses on evaluating automated grading specifically for CBSE-style short descriptive answers, which remains underexplored compared to Western educational datasets.

The work aims to bridge that gap using lightweight semantic models and explainable grading logic.

## Author 
Aishik Das
Class 12th Student 
Research Project on Educational Technology

## License

This project is developed for academic, educational, and research purposes only.

It is intended as a research prototype for studying automated short answer grading using semantic similarity and concept coverage.

This repository is not licensed for commercial use without prior permission from the author.

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def tfidf_similarity(student_answer, model_answer):

    texts = [student_answer, model_answer]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    score = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    return float(score[0][0])


def grade(score, question_marks):
    final_score = round(score * question_marks, 1)

    if final_score >= question_marks * 0.85:
        label = "Excellent"
    elif final_score >= question_marks * 0.65:
        label = "Good"
    elif final_score >= question_marks * 0.45:
        label = "Average"
    else:
        label = "Needs Improvement"

    return {
        "final_score": final_score,
        "grade": label
    }


def evaluate_baseline():
    file_path = input("Enter file path: ").strip().strip('"')
    df = pd.read_csv(file_path)

    total_error = 0
    total_samples = len(df)

    teacher_scores = []
    system_scores = []

    for index, row in df.iterrows():
        student_answer = row["student_answer"]
        model_answer = row["model_answer"]

        similarity_score = tfidf_similarity(
            student_answer,
            model_answer
        )

        final_result = grade(
            similarity_score,
            row["question_marks"]
        )

        predicted_score = final_result["final_score"]
        teacher_score = float(row["teacher_score"])

        teacher_scores.append(teacher_score)
        system_scores.append(predicted_score)

        error = abs(predicted_score - teacher_score)
        total_error += error

        print("===================================")
        print(f"Teacher Score   : {teacher_score}")
        print(f"TF-IDF Score    : {predicted_score}")
        print(f"Difference      : {round(error, 2)}")
        print(f"Grade Label     : {final_result['grade']}")
        print("===================================\n")

    mae = total_error / total_samples

    print("======= BASELINE FINAL RESULT =======")
    print(f"Total Samples Tested : {total_samples}")
    print(f"Baseline MAE         : {round(mae, 2)}")
    print("=====================================")


if __name__ == "__main__":
    evaluate_baseline()
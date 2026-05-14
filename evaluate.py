import pandas as pd
from scipy.stats import pearsonr
from app.preprocessor import preprocess
from app.similarity import similarity
from app.grader import get_keywords, grade


def evaluate():
    file_path = input("Enter file path: ").strip().strip('"')
    df = pd.read_csv(file_path, encoding='latin-1')

    total_error = 0
    total_samples = len(df)

    teacher_scores = []
    system_scores = []

    for index, row in df.iterrows():
        clean_student = preprocess(row["student_answer"])
        clean_model = preprocess(row["model_answer"])

        similarity_score = similarity(clean_student, clean_model)

        keyword_result = get_keywords(clean_student, clean_model)

        final_result = grade(
            similarity_score,
            keyword_result["concept_ratio"],
            row["question_marks"]
        )

        predicted_score = final_result["final_score"]
        teacher_score = float(row["teacher_score"])

        teacher_scores.append(teacher_score)
        system_scores.append(predicted_score)

        error = abs(predicted_score - teacher_score)
        total_error += error

        print("===================================")
        print("Question Checked")
        print(f"Teacher Score   : {teacher_score}")
        print(f"Predicted Score : {predicted_score}")
        print(f"Difference      : {round(error, 2)}")
        print(f"Grade Label     : {final_result['grade']}")
        print("===================================\n")

    mae = total_error / total_samples
    correlation, p_value = pearsonr(teacher_scores, system_scores)

    print("======= FINAL RESULT =======")
    print(f"Total Samples Tested : {total_samples}")
    print(f"Final MAE            : {round(mae, 2)}")
    print(f"Pearson Correlation  : {round(correlation, 2)}")
    print("=====================================")


if __name__ == "__main__":
    evaluate()

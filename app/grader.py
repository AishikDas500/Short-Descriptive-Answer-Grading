def get_keywords(student_answer, model_answer):
    model_words = set(model_answer.split())
    student_words = set(student_answer.split())

    matched = []
    missing = []

    weightage = {}

    for word in model_words:
        if len(word) < 4:
            continue

        if len(word) >= 8:
            weightage[word] = 2
        else:
            weightage[word] = 1

    concept_score = 0
    total_score = sum(weightage.values())

    for keyword, weight in weightage.items():
        if keyword in student_words:
            matched.append(keyword)
            concept_score += weight
        else:
            missing.append(keyword)

    if total_score > 0:
        concept_ratio = concept_score/total_score
    else:
        concept_ratio = 0

    return {
        "matched": matched,
        "missing": missing,
        "concept_ratio": round(concept_ratio, 2)
    }


def grade(similarity_score, concept_ratio, question_marks):
    final_score = (
        0.5 * similarity_score
    ) + (
        0.5 * concept_ratio
    )

    marks = round(final_score * question_marks, 1)

    if marks >= question_marks * 0.85:
        label = "Full Marks"
    elif marks >= question_marks * 0.65:
        label = "Partial Marks"
    elif marks >= question_marks * 0.45:
        label = "Needs Improvement"
    else:
        label = "Answer is Insufficient"

    return {
        "final_score": marks,
        "grade": label
    }
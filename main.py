from app.similarity import similarity
from app.preprocessor import preprocess
from app.grader import grade , get_keywords
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GradeRequest(BaseModel):
    student_answer: str
    model_answer: str
    question_marks: int

@app.get("/")
def read_index():
    return FileResponse("index.html")

@app.post("/grade")
def grade_answer(request: GradeRequest):
    clean_student = preprocess(request.student_answer)
    clean_model = preprocess(request.model_answer)

    similarity_score = similarity(clean_student, clean_model)

    keyword_result = get_keywords(clean_student, clean_model)

    final_result = grade(
    similarity_score,
    keyword_result["concept_ratio"],
    request.question_marks
)

    return {
        "score": final_result["final_score"],
        "grade": final_result["grade"],
        "keywords": {
            "matched": keyword_result["matched"],
            "missing": keyword_result["missing"]
        }
    }
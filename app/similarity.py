from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def similarity(cleaned , model_answer):
    embedding1 = model.encode(cleaned)
    embedding2 = model.encode(model_answer)
    score = cosine_similarity([embedding1] , [embedding2])
    return float(score[0][0])
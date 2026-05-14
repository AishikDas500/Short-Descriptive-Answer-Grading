import nltk
import string

nltk.download("stopwords")
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))


def preprocess(text):
    text = text.lower()

    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()


    cleaned = [word for word in words if word not in stop_words]

    return " ".join(cleaned)
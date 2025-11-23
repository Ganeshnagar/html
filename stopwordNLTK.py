import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

# Read passage from file
text = open("input.txt", "r", encoding="utf-8").read()

words = word_tokenize(text)
filtered = [w for w in words if w.lower() not in stopwords.words("english")]

print("Original:", text)
print("Without Stopwords:", " ".join(filtered))

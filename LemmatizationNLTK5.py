import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("wordnet")

text = "The children are playing with the toys and the cats are running fast"
lemmatizer = WordNetLemmatizer()

words = word_tokenize(text)
lemmatized = [lemmatizer.lemmatize(w) for w in words]

print("Original:", text)
print("Lemmatized:", " ".join(lemmatized))

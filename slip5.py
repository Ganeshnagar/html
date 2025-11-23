import nltk
from nltk.stem import WordNetLemmatizer

text = "studies studying studied"

# Tokenize the text 
tokenized_text = nltk.word_tokenize(text)
print("Tokenized text:", tokenized_text)

lemmatizer = WordNetLemmatizer() 

print("Lemmatized tokens:")
for token in tokenized_text:
    print(lemmatizer.lemmatize(token))

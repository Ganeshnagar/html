sentence = input("Enter any sentence : ")

words = sentence.split()
words.sort()

print("The sorted words are:")
for word in words:
  print(word)

sorted_sentence = ' '.join(words)
print(f"\nThe sentence after sorting the words is: \n{sorted_sentence}")

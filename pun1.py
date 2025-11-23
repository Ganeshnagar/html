import string

input_str = input("Enter the input String which contain punctuations : ")

# Remove punctuations
nopunc = ""
for char in input_str:
   if char not in string.punctuation:
       nopunc = nopunc + char

print(nopunc)

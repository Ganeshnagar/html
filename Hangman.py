import random

words = "python", "computer", "science", "programming", "hangman", "artificial",
"intelligence"
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print(" ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i, ch in enumerate(word):
            if ch == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("You win! The word was:", word)
else:
    print("You lose! The word was:", word)

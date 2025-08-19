import random

def hangman():
    words = ["apple", "grape", "peach", "mango", "lemon"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while tries > 0 and "".join(guessed) != word:
        print("\nWord:", " ".join(guessed))
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct!")
        else:
            tries -= 1
            print("Incorrect!")

    if "".join(guessed) == word:
        print(f"\nCongratulations, you guessed the word: {word}")
    else:
        print(f"\nSorry, you ran out of tries. The word was: {word}")

if __name__ == "__main__":
    hangman()

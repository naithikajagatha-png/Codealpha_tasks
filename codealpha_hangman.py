import random
words = ["apple", "mango", "grape", "tiger", "house"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nword:", display)

    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining Chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The word was:", word)

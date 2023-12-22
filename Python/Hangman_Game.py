import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(secret_word, guessed_letters)
        print("Current word:", current_display)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess!")

        if set(guessed_letters) == set(secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", secret_word)

hangman()
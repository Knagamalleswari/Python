
import random
print("Welcome To Hangman Game")
name = input("What is your name? ")
 
# User Will be Enter their Name
 
print("All The Best! ", name)
 
words = ['hi', 'hello', 'welcome', 'malli',
         'anu', 'go', 'malleswari', 'say',
         'jyothi', 'reddy', 'skrypton', 'python']
 
# It will Choose one Random Word
word = random.choice(words)

print("Guess the characters")

#All Inputs Stored in Guesses 
guesses = ''

#How Many Turnes We want
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            
            failed += 1
 
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
  
    guess = input("guess a character:")
 
    # every input character will be stored in guesses
    guesses += guess
    
    if guess not in word:
 #If Guess char is wrong Every time turns will be decrease
        turns -= 1
        print("Wrong")
       
 
        if turns == 0:
            print("You Loose")

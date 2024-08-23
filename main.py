#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear
from art import logo
def guess_number():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1,100)
  choose_level = input("choose a difficulty. Type 'easy' or 'hard': ")
  if choose_level == "easy":
    attempts = 10
   
    while attempts >0:
      print(f"You have {attempts} attempts remaining to guess the number.")
      guess = int(input("Makee a guess: "))
      if guess == number:
        print(f"you got it! The answer was {number} ")
        attempts =0
      elif guess > number:
        print("Too high.\nGuess agains. ")
      elif guess < number:
        print("Too low.\nGuess agains. ")
      attempts -=1
  else:
      if choose_level == "hard":
        attempts = 5
        
        while attempts >0:
          print(f"You have {attempts} attempts remaining to guess the number.")
          guess = int(input("Makee a guess: "))
          if guess == number:
            print(f"you got it! The answer was {number} ")
            attempts =0
          elif guess > number:
            print("Too high.\nGuess agains. ")
            
          elif guess < number:
            print("Too low.\nGuess agains. ")
           
          attempts -=1
  while input("Do you want to play again? Type 'y' or 'n': ") == "y":
      clear()
      guess_number()
guess_number()
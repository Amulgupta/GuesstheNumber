from art import logo
import random

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  actual_number = random.randint(1,100)
  # print(actual_number)

  
  mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if mode == "hard":
    attempts = 5
    
  elif mode == "easy":
    attempts = 10

  else:
    print("Only two modes available. Try again!!!")
    return 0

  # print(f"You have {attempts} attempts remaining to guess the number.")
  
  count = 0
  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    count += 1
    if guess == actual_number:
      print(f"You got it! The answer was {actual_number}.")
      print(f"You guessed it in {count} attempts.")
      return

    elif guess > actual_number:
      print("Too high.")
      attempts -= 1
      # print(f"You have {attempts} attempts remaining to guess the number.")

    elif guess < actual_number:
      print("Too low.")
      attempts -= 1
      # print(f"You have {attempts} attempts remaining to guess the number.")

    if attempts == 0:
      print("You've run out of guesses, you lose.")
    else:
      print("Guess again.")
      
  reply =  input("Do you want to play the game again? Type Y for yes and N for no. ").lower()

# Functionality to play endlessly.
reply = input("Do you want to play the number guessing game? Type Y for yes and N for no. ").lower()

while(reply == 'y'):
  game()
  

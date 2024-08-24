import Guessing_number_art as art
import random
print(art.logo)
print("Welcome to number guessing game !!!")
print("I am thinking of a number between 1 to 100")

guessed_number=random.randint(1,100)
    

difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard'").lower()

def guess_number():
    if difficulty_level=='easy':
        attempts=10
        print("You have 10 attempts remaining to guess the number")
    else:
        attempts=5
        print("You have 5 attempts remaining to guess the number")

    for attempt in range(attempts):
        num_guess=int(input("Make a guess :"))
        rem_attempts=attempts-(attempt+1)
        if num_guess<guessed_number and rem_attempts>0:
            print("Too low !!!")
        elif num_guess>guessed_number:
            print("Too high !!!")
        else:
            print(f"You got it. the answer was {num_guess}")
            break
        if rem_attempts>0:
            print("Guess again")
            print(f"You have {rem_attempts} attempts remaining to guess the number")      
        else:
            print("You ran out of attempts !!! you lose")
guess_number()    




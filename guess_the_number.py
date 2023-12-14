from art import logo
import random

print(logo)
print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
In hard mode You have only 5 chance to guess. In easy mode You have 10 chance to guess. 
Choose a difficulty. Type 'easy' or 'hard':
""")

difficulty_level = input()

random_number = random.choice(range(0, 101))
attempts_level_easy = 10
attempts_level_hard = 5
flag = True

while flag:

    if difficulty_level == 'easy':
        if attempts_level_easy < 1:
            print(f"No more guessing. Correct answer was {random_number}")
            break
        player_type = int(input("Make a guess: "))
        if player_type == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        elif player_type > random_number and attempts_level_easy != 0:
            attempts_level_easy -= 1
            print("Too high.")
            print(f"You have {attempts_level_easy} attempts remaining to guess the number.")
        elif player_type < random_number and attempts_level_easy != 0:
            attempts_level_easy -= 1
            print("Too low.")
            print(f"You have {attempts_level_easy} attempts remaining to guess the number.")

    elif difficulty_level == 'hard':
        if attempts_level_hard < 1:
            print(f"No more guessing. Correct answer was {random_number}.")
            break
        player_type = int(input("Make a guess: "))
        if player_type == random_number:
            print(f"You got it! The answer was {random_number}")
            break
        elif player_type > random_number and attempts_level_hard != 0:
            attempts_level_hard -= 1
            print("Too high.")
            print(f"You have {attempts_level_hard} attempts remaining to guess the number.")
        elif player_type < random_number and attempts_level_hard != 0:
            attempts_level_hard -= 1
            print("Too low.")
            print(f"You have {attempts_level_hard} attempts remaining to guess the number.")

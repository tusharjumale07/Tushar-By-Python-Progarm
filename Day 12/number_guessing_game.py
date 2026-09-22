import random

random_number = random.randint(1, 100)
print("Welcome to Number Guessing Game...")
level = input("Select the level, EASY or HARD?: ").upper()
if level == "EASY":
    turn = 10
elif level == "HARD":
    turn = 5
else:
    print("Select appropraite option..")

while turn > 0:

    current_lives = turn
    user_input = int(input(f"You have {current_lives} lives left. Guess the number: "))
    if user_input > random_number:
        print("Your guess is too high...")
        turn = turn - 1
    elif user_input < random_number:
        print("Your guess is too low...")
        turn = turn - 1
    else :
        turn = 0
        print("Congrats you won the game...")
if user_input != random_number:
    print(f"Better Luck Next Time. The number guessed by computer was {random_number}")
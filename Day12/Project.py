import random

def guess_number():
    return random.randint(1, 100)

def set_difficulty(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Invalid input")
        return 0

def check_answer(guess, answer):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return attempts - 1
    elif guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    return attempts - 1

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = guess_number()
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = set_difficulty(difficulty)

guess = 0
while guess != answer:
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = check_answer(guess, answer)
import random

# Generates a random number between 1 and 100
secret_number = random.randint(1, 10)
attempts = 0
guess = None

print("Welcome to the Number Guessing Game! 🎯")
print("I have selected a number between 1 and 10. Try to guess it!")

# While loop runs until the user guesses correctly
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")

print(f"Congratulations! 🎉 You guessed the number {secret_number} in {attempts} attempts.")

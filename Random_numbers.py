import random
def Random_numbers_Game():
    print("Welcome to the Random Numbers Game!")
    print("I will generate a random number between 1 and 100.")
    print("You have to guess the number. You have 10 attempts.")
    
    random_number = random.randint(1, 100)
    attempts = 10
    
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} correctly!")
            break
        
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {random_number}.")

Random_numbers_Game()
    
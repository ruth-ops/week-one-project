import random
print("welcome to number guessing game") 

secret_number = random.randint ( 1, 100)
print("im thinking of a number between 1 to 100")

level = input("pick a level: 'easy' ,'medium','hard'): ").strip().lower()

if level == "easy":
    attempts = 10
elif level == "medium":
    attempts = 7
else:
    attempts = 5
    used_attempts = 0
    total_attempts = attempts

while attempts > 0:
    print(f"\nattempts remaining: {attempts}")
    try:
        guess = int(input("make a guess: "))
    except ValueError:
        print("invalid input.please enter a valid number whole number.")
        continue
    if guess < 1 or guess > 100:
        print("invalid input.please enter a number between 1 and 100.")
        continue
    used_attempts += 1
        
    if guess == secret_number:
        print(f"you win! you guessed the number {secret_number} in {used_attempts} attempts.")
       
    elif guess > secret_number:
        print("too high")
        attempts -= 1
    else:
        print("too low")
        attempts -= 1
   
if attempts == 0:
    print(f"\ngame over the number was {secret_number}.")


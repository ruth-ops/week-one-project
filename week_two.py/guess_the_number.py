import random
print("welcome to number guessing game") 

secret_number = random.randint ( 1, 100)
print("im thinking of a number between 1 to 100")
level = input("pick a level: 'easy' ,'medium','hard' ")

if level == "easy":
    attempts = 10
elif level == "medium":
    attempts = 7
else:
    attempts = 5
while attempts > 0:
    print("attempts remaining" + str(attempts))
    guess = int(input("make a guess:"))
    if guess == secret_number:
        print("you win")
        attempts = 0

    elif guess > secret_number:
        print("too high")
    else:
        print("too low")

    attempts -= 1
if attempts == 0:
    print("game over")


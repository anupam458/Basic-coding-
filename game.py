import random
secret_number = random.randint(1,10)
count = 0
while True:
    guess = int(input("Guess the number between 1 to 10 = "))
    if guess > secret_number:
        print("Too high :")
        count += 1
    elif guess < secret_number:
        print("Too low :")
        count += 1
    else:
        print("Correct guess, you won")
        count += 1
        print("You take ",count,"attempts :")
        break
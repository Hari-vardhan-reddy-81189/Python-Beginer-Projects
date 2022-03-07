actual_number = 34
attempts = 0
while True:
    attempts +=1
    guess = int(input("Enter a number"))
    if guess<actual_number:
        print("Your Guess is low")
    
    elif guess>actual_number:
        print("Your guess is high")
    else:
        print(f"You guessed the number in {attempts} attempts")
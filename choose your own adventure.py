name = input("Enter your name?: ")
print("Welcome", name, "to this adventure")
answer = input("You are in a dirt road, it has come an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come to river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")
    if answer == "swim":
        print("You swam across and were eaten by alligators.")
    elif answer == "walk":
        print("You wlked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option.")
    
elif answer == "right":
    answer = input("you come to a bridge, it looks like woobly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and lose")
    if answer == "cross":
        answer = input("You cross the bridge and met the stranger. Do you talk to them (yes/no)")
        
        if answer == "yes":
            print("You talk to the stranger and they give gold. You Win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose. ")
        else:
            print("Not a valid option. You lose. ")
    else:
        print("Not a valid option. You lose. ")

else:
    print("Not a valid option. You lose.")

print("Thank You!")
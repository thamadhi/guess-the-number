
import random
number=random.randint(1,10)
tries=0

print("Hello!!!")
print("Would You Like To Play A Game?")
print("yes")
print("no")

option=input("Select Your Option:")

if option=="yes":
    print("I Am Thinking Of A Number Between 1-10")
    print("You Have 3 Tries To Guess The Number I Am Thinking Of")

    guess = input("Enter Your Guess: ")
    guess = int(guess)
    tries = tries + 1

    if guess>number:
        print("Guess LOWER")
    if guess<number:
        print("Guess HIGHER")

    if guess!=number and tries<3:
        guess = input("enter your guess: ")
        guess =int(guess)
        tries = tries +1

    if guess>number:
        print("Guess LOWER")
    if guess<number:
        print("Guess HIGHER")

    if guess!= number and tries<3:
        guess= input("Enter Your Guess: ")
        guess= int(guess)
        tries= tries +1
        
    if guess==number:
        print("You Won!!")
        print("Number Of Tries: " +str(tries))
    else:
        print("Aww You Lost!!")
        print("Number Of Tries:" + str(tries))
elif option=="no":
    print("Thank You!!")
else:
    print("INVALID OPTION!")        

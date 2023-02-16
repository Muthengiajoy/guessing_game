# this program demonstrates a guessing game
#1.Get user name
#2.get user number using while loops
#3.generate random number outside the while loop
#3.Using a while loop check if user input is equal to generated random number
from random import randint
user_name = input("what_is_your_name:")
print("hello there"+user_name +"1")


random_number = randint(10,50)
counter = 0
while counter < 5:
    user_number = eval(input("enter_Random_number:"))
    counter == counter+1
    if user_number < random_number:
        print("your guess is too low")
    elif user_number > random_number:
        print("your guess id too high")
    elif user_number == random_number:
        break
    print("game over:")
    if user_number == random_number:
        print("you win!")
    else:
        print("Game over ! The correct number is:")
        print(random_number)


# this program demonstrates a guessing game
#1.Get user name
#2.get user number using while loops
#3.generate random number outside the while loop
#3.Using a while loop check if user input is equal to generated random number
from random import randinit
user_name = input("what_is_your_name:")
print("hello there"+user_name +"1")
number = randinit(10,50)


counter = 0
while counter < 5:
    user_number = eval(input("enter_a_Random_number:"))


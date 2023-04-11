from random import *
end = False
while end != True:
    end = input("Would you like to roll the dice? ").lower()
    if end == 'no' or end == 'n':
        end = True
        print("Thank you for using my Dice application")
    else:
        diceRoll = randint(1,6)
        print(diceRoll)
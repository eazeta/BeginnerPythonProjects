from random import randint

difficulty = ""
while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
    difficulty = input("Please enter a difficulty, 'easy', 'medium' or 'hard': ").lower()

if difficulty == "easy":
    upperLimit = 5
elif difficulty == "medium":
    upperLimit = 10
else:
    upperLimit = 50

print(f"I have a number in mind and you have to guess what it is. It's a number between 1 and {upperLimit}.")

userNumber = input("Enter your number: ")
while not userNumber.isdigit():
    print("Invalid input!")
    userNumber = input("Enter your number: ")

myNumber = randint(1, upperLimit)

if userNumber == myNumber:
    print(f"You Won! We both guessed {userNumber}")
else:
    print(f"You Lose! My number was {myNumber} but your guess was {userNumber}")
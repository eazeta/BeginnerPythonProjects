import random as r

# This is a function which returns the life points in the code. This wasn't necessary for the game but I just added it to showcase functions.
def displayLives(lives):
    output = ""
    for i in range(0,lives):
        output += "♡"
    return output
play = True
while play == True:
    # This is the list of words you can choose from
    list_of_words = ['emmanuel','python','data','computer','environment','science','statistics']
    # This uses the choice method from the random library to randomly select a word in the list
    word = r.choice(list_of_words)
    word_list = []
    guess_list = []
    lives = 5
    # Separates the characters in the word in a list
    for i in range(0,len(word)):
        word_list.append(word[i])
        guess_list.append('*')
    # Start of the game. The lives are outputted and a while loop keeps the game running until they've guessed the word or they've run out of life points. 
    while '*' in guess_list and lives > 0:
        print(f"You have {lives}HP: ",displayLives(lives))
        print("\n")
        print(guess_list)
        print("\n")
        guess = input("Enter your guess: ")
        if guess in guess_list:
            print("You have already chosen this value!")
        else:
            if guess in word_list:
                for i in range(0,len(word_list)):
                    if word_list[i] == guess:
                        guess_list[i] = word_list[i]
                    else:
                        continue
            elif guess not in word_list:
                lives -= 1
                print("Incorrect guess")

    print(guess_list)
    print("\n")

    if guess_list == word_list:
        print("Congratulations! You guessed the word!")
    else:
        print(f"You lost! The word is {word}")
    
    playAgain = input("Would you like to play again? Enter 'y' if yes or 'n' if no: ")

    play = True if playAgain == 'y' else False
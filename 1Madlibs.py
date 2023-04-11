# Asks a user to input a variety of variables to later use in the madlib
gender = input("Please enter boy, girl or non-binary person for your character: ").lower()
fruit = input("Please enter a fruit (plural): ")
if gender == "boy":
    pronoun = "he"
elif gender == "girl":
    pronoun = "she"
else:
    pronoun = "they"

colour = input("Please enter your favourite colour: ")
verb1 = input("Enter a verb in the past tense: ")

# Outputs madlib
print(f"There once was a {gender} who loved eating {fruit}. One day {pronoun} walked through a field and {pronoun} came across a tree with {fruit} hanging off of it. The {gender} gasped because {pronoun} noticed that the fruit were {colour}. The {gender} climbed up the tree, grabbed one of the {colour} {fruit} and {verb1} it.")
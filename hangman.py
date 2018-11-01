


# This is an ARRAY of the body parts of the man that will appear when a wrong guess is entered
hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]

# This variable sets the number of allowed guesses
# Notice we used the len function to COUNT the number of items in the array/list
num_wrong_guesses_allowed = len(hangman_parts)

# This is setting words that can be used for guesses...in an ARRAY
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]
# this function will draw based on the number of wrong guesses
def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        # increment the count if wrong guess
        num_wrong_guesses = num_wrong_guesses_allowed

# this is a DICTIONARY of the characters used for the body parts NOTE '{' and not '['
    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }

    hangman_newlines = [ "head", "right arm", "right leg" ]
    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)

# Below using an input funtion to prompt the player for his/her name
name = input("What is your name? ")

# Print hello and the name entered (basically printing a string of text WITH name by concatenating
print("Hello " + name + " lets play the hangman")

#set the counter for your loop
wrong_guesses = 0

# the variable used below named num_wrong_guesses_allowed is a count of the body parts...if you added additional body parts later, your guesses would increase automatically
while wrong_guesses < num_wrong_guesses_allowed:
    # using input() and lower() the lower function is used incase a guess is UPPERCASE
    guess =input("What is your guess? ").lower()
    if guess in words:
        print("Correct")
    else:
        print("Wrong")
        # below is your counter for the guesses...everytime an incorrect guess is entered, you need to increase the guess count by ONE
        wrong_guesses=wrong_guesses + 1
    # below is teh function that will draw the man based on the number of guesses made
    draw_hangman(wrong_guesses)
    #the statement below uses logic to see if the nnumber of guess and guess allowed has been met, if so than game over!
if wrong_guesses == num_wrong_guesses_allowed:
    print ("Sorry, You Lost, game over")

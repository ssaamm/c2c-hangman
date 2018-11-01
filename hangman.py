# list of the body parts that will appear when a wrong guess is entered
hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]

num_wrong_guesses_allowed = len(hangman_parts)  # notice: len() gets us the length of the list

# words that our program chooses between to guess
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

# convenience function provided to 
def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        # increment the count if wrong guess
        num_wrong_guesses = num_wrong_guesses_allowed

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

# prompt player for her/his name
name = input("What is your name? ")

print("Hello", name, " let's play Hangman!")

# need to track the number of incorrect guesses made so far
wrong_guesses = 0
word = 'apple'

while wrong_guesses < num_wrong_guesses_allowed:
    guess = input("What is your guess? ").lower()  # .lower()
    if guess in word:
        print("Correct")
    else:
        print("Wrong")
        wrong_guesses += 1
    draw_hangman(wrong_guesses)

if wrong_guesses == num_wrong_guesses_allowed:
    print("GAME OVER")

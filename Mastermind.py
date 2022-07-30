#Import some libraries
import os
import random

#Game colors
colors = {
    "E" : (100, 100, 100),

    "R" : (255, 0, 0),
    "Y" : (255, 255, 0),
    "G" : (0, 255, 0),
    "B" : (0, 0, 255),
    "K" : (0, 0, 0),
    "W" : (255, 255, 255),
}

#The original base (board)
base = [
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'N', 'E', 'N', 'E', 'N', 'E', 'N', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'K'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'K', 'E', 'K', 'E', 'K', 'E', 'K', 'E', 'E', 'K', 'K', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
]

#Print text of a certain color
def color(rgb, text = "  "):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    print("\033[48;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text), end = "")
    print("\033[48;2;{};{};{}m{}\033[38;2;255;255;255m".format(0, 0, 0, ""), end = "")

#Get the number of red and white pins needed
def check():
    tChoice = list(choice)
    tGuess = list(guess)
    red = 0
    white = 0

    for letter in tChoice:
        if tGuess[tChoice.index(letter)] == letter:
            red += 1
            tGuess[tGuess.index(letter)] = ""
        elif letter in tGuess and tChoice[tGuess.index(letter)] != letter:
            white += 1
            tGuess[tGuess.index(letter)] = ""
        tChoice[tChoice.index(letter)] = ""

    return (red, white)

#Draw the base
def draw():
    os.system('clear')
    count = -1
    for row in base:
        for letter in row:
            #color(colors[letter if letter != "N" else choice[count] if (count := count + 1) < 4 else None])
            color(colors[letter if letter != "N" else "K"])
        color(colors["K"], "\n")
    print()

print("Welcome to Mastermind!\n")
if input("Do you know how to play [y/n]? ").upper() == "N":
    print()
    print("The computer is the codemaker, you are the codebreaker")
    print("As the codebreaker, you're trying to break the codemaker's code in ten guesses or less")
    print("The code is a sequence of four colored pins, allowing duplicates\n")
    print("The colors are:")
    print("  - R: red")
    print("  - Y: yellow")
    print("  - G: greed")
    print("  - B: blue")
    print("  - W: white")
    print("  - K: black\n")
    print("Feedback will be given based on your guess (you'll see this on the right)")
    print("  - Each white pin signifies that one of the pins in your guess is good in color but is in the wrong position")
    print("  - Each red pin signifies that one of the pins in your guess is good in both color and position")
    print("You type your four pin long combination at once, so you won't know which feedback pin applies to which of the pins in your guess")
    if input("Would you like to see an example [y/n]? ").upper() == "Y":
        print()
        print("Assume the code is RWGR")
        print("You, not knowing the code, type in RGYB")
        print("Both the code and the guess have R as their first color")
        print("The only other common colored pin is G but your positioning is wrong")
        print("Thus, you will receive one red pin (for the red) and one white pin (for the green) as your feedback")
        print("Of course, you won't know that the red feedback pin is for your red guess pin and that the white feedback pin applies to your green guess pin")
        input("Type enter to continue")

fbHelp = input("Would you like to enable feedback help [y/n]? ").upper() == "Y"

#Make the code
choice = []
for i in range(4):
    choice.append(random.choice(list(colors.keys())[1:]))

#Draw the base
color(colors["K"], "\n")
draw()

#Variables needed for running the game
guess = None
rnd = 0

#Run the game
while guess != choice and rnd < 10:
    #Increment the round by 1
    rnd += 1

    #Give feedback help if enabled
    if rnd > 1 and fbHelp:
        if tRed != 0: print(f"{tRed} {'pin' if tRed == 1 else 'pins'} {'is' if tRed == 1 else 'are'} the right color and in the right position")
        if tWhite != 0: print(f"{tWhite} {'pin' if tWhite == 1 else 'pins'} {'is' if tWhite == 1 else 'are'} the right color but in the wrong position")
    print()

    #Get the user's guess
    print("R: red, Y: yellow, G: green")
    print("B: blue, W: white, K: black")
    guess = list(input("Guess: ").upper())[:4]
    while not all(letter in list(colors.keys())[1:] for letter in guess):
        print("\033[F", end = "")
        print("\033[K", end = "")
        guess = list(input("One or more of those letters are invalid; Guess: ").upper())[:4]
    
    #Get the number of red/white pins
    red, white = check()
    tRed, tWhite = red, white

    #Update the base with the guess and pins
    base[35 - 3 * rnd] = ["E" if letter == "E" else "R" if (red := red - 1) >= 0 else "W" if (white := white - 1) >= 0 else "K" for letter in base[35 - 3 * rnd]]
    count = -1
    base[36 - 3 * rnd] = ["E" if letter == "E" else guess[count] if (count := count + 1) < 4 else "R" if (red := red - 1) >= 0 else "W" if (white := white - 1) >= 0 else "K" for letter in base[36 - 3 * rnd]]
    
    #Redraw the updated base
    draw()

#Update the base with the code
count = -1
base[1] = ["E" if letter == "E" else choice[count] if (count := count + 1) < 4 else None for letter in base[1]]

#Redraw the updated base
draw()

#Print whether the user wins or loses
if guess != choice: print("You lost")
else: print("You won")
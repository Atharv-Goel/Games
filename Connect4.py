import os
import random
from math import log2
from contextlib import suppress

board = [
  ["", "", "", "", "", "", ""],
  ["", "", "", "", "", "", ""],
  ["", "", "", "", "", "", ""],
  ["", "", "", "", "", "", ""],
  ["", "", "", "", "", "", ""],
  ["", "", "", "", "", "", ""]
]

def draw():
    for row in board:
        print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 255, " " * 29), end = "")
        print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 0, ""))
        
        for column in row:
            print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 255, " "), end = "")
            if column == "":
                print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 0, " "), end = "")
            elif column == "R":
                print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(255, 0, 0, " "), end = "")
            else:
                print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(255, 255, 0, " "), end = "")
        
        print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 255, " "), end = "")
        print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 0, ""))
    
    print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 255, " " * 29), end = "")
    print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 0, ""))

def check(state):
    red = int("".join(["1" if column == "R" else "0" for row in state for column in row]), 2)
    red2 = int("".join(["1" if row[column] == "R" else "0" for column in range(len(state[0])) for row in state]), 2)
    yellow = int("".join(["1" if column == "Y" else "0" for row in state for column in row]), 2)
    yellow2 = int("".join(["1" if row[column] == "Y" else "0" for column in range(len(state[0])) for row in state]), 2)

    convert = (lambda x: (x % 7 * 6) + (x // 7))
    
    numbers = {
      1: 6,
      6: 5,
      7: 1,
      8: 7
    }

    for number in numbers:
        with suppress(ValueError):
            if number != 6:
                if convert(log2((red & red >> number) & (red & red >> number) << 2 * number)) == log2((red2 & red2 >> numbers[number]) & (red2 & red2 >> numbers[number]) << 2 * numbers[number]):
                    return "R"
            else:
                if convert(log2((red & red >> number) & (red & red >> number) << 2 * number)) == log2((red2 & red2 << numbers[number]) & (red2 & red2 << numbers[number]) >> 2 * numbers[number]):
                    return "R"

    for number in numbers:
        with suppress(ValueError):
            if number != 6:
                if convert(log2((yellow & yellow >> number) & (yellow & yellow >> number) << 2 * number)) == log2((yellow2 & yellow2 >> numbers[number]) & (yellow2 & yellow2 >> numbers[number]) << 2 * numbers[number]):
                    return "Y"
            else:
                if convert(log2((yellow & yellow >> number) & (yellow & yellow >> number) << 2 * number)) == log2((yellow2 & yellow2 << numbers[number]) & (yellow2 & yellow2 << numbers[number]) >> 2 * numbers[number]):
                    return "Y"

def check3(state, clr):
    if clr == "R": anticlr = "Y"
    else: anticlr = "R"
    red = int("".join(["1" if column == clr else "0" for row in state for column in row]), 2)
    red2 = int("".join(["1" if row[column] == clr else "0" for column in range(len(state[0])) for row in state]), 2)
    yellow = int("".join(["1" if column == anticlr else "0" for row in state for column in row]), 2)

    order = (lambda x: format(x, "b")[max(len(format(x, "b")) - 42, 0):].zfill(42))
    switch = (lambda x: int("".join([order(x)[column * 6 + row] for row in range(6) for column in range(7)]), 2))

    numbers = {
      7: 1,
      1: 6,
      6: 5,
      8: 7
    }

    nines = 0

    for number in numbers:
        if number != 6:
            nine = ((red & red >> number) & (red & red >> number) >> number)
            nine2 = (red2 & red2 >> numbers[number]) & (red2 & red2 >> numbers[number]) >> numbers[number]
            nine = ((nine >> number) | nine << 3 * number) & switch((nine2 << 3 * numbers[number]) | (nine2 >> numbers[number]))
            nines = nines | nine
        else:
            nine = ((red & red << number) & (red & red << number) << number)
            nine2 = (red2 & red2 >> numbers[number]) & (red2 & red2 >> numbers[number]) >> numbers[number]
            nine = ((nine >> 3 * number) | nine << number) & switch((nine2 << 3 * numbers[number]) | (nine2 >> numbers[number]))
            nines = nines | nine
    
    for number in list(numbers.keys())[1:]:
        if number != 6:
            nine = ((red & red >> number) & red << 2 * number) & switch((red2 & red2 >> numbers[number]) & red2 << 2 * numbers[number])
            nine2 = ((red & red << number) & red >> 2 * number) & switch((red2 & red2 << numbers[number]) & red2 >> 2 * numbers[number])
            nines = nines | nine >> number | nine2 << number
        else:
            nine = ((red & red << number) & red >> 2 * number) & switch((red2 & red2 >> numbers[number]) & red2 << 2 * numbers[number])
            nine2 = ((red & red >> number) & red << 2 * number) & switch((red2 & red2 << numbers[number]) & red2 >> 2 * numbers[number])
            nines = nines | nine << number | nine2 >> number

    return order(nines ^ (nines & yellow))

def trap(nines):
    filled = ["1" if column != "" else "0" for row in board for column in row]
    for nine in range(38):
        if nines[nine] == "1" and nines[nine + 4] == "1":
            if nine % 7 < 3:
                if nine < 35:
                    if filled[nine + 7] == "1" and filled[nine + 11] == "1":
                        return True
                else:
                    return True
    nines = int(nines, 2)
    if nines & nines << 7:
        return True
        

def fall(move):
    for row in range(6):
        if row == 5 or board[row + 1][move] != "":
            return row

def player(clr):
    while True:
        try:
            choice = abs(int(input("Column Number (1-7): "))) - 1
            if board[0][choice] == "":
                break
        except:
            print("\033[F", end = "")
            print("\033[K", end = "")
            continue
        print("\033[F", end = "")
        print("\033[K", end = "That column is full\n")
    board[fall(choice)][choice] = clr

def ai(clr):
    columns = [column for column in range(7) if board[0][column] == ""]
    ninesY = check3(board, "Y")
    ninesR = check3(board, "R")
    for value in range(42):
        if ninesY[value] == "1" or ninesR[value] == "1":
            if value > 34:
                board[fall(value % 7)][value % 7] = "Y"
                return None
            elif [column for row in board for column in row][value + 7] != "":
                board[fall(value % 7)][value % 7] = "Y"
                return None
            elif [column for row in board for column in row][value + 7] == "":
                if value > 27:
                    columns.remove(value % 7)
                elif value > 20 and [column for row in board for column in row][value + 14] != "":
                    columns.remove(value % 7)
    for column in columns:
        row = fall(column)
        if row > 0:
            stateY = [[column for column in row] for row in board]
            stateR = [[column for column in row] for row in board]
            stateY[row - 1][column] = "Y"
            stateR[row - 1][column] = "R"
            if trap(check3(stateY, "Y")) or trap(check3(stateR, "R")):
                columns.remove(column)
    for column in columns:
        stateY = [[column for column in row] for row in board]
        stateY[fall(column)][column] = "R"
        stateR = [[column for column in row] for row in board]
        stateR[fall(column)][column] = "R"
        if trap(check3(stateY, "Y")) or trap(check3(stateR, "R")):
            board[fall(column)][column] = "Y"
            return None
    if not columns:
        columns = [column for column in range(7) if board[0][column] == ""]
    column = random.choice(columns)
    board[fall(column)][column] = "Y"

print("Welcome to Connect 4!\n")
if input("Do you know how to play [y/n]? ").upper() == "N":
    print("The game is very similar to Tic Tac Toe")
    print("Instead of 3 in a row, though, the goal is to connect 4")
    print("Also, the game is played vertically, so gravity always pulls pieces down")
    print("That means that players play their move by choosing a column")

erase = input("Would you like to enable erase mode [y/n]: ").upper() == "Y"

print()
while True:
    try: 
        players = int(input("1 player or 2 players [1/2]: "))
        if players in [1, 2]: break
        else: int("")
    except ValueError:
        print("\033[F", end = "")
        print("\033[K", end = "")
        print("\033[F", end = "")
        print("\033[K", end = "")
        print("That is an invalid number of players")


print("\033[48;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 0, ""))
os.system("clear")
draw()

while [column for column in range(7) if board[0][column] == ""]:
    
    player("R")
    print()
    if erase: os.system("clear")
    draw()
    if check(board) == "R":
        print("Red Won!")
        break

    if players == 2: player("Y")
    else: ai("R")
    print()
    if erase: os.system("clear")
    draw()
    if check(board) == "Y":
        print("Yellow Won!")
        break

if not [column for column in range(7) if board[0][column] == ""]:
    print("Draw game")
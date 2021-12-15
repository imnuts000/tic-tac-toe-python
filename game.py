import random

field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
winner = ''

def print_field(field):
    for row in field:
        print("|", end="")
        for cell in row:
            print(" " + cell + " |", end="")
        print("\n-------------")


def enemy_move(field, side):
    pos = ''
    while True:
        pos1 = random.randint(1,3)
        pos2 = random.randint(1,3)
        pos = str(pos1)+str(pos2)
        if(field[int(pos[0])-1][int(pos[1])-1] == ' '):
            break
    field[int(pos[0])-1][int(pos[1])-1] = side


def check_winner(field):
    global winner
    three_row = []
    # check rows
    for row in field:
        for cell in row:
            if(cell != " "):
                three_row.append(cell)
                if (len(three_row) == 3):
                    if (three_row[0] == three_row[1] == three_row[2]):
                        winner = three_row[0]
                        print_field(field)
                        return True
        three_row = []
    #check collums
    for cell in range(0, 3, 1):
        for row in range(0, 3, 1):
            if(field[row][cell] != " "):
                three_row.append(field[row][cell])
                if(len(three_row)==3):
                    if(three_row[0] == three_row[1] == three_row[2]):
                        winner = three_row[0]
                        print_field(field)
                        return True
        three_row = []
    #check diagonals
    if(field[0][0] == field[1][1] == field[2][2]):
        winner = field[0][0]
        print_field(field)
        return True
    elif(field[0][2] == field[1][1] == field[2][0]):
        winner = field[0][2]
        print_field(field)
        return True
    return False


# selection side loop
side = ''
enemy_side = ''

while True:
    side = input("who are you gonna play as (x or o): ")
    if(side == "x" or side == "o"):
        if(side == "x"):
            enemy_side = "o"
        elif(side == "o"):
            enemy_side = "x"
        break
    else:
        print("It's gotta be x or o")

print_field(field)

# main game loop
while True:
    # selecting coordinated loop
    while True:
        pos = input("enter to numbers witch will be the position of your move (eg 13, 21): ")
        if (len(pos) == 2):
            if (field[int(pos[0]) - 1][int(pos[1]) - 1] == ' '):
                field[int(pos[0]) - 1][int(pos[1]) - 1] = side
                break
            else:
                print("You can't put it there")
        else:
            print("Wrong possittion")

    if (check_winner(field) == True):
        print(f"{winner} won!")
        break

    enemy_move(field, enemy_side)

    if (check_winner(field) == True):
        print(f"{winner} won!")
        break

    print_field(field)
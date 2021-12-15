import random

field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
winner = ''

def print_field(field):
    for row in field:
        print("|", end="")
        for cell in row:
            print(cell + "|", end="")
        print("\n-------")


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
    # check rows
    three_row = []
    for row in field:
        for cell in row:
            if(cell != " "):
                three_row.append(cell)
                if (len(three_row) == 3):
                    if (three_row[0] == three_row[1] == three_row[2]):
                        winner = three_row[1]
                        print_field(field)
                        return True
        three_row = []
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
            break
        else:
            print("Wrong possittion")
    # drawig
    while True:
        if (field[int(pos[0]) - 1][int(pos[1]) - 1] == ' '):
            field[int(pos[0]) - 1][int(pos[1]) - 1] = side
            break
        else:
            print("You can't put it here")

    if (check_winner(field) == True):
        print(f"{winner} won!")
        break

    enemy_move(field, enemy_side)

    if (check_winner(field) == True):
        print(f"{winner} won!")
        break

    print_field(field)
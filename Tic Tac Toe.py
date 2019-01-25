def displayArena():
    print(
    """

    # {0}  {1}  {2} #
    # {3}  {4}  {5} #
    # {6}  {7}  {8} #

    """.format(arena[0][0], arena[0][1], arena[0][2], arena[1][0], arena[1][1], arena[1][2], arena[2][0], arena[2][1], arena[2][2])
    )

def checkMate(symbol):
    global game
    if (arena[0][0] == arena [1][1] == arena[2][2] == symbol):
        game = False
    elif (arena[0][2] == arena [1][1] == arena[2][0] == symbol):
        game = False
    else:
        for i in range(3):
            if (arena[i][0] == arena [i][1] == arena[i][2] == symbol):
                game = False
                break
            elif (arena[0][i] == arena [1][i] == arena[2][i] == symbol):
                game = False
                break

arena = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]

game = True

print("""
 ###############################################
# The input format is row x Col, starts with 0  #
# First element is 0 x 0                        #
# Last element is 2 x 2                         #
 ###############################################
""")

count = 0

print("Player1 enter your name")
player1  = [input(), '0']
print("Player1 enter your name")
player2  = [input(), '1']

while game:
    if (count % 2 == 0):
        player = player1
    else:
        player = player2
    print("{}'s turn'".format(player[0]))
    userInput = input("")
    try:
        r, c = userInput.split(" x ")
    except ValueError:
        print("Enter the place in correct format")
        continue
    try:
        if arena[int(r)][int(c)] == "-":
            arena[int(r)][int(c)] = player[1]
        else:
            print("The place is already taken, try another place!")
            continue
    except IndexError:
        print("Please enter correct place value!")
        continue
    displayArena()
    checkMate(player[1])
    if not game:
        print("{} wins ... ".format(player[0]))
    count += 1

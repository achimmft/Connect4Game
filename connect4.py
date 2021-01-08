'''
    Connect 4 game
'''

'''
    Hi there, I'm working on the connect 4 game. I think i have done a lot ,but they are not enough 
    to make the game done. They only question that i'm having is to figure out how a player can win. 
    would you please help me with this? what i need is the clue on how i can get started. I would appreciate
    for that.

    Thank you in advance!
'''

# This is how game will look like

# | | | | | | | | 0
# --------------- 1
# | | | | | | | | 2
# --------------- 3
# | | | | | | | | 4
# --------------- 5
# | | | | | | | | 6
# --------------- 7
# | | | | | | | | 8
# --------------- 9
# | | | | | | | | 10
# 0123456789.....


def drawField(field):
    for row in range(11):
        if row % 2 == 0:
            pacticalRow = int(row / 2)
            for column in range(15):  # we have 15 columns
                if column % 2 == 0:
                    if column != 14:
                        print("|", end="")
                    else:
                        print("|")
                else:
                    if column == 1:
                        practicalColumn = 0
                    elif column == 3:
                        practicalColumn = 1
                    elif column == 5:
                        practicalColumn = 2
                    elif column == 7:
                        practicalColumn = 3
                    elif column == 9:
                        practicalColumn = 4
                    elif column == 11:
                        practicalColumn = 5
                    else:
                        practicalColumn = 6
                    print(field[practicalColumn][pacticalRow], end="")
        else:
            print("---------------")


# drawField()
playerTurn = 1
currentField = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [
    " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
drawField(currentField)
# print(currentField)
while(True):
    print("Player's turn", playerTurn,)
    moveRow = int(input("Please enter Row: "))
    moveColumn = int(input("Please enter column: "))

    if playerTurn == 1:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "X"
            playerTurn = 2
    else:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "O"
            playerTurn = 1

    drawField(currentField)

'''
    Hi there, I'm working on the connect 4 game. I think i have done a lot ,but they are not enough 
    to make the game done. They only question that i'm having is to figure out how a player can win. 
    would you please help me with this? what i need is the clue on how i can get started. I would appreciate
    for that.

    Thank you in advance!
'''

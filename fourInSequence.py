#Paige LaFave            3/30/2024


'''
This code is an adaptation from the game "Connect 4" - which we've called "Four In Sequence".
    It allows a user to play the game, read the instructions, and quit.
    If played, you can play with 1 or 2 Players (1 being vs a Computer)
    The game will consistently update the game board with the player choices and print whether there is a winner.
    At the game of the game, you will have the option to play again, read the instructions, or quit. 
NOTE: Red explanation comments were deleted prior to understanding the uses. 
    New comments were made to adapt to the creators understanding and explanations, leaving in what was required. 


CITATION: Adaptation and Modification - 
        URL: https://chat.openai.com
        ACCESSED: 3-15-2023
CITATION: Instructions - 
        URL: https://www.unco.edu/hewit/pdf/giant-map/connect-4-instructions.pdf
        ACCESSED: 4-1-2024
'''

import random
import sys

def printTitleMaterial(): #Prints tital, Author, and class information
    print("Four In Sequence!")
    print()
    print("By: Paige LaFave")
    print()
    print("This is an adaptation from the game Connect Four. \nThis program allows a user to play the game, read the instructions, and quit.\nIf played, you can play with 1 or 2 Players (1 being vs a Computer).")

def initialChoice(): # options: play, instructions, quit
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ") #choose function

    while choice != "p" and choice != "i" and choice != "q": #invalid choice
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")

    return choice

def chooseNumPlayers():
    numPlayers = int(input("Number of Players? [1] / [2]: ")) #choose num of players (1 or 2)

    while numPlayers != 1 and numPlayers != 2: #invalid choice
        print("ERROR: Please enter either 1 or 2...")
        numPlayers = int(input("Number of Players? [1] / [2]: "))

    return numPlayers

def printBanner(): #prints out banner in beginning of game
    print("#######################################################################") 
    print()
    print("~~ Starting New Round ~~")
    print()

def getPlayerPiece(playerNumber): # connects player to piece icon (., X, O)
    piece = ""
    if playerNumber == 0:
        piece = "."
    elif playerNumber == 1:
        piece = "X"
    elif playerNumber == 2:
        piece = "O"
    return piece

def createBoard(width, height):#(7,6) already chosen - no input
    empty = getPlayerPiece(0)
    board = []

    for i in range(0, height):
        board.append([])
        for j in range(0, width):
            board[i].append(empty)

    return board

def printBoard(board): #pritns gameboard with labels (digits)

    for row in board:

        for column in row:
            print(column, end="")
        print()

    for i in range(0, len(board[0])):
        print(i, end="")

    print()
    print()


def getColumnInt(board, playerNumber): #takes in user input as int. -- chooses column to place piece

    return int(input("Player {0}, please select a column between (0-{1}): ".format(playerNumber, len(board[0]) - 1)))


def getInputInRange(board, playerNumber):
    col = getColumnInt(board, playerNumber) #runs function - choose column

    while col < 0 or col > len(board[0]) - 1: #if not in column range - prints error
        print("ERROR: Value must be between (0-{0}). You entered: {1}".format(len(board[0]) - 1, col))
        col = getColumnInt(board, playerNumber) #runs while invalid

    return col


def getHumanInput(board, playerNumber):
    col = getInputInRange(board, playerNumber) #runs function to get range for column

    while getOpenRow(board, col) == -1: #ensures in range - prints error
        print("ERROR: Column {0} is full! Please choose a different column...".format(col))
        col = getInputInRange(board, playerNumber) #runs while invalid

    return col


def checkForNextMoveWin(board, playerNumber): #win?

    empty = getPlayerPiece(0)
    piece = getPlayerPiece(playerNumber)

    # TODO: Write code in this function that accomplishes the specification outlined in the documentation comment above.

    x = len(board[0])
    for column in range(x): # iterates through all columns and assigns each column number to loop vairable
        row = getOpenRow(board, column) # runs function -- is there an open row? returns row number

        if row != -1: #yes open row
            board[row][column] = piece #sets board location at [row][column] with player piece found with placePiece()

            if checkWinner(board, playerNumber): #runs function -- is there a winner?
                board[row][column] = empty #yes winner
                return column #return current column
            
            board[row][column] = empty # resets board at [row][column]

    return -1 #there was no winner, == -1


def checkAdjacent(board, playerNumber):
    col = -1
    piece = getPlayerPiece(playerNumber)
    adjacents = []

    # TODO: Write code in this function that accomplishes the specification outlined in the documentation comment above.


    for column in range(0, len(board[0])): #iterates through columns
        row = getOpenRow(board, column)

        if row != -1: # checks to make sure there is an open row

            #upper left piece (up one row, left one column)
            if (row - 1) >= 0 and column - 1 >= 0: #ensures not out of range

                if board[row-1][column-1] == piece: # = to piece?
                    adjacents.append(column) #appends column


            # left piece (left one column)
            if (column -1) >= 0:  #ensures not out of range

                if board[row][column - 1] == piece: # = to piece?
                    adjacents.append(column) #appends column

            #lower left piece (down one row, left one column)
            if (row + 1) < len(board) and (column - 1) >= 0: #ensures in range
                    
                    if board[row+1][column - 1] == piece: # = to piece?
                        adjacents.append(column) #appends column


            # lower piece (down one row)
            if (row + 1) < len(board): # ensures range
               
               if board[row + 1][column] == piece: # = to piece?
                   adjacents.append(column) #appends column


            # lower right piece (down one row, right one column)
            if (row + 1) < len(board) and (column + 1) < len(board): #ensures in range
                
                if board[row+1][column+1] == piece: # = to piece?
                    adjacents.append(column) #appends column


            #right piece (right one column)
            if (column + 1) < len(board[0]): #ensures in range

                if board[row][column + 1] == piece: # = to piece?
                    adjacents.append(column) # appends column


            # upper right piece (up one row, right one column)
            if (row - 1) >= 0 and (column + 1) < len(board): #ensrues in range

                if board[row-1][column+1] == piece: # = to piece?
                    adjacents.append(column) #appends column
 

    if len(adjacents) > 1:
        randVal = random.randrange(0, len(adjacents))
        col = adjacents[randVal]
        # print("piece:", piece, "adjacents:", adjacents, "randVal:", randVal, "col:", col) # for debugging
    
    return col


def getComputerInput(board, currentPlayerTurn): #gets the input for 1 human v computer
    opponentPlayerTurn = switchTurns(currentPlayerTurn)
    col = checkForNextMoveWin(board, currentPlayerTurn) #winning move, the computer will take it

    if col != -1: # computer wins if col != -1
        print("WIN")

    # check if the opponent has a winning move - if there is then block it
    if col == -1:
        col = checkForNextMoveWin(board, opponentPlayerTurn)
        print("BLOCK")

    # check if there are any adjacent pieces available - try to connect to them
    if col == -1:
        col = checkAdjacent(board, currentPlayerTurn)
        print("ADJACENT")
    
    # if no winning move is available, and no block is avaialable, and no adjacent pieces are available - choose a random column
    if col == -1:
        col = random.randrange(0, len(board[0]))
        while getOpenRow(board, col) == -1:
            col = random.randrange(0, len(board[0]))
        print("RANDOM")

    # print out a string stating the column that was chosen
    print("Player {0}, please select a column between (0-{1}): {2}".format(currentPlayerTurn, len(board[0]) - 1, col))

    return col

def getOpenRow(board, col): #iterates through all rows of given column and returns first open row
    empty = getPlayerPiece(0)

    for row in range(len(board) - 1, -1, -1):

        if board[row][col] == empty:
            return row
        
    return -1

def placePiece(board, row, col, piece):#inserts piece into gameboard as a specific position
    board[row][col] = piece


def dropPieceIntoBoard(board, col, playerNumber): # inserts a piece into gameboard in given column
    row = getOpenRow(board, col)

    placePiece(board, row, col, getPlayerPiece(playerNumber))


def checkDraw(board): #checks for draw (no more spots open)
    empty = getPlayerPiece(0) # runs functions

    # TODO: Write code in this function that accomplishes the specification outlined in the documentation comment above.

    y = len(board[0])
    for row in range(y): # iterate through all the rows in the board

        for column in range(y): # iterate through all the columns in a row

            if board[row][column] == empty: #is column empty?
                return False #draw is not possible == False

    return True # there is a draw == True

def checkWinner(board, playerNumber): #is there a winner? (4 in row) -- horizontal, vertical, slope (+/-)

    # TODO: Write code in this function that accomplishes the specification outlined in the documentation comment above.

    piece = getPlayerPiece(playerNumber)

    # check horizontal locations
    for row in range(len(board)): 
        for column in range(len(board[row]) - 3):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True # === win if 4 in row like --

    # check vertical locations
    for column in range(len(board[0])):
        for row in range(len(board) -3):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece and board [row + 3][column] == piece:
                return True # === win if 4 in row like |


    # check negatively sloped diagonals
    for row in range(len(board) - 3):
        for column in range(len(board[0]) - 3):
            if board[row][column] == piece and board[row+1][column -1] == piece and board[row + 2][column-2] == piece and board[row+3][column-3] == piece:
                return True # === win if 4 in row like \

    # check positively sloped diagonals 
    for row in range(3, len(board)):
        for column in range(len(board[0]) - 3):
            if board[row][column] == piece and board[row-1][column+1] == piece and board [row - 2][column + 2] == piece and board [row - 3] [column + 3] == piece:
                return True # === win if 4 in row like /

    return False # else = no win yet


def resetGameOptions(): #reset all relvant gameplay variables to original state

    currentPlayerTurn = 1
    winner = False
    draw = False

    return currentPlayerTurn, winner, draw


def switchTurns(currentPlayerTurn): #switches player (1 or 2)
    return ((currentPlayerTurn % 2) + 1)

def main(): # main function - runs other functions 
    running = True # running control variable 
    
    # gameplay variables
    currentPlayerTurn = 1 # can be 1 or 2
    winner = False
    draw = False

    # print the title/ author information
    printTitleMaterial()

    # play the game
    while running: # if running = True - yes to play game

        choice = initialChoice()
        if choice == "p": #p = play
            currentPlayerTurn, winner, draw = resetGameOptions() #reset relevant gamplay variables (runs function)
            numPlayers = chooseNumPlayers() # chooses number of players (runs function)
            board = createBoard(7, 6) #creats the game board (runs function)

            printBanner() # round setup
            printBoard(board) #prints board

            while True: #main game loop
                if numPlayers == 1: # gets the input fr dropping a piece inside the board (switches between P1 and P2(computer))
                    if currentPlayerTurn == 1: #Player 1 turn
                        col = getHumanInput(board, currentPlayerTurn) #runs function
                    elif currentPlayerTurn == 2: #Player 2 turn (computer)
                        col = getComputerInput(board, currentPlayerTurn) #runs function
                    else: #invalid choice
                        print("ERROR: currentPlayerTurn is neither 1 or 2! It is actually: {0}".format(currentPlayerTurn))
                        sys.exit()

                elif numPlayers == 2: # Gets input for dropping piece inside board (2 human players)
                    col = getHumanInput(board, currentPlayerTurn) # runs function

                else: #invalid choice
                    print("ERROR: numPlayers is neither 1 or 2! It is actually: {0}".format(numPlayers))
                    sys.exit()
                

                dropPieceIntoBoard(board, col, currentPlayerTurn) # update baord with new piece (runs function)

                printBoard(board) # prints new board

                winner = checkWinner(board, currentPlayerTurn) # checks to see if there is a win (runs function)

                draw = checkDraw(board) # checks to see if draw (no empty spaces) (runs function)
                
                if winner == True: #checks if game is over
                    print("~~ Player {0} ({1}) Wins! ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    break # game is over - P1 wins

                elif draw == True:
                    print("~~ Draw! ~~")
                    print()
                    break # game is over - draw

                else: # if the game is not over, print that the turn is over
                    print("~~ End Of Player {0} ({1}) Turn ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    # switch turns -- game not over
                    currentPlayerTurn = switchTurns(currentPlayerTurn) #new turn (runs function)
                    
        elif choice == "i": #i = print instructions:
            print()
            print("These are the instructions to play Four In Sequence: \n")
            print("\t (1) This is a 2 player game, with comes with each player having a total of 21 moves each.\n\t\t - These being labeled with either an X or an O.")
            print("\t\t - Thus there is a 7x6 board with a total of 42 spots. ")
            print("\n\t (2) You can play this game with 1 Player (Human vs Computer), or 2 Players (Human vs Human).")
            print("\n\t (3) The objective of this game is to place 4 of your pieces in a row without being blocked.")
            print("\t\t - You can win four in sequence horizontally, verticall, or diagnoally.")
            print("\t\t - Note: Your piece fall down the columns, so you cannot pick the row it goes into. \n\t\t\t * i.e. Your piece will fall to the next open row in your selected column.\n")
            print("\t(4) The turns will rotate back and forth with no way to have a turn twice in a row.")
            print("\n\t(5) After each turn, a new board will print.")
            print("\t\t - Make sure to look at the most recent board when choosing a column.")
            print("\t\t - Note: Empty slots are shown with '.'. ")
            print("\t\t\t * X and O suggest a piece from its corresponding player.")
            print("\n\t (6) Once someone wins, you will have the option to play again, read the instrucitons, or quit!")
            print()
        elif choice == "q": # q = quit - set running variable to fals and print goodbye message
            running = False
            print()
            print("Goodbye, player! Thank you for playing!")
            print()

        else: #invalid choice
            print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was:", choice)
            quit()

if __name__ == "__main__": #runs main function 
    main()

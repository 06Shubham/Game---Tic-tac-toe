board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentPlayer = "X"
winner = None
gameRunning = True

# printing the board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# player input
def playerInput(board):
    inp = int(input("Enter a number (1-9): "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops, spot already taken!")

# switch player
def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

# checking horizontal win
def checkHorizontal(board):
    global winner
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            winner = board[i]
            return True
    return False

# checking vertical win
def checkVertical(board):
    global winner
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            winner = board[i]
            return True
    return False

# checking diagonal win
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

# checking for tie
def checkTie(board):
    return "-" not in board

# checking win or tie
def checkWin():
    return checkHorizontal(board) or checkVertical(board) or checkDiagonal(board)

# game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    if checkWin():
        print(f"The winner is {winner}")
        break
    if checkTie(board):
        print("It's a tie!")
        break
    switchPlayer()

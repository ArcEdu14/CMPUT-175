# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 2 - Debugging: Tic-Tac-Toe
#
# ~ Created by CMPUT 175 Team ~
# =================================================================
import time, os
from ticTacToe import TicTacToe

def clear():
    '''
    clears the screen
    '''
    if os.name == "posix":
        print("posix")
        os.system('clear')
    else:
        print("cls")
        os.system('cls')


def getCoord(player, dimension):
    '''
    Prompts for an index value corresponding to either the row or column (as
    described by dimension) of a square on the board
    Inputs:
       player (int) - number of current player (1 or 2)
       dimension (str) - describes what the index relates to (e.g. 'row' or 'column')
    Returns: int index (either row or column)
    '''
    LOWER = 0
    UPPER = 3  # BUG HERE (logic/functional) range function produces the range up to but not including the upper bound, so this needs to be 1 above the maximum input
    index = input('Player ' + str(player) + ', please enter a ' + dimension+': ')
    while True:
        if index.isdigit() and int(index) in range(LOWER, UPPER):
            return int(index)  # BUG HERE (functional) the input needs to be converted to an int to be used
        else:
            index = input(f"Invalid input! Please enter a valid {dimension}: ")


def isGameOver(myBoard, player):
    '''
    The game is over if the current player has won, or there are no empty squares
    left for the next player to select.
    Inputs:
       myBoard (TicTacToe) - object containing current state of game board
       player (int) - number of current player (1 or 2)
    Returns: True if game if over; False otherwise
    '''
    if myBoard.isWinner(player):
        clear()
        myBoard.drawBoard()  # BUG HERE (syntax) the function name was incorrectly written as drawboard() instead of drawBoard()
        print ('Player', player ,"wins. Congrats!")           
        return True
    elif myBoard.boardFull():
        clear()
        myBoard.drawBoard()
        print ("It's a tie.")             
        return True
    return False


def playAgain():
    '''
    Asks if a new game should be started. A valid answer is any entry that begins
    with y/Y/n/N.
    Inputs: none
    Returns: True if a new game should start; False otherwise
    '''
    playAgain = ' ' 
    # validate user's input
    while playAgain[0].upper() not in ['Y', 'N']:
        playAgain=input("Do you want to play another game? (Y/N) ")
    return playAgain[0].upper() == "Y"   


def main():
    '''
    Controls the game flow for a 2-player version of Numerical Tic Tac Toe.
    Inputs: none
    Returns: None
    '''
    newGame = True
    TITLE = "Starting new Numerical Tic Tac Toe game"  # BUG HERE (functional) If you don't want this to print every new game, then move outside the main loop
    print("-" * len(TITLE))
    print(TITLE)
    print("-" * len(TITLE))
    while newGame:
        myBoard = TicTacToe()
        gameOver=False
        turn = 0
        while not gameOver:
            myBoard.drawBoard()  # BUG HERE (syntax) the function name was incorrectly written as drawboard() instead of drawBoard()
            
            # get input from user
            entry = ['O','X'][turn]
            
            row = getCoord(turn+1, 'row')
            col = getCoord(turn+1, 'column')
                                   
            # update board and check if game continues
            if myBoard.update(row, col, entry):
                print(f"Player {turn+1}'s turn ended")
                gameOver = isGameOver(myBoard, turn+1)
                turn = (turn+1) % 2  # BUG HERE (calculation) Floor divide will not cycle between 0 and 1 in the right order, need to use modulus instead
            # need to reprompt for new input for given player
            else:
                print('Error: could not make move!')
            time.sleep(1)
            if not gameOver:
                clear()  # BUG HERE (functional, logic) the clear() was in the incorrect location outside the loop previously, and also there needs to be a check if the game is over or else it will clear before asking if you want to play again
        newGame = playAgain()  # BUG HERE (syntax) missing parenthesis does not call function correctly
        if newGame:
            clear()  # BUG HERE (logic) to clear after starting a new game, and also don't clear if game ends

    print('Thanks for playing! Goodbye.')

if __name__ == "__main__":
    main()  # BUG HERE (system level/functional) main should be outside of the function, the name==main doesn't technically have to be there since this file isn't the imported one but its good practice
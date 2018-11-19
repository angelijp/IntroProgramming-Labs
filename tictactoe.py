# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Angeli Pinol
# Created: 2018 Nov 8
import random     
# Board as a 3x3 matrix
symbol = [ " ", "x", "o" ]
print("Welcome to Tic-Tac-Toe!")
board = [0,1,2,
         3,4,5,
         6,7,8]
def printboard():
        # print the top border
        print("+-----------+")
        print("|",board[0], '|',board[1], '|',board[2],"|")    # for each row in the board...
        print("-------------")
        print("|",board[3], '|',board[4], '|',board[5],"|") # print the row
        print("-------------")
        print("|",board[6], '|',board[7], '|',board[8],"|")
        print("+-----------+")
while True:
        spot = int(input("Choose a space from 0-8: "))

        if board[spot]!= 'X' and board[spot] != 'O':
                board[spot] = 'X'
        else:
                print("Sorry, pick another spot.")# this will check the spaces which the player can take/not take.
        printboard()
                                                
while True:
        opponent = random.randint(0,8)

        if board[opponent] != "o" and board[opponent] != "x":
                board[opponent] = "o"
        else:
                print("Sorry, pick another spot.")
                break
                

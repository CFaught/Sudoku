#########################################
#
# Author: Caleb Faught
#
# Date: 12/27/2015
#
# This script generates new sudoku
# grids (filled grids). to do: write
# the part that takes away numbers
# until the puzzle is still solvable
# and write a solver to check complexity
#########################################

import random

random.seed

grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
[4, 5, 6, 7, 8, 9, 1, 2, 3],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[2, 3, 4, 5, 6, 7, 8, 9, 1],
[5, 6, 7, 8, 9, 1, 2, 3, 4],
[8, 9, 1, 2, 3, 4, 5, 6, 7],
[3, 4, 5, 6, 7, 8, 9, 1, 2],
[6, 7, 8, 9, 1, 2, 3, 4, 5],
[9, 1, 2, 3, 4, 5, 6, 7, 8]]


def shuffleRows():
    # This section shuffles rows within the same block
    randNum = random.randint(0,8)
    if(randNum < 2):
        nextRand = random.randint(0, 2)
        if( randNum != nextRand):
            tmp = grid[randNum]
            grid[randNum] = grid[nextRand]
            grid[nextRand] = tmp
    elif(randNum < 5):
        nextRand = random.randint(2, 5)
        if( randNum != nextRand):
            tmp = grid[randNum]
            grid[randNum] = grid[nextRand]
            grid[nextRand] = tmp
    else:
        nextRand = random.randint(5, 8)
        if( randNum != nextRand):
            tmp = grid[randNum]
            grid[randNum] = grid[nextRand]
            grid[nextRand] = tmp


def shuffleCols():
    # This section shuffles columns within the same block
    randNum = random.randint(0,8)
    if(randNum < 2):
        nextRand = random.randint(0, 2)
        if( randNum != nextRand):
            for i in range(9):
                tmp = grid[i][randNum]
                grid[i][randNum] = grid[i][nextRand]
                grid[i][nextRand] = tmp
    elif(randNum < 5):
        nextRand = random.randint(2, 5)
        if( randNum != nextRand):
            for i in range(9):
                tmp = grid[i][randNum]
                grid[i][randNum] = grid[i][nextRand]
                grid[i][nextRand] = tmp
    else:
        nextRand = random.randint(5, 8)
        if( randNum != nextRand):
            for i in range(9):
                tmp = grid[i][randNum]
                grid[i][randNum] = grid[i][nextRand]
                grid[i][nextRand] = tmp

def printGrid():
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
            if((j + 1) % 3 == 0 and  j != 8):
                print("|", end="")

        print("", end="\n")
        if ( (i + 1) % 3 == 0 and i != 8):
            print("-------------------")

shuffle = random.randint(20, 30)
for i in range(shuffle):
    shuffleRows()
    shuffleCols()
printGrid()
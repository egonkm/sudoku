#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:08:34 2024

@author: egon
"""
import random 

random.seed(1)
SIZE = 9
board = [0]*(SIZE*SIZE)

def random_board(fill=10):

    board = [0]*(SIZE*SIZE)

    while fill>0:
        position = random.randint(0,SIZE*SIZE-1)
        number = random.randint(1,9)
        if not possible(board, position, number): continue
        board[position] = number
        fill = fill - 1

    return board

def possible(board, position, number): # is it possible to put number at position in board ?
    
    col = position % 9
    row = position // 9
        
    col_vals = (board[r*SIZE+col] for r in range(9))
    
    if number in col_vals: return False
    
    row_vals = (board[row*SIZE+c] for c in range(9))

    if number in row_vals: return False
    
    box_col = col // 3 
    box_row = row // 3 
    
    box_vals = (board[r*SIZE+c] for r in range(box_row*3, box_row*3+3)
                         for c in range(box_col*3, box_col*3+3))
    
    if number in box_vals: return False

    return True

def solve(board, max_solutions=10000):
    
    for free in range(SIZE*SIZE):
        if board[free] == 0: break

    q = [(board[:], free)] # queue with incomplete boards and at what position to continue to try
    tries = 1
    solutions  = []

    while q and (len(solutions)<max_solutions):

        if tries%100000==0: print(tries, len(q), len(solutions))
        tries += 1 

        #print("Len q:", len(q))

        board, position = q.pop()

        
        for number in range(1,10): # try to put numer 1 to 9 in position
            
            if possible(board, position, number):
                #print("Put", number, "in position", _pos)
                _board = board[:]
                _board[position] = number

                _position = position 
                while _position<SIZE*SIZE and _board[_position] != 0:
                    _position = _position+1

                if _position == SIZE*SIZE: # found a solution
                    #print("Solution:")
                    #print(_board)
                    solutions.append(_board)
                    continue
                    # return True, _board

                q.append( (_board, _position))
                
    return solutions, tries 

    
def print_board(board):
    
    for pos in range(SIZE*SIZE):
        
        if pos % 9==0: print("")
        print(board[pos],"\t", end="")
        
    print() 
    
        
if __name__ == "__main__":
    
    for fill in range(1,24): # how many numbers already in our board before we try to solve it ? 

        print("Fill:", fill)
        partial_board = random_board(fill)
        print_board(partial_board)
        s, tries = solve(partial_board, 1)
        for board in s: print_board(board)
        print(tries)
        # print(len(s))
    
    
    
    

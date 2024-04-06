#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:08:34 2024

@author: brengineer
"""

SIZE = 9
board = [0]*(SIZE*SIZE)

def possible(board, position, number):
    
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

def solve(board):
    
    q = [(board[:],0)]
    tries = 1

    while q:

        print(tries, len(q))
        tries += 1 

        #print("Len q:", len(q))

        board, position = q.pop()
        
        for number in range(1,10):
            
            if possible(board, position, number):
                #print("Put", number, "in position", _pos)
                _board = board[:]
                _board[position] = number
                _position = position + 1
                if _position == SIZE*SIZE: return True, _board

                q.append( (_board, _position))
                
    return False, _board 

    
def print_board(board):
    
    for pos in range(SIZE*SIZE):
        
        if pos % 9==0: print("")
        print(board[pos],"\t", end="")
        
    print() 
    
        
if __name__ == "__main__":
    
    c, board = solve(board)
    print_board(board)
    print(c)
    
    
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:08:34 2024

@author: brengineer
"""

SIZE = 9
board = [0]*(SIZE*SIZE)


def full(board):
    
    for x in board:
        if x == 0: return False
        
    return True
    
def find_position(board):
    
    for index, x in enumerate(board):
        if board[index]==0: return index
        
def choose_number(board, position):
    
    
    for number in range(1,10):
        
        if possible(board, position, number): return number
        
    return None

def possible(board, position, number):
    
    col = position % 9
    row = position // 9
        
    col_vals = [board[r*SIZE+col] for r in range(9)]
    
    if number in col_vals: return False
    
    row_vals = [board[row*SIZE+c] for c in range(9)]

    if number in row_vals: return False
    
    box_col = col // 3 
    box_row = row // 3 
    
    box_vals = [board[r*SIZE+c] for r in range(box_row*3, box_row*3+3)
                         for c in range(box_col*3, box_col*3+3)]
    
    if number in box_vals: return False

    return True

from random import shuffle

def solve(board):
    
 
    def solve_it(board, position):
        
        
        if position = SIZE*SIZE: return True  
        
        for number in range(1,10):
            
            if possible(board, position, number):
                board[position] = number 
                if solve_it(board, position+1): return True
            
        return solve_it(board, position-1)
    
    position = 0
    
    solve_it(board, position)
    
def print_board(board):
    
    for pos in range(SIZE*SIZE):
        
        if pos % 9==0: print("")
        print(board[pos],"\t", end="")
        
    print() 
    
        
if __name__ == "__main__":
    
    c = solve(board)
    print_board(board)
    print(c)
    
    
    
    
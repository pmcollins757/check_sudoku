# -*- coding: utf-8 -*-
"""
Author: Patrick Collins
"""
# Sudoku puzzle solution checker that takes as input 
# a square list of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square solution and returns the boolean False
# otherwise.

# A valid sudoku square solution satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# Assuming the the input is square and contains at
# least one row and one column.


correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]
             
incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

incorrect6 = [[0,1,2], 
              [2,0,1], 
              [1,2,0]]
               
def check_sudoku(puzzle):
    sqr_size = len(puzzle)
    column_puzzle = zip(*puzzle)
    for row in puzzle:
        for x in row:
            if not isinstance(x, int) or x > sqr_size or x < 1:
                return False
        if sum(row) != sum(set(row)):
            return False
    
    for column in column_puzzle:
        if sum(column) != sum(set(column)):
            return False
     
    return True               
    
    
print check_sudoku(correct), "True"
#>>> True
    
print check_sudoku(incorrect), "False"
#>>> False

print check_sudoku(incorrect2), "False2"
#>>> False

print check_sudoku(incorrect3), "False3"
#>>> False

print check_sudoku(incorrect4), "False4"
#>>> False

print check_sudoku(incorrect5), "False5"
#>>> False

print check_sudoku(incorrect6), "False6"
#>>> False

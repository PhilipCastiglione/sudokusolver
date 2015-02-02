"""
This file contains the framework for the Sudoku Solver program
"""

### import solving logic and python modules
from ss_solvers import *
import sys
import time

timestamp = time.time()

### check if debug mode set and define debugging functions (NB: run with argument debug for debug mode)
if len(sys.argv) != 2:
	debug_mode = False
else:
	script, debug_mode = sys.argv
	if not debug_mode == 'debug':
		print "debug_mode not set as expected."
		print "Exiting now."
		sys.exit()

def game_grid_print(message):
	""" This function prints the current game grid values to the console for 
	debugging. game_grid_ASCII_print is preferred UNLESS detailed content of
	unsolved cells is required."""
	print "~" * 20, message, "~" *20
	for key in rowcol_list:
		print key, game_grid[key]
	print '\n'

def game_grid_ASCII_print(message):
	""" This function prints the current game grid to the console in ASCII for 
	debugging."""
	print "~" * 20, message, "~" *20
	print '\n'
	print '-' * 41
	
	for rx in range (1,10):
		for cx in range (1,10):
			for item in rowcol_list:
				if item[3] == str(rx) and item[5] == str(cx):
					if len(game_grid[item]) == 1:
						print game_grid[item],
					else:
						print [0],
		print '\n'


### establish empty sudoku game grid as dictionary - key format 
### rxcx (row x, column x) - column format list w/ digits 1-9
game_grid = {}

rowcol_list = []

def rowcol_list_build(r1,r2,c1,c2,s):
	for rx in range(r1,r2):
		for cx in range(c1,c2):
			rowcol_list.append('s' + str(s) + 'r' + str(rx) + 'c' + str(cx))
			
rowcol_list_build(1,4,1,4,1)
rowcol_list_build(1,4,4,7,2)
rowcol_list_build(1,4,7,10,3)
rowcol_list_build(4,7,1,4,4)
rowcol_list_build(4,7,4,7,5)
rowcol_list_build(4,7,7,10,6)
rowcol_list_build(7,10,1,4,7)
rowcol_list_build(7,10,4,7,8)
rowcol_list_build(7,10,7,10,9)
		
for rowcol in rowcol_list:
	game_grid.update({rowcol: range(1,10)})

if debug_mode:
	game_grid_ASCII_print("Initial Game Grid")

### provide user input medium content
"""PLACEHOLDER"""

### receive user input for initial grid state and modify current game grid
""" For now I will enter the info directly based on a sample sudoku pre-prepared"""
from docs import sample_sudoku4

user_grid_input = sample_sudoku4.user_grid_input

for key in user_grid_input:
	game_grid[key] = [user_grid_input[key]]

if debug_mode:
	game_grid_ASCII_print("Modified Game Grid w/ user input")
	
"""add errors for incorrect input"""

### establish framework for solver logic tests and iterate through tests until 
### either success or not able to progress
complete = False
iteration = 0
	
while not complete:
	digits_before_solve = 0
	digits_after_solve = 0
	iteration += 1
	
	for key in game_grid:
		digits_before_solve += len(game_grid[key])
	
	if debug_mode:
		print digits_before_solve
		
	game_grid = Solve1(game_grid)
	game_grid = Solve2(game_grid)
	game_grid = Solve3(game_grid)
	game_grid = Solve4(game_grid)
	game_grid = Solve5(game_grid)
	
	for key in game_grid:
		digits_after_solve += len(game_grid[key])
		
	if debug_mode:
		print digits_after_solve
		game_grid_ASCII_print("Grid after iteration %d." % iteration)
		raw_input("press enter to continue:")
	
	"""add error for multiple x on one row/col/sq
	for i in range(1,10):
		for key in game_grid:
			if len(game_grid[key]) == 1 and"""
	
	if digits_before_solve == digits_after_solve:
		if debug_mode:
			game_grid_print("final details")
		print "Solve logic unable to progress Sudoku puzzle."
		print "Either starting grid entered incorrectly or the puzzle is not solvable."
		print "Exiting now."
		sys.exit()
	
	if digits_after_solve == 81:
		complete = True
		
### provide content to user in medium (solved grid or message)
"""PLACEHOLDER"""

timestamp = time.time() - timestamp
print "Sudoku solved after %d iterations in %f seconds." % (iteration, timestamp)

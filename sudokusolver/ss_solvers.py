def Solve1(starting_grid):
	"""First logical solve rule: for a given solved cell, all associated cells
	in the same column, row and grid square cannot contain the solved value."""
	solving_grid = starting_grid
	
	for key in solving_grid:
		square = key[0:2]
		row = key[2:4]
		col = key[4:6]
		
		if len(solving_grid[key]) == 1:
			
			for i in solving_grid:
				if i == key:
					pass
				elif row in i and solving_grid[key][0] in solving_grid[i]:
					solving_grid[i].remove(solving_grid[key][0])
				elif col in i and solving_grid[key][0] in solving_grid[i]:
					solving_grid[i].remove(solving_grid[key][0])
				elif square in i and solving_grid[key][0] in solving_grid[i]:
					solving_grid[i].remove(solving_grid[key][0])
				else:
					pass
					
	return solving_grid

def Solve2(starting_grid):
	"""Second logical solve rule: where a value is solved to be in a particular
	row or column within a square, all associated cells in the same row or
	column cannot contain the solved value."""
	solving_grid = starting_grid
	
	for digit_i in range(1,10):
		count_dict = {}
		
		for key in solving_grid:
			count_dict.update({key: solving_grid[key].count(digit_i)})
	
		for square_i in range(1,10):
			square_count = 0
			for key in count_dict:
				if 's'+str(square_i) in key:
					square_count += count_dict[key]

			def remove_square_solved_digit(grid_segment):
				for grid_segment_i in range(1,10):
					grid_segment_count = 0
					for key in count_dict:
						if grid_segment[0]+str(grid_segment_i) in key and 's'+str(square_i) in key:
							grid_segment_count += count_dict[key]
					if grid_segment_count == square_count:
						for i in solving_grid:
							if 's'+str(square_i) in i:
								pass
							elif grid_segment[0]+str(grid_segment_i) in i and digit_i in solving_grid[i]:
								solving_grid[i].remove(digit_i)
							else:
								pass
			
			remove_square_solved_digit('row')
			remove_square_solved_digit('column')
	
	return solving_grid

def Solve3(starting_grid):
	"""Third logical solve rule: where a value exists only once in a given row
	column or square, remove all the other values in that cell."""
	solving_grid = starting_grid
	
	for digit_i in range(1,10):
		count_dict = {}
		
		for key in solving_grid:
			count_dict.update({key: solving_grid[key].count(digit_i)})
		
		def solve_cell_in_segment(grid_segment):
			for segment_i in range(1,10):
				segment_count = 0
				for key in count_dict:
					if grid_segment[0]+str(segment_i) in key:
						segment_count += count_dict[key]
				if segment_count != 1:
					pass
				else:
					for i in solving_grid:
						if grid_segment[0]+str(segment_i) in i and digit_i in solving_grid[i]:
							solving_grid[i] = [digit_i]
		
		solve_cell_in_segment('square')
		solve_cell_in_segment('row')
		solve_cell_in_segment('column')

	return solving_grid

def Solve4(starting_grid):
	"""Fourth logical solve rule: where a row or column is solved to the point
	that a value is known to be in a particular grid square, other cells in that
	grid square cannot contain the solved value."""
	solving_grid = starting_grid
	
	for digit_i in range(1,10):
		count_dict = {}
		
		for key in solving_grid:
			count_dict.update({key: solving_grid[key].count(digit_i)})

		def clear_square_of_solved_segment(grid_segment):
			for segment_i in range(1,10):
				segment_count = 0
				for key in count_dict:
					if grid_segment[0]+str(segment_i) in key:
						segment_count += count_dict[key]
							
				for square_i in range(1,10):
					square_count = 0
					for key in count_dict:
						if grid_segment[0]+str(segment_i) in key and 's'+str(square_i) in key:
							square_count += count_dict[key]
									
					if square_count != segment_count:
						pass
					elif square_count == 1:
						pass
					else:
						for i in solving_grid:
							if 's'+str(square_i) in i and \
							not grid_segment[0]+str(segment_i) in i and \
							digit_i in solving_grid[i]:
								solving_grid[i].remove(digit_i)
		
		clear_square_of_solved_segment('row')
		clear_square_of_solved_segment('column')
							
	return solving_grid

def Solve5(starting_grid):
	"""Fifth logical solve rule: where x possibilities are solved to x cells in
	a given square, row or column, those digits cannot be possibilities 
	elsewhere in that same square, row or column."""
	solving_grid = starting_grid
		
	for key in solving_grid:
		if len(solving_grid[key]) == 1:
			pass
		else:
			square = key[0:2]
			row = key[2:4]
			col = key[4:6]
			temp_cell = solving_grid[key]
			temp_cell_length = len(solving_grid[key])
			
			def clear_segment_of_solved_cell_multiple(grid_segment):
				segment_cell_count = 0
				temp_segment_list = []
				
				for segment_key in solving_grid:
					if grid_segment not in segment_key:
						pass
					else:
						if solving_grid[segment_key] == temp_cell:
							segment_cell_count += 1
							temp_segment_list.append(segment_key)
				
				if segment_cell_count == temp_cell_length:
					for i in solving_grid:
						if i in temp_segment_list:
							pass
						elif grid_segment not in i:
							pass
						else:
							for digit_i in temp_cell:
								if digit_i in solving_grid[i]:
									solving_grid[i].remove(digit_i)
				else:
					pass
				
			clear_segment_of_solved_cell_multiple(square)
			clear_segment_of_solved_cell_multiple(row)
			clear_segment_of_solved_cell_multiple(col)

	return solving_grid
	
	
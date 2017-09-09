max_cost = float('inf')

def find_shortest_path(grid, row,col, cost):
	global max_cost
	if row == len(grid) and col == len(grid):


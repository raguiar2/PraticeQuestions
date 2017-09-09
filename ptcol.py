max_rows = 0


def get_count(matrix):
	global max_rows
	count = 0
	for row in matrix:
		if row == 'PPP':
			count += 1
	if count > max_rows:
		max_rows = count


def flip_col(index, matrix):
	for j in range(len(matrix)):
		row_str = list(str(matrix[j]))
		if row_str[index] == 'T':
			row_str[index] = 'P'
			matrix[j] =''.join(row_str)
		else:
			row_str[index] = 'T'
			matrix[j] = ''.join(row_str)



def find_flips(matrix,numflips):
	if numflips == 0:
		get_count(matrix)
		return
	# for each col in the matrix
	# flip the col
	# recursivley do the flips on new matrix but with flips minus one 
	num_cols = len(matrix[0])
	num_rows = len(matrix)
	for i in range(num_cols):
		temp_matrix = matrix
		flip_col(i,temp_matrix)
		find_flips(temp_matrix,numflips-1)
		


matrix = ['PPP','TPT','TTT']
numflips = 1
find_flips(matrix,numflips)
print(max_rows)
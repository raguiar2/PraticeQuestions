def zero_matrix(matrix):
	zerorows = set([])
	zerocols = set([])
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 0:
				if i not in zerorows and j not in zerocols:
					zerocols.add(j)
					zerorows.add(i)
					for x in range(len(matrix[i])):
						matrix[i][x] = 0
					for row in matrix:
						row[j] = 0
	print(matrix)


zero_matrix([
	[1,2],
	[0,1],
	[1,1]
	])
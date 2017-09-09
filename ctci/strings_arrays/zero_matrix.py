
def zero_row(matrix,row):
    matrix[row] = [0] * len(matrix[row])
def zero_col(matrix,col):
    for row in range(len(matrix)):
        print(matrix[row])
        print(col)
        matrix[row][col] = 0 
def zero_matrix(matrix):
    rows = []
    cols = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] ==0:
                zero_row(matrix,row)
                zero_col(matrix,col)
    print(matrix)

zero_matrix([[1,1,1],[1,0,0]])

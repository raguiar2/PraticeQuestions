

def rotate_matrix(matrix):
    start = 0
    end = len(matrix)-1
    while start < end:
        matrix[start],matrix[end] = matrix[end], matrix[start]
        start += 1
        end -= 1
    print(matrix)

rotate_matrix([[0,0],[0,0]])
rotate_matrix([[0,0],[0,1]])
rotate_matrix([[0,0,0],[0,0,0],[0,1,0]])


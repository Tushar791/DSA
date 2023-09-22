"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""
def mark_columns(matrix, col):

    for i in range(len(matrix)):
        if matrix[i][col] != 0:
            matrix[i][col] = -1

def mark_rows(matrix,row):
    for i in range(len(matrix[0])):
        if matrix[row][i] != 0:
            matrix[row][i] = -1


def set_matrix_to_zero(matrix):



    #capture the length of rows and columns in m and n
    m = len(matrix) # count columns
    n = len(matrix[0]) # count rows

    for i in range(m): #iterate over rows
        for j in range(n): #iterate over columns
            if matrix[i][j] == 0:
                mark_columns(matrix,j)
                mark_rows(matrix,i)
                print(matrix)
                

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 0



if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_matrix_to_zero(matrix)
    print(matrix)
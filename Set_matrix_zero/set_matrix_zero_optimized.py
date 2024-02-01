"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

time complexity - 2*O(n*m)

"""

def set_matrix_zero(matrix):
    n = len(matrix) # row count
    m = len(matrix[0]) #column count
    col0=1
    #caputure rows and cols that are 0 in 0th row and col for 0th col col0 is the marker
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    
    #set cols and rows to zero from(1,1) till (n-1,m-1)
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] =0

    # set 0th row and col to 0
    if matrix[0][0] == 0:
        for i in range(m):
            matrix[0][i] =0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] =0


    return matrix

if __name__ == "__main__":

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_matrix_zero(matrix)
    print(matrix)
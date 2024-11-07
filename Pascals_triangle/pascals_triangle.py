""" Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

Time complexity - O(n**2)

"""

def value_of_nth_row(row):
    ans,lst = 1,[1]
    for i in range(1,row):
        ans = ans*(row-i)
        ans = ans/(i)
        lst.append(int(ans))
    return lst

def pascal_triangle(num_rows):
    lst=[]
    if num_rows ==1:
        return [[1]]
    for i in range(1,num_rows+1):
        lst.append(value_of_nth_row(i))
    return lst

if __name__ == '__main__':
    print(pascal_triangle(5))




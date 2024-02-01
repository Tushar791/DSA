"""Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects
 of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]"""

"""
Time complexity = O(N)+O(N)
"""

def sort_three_digit(arr):
    d0,d1,d2 = 0,0,0
    for i in range(len(arr)):
        if arr[i] == 0:
            d0 +=1
        elif arr[i] == 1:
            d1 += 1
        elif arr[i] == 2:
            d2 += 1
    
    for i in range(0,d0):
        arr[i] = 0
    for j in range(d0,d1+d0):
        arr[j] = 1
    for k in range(d1+d0,d2+d1+d0):
        arr[k] = 2


if __name__ == "__main__":
    arr = [2,0,1]
    print(arr)
    sort_three_digit(arr)
    print(arr)
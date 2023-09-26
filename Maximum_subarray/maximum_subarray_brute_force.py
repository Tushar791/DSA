"""Given an integer array nums, find the subarray with the largest sum, and return its sum and subarray.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6,[4,-1,2,1]
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1,[1]
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23,[5,4,-1,7,8]
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23."""

""" 
Time compelexity = O(n^2)
Space complexity = O(1)
 """



import sys

def max_sub_array(arr):
    max = -(sys.maxsize)
    for i in range(len(arr)):
        sum =0
        for j in range(i, len(arr)):

            sum+=arr[j]

            if sum > max:
                max = sum
                start,end =i, j+1

    return (max, arr[start:end])


if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]

    sum_of_max_sub_array,sub_arr = max_sub_array(arr)
    print(sum_of_max_sub_array,sub_arr)

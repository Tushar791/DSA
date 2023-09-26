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
Time compelexity = O(n)
Space complexity = O(1)
"""
import sys 
def get_max_sum_subarr(arr):
    max,sum = -sys.maxsize,0
    start = 0
    for i in range(len(arr)):
        if sum < 0:
            sum = 0
            start = i
        sum+=arr[i]
        if sum > max:
            max = sum
            end = i
    return max,arr[start:end+1]


if __name__ == "__main__":
    arr = [5,4,-1,7,8]
    sum,subarr = get_max_sum_subarr(arr)
    print(sum, subarr)
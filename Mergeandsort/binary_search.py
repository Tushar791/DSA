"""Binary search

Time complexity - O(Log N)

"""

def binary_search( arr ,  target):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid+1
    return -1


arr = [1,3,4,6,8]
target = 6
print(binary_search(arr, target))





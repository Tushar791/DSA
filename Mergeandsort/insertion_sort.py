"""
Insertion sort

Time complexity - O(N**2)
"""
def insertion_sort(arr):

    for i in range(1, len(arr)):
        key= arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key

arr = [4,1,7,5,2,9,0]
insertion_sort(arr)
print(arr)
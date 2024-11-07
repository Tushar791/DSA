## time complexity O(n^2)

def twoSum( nums: list[int], target: int) -> list[int]:
    ### get length of an array and create double loop to check if two integers are matching
       nums_len = len(nums)
       for i in range(0,nums_len - 1):
           for j in range(i+1,nums_len):
               if nums[i] + nums[j] == target:
                   return [i,j]
       return []
    
if __name__ == "__main__":
    print(twoSum([3,2,4],6))
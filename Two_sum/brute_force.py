def twoSum( nums: List[int], target: int) -> List[int]:
       nums_len = len(nums)
       for i in range(0,nums_len - 1):
        for j in range(i+1,nums_len):
            if nums[i] + nums[j] == target:
                return [i,j]
        return []
    
if __name__ == "__main__":
    print(two_sum([3,2,4],6))
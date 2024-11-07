## time complexity O(2n)

def twoSum( nums: list[int], target: int) -> list[int]:
    ### get length and create empty dictionary
        nums_len = len(nums)
        nums_map = {}
    ### load values in dictionar
        for i in range(0,nums_len):
            nums_map[nums[i]] = i
    ### get compliment value by subtracting target - nums if found in nums_map return
        for i in range(0,nums_len):
            compliment = target - nums[i]
            if (compliment in nums_map) and nums_map[compliment] != i:
                return [i,nums_map[compliment]]
        return []        
    
if __name__ == "__main__":
    print(twoSum([3,2,4],6))
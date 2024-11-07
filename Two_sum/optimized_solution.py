## time complexity O(n)

def twoSum( nums: list[int], target: int) -> list[int]:
    ### get length and create empty dictionary
        nums_len = len(nums)
        nums_map = {}
            
    ### get compliment value by subtracting target - nums if found in nums_map return 
    ### else capture the value in dictionary 
        for i in range(0,nums_len):
            compliment = target - nums[i]
            if (compliment in nums_map) and nums_map[compliment] != i:
                return [nums_map[compliment],i]
            nums_map[nums[i]] = i
        return []        
    
if __name__ == "__main__":
    print(twoSum([3,2,4],6))
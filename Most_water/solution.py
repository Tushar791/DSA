def maxArea( height: list[int]) -> int:
    right,left,max_area = len(height)-1,0,0
    while left < right:
        if min(height[left],height[right])*(right-left) > max_area:
            max_area = min(height[left],height[right])*(right-left)
        
        if height[left] > height[right]:
            right -=1
        else:
            left +=1
        
    return max_area
        
        
    
    
if __name__ == "__main__":
    print(maxArea([1,2,1]))
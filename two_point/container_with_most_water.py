# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

from typing import List 

def two_point(nums: List[int]) -> int: 
    left, right = 0, len(nums) - 1
    area_biggest = 0 

    while left < right:
        width = right - left 
        h = min(nums[left], nums[right])
        
        area_current = h * width
        area_biggest = max(area_biggest, area_current)

        if nums[left] <= nums[right]: left += 1 
        else: right -= 1 

    return area_biggest 
    

if __name__ == "__main__": 
    nums = [1,8,6,2,5,4,8,3,7]
    print(two_point(nums))
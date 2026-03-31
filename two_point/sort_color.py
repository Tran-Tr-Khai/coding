# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Input: nums = [2,0,1]
# Output: [0,1,2]

from typing import List

# C1
# hashmap để tính số lượng. 
# Sau đó dùng tạo list bằng key * số lượng. 
def hash_map(nums: List[int]) -> List[int]: 
    pass 

# C2
# Dùng 2 con trỏ, duyệt một lần để sắp xếp một số đúng vị trí. Sau đó duyệt lần 2 để sắp xếp 2 số còn lại. 
# vis du: [2,0,2,1,1,0] -> [0, 1, 1, 0, 2, 2] -> [0, 0, 1, 1, 2, 2]

def two_pass_partition(nums: List[int]) -> List[int]: 
    l = 0 
    for r in range(len(nums)):
        if (nums[r] == 0): 
            nums[l], nums[r] = nums[r], nums[l]

            l += 1 
    
    # 
    # l_new = l 
    r = len(nums) - 1 
    for l in reversed(range(len(nums))):
        if (nums[l] == 2):
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1          
    # print(l)
    return nums


def two_point(nums: List[int]) -> List[int]: 
    left = 0
    mid = 0 
    right = len(nums) - 1
    while mid < right: 
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1 
            mid += 1 
        elif nums[mid] == 1: 
            mid += 1
        else: 
            nums[right], nums[mid] = nums[mid], nums[right]
            right -= 1

    return nums
        
if __name__ == "__main__":     
    nums = [2,0,2,1,1,0]
    print(two_pass_partition(nums)) 
    print(two_point(nums))


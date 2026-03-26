# [1, 2, 3, 1] -> true
from typing import List

def brute_force(nums: List[int]) -> bool:
    is_check = False
    for i in range(len(nums) - 1): 
        for j in range(i+1, len(nums)): 
            if nums[i] == nums[j]:
                is_check = True
                break
    return is_check
                

# time: O(n), space: O(n)
def hashset(nums: List[int]) -> bool: 
    is_check = False
    s = set() 
    for i in range(len(nums)):
        if nums[i] not in s: 
            s.add(nums[i])
        else: 
            is_check=True 
            break 

    return is_check

# time: O nlogn, space O(1)
def two_point(nums: List[int]) -> bool: 
    nums.sort()
    j = 1 
    is_check = False
    for i in range(len(nums)): 
        if nums[i] != nums[j]: 
            j += i 
        else: 
            is_check = True

    return is_check




if __name__ == "__main__":
    nums = [1, 2, 3, 1] 
    print(brute_force(nums))

    print(hashset(nums))

    print(two_point(nums))
# time: O (logn), space: O(1)
# Chia để trị

def binary_search_rotate(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right - left) // 2

        if nums[mid] >= nums[left]: 
            if nums[left] <= target < nums[mid]: 
                right = mid - 1
            else:
                left = mid + 1
        else: 
            if nums[mid] < target <= nums[right]: 
                left = mid + 1 
            else: 
                right = mid - 1 
    return -1 


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 8, 0, 1, 2]
    target = 3
    print(binary_search_rotate(nums, target)) 
    
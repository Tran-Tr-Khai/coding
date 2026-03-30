# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

from typing import List

def three_sum_two_point(nums: List[int]) -> List[List[int]]:
    # Sort mảng để xác định được vị trí con trỏ cần chạy không sort cần phải duyệt tất cả
    nums.sort() # In-place sort để tối ưu bộ nhớ
    res = []
    n = len(nums)

    for i in range(n):
        # Nếu số đầu tiên > 0, tổng 3 số dương không bao giờ = 0
        if nums[i] > 0: break
        
        # Bỏ qua i trùng lặp (chốt chặn 1)
        if i > 0 and nums[i] == nums[i-1]:
            continue # Bỏ qua công đoạn tính bên dưới để sang vòng lặp tiếp theo

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # Tìm thấy bộ ba!
                res.append([nums[i], nums[left], nums[right]])
                
                # Bỏ qua left/right trùng lặp (Chốt chặn 2)
                # Phải di chuyển ít nhất 1 bước trước đã
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    
    return res

def three_sum_brute_force(nums):
    res = set() # Dùng set để tự động loại bỏ các bộ ba trùng nhau
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort bộ ba trước khi bỏ vào set để [-1, 0, 1] giống [0, -1, 1]
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    res.add(triplet)
                    
    return [list(t) for t in res]


def three_sum_hash_set(nums):
    # a + b + c = 0 -> b + c = -a -> c = -a - b 
    # Chuyển dạng bài toán thành two sum quen thuộc
    res = set()
    
    nums.sort() # sort 
    for i in range(len(nums)): 
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i] # b + c = -a
        seen = set() # Để tìm giá trị 
        for j in range(i + 1, len(nums)): 
            c = target - nums[j] # c = -a - b 
            if c in seen: 
                res.add((nums[i], c, nums[j])) # Không thế dùng set(list()) vì list không bất biến nên gây ra lõi cho chường trình
            seen.add(nums[j])

    return [list(i) for i in res]


if __name__ == "__main__": 
    nums = [-1,0,2,-1, 1, -4]
    print(three_sum_two_point(nums))
    print(three_sum_hash_set(nums))
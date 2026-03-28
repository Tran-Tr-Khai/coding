# Input: nums = [100,4,200,1,3,2]
# Output: 4

from typing import List
# C1: 
# Dùng hashet để tránh trùng lặp 
# Add tất cả giá trị chưa có vào hashset 
# Sắp xếp 
# Check i vs i + 1 -> result 

# Time: Sort O(nlogn), Space: O(1)
def hashset(nums: List[int]) -> int:
    if not nums: return 0
    l = sorted(list(set(nums))) 
    
    max_streak = 1
    current_streak = 1

    for i in range(len(l) - 1):
        if l[i + 1] == l[i] + 1:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 1
        
    return max(max_streak, current_streak)


# C2: 
# Vẫn dùng hashet nhưng lần này ta sẽ dùng toán tử in + hashset để thể hiện sức mạnh của hashset
# Dùng 1 cờ để tìm ra số đứng trước liên tiêp nhỏ nhất 
# Khi tìm thấy được số nhỏ nhất ta sẽ duyệt qua set nhờ sức mạnh của toán tử in trong set để tìm các số liên tiếp lớn hơn. 

def hashset_pro(nums: List[int]) -> int: 
    if not nums: return 0
    num_set = set(nums)
    longest_streak = 1
    for num in num_set: 
        if num - 1 not in num_set: 
            current_num = num 
            current_streak = 1


            while current_num + 1 in num_set: 
                current_num += 1 
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)


    return longest_streak

if __name__ == "__main__": 
    nums = [100,4,200,1,3,2]
    print(hashset_pro(nums))



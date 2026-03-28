# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# hashmap,  
from typing import List

def hashmap(nums: List[int], k: int) -> List[int]: 
    ht = {}
    for i in nums:
        if i not in ht:
            ht[i] = 1
        else: 
            ht[i] += 1
        # ht[i] = ht.get(i, 0) + 1 # Lấy giá trị cũ (nếu không có thì mặc định là 0) rồi cộng 1, pythonic 


    # Chuyển HashMap thành một danh sách các cặp (Số, Tần suất) vì dictionary không thê sắp xếp
    items = list(ht.items()) 
    # Kết quả: [(1, 3), (2, 2), (3, 1)]

    # Sắp xếp danh sách này theo Tần suất (giảm dần)
    items.sort(key=lambda x: x[1], reverse=True) # lambda input: output, sort(key, reverse) nếu trong list không phải giá trị single 

    # Lấy k phần tử đầu tiên và chỉ lấy cái "Số" (Key)
    result = [items[i][0] for i in range(k)]

    return result 

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3] 
    print(hashmap(nums, 2))
# Mô tả: Thiết kế một class KthLargest để tìm phần tử lớn thứ $k$ trong một luồng dữ liệu (stream). 
# Lưu ý rằng đây là phần tử lớn thứ $k$ theo thứ tự đã sắp xếp, không phải là phần tử duy nhất thứ $k$.
# Class cần hỗ trợ các phương thức sau:
# KthLargest(int k, int[] nums): Khởi tạo đối tượng với số nguyên $k$ và mảng số nguyên ban đầu nums.
# int add(int val): Thêm một giá trị mới val vào luồng dữ liệu và trả về phần tử lớn thứ $k$ hiện tại của toàn bộ luồng.
# Ví dụ minh họa
# Input:["KthLargest", "add", "add", "add", "add", "add"][[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output:[null, 4, 5, 5, 8, 8]

# Bài toán này thường sử dụng trong top thình hành xem videos 

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k  
        self.heap = nums 
        heapq.heapify(self.heap)
        
        # Vì mình chỉ cần tìm phần tử lớn thứ k, 
        # nên tủ lạnh chỉ cần giữ lại đúng k thằng lớn nhất thôi.
        # Thằng nào nhỏ quá thì bỏ đi.
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
    

# import heapq

# # Khởi tạo "bộ nhớ" ở ngoài hàm (Global)
# _k = 0
# _heap = []

# def init_kth_largest(k, nums):
#     global _k, _heap
#     _k = k
#     _heap = nums
#     heapq.heapify(_heap)
#     while len(_heap) > k:
#         heapq.heappop(_heap)

# def add_to_stream(val):
#     global _heap, _k
#     heapq.heappush(_heap, val)
#     if len(_heap) > _k:
#         heapq.heappop(_heap)
#     return _heap[0]

# # Sử dụng
# init_kth_largest(3, [4, 5, 8, 2])
# print(add_to_stream(3)) # Output: 4

# import heapq

# def add_to_stream_functional(val, current_heap, k):
#     """
#     Hàm này không 'nhớ' gì cả, 
#     bạn phải đưa 'k' và 'current_heap' cho nó xử lý.
#     """
#     heapq.heappush(current_heap, val)
#     if len(current_heap) > k:
#         heapq.heappop(current_heap)
#     return current_heap[0], current_heap # Trả về kết quả và mảng đã cập nhật

# # Sử dụng
# k = 3
# my_heap = [4, 5, 8, 2]
# heapq.heapify(my_heap)
# while len(my_heap) > k:
#     heapq.heappop(my_heap)

# # Mỗi lần add là phải truyền my_heap vào và nhận my_heap mới ra
# res, my_heap = add_to_stream_functional(3, my_heap, k)
# print(res)

if __name__ == "__main__": 
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    
    # 2. Gọi hàm add liên tục và in kết quả
    print(f"Add 3: {kthLargest.add(3)}")   # Output: 4
    print(f"Add 5: {kthLargest.add(5)}")   # Output: 5
    print(f"Add 10: {kthLargest.add(10)}") # Output: 5
    print(f"Add 9: {kthLargest.add(9)}")   # Output: 8
    print(f"Add 4: {kthLargest.add(4)}")   # Output: 8
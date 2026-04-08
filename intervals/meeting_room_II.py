# Đề bài: Meeting Rooms II
# Cho một mảng các khoảng thời gian diễn ra cuộc họp intervals, trong đó mỗi cuộc họp được biểu diễn bằng một mảng gồm thời gian bắt đầu và kết thúc: intervals[i] = [start_i, end_i].
# Hãy tìm số lượng phòng họp tối thiểu cần thiết để có thể tổ chức tất cả các cuộc họp này mà không bị trùng lặp. (Hay nói cách khác: Tại thời điểm đông đúc nhất, có bao nhiêu cuộc họp đang diễn ra cùng lúc?)

# Ví dụ minh họa
# Ví dụ 1:
# Input: intervals = [[0, 30], [5, 10], [15, 20]]
# Output: 2

# Giải thích:
# Cuộc họp 1 [0, 30] bắt đầu. Ta cần mở Phòng 1.
# Cuộc họp 2 [5, 10] bắt đầu. Lúc này Phòng 1 đang bận (vì đến phút 30 mới xong), nên ta bắt buộc phải mở thêm Phòng 2. (Đang dùng 2 phòng).
# Cuộc họp 3 [15, 20] bắt đầu. Lúc này, cuộc họp 2 (ở Phòng 2) đã kết thúc từ phút thứ 10. Do đó, Phòng 2 đã trống và ta có thể xếp cuộc họp 3 vào Phòng 2.
# Tổng kết: Chỉ cần thuê tối đa 2 phòng là đủ chỗ cho tất cả.

# Ví dụ 2:
# Input: intervals = [[7, 10], [2, 4]]
# Output: 1
# Giải thích: Hai cuộc họp không hề đụng nhau. Xếp cuộc họp [2, 4] vào Phòng 1. Đợi họp xong, phòng trống, ta tiếp tục cho cuộc họp [7, 10] dùng lại Phòng 1. Chỉ cần 1 phòng duy nhất.

import heapq
# Time: O(nlogn), space: O(n
def minHeap(intervals: list[list[int]]) -> int:
    if not intervals: return 0
    intervals.sort(key=lambda x: x[0])
    rooms_heap = []
    heapq.heappush(rooms_heap, intervals[0][1])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= rooms_heap[0]:
            heapq.heappop(rooms_heap)
        heapq.heappush(rooms_heap, intervals[i][1])
        
    return len(rooms_heap)


# Time: O(nlogn), space: O(n)
def twoPointer(intervals: list[list[int]]) -> int: 
    if not intervals: return 0
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    s_ptr = 0
    e_ptr = 0
    used_rooms = 0

    while s_ptr < len(intervals): 
        if starts[s_ptr] < ends[e_ptr]: 
            used_rooms += 1 
            s_ptr += 1 
        else: 
            s_ptr += 1
            e_ptr += 1
        
    return used_rooms


if __name__== "__main__": 
    intervals = [[0, 30], [5, 10], [15, 20]]
    intervals_2 = [[7, 10], [2, 4]]
    intervals_3 = [[0, 10], [5, 20], [11, 15]] # trường hợp bẫy nếu làm theo bài toán meeting_room_II.py
    print(twoPointer(intervals))
    print(twoPointer(intervals_2))
    print(twoPointer(intervals_3))
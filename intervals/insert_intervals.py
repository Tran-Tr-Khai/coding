# Đề bài: 
# Chèn Khoảng (Insert Interval) Cho một danh sách các khoảng thời gian không chồng lấn intervals, 
# trong đó mỗi khoảng được biểu diễn bởi $intervals[i] = [start_i, end_i]$. 
# Danh sách này đã được sắp xếp theo thứ tự tăng dần của $start_i$.
# Bạn cũng được cho một khoảng mới là newInterval = [start, end].
# Nhiệm vụ: Chèn newInterval vào danh sách intervals sao cho danh sách vẫn được sắp xếp 
# theo thứ tự tăng dần của các điểm bắt đầu và không có các khoảng nào bị chồng lấn lên nhau. 
# Nếu có sự chồng lấn, bạn phải hợp nhất (merge) chúng lại thành một khoảng duy nhất.

# Ví dụ 1:
# Đầu vào: intervals = [[1,3], [6,9]], newInterval = [2,5]
# Đầu ra: [[1,5], [6,9]] Giải thích: Khoảng [2,5] chồng lên [1,3], nên chúng được hợp nhất thành [1,5].
# Ví dụ 2:
# Đầu vào: intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]], newInterval = [4,8]
# Đầu ra: [[1,2], [3,10], [12,16]] Giải thích: Khoảng mới [4,8] chồng lấn lên các khoảng [3,5], [6,7], [8,10]. 
# Khi hợp nhất lại, ta được [3,10].


def insert_intervals(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]: 
    results = []
    inserted = False 
    
    for i in range(len(intervals)): 
        if intervals[i][1] < new_interval[0]: 
            results.append(intervals[i])
        elif intervals[i][0] > new_interval[1]: 
            if not inserted:
                results.append(new_interval)
                inserted = True
            results.append(intervals[i])
        else: 
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
    if not inserted: 
        results.append(new_interval)
        
    return results

if __name__ == "__main__": 
    intervals1 = [[1,3], [6,9]]
    new_interval1 = [2,5]
    print(insert_intervals(intervals1, new_interval1)) 

    intervals2 = [[1,2], [3,5], [6,7], [8,10], [12,16]]
    new_interval2 = [4,8]
    print(insert_intervals(intervals2, new_interval2))
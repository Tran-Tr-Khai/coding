# 📝 Đề bài: Hợp nhất các phiên (Merge Intervals)
# Bối cảnh: 
# Giả sử bạn có một danh sách các khoảng thời gian (intervals) đại diện cho các phiên hoạt động của người dùng trên hệ thống. 
# Một số phiên có thể bị chồng lấn (overlap) hoặc nối tiếp nhau do lỗi ghi log hoặc người dùng mở nhiều tab cùng lúc.
# Yêu cầu: Cho một mảng các khoảng thời gian intervals, 
# trong đó $intervals[i] = [start_i, end_i]$. 
# Hãy hợp nhất tất cả các khoảng thời gian chồng lấn và trả về một mảng các khoảng thời gian không chồng lấn, 
# bao phủ toàn bộ các khoảng thời gian ban đầu.

# 📥 Ví dụ 1:
# Đầu vào: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Đầu ra: [[1,6],[8,10],[15,18]]
# Giải thích: Vì khoảng [1,3] và [2,6] chồng lấn nhau (số 2 nằm giữa 1 và 3), nên chúng được hợp nhất thành [1,6].

# 📥 Ví dụ 2:
# Đầu vào: intervals = [[1,4],[4,5]]
# Đầu ra: [[1,5]]
# Giải thích: Khoảng [1,4] và [4,5] được coi là chồng lấn tại điểm 4.

def merge_intervals (intervals: list[list[int]]) -> list[list[int]]: 
    results = []
    # if mảng không tăng dần ta cần sort lại vì nếu không sort ta không thể thực hiện append trong list
    # mà cần kiểm tra với giá trị đã append trước đó thì khi kiểm tra trong list sẽ tôn O(n) time 
    # bài toán time O(n^2)
    intervals.sort(key = lambda x: x[0])

    results.append(intervals[0])  
    for i in range(1, len(intervals)):
        if intervals[i][0] > results[-1][1]: 
            results.append(intervals[i])
        else: 
            results[-1][1] = max(results[-1][1], intervals[i][1])

    return results




if __name__ == "__main__": 
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals_2 = [[1,4],[4,5]]

    print(merge_intervals(intervals))
    
    print(merge_intervals(intervals_2))

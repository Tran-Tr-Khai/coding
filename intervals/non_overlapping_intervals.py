# Đề bài: Non-overlapping Intervals
# Mô tả:
# Cho một mảng các khoảng (intervals) intervals, trong đó mỗi phần tử intervals[i] = [start_i, end_i] 
# đại diện cho một khoảng thời gian hoặc không gian bắt đầu từ start_i và kết thúc tại end_i.
# Nhiệm vụ của bạn là trả về số lượng tối thiểu các khoảng cần phải loại bỏ để các khoảng còn lại 
# trong mảng không bị chồng chéo (giao nhau) với nhau.
# Lưu ý: Hai khoảng có chung một điểm mút (ví dụ: [1, 2] và [2, 3]) thì không được coi là chồng chéo nhau.

# Ví dụ minh họa
# Ví dụ 1:
# Input: intervals = [[1,2], [2,3], [3,4], [1,3]]
# Output: 1
# Giải thích: Bạn chỉ cần loại bỏ khoảng [1,3] để các khoảng còn lại là [[1,2], [2,3], [3,4]]
# hoàn toàn không bị chồng chéo.

# Ví dụ 2:
# Input: intervals = [[1,2], [1,2], [1,2]]
# Output: 2
# Giải thích: Bạn cần loại bỏ hai khoảng [1,2] để khoảng [1,2] còn lại duy nhất không bị chồng chéo với bất kỳ khoảng nào khác.

# Ví dụ 3:
# Input: intervals = [[1,2], [2,3]]
# Output: 0
# Giải thích: Các khoảng đã cho vốn dĩ không bị chồng chéo, do đó bạn không cần phải loại bỏ khoảng nào.

def greedy(intervals: list[list[int]]) -> int: 
    intervals.sort(key = lambda x: x[1])
    deleted = 0
    prev_end = intervals[0][1]
    for i in range(1, len(intervals)): 
        if intervals[i][0] < prev_end: 
            deleted += 1
        else: 
            intervals[i][1] = prev_end 
    return deleted



if __name__ == "__main__": 
    intervals = [[1,2], [2,3], [3,4], [1,3]]
    intervals2 = [[1,2], [1,2], [1,2]]
    intervals3 = [[1,2], [2,3]]
    intervals4 = [[1, 4], [3, 5], [4, 6]] # prev_end 
    print(greedy(intervals))
    print(greedy(intervals2))
    print(greedy(intervals3))
    print(greedy(intervals4))
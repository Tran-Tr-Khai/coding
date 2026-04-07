# Đề bài: Meeting Rooms
# Cho một mảng các khoảng thời gian diễn ra cuộc họp intervals, trong đó mỗi cuộc họp được biểu diễn bằng một mảng gồm thời gian bắt đầu và kết thúc: intervals[i] = [start_i, end_i].
# Hãy xác định xem một người có thể tham dự tất cả các cuộc họp hay không (tức là không có bất kỳ khoảng thời gian nào của các cuộc họp bị chồng chéo lên nhau).
# Ví dụ minh họa.

# Ví dụ 1:
# Input: intervals = [[0,30], [5,10], [15,20]]
# Output: false
# Giải thích: Cuộc họp đầu tiên kéo dài từ phút thứ 0 đến phút thứ 30. Cuộc họp thứ hai (5 đến 10) và thứ ba (15 đến 20) đều diễn ra trong lúc cuộc họp đầu tiên chưa kết thúc. Do có sự xung đột lịch trình, người này không thể tham gia tất cả các cuộc họp.

# Ví dụ 2:
# Input: intervals = [[7,10], [2,4]]
# Output: true
# Giải thích: Cuộc họp thứ nhất diễn ra từ 2 đến 4, cuộc họp thứ hai từ 7 đến 10. Hai khoảng thời gian này hoàn toàn độc lập và không giao nhau, nên có thể tham gia cả hai.


# sorting và so sánh mốc
def giaithuat(intervals: list[list[int]]) -> bool:
    if len(intervals) <= 1:
        return True
    intervals.sort(key=lambda x: x[0])
    end = intervals[0][1]
    for i in range(1, len(intervals)): 
        if intervals[i][0] >= end: end = intervals[i][1]
        else: return False
    return True




if __name__ == "__main__": 
    intervals = [[0,30], [5,10], [15,20]] # -> [[0,30], [5,10],[15,20]]
    intervals_2 = [[7,10], [2,4]]
    print(giaithuat(intervals))
    print(giaithuat(intervals_2)) 



# time: O(log m + log n), space: O(1)
def binary_search_2d(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    
    ROWS, COLS = len(matrix), len(matrix[0])
    
    # Ta dùng Binary Search trên cột đầu tiên (index 0 của mỗi dòng)
    top, bot = 0, ROWS - 1
    row_idx = -1
    
    while top <= bot:
        mid = (top + bot) // 2
        if target < matrix[mid][0]:
            bot = mid - 1
        elif target > matrix[mid][-1]: # So sánh với phần tử CUỐI của dòng mid
            top = mid + 1
        else:
            # Target nằm trong khoảng của dòng mid
            row_idx = mid
            break
            
    if row_idx == -1: 
        return False # Không tìm thấy dòng nào thỏa mãn

    # Tìm target trong dòng đã chọn (row_idx) ---
    left, right = 0, COLS - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[row_idx][mid] == target:
            return True
        elif matrix[row_idx][mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False


# time: O(log m x n), space: O(1)
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix: return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, (m * n) - 1 # Coi như một mảng dài m * n phần tử
    
    while left <= right:
        mid = (left + right) // 2
        # Biến đổi chỉ số phẳng thành chỉ số 2D
        mid_val = matrix[mid // n][mid % n]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(binary_search_2d(matrix, target=3))  # True
    print(binary_search_2d(matrix, target=13)) # False

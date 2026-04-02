def sliding_window_hashmap(s: str, k: int) -> int: 
    count = {} 
    L = 0
    res = 0 
    max_freq = 0 
    for R in range(len(s)): 
        count[s[R]] = 1 + count.get(s[R], 0)
        max_freq = max(max_freq, count[s[R]])

        if (R - L + 1) - max_freq > k: 
            count[s[L]] -= 1 # Trượt để tìm giá trị chính xácc 
            L += 1 

    
    return count, max_freq, L, R





# Kinh nghiệm: 
# Tư duy theo "Trạng thái" (Invariants) thay vì "Hành động" (Actions)
# Sai lầm: Nghĩ về hành động ("Mình sẽ đổi chữ B này thành A").
# Tiến bộ: Nghĩ về điều kiện cần duy trì ("Cửa sổ này có đủ điều kiện để tồn tại không?").
# Mẹo: Mỗi khi gặp bài toán cho phép "thay đổi", "xóa" hoặc "chèn" $k$ lần, 
# hãy chuyển nó ngay thành bài toán "Tìm đoạn dài nhất thỏa mãn điều kiện X". 
# Đừng thực hiện hành động đó, hãy coi $k$ là một loại tài nguyên tiêu hao.


if __name__ == "__main__": 
    s = "AABABBA"
    k = 1
    print(sliding_window_hashmap(s, k))
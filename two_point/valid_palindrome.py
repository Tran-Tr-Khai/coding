# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Hàm	          Mục đích	            Cách dùng phổ biến
# re.sub()	      Thay thế / Xóa	    Dùng để xóa ký tự đặc biệt, chuẩn hóa text. (sub = substitute)
# re.findall()	  Trích xuất	        Tìm tất cả số điện thoại, email, mã đơn hàng trong một văn bản.
# re.search()	  Kiểm tra	            Xem trong chuỗi có chứa mẫu (pattern) nào đó không.

# \d: Là con số (digit).
# \w: Là chữ cái và số (word character - tương đương isalnum).
# \s: Là khoảng trắng (space).
# ^: Phủ định (Nếu nằm trong ngoặc vuông [^...]).

import re

# time: O(n),  space: O(1)

def two_point(s: str) -> bool:
    # space O(1)
    s_clean = "".join(c.lower() for c in s if c.isalnum())
    # s_clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # dùng re.sub sẽ tạo ra một chuỗi mới thì space: O(n)

    j = len(s_clean) - 1 
    for i in range(len(s_clean)): 
        if (i <= j):
            if s_clean[i] != s_clean[j]: 
                return False        
            j -= 1 
        else: break 

    return True



if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    u = "amanaplanacanalpanama" 
    print(len(u))
    # amanaplanacanalpanama 
    print(two_point(s))
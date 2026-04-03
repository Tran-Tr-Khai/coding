# stack (last in first out)
# operations: 
# push(): thêm vào đầu
# pop(): lấy phần tử ra 
# peak(): Truy cập phần tử top 


# time: O(n), space: O(1)
def stack(s: str) -> bool:
    stack = []
    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)

        else: 
            if not stack: return False
            
            top = stack.pop()
            if c == ")" and top != "(":
                return False
            if c == "]" and top != "[":
                return False
            if c == "}" and top != "{":
                return False
    return True 

# Cách nây dùng co dự án mở rộng

# time: O(n), space: O(1) (Dựa vào số ký tự tồn tại trong string)
def stack_hashmap(s: str) -> bool:
    mapping = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c in mapping: 
            top = stack.pop() if stack else "k"
            if top != mapping[c]: 
                return False 
        else: 
            stack.append(c)


    return not stack # Kiểm tra stack còn dư không, 
                     # không return true đưuọc vì nếu string gồm dấu ngoặc mở 
                     # Mã sẽ không vào kiểm tra chỗ False

    


if __name__  == "__main__": 
    s = "()[]{}"
    s1 = "([)]"
    print(stack_hashmap(s))


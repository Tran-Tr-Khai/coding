# Evaluate Reverse Polish Notation 
# Example
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


# Nên tách thành số với kí hiêu thành 2 mảng -> sai 
# Gặp toán tử thì lấy ra số ví dụ gặp phép cộng thì lấy ra "9"

def stack(tokens: str) -> int: 
    stack = []
    for token in tokens: 
        if token in "+-*/": 
            # Lấy 2 số hạng ra khỏi stack
            # Lưu ý: số lấy ra trước là số hạng thứ hai (b)
            b = stack.pop()
            a = stack.pop()

            if token == '*': 
                stack.append(a * b) 
            if token == '+': 
                stack.append(a + b) 
            if token == '-': 
                stack.append(a - b) 
            if token == '/': 
                stack.append(int(a / b))
        else: 
            stack.append(int(token))

    return stack



if __name__ == "__main__": 
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(stack(tokens))
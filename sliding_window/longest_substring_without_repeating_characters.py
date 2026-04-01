# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# longest streak

def hashset_while(s: str) -> int:
    char_set = set()
    left = 0
    longest_streak = 0
    for right in range(len(s)):
        while s[right] in char_set: # Tạo 1 vòng lặp để xóa giá trị trong chuỗi và tịnh tiến left
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        
        longest_streak = max(longest_streak, right - left + 1)
        
    return longest_streak

def hashset(s: str) -> int: 
    char_set = set()
    left = 0
    right = 0
    longest_streak = 0
    n = len(s)

    while right < n:
        if s[right] not in char_set:
            char_set.add(s[right])
            right += 1
            longest_streak = max(longest_streak, right - left)
        else:
            char_set.remove(s[left])
            left += 1
            
    return longest_streak

def hashmap(s: str) -> int:
    char_map = {} # Lưu {ký tự: index}
    left = 0
    longest_streak = 0
    
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        
        char_map[s[right]] = right
        longest_streak = max(longest_streak, right - left + 1)
        
    return longest_streak

# Sliding Window (Map)

if __name__ == "__main__": 
    s1, s2, s3 = 'abcabcbb', 'bbbbb', 'pwwkew'
    print(f"Test 1: {hashset(s1)}") # Output: 3
    print(f"Test 2: {hashset(s2)}") # Output: 1
    print(f"Test 3: {hashset(s3)}") # Output: 3
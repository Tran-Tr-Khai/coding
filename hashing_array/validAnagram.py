# s = "anagram", t = "nagaram" -> True 
# 
# time O(n), space O(n)
def hashmap(s: str, t:str) -> bool:
    is_check = False
    if (len(s) != len(t)):
        return is_check
    
    counter = {}
    for char in s: 
        if char in counter: 
            counter[char] += 1
        else: 
            counter[char] = 1
    for char in t:
        if char != counter[char] and counter[char] == 0: 
            return False   
        counter[char] -= 1
    return True

# 
from collections import Counter
# s = "anagram"
# print(Counter(s))
# # Kết quả: Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})
def pythonic(s: str, t: str) -> bool: 
    return Counter(s) == Counter(t)


def sort(s, t):
    return sorted(s) == sorted(t)




if __name__ == "__main__": 
    s = "anagram"
    t = "nagaram"
    print(hashmap(s, t))
    print(pythonic(s, t))
    print(sort(s, t))
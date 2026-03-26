# nums = [7, 8, 3, 7],  k = 14

# C1: brute force (time: O(n^2), space: O(1))
def brute_force(nums, k): 
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k: 
                return nums[i], nums[j] # Tra ve tuple 
    return None

# C2: hashset (time: O(n), space: O(n))
def hashset(nums, k): 
    s = set()
    for i in range(len(nums)): 
        if k - nums[i] in s: 
            return k-nums[i], nums[i]
        s.add(nums[i])
    return None
 
# C3: Two point (Time: O(nlogn), space: 0(1))
# O(nlogn) la mang chua sort. Neu sort roi se la O(n). 
def two_point(nums, k): 
    nums = sorted(nums) # [3, 7, 7, 8]
    i = 0 
    j = len(nums) - 1; 
    while (i < j): 
        if (nums[i] + nums[j] == k): 
            return nums[i], nums[j]
        if (nums[i] + nums[j] < k): 
            i+=1
        else: 
            j-=1 

    return None

    
if __name__ == "__main__": 
    nums = [7, 8, 3, 7]
    k = 14
    print(brute_force(nums, k))
    print(hashset(nums, k))
    print(two_point(nums, k))
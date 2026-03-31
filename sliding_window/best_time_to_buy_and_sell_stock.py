# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

from typing import List
# Dùng 2 con trỏ bởi vì bài toán không tính đến lợi nhuận khi mua ở mỗi ngày. Nên ta chỉ cần biết max, min được rồi
# Đầu tiên ta cần kiểm tra giá trị nhỏ nhất. -> lưu vào con trỏ min.
# Sau đó ta duyệt kiếm lơi -> lưu vào con trỏ max  



def sliding_window (nums: List[int]) -> int: 
    min_idx = 0
    max_idx = 1 
    profit_max = 0
    while max_idx < len(nums):
        if (nums[max_idx] < nums[min_idx]): 
            min_idx = max_idx
        else:
            profit_cur = nums[max_idx] - nums[min_idx]
            profit_max = max(profit_cur, profit_max)
        max_idx += 1
    return profit_max



if __name__ == "__main__": 
    nums = [7,1,5,3,6,4]
    print(sliding_window(nums))
    
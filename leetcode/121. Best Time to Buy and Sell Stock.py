from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profits = {}
#         length = len(prices)
#         for i in range(length):
#             for j in range(i + 1, length):
#                 profit = prices[j] - prices[i]
#                 if profit > 0:
#                     if profits.get(i) is None or profit > profits.get(i):
#                         profits.update({i: profit})
#         if not profits:
#             return 0
#         return max(profits.values())
# Time Limit Exceeded


class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit


print(Solution().maxProfit([7,6,4,3,1]))
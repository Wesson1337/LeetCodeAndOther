from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path: List[int]):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not nums[i] in path:
                    backtrack(path + [nums[i]])
        backtrack([])
        return res

print(Solution().permute([1, 2, 3]))


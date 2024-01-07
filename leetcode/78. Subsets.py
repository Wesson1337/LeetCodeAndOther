from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(s: int, path: List[int]):
            res.append(path)
            for i in range(s, len(nums)):

                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res


print(Solution().subsets([0]))
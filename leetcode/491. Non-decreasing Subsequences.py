from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(s: int, path: List[int]):
            if len(path) > 1:
                res.append(path)

            used = set()

            for i in range(s, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    backtrack(i + 1, path + [nums[i]])
        backtrack(0, [])
        return res

print(Solution().findSubsequences([4, 6, 7, 7]))
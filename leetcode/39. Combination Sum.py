from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(s: int, path: List[int], target: int):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
                return
            for i in range(s, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
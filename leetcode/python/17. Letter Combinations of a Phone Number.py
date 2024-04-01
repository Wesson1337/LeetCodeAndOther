from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(s: int, path: str):
            if len(path) == len(digits):
                res.append(path)
                return
            letters = digits_map[digits[s]]
            for i in range(len(letters)):
                backtrack(s + 1, path + letters[i])

        if digits:
            backtrack(0, "")
        return res

print(Solution().letterCombinations("234"))


# Space:
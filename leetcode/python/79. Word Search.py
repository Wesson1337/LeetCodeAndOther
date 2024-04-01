from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_y = len(board)
        len_x = len(board[0])
        path = set()

        def backtrack(x: int, y: int, i: int):
            if i == len(word):
                return True
            if x < 0 or y < 0 or x >= len_x or y >= len_y or word[i] != board[y][x] or (y, x) in path:
                return False

            path.add((y, x))
            res = (backtrack(x + 1, y, i + 1) or
                   backtrack(x - 1, y, i + 1) or
                   backtrack(x, y - 1, i + 1) or
                   backtrack(x, y + 1, i + 1))
            path.remove((y, x))
            return res

        for x in range(len_x):
            for y in range(len_y):
                if backtrack(x, y, 0): return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

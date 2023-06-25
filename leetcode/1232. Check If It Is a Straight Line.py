from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x1 - x0
        dy = y1 - y0

        for x, y in coordinates[2:]:
            if (x - x0) * dx != (y - y0) * dy:
                return False
        return True


print(Solution().checkStraightLine([[0,0],[0,1],[0,-1]]))
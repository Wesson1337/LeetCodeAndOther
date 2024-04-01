import math
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[1])

        arrow_number = 0
        arrow_x = -math.inf

        for point in sorted_points:
            if point[0] > arrow_x:
                arrow_number += 1
                arrow_x = point[1]

        return arrow_number

print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))


# Memory: O(n)
# Time: O(n log n)
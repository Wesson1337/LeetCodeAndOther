from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1
        while p1 <= p2:
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]


# time - O(n)
# memory - 0(1)

print(Solution().twoSum([1, 3, 5, 7, 9, 11], 20))
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maximum = 0
        for n in nums:
            if (n - 1) not in nums:
                length = 0
                while (n + length) in nums:
                    length += 1
                maximum = max(maximum, length)
        return maximum


print(Solution().longestConsecutive([2, 1]))
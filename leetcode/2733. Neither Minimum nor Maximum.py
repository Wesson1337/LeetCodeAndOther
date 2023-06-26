from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        nums = sorted(nums)
        return nums[len(nums) // 2]

# runtime 374 ms, beats 92.84%
# memory 16.3 mb, beats 48.5%

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        return not last_index


# Runtime 450 ms, beats 90.72%
# Memory 17.5 MB beats 84.5%

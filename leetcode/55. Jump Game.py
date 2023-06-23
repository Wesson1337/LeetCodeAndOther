from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        if last_index == 0:
            return True



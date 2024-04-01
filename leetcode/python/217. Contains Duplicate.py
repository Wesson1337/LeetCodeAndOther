from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)

# runtime 539 ms, beats 82.48%
# memory 30.7 mb, beats 80.22%

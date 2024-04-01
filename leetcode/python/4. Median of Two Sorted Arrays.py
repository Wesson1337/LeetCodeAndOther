from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = sorted(nums1 + nums2)
        length = len(merged_nums)
        if length % 2 == 0:
            return (merged_nums[length // 2] + merged_nums[length // 2 - 1]) / 2
        else:
            return merged_nums[length // 2]

# runtime 95 ms, beats 93.34%
# memory 16.6 MB, beats 71.79%

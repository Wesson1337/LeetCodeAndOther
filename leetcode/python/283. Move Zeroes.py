from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        nulls_count = 0
        while True:
            if len(nums) == count + nulls_count:
                break
            if nums[count] == 0:
                del nums[count]
                nums.append(0)
                nulls_count += 1
            else:
                count += 1


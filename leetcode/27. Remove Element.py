from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        count = 0
        i = 0
        while i < length:
            if nums[i] == val:
                count += 1
                del nums[i]
                length -= 1
                i -= 1
            i += 1
        return length


print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
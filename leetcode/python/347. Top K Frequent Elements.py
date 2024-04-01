from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        freq = {}
        for num in nums:
            count_nums[num] = 1 + count_nums.get(num, 0)

        for num, counter in count_nums.items():
            if freq.get(counter) is None:
                freq[counter] = [num]
            else:
                freq[counter].append(num)

        res = []
        while True:
            max_num = max(freq)
            for n in freq[max_num]:
                res.append(n)
                if len(res) == k:
                    return res
            del freq[max_num]


# time: O(n)
# memory: O(klogn)


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in group_dict:
                group_dict[sorted_word].append(word)
            else:
                group_dict[sorted_word] = [word]

        return group_dict.values()


# Runtime 110 ms, beats 82.55%
# Memory 20.2 MB, beats 52.81%

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

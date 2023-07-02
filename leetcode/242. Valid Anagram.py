class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        if length != len(t):
            return False

        s_count, t_count = {}, {}
        for i in range(length):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        for letter in s_count:
            if s_count.get(letter) != t_count.get(letter):
                return False
        return True

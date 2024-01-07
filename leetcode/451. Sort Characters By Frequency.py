class Solution:
    def frequencySort(self, s: str) -> str:
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1

        res = ""
        for char, number_of_chars in sorted(chars.items(), key=lambda x: x[1], reverse=True):
            res += char * number_of_chars

        return res

print(Solution().frequencySort('Aabb'))

# Memory: O(n)
# Time: O(n log n)
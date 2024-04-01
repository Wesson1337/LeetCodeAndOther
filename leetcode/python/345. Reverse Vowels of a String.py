class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_set = {"a", "e", "i", "o", "u"}
        vowels = []
        for i in range(len(s)):
            if s[i].lower() in vowels_set:
                vowels.append(s[i])

        result = ""
        for i in range(len(s)):
            if s[i].lower() in vowels_set:
                result += vowels.pop()
            else:
                result += s[i]

        return result


print(Solution().reverseVowels("hello"))
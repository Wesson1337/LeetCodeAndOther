class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = len(haystack) - 1
        needle_end = len(needle) - 1

        while start <= end and end - start >= needle_end:
            if haystack[start] == needle[0]:
                needle_start = 0
                while needle_start + start <= end + 1:
                    if needle_start > needle_end:
                        return start
                    if haystack[start + needle_start] != needle[needle_start]:
                        break
                    needle_start += 1
            start += 1
        return -1

print(Solution().strStr("mississippi", "issipi"))

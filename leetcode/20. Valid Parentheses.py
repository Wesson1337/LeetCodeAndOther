class Solution:
    def isValid(self, s):
        stack = []
        parenthesis = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in parenthesis:
                stack.append(char)
            elif not stack or parenthesis[stack.pop()] != char:
                return False

        return not stack


print(Solution().isValid("(([]){})"))
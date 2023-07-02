class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs: list[str]):
        res = ""
        for string in strs:
            res += f"{str(len(str(string)))}{string}"
        return res


    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, string: str):
        res, i = [], 0

        while i < len(string):
            res.append(string[1 + i:1 + i + int(string[i])])
            i += 1 + int(string[i])
        return res




print(Solution().decode(Solution().encode([123, "hello", "hey", "", ""])))
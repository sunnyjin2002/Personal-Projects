class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words = [i for i in words if i != " " and i != ""]
        return len(words[-1])
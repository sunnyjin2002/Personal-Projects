class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        find_0 = False
        no_one_after_zero = True
        for i in range(1, len(s)):
            if s[i] == "0":
                find_0 = True
            if find_0 and s[i] == "1":
                no_one_after_zero = False
                break
        return no_one_after_zero
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0  #length

        # s.length can be zero.
        if s == "":
            return 0

        for i in range(len(s)):
            currLen = 0
            d = [] # stores chracters we've seen
            for j in range(len(s) - i):
                if s[i+j] not in d:
                    currLen += 1
                    d.append(s[i+j])
                else:
                    break
            if maxLen < currLen:
                maxLen = currLen
        return maxLen

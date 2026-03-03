class Solution:
    def reverse_invert(self, s):
        """Returns the reverse of invert of a binary string s.
        """
        newstr = ""
        for i in range(len(s)):
            if s[-1-i] == "0":
                newstr += "1"
            else:
                newstr += "0"
        return newstr

    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(1, n):
            s = s + "1" + self.reverse_invert(s)
            # Early break
            if k <= len(s):
                break
        return s[k-1]
            
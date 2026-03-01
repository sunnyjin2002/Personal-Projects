class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modval = 10**9 + 7
        s = ""
        for i in range(1, n+1):
            s += str(bin(i))[2:]
        result = int(s,2)
        if result >= modval:
            result = result - (result // modval) * modval
        return result
        
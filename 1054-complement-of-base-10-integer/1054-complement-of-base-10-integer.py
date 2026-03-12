class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s = str(bin(n))[2:]
        result = 0
        # Add digits from the back
        for i in range(len(s)):
            if s[-1-i] == '0':
                result += 1 * (2 ** i)
            #else: result += 0
        return result
        
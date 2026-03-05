class Solution:
    def minOperations(self, s: str) -> int:
        # There are 2 possible alternating binary string for any length:
        # Starting with 1 or starting with 0
        # Check both possibilities and return the smaller change.
        count0 = 0
        count1 = 0
        for i in range(len(s)):
            if i % 2 == 0: # even indices
                if s[i] == '0':
                    count1 += 1
                else:
                    count0 += 1
            else: #odd indices
                if s[i] == '0':
                    count0 += 1
                else:
                    count1 += 1

        return min(count0, count1)
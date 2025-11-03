class Solution:
    def maximumLength(self, s: str) -> int:
        d = {} #dictionary. special_str:occurance
        maxLen = -1

        # Loop through all indices
        for i in range(len(s)):
            # Loop through substring until not special.
            for j in range(len(s) - i):
                # Still special
                if s[i] == s[i+j] and s[i:i+j+1] not in d:
                    d[s[i:i+j+1]] = 1
                elif s[i] == s[i+j] and s[i:i+j+1] in d:
                    d[s[i:i+j+1]] += 1
                    if d[s[i:i+j+1]] >= 3 and j+1 > maxLen:
                        maxLen = j+1
                # Not special anymore
                else:
                    break
                
        return maxLen
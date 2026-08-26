class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        result = ""
        if s.count('1') < k:
            return result

        # Try diff lengths, from smallest
        for l in range(1, len(s)+1):
            #Try starting positions
            for i in range(len(s)-l+1):
                substring = s[i:i+l]
                if substring.count('1') == k:
                    if result == "":
                        result = substring
                    elif substring < result:
                        result = substring
                    

            # A result was found for length l, over all beginning indices    
            if result != "":
                break
        return result
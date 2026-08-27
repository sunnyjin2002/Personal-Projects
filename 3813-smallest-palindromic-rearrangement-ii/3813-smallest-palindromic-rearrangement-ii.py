class Solution:
    def popSmallestFromDict(self, d: dict) -> str:
        """
        Returns the letter that is the smallest in the dictionary.
        Reduce the letter's value by 1. If it would become 0, remove the key.
        """
        k = min(d.keys())
        if d[k] == 1:
            del d[k]
        else:
            d[k] = d[k] - 1
        return k
    

    def smallestPalindrome(self, s: str, k: int) -> str:
        def getcomb(d: dict, k: int) -> int:
            import math
            comb = 1
            curr_len = 0
            # Try building strings
            for char in sorted(d.keys()):
                count = d[char]
                curr_len += count
                comb *= math.comb(curr_len, count)
                if comb > k:
                    return k + 1
            return comb
        
        l = list(s)# obtain list of chars  
        # obtain no. of occurances for each char.
        unique = sorted(list(set(l)))
        dictionary = dict.fromkeys(unique) # char occurance halved.
        odd = "" #In a palindrome, at most 1 char can have odd occurance, in the middle.
        num_chars = 0 # will store the number of chars for 1st half of result string
        for letter in unique:
            occurance = s.count(letter)
            if occurance % 2 == 1:
                odd = letter
                dictionary[letter] = (occurance - 1) // 2
                num_chars += (occurance - 1) // 2
            else:
                dictionary[letter] = occurance // 2
                num_chars += occurance // 2
        
        if getcomb(dictionary, k) < k:
            return ""
        
        # construct first half of the string
        count = 0
        s = ""
        for _ in range(num_chars):
            # As per hint 4, if fix char with smallest
            # would have possibilities > k, fix char
            for letter in unique:
                if dictionary[letter] > 0:
                    dictionary[letter] -= 1
                    comb = getcomb(dictionary, k)

                    if comb >= k:
                        s = s + letter
                        break
                    else:
                        k -= comb
                        dictionary[letter] += 1                
        
        return s + odd + s[::-1]
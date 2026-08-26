class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = list(s)# obtain list of chars
        # obtain no. of occurances for each char.
        unique = sorted(list(set(l)))
        dictionary = dict.fromkeys(unique)
        odd = "" #In a palindrome, at most 1 char can have odd occurance, in the middle.
        for letter in unique:
            occurance = s.count(letter)
            if occurance % 2 == 1:
                odd = letter
                dictionary[letter] = (occurance - 1) / 2
            else:
                dictionary[letter] = occurance / 2
        
        # construct first half of the string
        s = ""
        for letter in sorted(dictionary.keys()):
            s = s + letter * int(dictionary[letter])
        
        return s + odd + s[::-1]
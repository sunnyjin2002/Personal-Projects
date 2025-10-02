class Solution:
    one = 'I'
    five = 'V'
    ten = 'X'
    fifty = 'L'
    hundred = 'C'
    fiveHundred = 'D'
    thousand = 'M'
    romanNumerals = {one: 1, five: 5, ten: 10, fifty: 50, hundred: 100,
    fiveHundred: 500, thousand: 1000}

    def getPreceding(self, numeral: str) -> bool:
        """
        Determines if numeral precedes it's preceding 5 or 10.
        Parameters
        ----------
        numeral: str
            A substring of 2 characters long. Assume numeral[0] in [one, ten, hundred].
        Return
        ------
            bool. True for "Yes subtract this num" False for "Add this number"
        """
        result = False
        if numeral[0] == self.one:
            if numeral[1] in [self.five, self.ten]:
                result = True
        elif numeral[0] == self.ten:
            if numeral[1] in [self.fifty, self.hundred]:
                result = True
        elif numeral[0] == self.hundred:
            if numeral[1] in [self.fiveHundred, self.thousand]:
                result = True
        return result
        

    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            # Working from the back as per the hint:
            index = len(s) - i - 1
            # Starter case: always addition
            if i == 0:
                result += self.romanNumerals[s[index]]
            # Other cases: Assume that there is a digit after index.
            else:
                # If this number is I, X, or C and precedes it's permitted '5' or '10', 
                # subtract this num.
                if s[index] in [self.one, self.ten, self.hundred]:
                    if self.getPreceding(s[index:index+2]):
                        result -= self.romanNumerals[s[index]]
                    else:
                        result += self.romanNumerals[s[index]]
                # If not, add this number.
                else:
                    result += self.romanNumerals[s[index]]
        return result

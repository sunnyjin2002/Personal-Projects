class Solution:
    # Define numerals
    one = 'I'
    five = 'V'
    ten = 'X'
    fifty = 'L'
    hundred = 'C'
    five_hundred = 'D'
    thousand = 'M'

    def getNumerals(self, pos: int) -> list:
        """
        Returns the set of numerals used for the corresponding position.
        Since we assume 1 <= num <= 3999, for the thousand position we only need the 'one'
        Numeral.

        Parameters:
            pos (int): Position of the digit. 4 for thousand, ..., 1 for one.
        Returns:
            list: A list of integers. Format: [1, 5, 10]
        """
        if pos == 1:
            return [self.one, self.five, self.ten]
        elif pos == 2:
            return [self.ten, self.fifty, self.hundred]
        elif pos == 3:
            return [self.hundred, self.five_hundred, self.thousand]
        else:
            return [self.thousand]

    def convertDigit(self, digit: int, pos: int) -> str:
        '''
        This helper function turns a given digit into the corresponding Roman numeral.
        Parameters:
            digit (int): A single digit integer.
            pos (int): Position of the digit. 4 for thousand, ..., 1 for one.

        Return:
            str: The corresponding Roman numeral. 
        '''
        result = ''
        numerals = self.getNumerals(pos)
        if digit <= 3:
            result = numerals[0] * digit
        elif digit == 4:
            result = numerals[0] + numerals[1]
        elif digit <= 8:
            result = numerals[1] + numerals[0] * (digit - 5)
        elif digit == 9:
            result = numerals[0] + numerals[2]
        
        return result


    def intToRoman(self, num: int) -> str:
        # Find how long this number is.
        num_str = str(num)
        num_len = len(num_str)

        result = ''
        for i in range(num_len):
            digit = int(num_str[i])
            pos = num_len - i

            result = result + self.convertDigit(digit, pos)
        return result
        

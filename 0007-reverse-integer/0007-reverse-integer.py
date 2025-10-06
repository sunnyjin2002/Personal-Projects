class Solution:
    max_len = 10 # The length of 2^31 in decimal is 10.
    pos_max_val = 2**31 - 1
    neg_max_val = 2**31
    def reverse(self, x: int) -> int:
        # Base case, otherwise lstrip('0') below will create an empty string
        if x == 0:
            return 0
        
        x_str = str(x)
        pos = True
        if x_str[0] == '-':
            pos = False
            x_str = x_str[1:]
        x_rev = x_str[::-1].lstrip('0') #reverse string and strip leading '0's
        x_rev_int = int(x_rev)      
        
        # If longer than max_len, definitely overflow
        if len(x_rev) > self.max_len:
            return 0
        # If str comparison > max value, also overflow
        elif (pos and (x_rev_int >= self.pos_max_val)) or (not pos and (x_rev_int >= self.neg_max_val)):
            return 0
        # Definitely no overflow - the normal case
        else:
            if pos:
                return x_rev_int
            else:
                return (-1) * x_rev_int
        
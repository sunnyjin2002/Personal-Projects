class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # base case
        if num == 0:
            return True
        # Check if have trailing zeros.
        elif str(num)[-1] == '0':
            return False
        else:
            return True
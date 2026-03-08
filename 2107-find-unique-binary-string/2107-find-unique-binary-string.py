class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # I'm going to use the method for Cantor's diagonization proof
        # any nums of length n has 2^n possible combinations, but only n in nums
        # Thus there is always a string not in nums, and answer is always possible.
        result = ""
        for i in range(len(nums)):
            if nums[i][i] == "0":
                result = result + "1"
            else:
                result = result + "0"
        return result
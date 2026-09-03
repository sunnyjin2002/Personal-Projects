class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d = {}
        prev = ''
        for num in nums:
            if not num in d.keys():
                d[num] = 1 #or True. Just to say it's there.
                prev = num
            elif num == prev:
                #prev = num
                pass
            else:
                d[num] += 1
                prev = num
        
        special = [k for k, v in d.items() if v == 1]
        return len(special)
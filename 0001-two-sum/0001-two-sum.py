class Solution:
    # METHOD 1: BRUTE FORCE
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    #    for i in range(len(nums)):
    #        for j in range(len(nums) - i - 1):
    #            if nums[i] + nums[i+j+1] == target:
    #                return [i, i+j+1]
    # METHOD 2: Hash map
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            else:
                hashmap[num] = i
        return
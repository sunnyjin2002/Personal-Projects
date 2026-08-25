class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        unique_nums = list(set(nums))
        unique_dict = dict.fromkeys(unique_nums, 0)
        # slice the subarrays, and for each subarray, add 1 for nums that appear
        for i in range(len(nums)-k+1):
            subarr = nums[i:i+k]
            for n in list(set(subarr)):
                unique_dict[n] += 1
        appear_once = [k for k,v in unique_dict.items() if v == 1]
        if appear_once:
            return max(appear_once)
        else:
            return -1
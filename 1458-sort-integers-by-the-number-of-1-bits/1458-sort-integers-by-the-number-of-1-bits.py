class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        #Since arr[i] has a max of 10^4, 14 digits long, hash map is 14 digits
        hmap = [[-1]] * 14
        for num in arr:
            # convert to bin, count 1s, and put in hashmap
            num_1 = bin(num).count('1')
            if hmap[num_1] == [-1]:
                hmap[num_1] = [num]
            else:
                hmap[num_1] = hmap[num_1] + [num]
        result = []
        for i in range(len(hmap)):
            if not hmap[i] == [-1]:
                result = result + sorted(hmap[i])
        return result
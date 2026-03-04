class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        candidates = []
        for row in range(len(mat)):
            num1 = [i for i in mat[row] if i == 1]
            if len(num1) == 1:
                candidates = candidates + [(row, mat[row].index(1))]

        count = 0   
        for c in candidates:
            special = True
            for i in range(len(mat)):
                if mat[i][c[1]] == 1 and i != c[0]:
                    special = False
            if special:
                count += 1
        return count
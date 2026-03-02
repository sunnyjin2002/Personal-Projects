class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        #base case: query = (0,0)
        if query_row == 0:
            return min(1, poured)
        
        for i in range(1, 100):
            # fill out new row
            new_row = [-1.0] * (i+1) #range starts with 1 so this always makes sense
            #i-th row has i+1 glasses
            for g in range(i+1):
                if g == 0:
                    new_row[g] = 0.5 * max(row[0] - 1, 0)
                elif g == i:
                    new_row[g] = 0.5 * max(row[-1] - 1, 0)
                else: # middle glasses
                    new_row[g] = 0.5 * max(row[g-1] - 1, 0) + 0.5 * max(row[g] - 1, 0)
            row = new_row
        
            if i == query_row:
                # check query_glass
                return min(1, row[query_glass])
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # For each row, count number of security devices.
        # If a row is not empty, check next row.
            # If non-empty, total += # dev row a * # dev row b
            # If empty, check next row. If no next row, exit loop
        
        prev_row = 0
        totalBeams = 0
        for row in bank:
            num_dev = row.count('1')

            # prev_row not initiated / no devices encountered yet.
            if prev_row == 0:
                prev_row = num_dev
            # this row has no devices - we skip it
            elif num_dev == 0:
                pass
            # There is a previous row, and this row has devices.
            else:
                totalBeams += prev_row * num_dev
                prev_row = num_dev
        return totalBeams
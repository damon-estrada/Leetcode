class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = [[1]]
        if numRows > 1:
            pascals_triangle.append([1, 1])
            current_row = [1, 1]
            next_row = [1]
            # what do i need to keep track of
            # 1 row above
            # The i and j pointer for row above
            # new_row sum [1, append sum ]
            # append new row to pascals_traingle

            while len(pascals_triangle) != numRows:

                i = 0
                j = 1
                while j < len(current_row):
                    next_row.append(current_row[i] + current_row[j])
                    i = i + 1
                    j = j + 1
                next_row.append(1)
                pascals_triangle.append(next_row)
                current_row = next_row
                next_row = [1]

        return pascals_triangle
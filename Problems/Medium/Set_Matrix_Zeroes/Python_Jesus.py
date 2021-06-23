class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = []
        zero_cols = []

        matrix_row_len = len(matrix[0])
        matrix_col_len = len(matrix)

        r = 0
        c = 0

        while r < matrix_col_len:
            while c < matrix_row_len:
                if matrix[r][c] == 0:
                    if r not in zero_rows:
                        zero_rows.append(r)
                    if c not in zero_cols:
                        zero_cols.append(c)
                c = c + 1
            c = 0
            r = r + 1

        for r in zero_rows:
            while c < matrix_row_len:
                matrix[r][c] = 0
                c = c + 1
            c = 0

        r = 0
        for c in zero_cols:
            while r < matrix_col_len:
                matrix[r][c] = 0
                r = r + 1
            r = 0
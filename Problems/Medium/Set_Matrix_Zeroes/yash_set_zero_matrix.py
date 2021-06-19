class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numRows = len(matrix)
        if (numRows != 0):
            numCols = len(matrix[0])
        i = 0
        j = 0
        zero_index = []
        for row in matrix:
            j = 0
            for col in row:
                if (col == 0):
                    zero_index.append((i, j))
                j += 1
            i += 1
            
        for row, col in zero_index:
            for j in range(numCols):
                matrix[row][j] = 0
            for i in range(numRows):
                matrix[i][col] = 0
        print(zero_index)
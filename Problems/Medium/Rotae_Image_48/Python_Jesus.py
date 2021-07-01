class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # I want to reverse to exterior and then swap across the diagnal 
        matrix.reverse()
        #I can use only one verable since both rows and cols are equal to n 
        n = len(matrix)
        i = 0
        while i < n:
            j = i
            while j < n:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j = j+1
            i = i + 1
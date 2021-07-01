void print_matrix(int ** matrix, int matrixSize)
{
    for (int i = 0; i < matrixSize ; i++) {
        for (int j = 0; j < matrixSize; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
    return;
}

/* I will explain that with pic lol. Too hard to write. Figure would help more

4x4 matrix for example. 
First iter 
i = 0
col = 0:2
1|2|3|1|     #|#|#|#
3|#|#|2|  => #|1|1|# => This is how it does it. Idk if that make sense, but I'll explain in call. 
2|#|#|3|     #|2|2|#       
1|3|2|1|     #|#|#|#
void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int row = 0;
    int col = 0;
    int tmp;
    int ans = matrix[matrixSize - 1][0];
    int count = 0;
    // print_matrix(matrix, matrixSize);
    // printf("\n\n");
    for(row = 0; row < matrixSize / 2 + 1; row++) {
        for (col = count; col < matrixSize - count - 1; col++) {
            // rowIndex = matrixSize - col - 1;
            // colIndex = (matrixSize - row - 1) % matrixSize;
            
            tmp = matrix[row][col];
            matrix[row][col] = matrix[matrixSize - col - 1][row];
            matrix[matrixSize - col - 1][row] = matrix[matrixSize - row - 1][matrixSize - col - 1];
            matrix[matrixSize - row - 1][matrixSize - col - 1] = matrix[col][matrixSize - row - 1];
            matrix[col][matrixSize - row - 1] = tmp;
            // print_matrix(matrix, matrixSize);
            // printf("\n\n");
            
        }
        count++;
    }
    // print_matrix(matrix, matrixSize);

}


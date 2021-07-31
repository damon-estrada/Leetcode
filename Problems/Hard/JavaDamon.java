class Solution {
    public int minDistance(String word1, String word2) {

        /* We do not need to do any work if both words are the same and if both */
        /* strings are empty. Therefore, return 0.*/
        if (word1.equals(word2) || (word1.length() == 0 && word2.length() == 0))
            return 0;
        
        /* As a base case, if one string is empty and the other one is not empty,
           then we know we can remove from the non-empty string to mathc the empty
           string and therefore end up with the length of the non-empty strings'
           minimum edit distance which would consists of all removals. */
        if (word1.length() == 0 && word2.length() > 0)
            return word2.length();

        if (word2.length() == 0 && word1.length() > 0)
            return word1.length();

        int numRows = word1.length() - 1;  // horse
        int numCols = word2.length() - 2; // ros

        /* Create the grid! [rows][cols]*/
        int[][] grid = new int[numRows + 1][numCols + 1];

        // Populating the base case section of the grid
        // The base case for the row
        for (int row = 0; row < numRows; row++) {
            grid[row][numCols] = numRows - row;
        }

        // The base case for the col
        for (int col = 0; col < numCols; col++) {
            grid[numRows][col] = numCols - col;
        }

        // Traverse the grid now to find the least number of operations required
        for (int row = numRows - 1; row > -1; row--) {
            for (int col = numCols - 1; col > -1; col--) {
                grid[row][col] =
                        /* Get the min of the three operations (min(min(a, b), c))*/
                        Math.min(Math.min(
                                grid[row][col + 1],        // Insert (col, row + 1)
                                grid[row + 1][col]        // Delete (col + 1, row)
                                ),  grid[row + 1][col + 1]   // Replace (col + 1, row + 1)
                        );

                /* If the two strings do not share a common character, we had to do an
                   operation (INS, DEL, REP) of other grid tiles plus the op (1). */
                if (word2.charAt(col) != word1.charAt(row))
                    grid[row][col] += 1;
            }
        }
        
        /*for (int i = 0; i < numRows + 1; i++) {
            for (int j = 0; j < numCols + 1; j++) {
                System.out.print(grid[i][j] + ", ");
                if (j % numCols == 0 && j != 0)
                    System.out.println("\n");
            }
        }*/


        return grid[0][0];
    }
}
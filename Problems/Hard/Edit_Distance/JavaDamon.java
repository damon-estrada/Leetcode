

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

        int numRows = word1.length();  // horse
        int numCols = word2.length(); // ros

        /* Create the grid! [rows][cols]*/
        int[][] grid = new int[numRows + 1][numCols + 1];

        // Populating the base case section of the grid


        // Traverse the grid now to find the least number of operations required
        for (int row = numRows; row > -1; row--) {
            for (int col = numCols; col > -1; col--) {

                if (row == numRows) {
                    grid[row][numCols] = numRows - row;
                }

                if (col == numCols) {
                    grid[numRows][col] = numCols - col;
                }


                if (word2.charAt(col - 1) == word1.charAt(row - 1)) {

                    grid[row][col] = grid[row + 1][col + 1];

                } else {
                    grid[row][col] = 1 +
                            /* Get the min of the three operations (min(min(a, b), c))*/
                            Math.min(Math.min(
                                    grid[row][col + 1],        // Insert (col, row + 1)
                                    grid[row + 1][col]        // Delete (col + 1, row)
                                    ),  grid[row + 1][col + 1]   // Replace (col + 1, row + 1)
                            );
                }
            }
        }

        return grid[0][0];
    }
}
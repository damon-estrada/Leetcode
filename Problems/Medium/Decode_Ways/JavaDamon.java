package Medium.Decode_Ways;

class Solution {
    public int numDecodings(String s) {

        /* Base case */
        if (s.length() < 1 || s.equals("0"))
            return 0;

        /* Pattern? */
        // In  : 1 2 1 2 1 2 ..
        // Ways: 1 2 3 5 8 11 ..
        // Ways[i] = Ways[i - 1] + Ways[i - 2]

        // With two cavets, the ways[i - 1/2] are rebtween 10-26 so we dont have a leading 0#
        // and if ways[i - 1] < 26

        // memorization (bottom up) - overlapping subproblems?
        int[] dp = new int[s.length() + 1];

        /* base case */
        dp[0] = 1; // length of zero

        if (s.charAt(0) == '0')
            dp[1] = 0; // zero ways to decode a zero character since it doesnt map to anything.
        else
            dp[1] = 1; // if we have a valid (1-26) range char, there is one way to decode this.

        /* Starting at 2 because we ahve already handled the base cases */
        for (int i = 2; i <= s.length(); i++) {
            int sDigit = Integer.parseInt(s.substring(i - 1, i)); // A single digit (9<)
            int dDigit = Integer.parseInt(s.substring(i - 2, i)); // Digits (10>=)
            if (sDigit > 0) {
                dp[i] += dp[i - 1];
            }

            if (dDigit >= 10 && dDigit <= 26) {
                dp[i] += dp[i - 2];
            }
        }

        return dp[s.length()];
    }
}
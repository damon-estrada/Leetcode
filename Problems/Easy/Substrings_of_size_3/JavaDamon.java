class Solution {
    public int countGoodSubstrings(String s) {

        int gStrings = 0, iVal = 0, jVal = 0, kVal = 0;

        if (s.length() < 3)
            return gStrings;

        for (int i = 0; i + 2 < s.length(); i++) {
            /* I am keeping a look ahead of two characters. */
            iVal = (int) s.charAt(i);
            jVal = (int) s.charAt(i+1);
            kVal = (int) s.charAt(i+2);

            /* If the 3 lettered substring is in order, compare the values to make sure they are contiguous sequenced*/
            if ((iVal != jVal && iVal != kVal) && jVal != kVal)
                gStrings++;
        }

        return gStrings;
    }
}
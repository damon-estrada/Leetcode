package Easy.Number_of_1_bits;

public class Java_Damon {
    public class Solution {
        // you need to treat n as an unsigned value
        public int hammingWeight(int n) {

            int mask = 1, numOfOnes = 0;

            for (int bitPos = 0; bitPos < 32; bitPos++) {
                if ((mask & n) != 0)
                    numOfOnes++;
                mask <<= 1;
            }
            return numOfOnes;
        }
    }
}

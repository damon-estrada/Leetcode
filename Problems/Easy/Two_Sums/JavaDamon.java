package Easy.Two_Sums;

import java.util.HashMap;

public class JavaDamon {
    HashMap<Integer, Integer> map = new HashMap();
    int remainder;
    public int[] twoSum(int[] nums, int target) {

        for (int i = 0; i < nums.length; i++) {
            /* Find the index that will add to the target. */
            remainder = target - nums[i];

            if (map.containsKey(remainder)) {
                return new int[]{map.get(remainder), i};
            }

            /* Reguardless, put the value in the map in case the value is the reaminder value we are looking for. */
            map.put(nums[i], i);
        }

        /* Empty array since there is no such indecies that exist. */
        return new int[]{};
    }
}

package Medium.Longest_Substring_Without_Repeating_Characters;

import java.util.HashMap;

public class JavaDamon {
    public int lengthOfLongestSubstring(String s) {

        /* Holds character then interger of longest word at that point. */
        HashMap<Character, Integer> charsVisit = new HashMap();
        int result = 0;
        int longest = 0;

        for (int i = 0; i < s.length(); i++) {

            if (charsVisit.containsKey(s.charAt(i))) {

                /* Start at repeat character to see if that is where the longest substring starts */
                i = charsVisit.get(s.charAt(i));

                charsVisit.clear(); // Clear hash map.
                result = 0;

            } else {
                result++;

                /* KEY/VALUE = char/index */
                charsVisit.put(s.charAt(i), i);
            }

            if (longest < result)
                longest = result;
        }
        return longest;
    }
}

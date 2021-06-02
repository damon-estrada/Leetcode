package Easy.Reverse_Integer;

public class JavaDamon {
    public int reverse(int x) {

        //intMAX = 2_147_483_647

        StringBuilder reverse = new StringBuilder();
        int rev = 0;
        int stop = 0;

        String numStr = String.valueOf(x);

        if (numStr.charAt(0) == '-') {
            reverse.append("-");
            stop = 1;
        }

        for (int i = numStr.length() - 1; i >= stop; i--)
            reverse.append(numStr.charAt(i));

        try {
            rev = Integer.parseInt(reverse.toString());
        } catch (NumberFormatException e) {
            return 0;
        }

        return rev;
    }
}

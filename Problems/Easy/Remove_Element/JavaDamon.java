package Easy.Remove_Element;

public class JavaDamon {

    public int removeElement(int[] nums, int val) {

        int nextElm = 0; // hold a 'poiunter' to the next element
        for (int elem : nums) {
            if (elem != val) {
                // since in java int[] are immutable, we need to move the elements around
                nums[nextElm] = elem;
                nextElm += 1; // return the number the new length which corresponds to how many elements to print.
            }
        }
        return nextElm;
    }
}

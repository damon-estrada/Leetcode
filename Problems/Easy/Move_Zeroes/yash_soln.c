void moveZeroes(int* nums, int numsSize){

    int i = 0;
    int j = 0;
    
    while (i < numsSize) { /* move elements as long as they're not zero. */
        if (nums[i] != 0) 
            nums[j++] = nums[i];
        i++;
    }
    
    while (j <numsSize) /* write zeros in the remaining spots */
        nums[j++] = 0;
}
    
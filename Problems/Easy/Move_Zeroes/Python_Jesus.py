class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # look for the index of the first 0

        i = 0
        nums_len = len(nums)
        zero_index = -1

        while i < nums_len and zero_index == -1:
            if nums[i] == 0:
                zero_index = i
                head = i
            i = i + 1

        # Now swap the 0 with the next none 0 value
        while i < nums_len:
            if nums[i] != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index = zero_index + 1
            i = i + 1
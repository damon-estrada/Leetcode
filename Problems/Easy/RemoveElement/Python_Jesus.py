class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        max_len = len(nums)-1
        while i <= max_len:
            if nums[i] == val:
                #swap the first with the last 
                nums[i], nums[max_len] = nums[max_len], nums[i]
                max_len = max_len - 1
                
            else:
                i = i + 1
        return max_len+1
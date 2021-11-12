class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # i want to find a window that works regardless of size, and then ask
        # then shrink the window by one and see if there is a solution until i reach the end
        head = 0
        tail = 1
        running_sum = nums[head]
        smallest_window = 0

        if nums[0] >= target:
            smallest_window = 1
        # there is an element that is equal to target is window size is 1
        # i dont like using random returns in the middle of my code so i just check
        while tail < len(nums) and smallest_window != 1:
            running_sum = running_sum + nums[tail]

            while running_sum >= target and smallest_window != 1:
                smallest_window = (tail - head) + 1
                # make the window smaller
                running_sum = running_sum - nums[head]
                head = head + 1

            # if i havent found target i want to make the window bigger else i want to shift it
            if head < len(nums) and smallest_window > 0:
                running_sum = running_sum - nums[head]
                head = head + 1
            tail = tail + 1

        return smallest_window
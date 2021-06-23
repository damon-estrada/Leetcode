class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        val = 2**32

        while n != 0:
            if val <= n:
                counter = counter + 1
                n = n - val
                val = val/2

            elif val >= 1:
                val = val/2

            else:
                # Need to account for that special 1
                counter = counter + 1
                n = n - val
                val = val - 1

        return counter
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Im going to need to keep track of three differnt arrays
        # 1) current_permutation: This will keep track of what ever permutation im currently building
        # 2) previous_permutations: this will keep track of what ever was retuned
        # from the previous recursive call
        # 3) permutations: this will keep track of the current set of all permutations

        # Note if i were doing this in another language i have all the information
        # i need to know the size of each arrays and i may get away with using a
        # 2d array instead of 2 sepreate arrays

        current_permutation = []
        permutations = []
        constant = nums[0]

        # Base case
        if len(nums) == 1:
            current_permutation.append(constant)
            permutations.append(current_permutation)

        else:

            # In another language i would need to pass the full array and the start index
            previous_permutation = self.permute(nums[1:])

            for x in previous_permutation:
                # I need a to keep track if i have inserted the constant and where i have done so
                per_len = len(x)
                current_insert_index = 0

                i = 0
                while current_insert_index < per_len:
                    have_inserted = False
                    current_permutation = []
                    while i < per_len and current_insert_index <= per_len:
                        if current_insert_index == i and not have_inserted:

                            current_permutation.append(constant)
                            current_insert_index = current_insert_index + 1
                            have_inserted = True

                        else:
                            current_permutation.append(x[i])
                            i = i + 1

                    permutations.append(current_permutation)
                    i = 0

                x.append(constant)
                permutations.append(x)

        return permutations

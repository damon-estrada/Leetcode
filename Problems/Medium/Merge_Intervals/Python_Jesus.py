class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting helps so you only have to look at the second values 
        intervals.sort(key=lambda x: x[0])
        new_start = 0
        new_end = 0
        merge_set = []

        i = 0
        # go through the list and your current start and end point for comparison later
        while i < len(intervals):
            j = i + 1
            new_start = intervals[i][0]
            new_end = intervals[i][1]

            # if you find an over lapping ranges keep track of the max end and keep moving through the list 
            while j < len(intervals) and new_end >= intervals[j][0]:
                new_end = max(intervals[j][1], new_end)
                j = j + 1

            # if you found over lapping rangers there should be a lap bettween i and j 
            # if i want to save memory space i can pop off the values from the original list and append new ones there as well but that will be slow 
            if i + 1 != j:
                merge_set.append([new_start, new_end])
            else:
                merge_set.append(intervals[i])
            i = j
        return merge_set
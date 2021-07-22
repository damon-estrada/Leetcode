class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        """
        1) Check if substring a is in dictionary used to keep track of repeats.
        2) If yes move
        3) If No check if it is in the rest of substring S
        4) If the substring a is in s then put it in the dictionary
        5) If not move on to the next substring and repeat
        6) Return the keys to the dictionary
        """

        repeats = {}
        start = 0
        end = 10
        str_len = len(s)

        while end <= str_len:
            a = s[start: end]
            if repeats.get(a) is None:
                repeats[a] = 1

            else:
                repeats[a] = repeats[a] + 1
            start = start + 1
            end = end + 1
        return [a for a in repeats.keys() if repeats[a] >= 2]
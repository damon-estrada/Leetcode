class Solution:

    def numDecodings(self, s: str) -> int:
        # Driver function
        # Place the base cases inside of the dic
        memo = {"0": 0}

        return self.numDecodings_recursion(s, memo)

    def numDecodings_recursion(self, s, memo):
        # Base case 1
        if len(s) == 0 or (len(s) == 1 and s == "0") or (len(s) == 2 and s[0] == "0"):
            return 0

        # Base case 2
        elif len(s) == 1 and s != "0":
            return 1
        # Base Case 2
        elif len(s) == 2:
            if int(s) <= 26:
                return 2
            else:
                return 1

        # s.pop(0)
        # check if it is in memo
        if s[1:] not in memo:
            memo[s[1:]] = self.numDecodings_recursion(s[1:], memo) + self.numDecodings_recursion(s[2:], memo)
        return memo[s[1:]]


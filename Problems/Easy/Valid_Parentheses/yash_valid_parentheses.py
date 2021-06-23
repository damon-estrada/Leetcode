class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        if (len(s) % 2):
            return False
        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                valid.append(c)
            else:
                if (len(valid) == 0):
                    return False
                if (valid[-1] == '(' and c == ')'):
                    valid.pop()
                elif (valid[-1] == '{' and c == '}'):
                    valid.pop()
                elif (valid[-1] == '[' and c == ']'):
                    valid.pop()
                else:
                    return False
        print(valid)
        if (len(valid) != 0):
            return False
        return True
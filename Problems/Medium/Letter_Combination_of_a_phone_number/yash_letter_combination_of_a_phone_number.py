class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        words = []
        digit = {}
        digit['2'] = ['a', 'b', 'c']
        digit['3'] = ['d', 'e', 'f']
        digit['4'] = ['g', 'h', 'i']
        digit['5'] = ['j', 'k', 'l']
        digit['6'] = ['m', 'n', 'o']
        digit['7'] = ['p', 'q', 'r', 's']
        digit['8'] = ['t', 'u', 'v']
        digit['9'] = ['w', 'x', 'y', 'z']
        
        newWords = []
        
        for i in range(len(digits)-1, -1, -1): # basically start from the end to beginning
            if (i == len(digits)-1): # for first time, list is empty, so just append them
                for elem in digit[digits[i]]: 
                    words.append(elem)
                continue
            else:
                newWords.clear() # jsut to clear stuff
                for elem in digit[digits[i]]: # iterate over alphabets of numbers
                    for i in range(len(words)): # iterate over words in dictionary and add new letter with these words
                        newWords.append(elem + words[i])
                    print(newWords) # keep newWords as this is a temp copy
                words.clear()
                words = newWords.copy() 
        return words
    
    
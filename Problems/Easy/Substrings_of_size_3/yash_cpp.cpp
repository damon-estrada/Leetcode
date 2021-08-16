class Solution {
public:
 int countGoodSubstrings(string s) {    
        if (s.length() <= 2)
            return 0;
        int count = 0;
        for (int i = 0; i < (s.length() - 2); i++) {
            if ((s[i] ^ s[i+1]) && (s[i+1] ^ s[i+2]) && (s[i+2] ^ s[i]))
                count++;
        }
        return count;
    }
};
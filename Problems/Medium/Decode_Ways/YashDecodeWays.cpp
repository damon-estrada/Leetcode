class Solution {
public:
    
    int dp[101] = {0}; 

    int numDecodings(string s) {
        memset(dp, 0, sizeof(dp));
        
        if (s[0] != '0')
            dp[0] = 1;
        
        for (int i = 1; i < s.length(); i++) {
            int first = s[i] - '0';
            int second = stoi(s.substr(i-1, 2));
            
            if (first >= 1 && first <= 9)
                dp[i] = dp[i-1];
            
            if (second >= 10 && second <= 26)
                if (i - 2 >= 0)
                    dp[i] += dp[i-2];
                else 
                    dp[i] += 1;
        }
        
        
        return dp[s.length()-1];
        
    }
};
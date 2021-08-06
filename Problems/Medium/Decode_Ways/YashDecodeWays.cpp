/* Doesn't work */

class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        
        if (s[0] == '0')
            return 0;
        

        
        if (n == 2 && ((s[0] == '1' && s[1] == '0') || (s[0] == '2' && s[1] == '0')))
            return 1;
                vector<int> dp(n+1, 1);
        
        for (int i = 1; i < n; i++) {
            if (s[i] == '0' && s[i-1] == '0') {
                return 0;
            } else if (s[i] == '0' && s[i-1] != '0') {
                if (s[i-1] == '1' || s[i-1] == '2')
                    dp[i] = dp[i-1];
                else 
                    return 0;
            } else if (s[i] != '0' && s[i-1] == '0') {
                dp[i] = dp[i-1];
            } else {
                if (stoi(s.substr(i-1, 2)) > 0 && stoi(s.substr(i-1, 2)) < 27)
                    dp[i] = dp[i-1] + 2;
                else 
                    dp[i] = dp[i-1];
            }
        }     
           
            
            
            // if (stoi(s.substr()))
        
//         for (int i = 0; i < n+1; i++)
//             cout << dp[i] <<"  ";
//         cout << endl;
        return dp[n-1];
        
        
    }
};

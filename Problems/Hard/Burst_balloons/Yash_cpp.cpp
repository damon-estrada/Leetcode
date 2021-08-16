class Solution {
public:
    int dp[502][502];
    int solve(vector<int>& arr, int left, int right) {
        if (right == left + 1)
            return 0;
        
        if (dp[left][right] != -1)
            return dp[left][right];
        
        int result = INT_MIN;
        int tmp;
        for (int i = left + 1; i < right; i++) {
            tmp = solve(arr, left, i) + solve(arr, i, right) + arr[left] * arr[i] * arr[right];
            
            result = max(result, tmp);
        }
        dp[left][right] = result;
        return result;
    }
    
    
    int maxCoins(vector<int>& nums) {

        if (nums.size() == 1)
            return nums[0];
        
        if (nums.size() == 2)
            return nums[0] * nums[1] + max(nums[0], nums[1]);
        
        if (nums.size() == 3) 
            return nums[0]*nums[1]*nums[2] + nums[0]*nums[2] + max(nums[0], nums[2]);
        
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        
        memset(dp, -1, sizeof(dp));
        
        return solve(nums, 0, nums.size() - 1);
        
    }
};
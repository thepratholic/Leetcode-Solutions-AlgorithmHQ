Contributed by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

class Solution {
public:
    int solve(vector<int>& nums, int index, int currentSum, int target, vector<unordered_map<int, int>>& dp) {
        if (index == nums.size()) return currentSum == target ? 1 : 0;
        if (dp[index].count(currentSum)) return dp[index][currentSum];

        int add = solve(nums, index + 1, currentSum + nums[index], target, dp);
        int subtract = solve(nums, index + 1, currentSum - nums[index], target, dp);

        return dp[index][currentSum] = add + subtract;
    }

    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        vector<unordered_map<int, int>> dp(n);
        return solve(nums, 0, 0, target, dp);
    }
};

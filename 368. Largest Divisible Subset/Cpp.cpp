//recursion code 

class Solution {
public:
   void helper(int idx,vector<int>&nums,vector<int>& ans,vector<int>& temp,int prev){
  
    if(idx>=nums.size()){
        if(temp.size()>ans.size()){
            ans  = temp;
        }

        return;
    }

    if(prev == -1 || nums[idx]%prev==0){
        temp.push_back(nums[idx]);
        helper(idx+1,nums,ans,temp,nums[idx]);
        temp.pop_back();
    }

    helper(idx+1,nums,ans,temp,prev);



   }
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        
        sort(nums.begin(),nums.end());   //sort the array
        vector<int>ans;
        vector<int>temp;

        helper(0,nums,ans,temp,-1);

        return ans;
    }
};

//memoization code 

class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // Sort the array

        int n = nums.size();
        // dp[i] stores the largest divisible subset ending with nums[i]
        vector<vector<int>> dp(n);

        vector<int> maxSubset;

        for (int i = 0; i < n; ++i) {
            dp[i].push_back(nums[i]);  // Start with current number
            for (int j = 0; j < i; ++j) {
                if (nums[i] % nums[j] == 0 && dp[j].size() + 1 > dp[i].size()) {
                    dp[i] = dp[j];  // Copy previous subset
                    dp[i].push_back(nums[i]);  // Append current number
                }
            }
            if (dp[i].size() > maxSubset.size()) {
                maxSubset = dp[i];
            }
        }

        return maxSubset;
    }
};


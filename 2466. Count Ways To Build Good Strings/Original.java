class Solution {
    // use mod to handle large values as mentioned in the problem
    int mod = 1000000007;
    public int countGoodStrings(int low, int high, int zero, int one) {
        // use dp array to keep track of overlapping sub-cases
        int[] dp = new int[high+1];
        Arrays.fill(dp, -1);
        return count(low, high, zero, one, 0, dp)%mod;
    }

    private int count(int low, int high, int zero, int one, int len, int[] dp) {
        // return 0 if length of the string crosses high
        if(len>high) return 0;
        if(dp[len]!=-1) return dp[len];
                   // recursive call for appending 0 zero times
        int ans = (count(low, high, zero, one, len+zero, dp)%mod
                   // recursive call for appending 0 zero times
                  + count(low, high, zero, one, len+one, dp)%mod)%mod;
        // add 1 to the ans if a string is formed using the operations given and satisfying all the conditions i.e. len>=low and len<=high 
        if(len>=low && low<=high) ans+=1;
        return dp[len]=ans%mod;
    }
}

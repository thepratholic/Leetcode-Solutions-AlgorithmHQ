class Solution {
    public int countSubarrays(int[] nums) {
        //Time complexity: O(n)
        int ans = 0;
        // iterate till <n-2 as 1st number should have its corresponding 3rd number
        for(int i=0; i<nums.length-2; i++) {
            // check for the required condition
            if((nums[i]+nums[i+2])*2==nums[i+1]) ans+=1; // O(1)
        }
        return ans;
    }
}

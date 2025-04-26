class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        long ans = 0;
        // consider 3 variables, one to skip the unwanted number, minI and maxI to keep track of latest index which contains minK and maxK respectively
        int skip=-1, minI=-1, maxI=-1;
        for(int i=0; i<nums.length; i++) {
            // update skip if an unwanted number arrives
            if(nums[i]<minK || nums[i]>maxK) skip=i; 
            // update minI if minK is arrives
            if(nums[i]==minK) minI=i;
            // update maxI if maxK is arrives
            if(nums[i]==maxK) maxI=i;
            // update ans with the total number of elements with which a fixed-bound subarray can be formed
            ans+=Math.max(0L, Math.min(minI, maxI)-skip);
        }
        return ans;
    }
}

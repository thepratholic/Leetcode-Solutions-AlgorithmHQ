class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int count = 0;
        // even stores the required parity at any index
        boolean even = nums[0]%2==0;
        for(int i=0; i<nums.length; i++) {
            // check if we've the required parity
            if((nums[i]%2==0)==even) {
                count+=1;
                even=!even;
            // set count = 1 if required parity not present
            } else {
                count=1;
                even = !(nums[i]%2==0);
            }
            nums[i] = count;
        }
        boolean ans[] = new boolean[queries.length];
        for(int i=0; i<ans.length; i++) {
            // calculate length of subarray represented by query
            int len = queries[i][1]-queries[i][0]+1;
            // check if a special subarray of length len ends at the 'to' index
            ans[i] = len<=nums[queries[i][1]];
        }
        return ans;
    }
}

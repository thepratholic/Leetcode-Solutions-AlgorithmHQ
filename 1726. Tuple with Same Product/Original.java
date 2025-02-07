class Solution {
    public int tupleSameProduct(int[] nums) {
        // using map to store products and thier count
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        for(int i=0; i<nums.length; i++) {
            for(int j=i+1; j<nums.length; j++) {
                // one tuple can be arranged in 8 ways
                ans+=8*map.getOrDefault(nums[i]*nums[j], 0);
                map.put(nums[i]*nums[j], 
                map.getOrDefault(nums[i]*nums[j], 0)+1);
            }
        }
        return ans;
    }
}

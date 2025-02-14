class Solution {
    public int maximumSum(int[] nums) {
        // Time complexity: O(N)
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        for(int i=0; i<nums.length; i++) {
            // calculate sum of digita of a number
            int sum = sumOfDigits(nums[i]);
            // check if the sum already exists
            if(map.containsKey(sum)) {
                // update ans if a greater value is found
                ans = Math.max(ans, nums[i]+map.get(sum));
            }
            // update map with the maximum of the stored value and current value
            map.put(sum, Math.max(nums[i], map.getOrDefault(sum, 0)));
        }
        return ans>0?ans:-1;
    }

    private int sumOfDigits(int num) {
        int sum = 0;
        while(num>0) {
            sum+=num%10;
            num/=10;
        }
        return sum;
    }
}

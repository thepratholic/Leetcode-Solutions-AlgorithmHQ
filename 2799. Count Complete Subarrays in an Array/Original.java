class Solution {
    public int countCompleteSubarrays(int[] nums) {
        // count total number of distinct elements in the array
        int distinct = (int) Arrays.stream(nums).distinct().count();
        // use a map to get the window which satisfies the condition
        Map<Integer, Integer> map = new HashMap<>();
        int left=0, ans=0;
        for(int right=0; right<nums.length; right++) {
            // increase window width
            map.put(nums[right], map.getOrDefault(nums[right], 0)+1);
            // decrease window width till no. of distinct elements in map is equal to total
            while(map.size()==distinct) {
                // increment ans with the value obtained after decreasing window size
                ans+=nums.length-right;
                map.put(nums[left], map.get(nums[left])-1);
                if(map.get(nums[left])==0) map.remove(nums[left]);
                left+=1;
            }
        }
        return ans;
    }
}

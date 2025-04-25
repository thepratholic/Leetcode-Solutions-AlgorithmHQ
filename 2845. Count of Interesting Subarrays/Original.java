class Solution {
    public long countInterestingSubarrays(List<Integer> nums, int modulo, int k) {
        long ans = 0;
        // start with prefix sum count = 0 
        int pc = 0; 
        // use a map to store how many times a target has occured before 
        Map<Integer, Long> map = new HashMap<>();
        // put target=0 and occurance=1 as we're starting with pc=0
        map.put(0, 1L);
        for(int i: nums) {
            // increase pc if an index is found satisfying the condition
            if(i%modulo==k) pc+=1;
            int mod = pc%modulo;
            // calculate target by getting the extra indices when we need exactly k number of indices 
            int target = mod-k;
            // add modulo if target becomes negative
            if(target<0) target+=modulo;
            // check if target is already present, if its already present that means we've a number of indices after an index which satisfies our condition
            ans+=map.getOrDefault(target, 0L);
            map.put(mod, map.getOrDefault(mod,0L)+1);
        }
        return ans;
    }
}

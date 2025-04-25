class Solution {
    public int countLargestGroup(int n) {
        // store group sizes according to thier sum
        Map<Integer, Integer> map = new HashMap<>();
        int max=0, ans=0;
        for(int i=1; i<=n; i++) {
            // calculate sum of digits
            int sum = sum(i);
            // update count of groups according to sum
            map.put(sum, map.getOrDefault(sum, 0)+1);
            // if found a new max, update max max and ans
            if(max<map.get(sum)) {
                max=map.get(sum);
                ans=1;
            // if found sum equal to max, update ans
            } else if(max==map.get(sum)) {
                ans+=1;
            }
        } 
        return ans;
    }

    private int sum(int n) {
        int sum = 0;
        while(n>0) {
            sum+=n%10;
            n/=10;
        }
        return sum;
    }
}

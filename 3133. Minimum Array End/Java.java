class Solution {
    public long minEnd(int n, int x) {
        // consider x as the first element
        long ans = x;
        // deduct n by 1 as we already considered first element
        n-=1;
        while(n-->0) {
            // find next larger element
            ans = (ans+1) | x;
        }
        return ans;
    }
}

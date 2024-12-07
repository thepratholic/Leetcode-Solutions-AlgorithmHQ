class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        Set<Integer> exclude = new HashSet<>();
        // add integers in hashset to check presence in O(1) time
        for(int i: banned) exclude.add(i);
        int select = 0;
        for(int i=1; i<=n; i++) {
            // check if integer can be selected
            if(!exclude.contains(i) && i<=maxSum) {
                select+=1;
                maxSum-=i;
            // break if current integer is greater than maxSum
            } else if(i>maxSum) break;
        }
        return select;
    }
}

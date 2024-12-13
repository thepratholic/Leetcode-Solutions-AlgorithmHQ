class Solution {
    public long findScore(int[] nums) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<>(){
            // sort on the basis of values
            public int compare(int[] a, int[] b){
                if(a[0]<b[0]) return -1;
                else if(a[0]>b[0]) return 1;
                // if values are same, sort on the basis of index
                return Integer.compare(a[1], b[1]);
            }
        });
        // use set to mark elements
        Set<Integer> marked = new HashSet<>();
        for(int i=0; i<nums.length; i++) pq.add(new int[]{nums[i], i});
        long score = 0;
        while(!pq.isEmpty()) {
            int current[] = pq.remove();
            // if current smallest is marked move forward
            if(marked.contains(current[1])) continue;
            // use smallest element to increase score, make appropriate markings
            score+=current[0];
            marked.add(current[1]);
            marked.add(current[1]-1);
            marked.add(current[1]+1);
        }
        return score;
    }
}

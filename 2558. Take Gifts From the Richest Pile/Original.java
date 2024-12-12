class Solution {
    public long pickGifts(int[] gifts, int k) {
        // heap to retrieve the maximum element at each second
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int g: gifts) pq.add(g);
        for(int i=0; i<k; i++) {
            // do an operation every second
            pq.add((int)Math.floor(Math.sqrt(pq.remove())));
        }
        long sum = 0;
        // calculate the sum after k seconds
        while(!pq.isEmpty()) {
            sum+=pq.remove();
        }
        return sum;
    }
}

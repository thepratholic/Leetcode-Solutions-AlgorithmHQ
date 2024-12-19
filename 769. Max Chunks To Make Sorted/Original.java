class Solution {
    public int maxChunksToSorted(int[] arr) {
       int max = 0, chunks=0;
       for(int i=0; i<arr.length; i++) {
            // calcuate maximum at every index
            max = Math.max(max, arr[i]);
            // if max is equal to the required value at index i, a new chunk is found
            if(max==i) chunks+=1;
       }
       return chunks;
    }
}

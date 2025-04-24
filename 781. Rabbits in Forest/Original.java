class Solution {
    public int numRabbits(int[] answers) {
        Map<Integer, Integer> map = new HashMap<>();
        // count number of rabbits which answer a particular value
        for(int a: answers) {
            map.put(a, map.getOrDefault(a, 0)+1);
        }
        int rabbits = 0;
        for(int key: map.keySet()) {
            // add number of rabbits to the ans which say they don't have a similar rabbit 
            if(key==0) rabbits+=map.get(key);
            else {
                // calculate min number of groups that can be formed using the answers of the rabbits
                int groups = (int)Math.ceil((double)map.get(key)/(key+1));
                rabbits+=((key+1)*groups);
            }
        }
        return rabbits;
    }
}

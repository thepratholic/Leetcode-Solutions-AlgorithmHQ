class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        // use max to get the max values of all values[i]+i
        int max = values[0];
        int score = Integer.MIN_VALUE;
        for(int j=1; j<values.length; j++) {
            // update score for every j
            score = Math.max(score, max+values[j]-j);
            // update max before moving on to the next j
            max = Math.max(max, values[j]+j);
        }
        return score;
    }
}

class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        // Time complexity: O(N), where N is the number of dominoes

        // Create a 2D array to count frequency of normalized dominoes
        int[][] count = new int[10][10];  // Only digits 1–9 are valid
        int ans = 0;

        for (int[] d : dominoes) {
            int first = d[0];
            int second = d[1];

            // Normalize the domino to ensure the smaller number comes first
            if (first > second) {
                int temp = first;
                first = second;
                second = temp;
            }

            // Count how many such normalized dominoes we've seen so far
            ans += count[first][second];

            // Increment the count for this normalized domino
            count[first][second]++;
        }

        return ans; // Total number of equivalent domino pairs
    }
}

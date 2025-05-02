class Solution {
    public int findNumbers(int[] nums) {
        // Time complexity: O(N), where N is the number of elements in the array
        int ans = 0;

        // Loop through each number in the array
        for (int i : nums) {
            // Check if the number has an even number of digits:
            // - Between 10 and 99 → 2 digits
            // - Between 1000 and 9999 → 4 digits
            // - Exactly 100000 → 6 digits
            if ((i > 9 && i < 100) || (i > 999 && i < 10000) || i == 100000) {
                ans += 1; // Increment the count if it satisfies any of the even-digit conditions
            }
        }

        // Return the total count of numbers with even number of digits
        return ans;
    }
}

class Solution {
    public int[] buildArray(int[] nums) {
        // Time complexity: O(N)
        // Space complexity: O(1) — in-place modification

        int n = nums.length;

        // First pass: Encode both old and new values into nums[i]
        for (int i = 0; i < n; i++) {
            // nums[nums[i]] % n extracts the original value at nums[nums[i]]
            // Multiply by n to shift it to higher order bits and add to current nums[i]
            nums[i] = nums[i] + n * (nums[nums[i]] % n);
        }

        // Second pass: Extract the new value by dividing by n
        for (int i = 0; i < n; i++) {
            nums[i] = nums[i] / n;  // Discard original and keep only the new value
        }

        return nums;
    }
}

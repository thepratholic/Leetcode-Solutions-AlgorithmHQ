class Solution {
    public long countSubarrays(int[] nums, long k) {
        // Initialize variables
        long sum = 0, ans = 0;
        int left = 0; // Left pointer for sliding window

        // Traverse the array with right pointer
        for (int right = 0; right < nums.length; right++) {
            sum += nums[right]; // Add the current element to the sum

            // While the current window's score is >= k, shrink the window from the left
            while ((sum) * (right - left + 1) >= k) {
                sum -= nums[left]; // Remove the leftmost element from sum
                left++; // Move left pointer forward
            }

            // After ensuring score < k, all subarrays ending at 'right' and starting from 'left' to 'right' are valid
            ans += (right - left + 1);
        }

        // Return the total number of valid subarrays
        return ans;
    }
}

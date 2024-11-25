# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float("inf")  # Initialize the minimum length as infinity
        window_start = window_end = 0  # Pointers for the sliding window
        bit_counts = [0] * 32  # Array to count bits for 32-bit integers

        # Expand window until the end of the array
        while window_end < len(nums):
            # Add the current number to the window and update its bit counts
            self._update_bit_counts(bit_counts, nums[window_end], 1)

            # Contract the window while the OR value is valid (i.e., >= k)
            while (window_start <= window_end and self._convert_bits_to_num(bit_counts) >= k):
                # Update the minimum length found so far
                min_length = min(min_length, window_end - window_start + 1)
                # Remove the element at the start of the window from the OR calculation
                self._update_bit_counts(bit_counts, nums[window_start], -1)
                window_start += 1  # Shrink the window from the left

            window_end += 1  # Expand the window by moving the right pointer

        # If no valid subarray was found, return -1; otherwise, return the min length
        return -1 if min_length == float("inf") else min_length

    # Helper function to update the bit counts based on a number and delta (+1 or -1)
    def _update_bit_counts(self, bit_counts, number, delta):
        for pos in range(32):
            if number & (1 << pos):  # Check if the bit at position 'pos' is set in 'number'
                bit_counts[pos] += delta  # Update the bit count for this bit position

    # Helper function to convert the bit counts back to a number
    def _convert_bits_to_num(self, bit_counts):
        result = 0
        for pos in range(32):
            if bit_counts[pos]:
                result |= 1 << pos  # Set the bit at position 'pos' if the count is non-zero
        return result  # Return the number formed by the OR of the current window's elements

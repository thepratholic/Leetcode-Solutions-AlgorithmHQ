# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Dictionary to keep track of the frequency of prefix sums mod 2
        # Initially, there's one prefix (empty subarray) with even sum (0 mod 2)
        mpp = {0: 1}
        MOD = 10**9 + 7  # Modulo constant to prevent overflow
        cnt = 0  # To count the number of subarrays with odd sum
        s = 0    # Current prefix sum

        # Iterate through each element in the array
        for num in arr:
            s += num  # Update prefix sum
            
            # Check the parity of the current prefix sum
            if s % 2 == 1:
                # If s is odd, then to form an odd subarray sum,
                # the earlier prefix must be even (0 mod 2)
                cnt += mpp.get(0, 0)
            else:
                # If s is even, then the earlier prefix must be odd (1 mod 2)
                cnt += mpp.get(1, 0)
            
            # Update the frequency of the current prefix sum's parity
            mpp[s % 2] = mpp.get(s % 2, 0) + 1

        # Return the result modulo MOD
        return cnt % MOD

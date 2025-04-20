# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0  # This will store the number of good triplets found

        # Iterate through all possible triplets (i, j, k) with i < j < k
        for i in range(n - 2):  # i goes from 0 to n-3
            for j in range(i + 1, n - 1):  # j goes from i+1 to n-2
                for k in range(j + 1, n):  # k goes from j+1 to n-1
                    # Check the given conditions for a triplet to be "good"
                    if (
                        abs(arr[i] - arr[j]) <= a and  # First condition
                        abs(arr[j] - arr[k]) <= b and  # Second condition
                        abs(arr[i] - arr[k]) <= c      # Third condition
                    ):
                        count += 1  # If all conditions are satisfied, increment count

        return count  # Return the total number of good triplets

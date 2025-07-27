# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        valid = 0  # To count all valid subarrays

        # conflictingPoints[i] will store all points (a) that conflict with i (b)
        conflictingPoints = [[] for _ in range(n + 1)]

        # For each conflict pair, ensure a < b and add a to conflictingPoints[b]
        for a, b in conflictingPairs:
            a, b = min(a, b), max(a, b)
            conflictingPoints[b].append(a)

        maxConflict = 0           # Largest conflicting point so far
        secondMaxConflict = 0     # Second largest conflicting point
        extra = [0] * (n + 1)     # Extra valid subarrays that extend from maxConflict range

        # Iterate over all possible subarray end points
        for end in range(1, n + 1):
            # Update the max conflicting points for current `end`
            for u in conflictingPoints[end]:
                if u >= maxConflict:
                    secondMaxConflict = maxConflict
                    maxConflict = u
                elif u > secondMaxConflict:
                    secondMaxConflict = u

            # All subarrays ending at `end` and starting after maxConflict are valid
            valid += end - maxConflict

            # Extra subarrays that end at `end` but start in the range 
            # between secondMaxConflict and maxConflict
            extra[maxConflict] += maxConflict - secondMaxConflict

        # Return total valid subarrays plus the best extension found
        return valid + max(extra)

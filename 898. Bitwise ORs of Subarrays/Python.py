# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def subarrayBitwiseORs(self, nums: list[int]) -> int:
        n = len(nums)

        result = set()  # This set will store all unique bitwise OR results
        prev = set()    # This set stores all OR results for subarrays ending at the previous index

        # Traverse each number in the array
        for i in range(n):
            cur = set()  # This will store all OR results for subarrays ending at index i

            # Extend all previous subarrays by nums[i]
            for x in prev:
                or_val = x | nums[i]  # Bitwise OR of previous result with current number
                cur.add(or_val)       # Add to current OR results
                result.add(or_val)    # Add to global result set

            # Also, start a new subarray with just nums[i]
            cur.add(nums[i])
            result.add(nums[i])

            # Update prev to cur for the next iteration
            prev = cur

        # The length of the result set gives number of unique OR values from all subarrays
        return len(result)

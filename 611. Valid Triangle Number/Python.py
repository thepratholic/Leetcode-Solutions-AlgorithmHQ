# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/



from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # If array has less than 3 sides, no triangle possible
        if n < 3:
            return 0

        # Sort numbers to apply two-pointer technique easily
        nums.sort()
        ans = 0

        # Fix the largest side (nums[k]) one by one from right to left
        for k in range(n - 1, 1, -1):  
            i = 0               # left pointer (smallest side)
            j = k - 1           # right pointer (middle side)

            # Now check pairs (i, j) for current k
            while i < j:
                # If nums[i] + nums[j] > nums[k], then 
                # all numbers between i..j-1 with nums[j] 
                # will also satisfy the triangle inequality
                if nums[i] + nums[j] > nums[k]:
                    ans += (j - i)   # count all valid pairs
                    j -= 1           # decrease j to check next
                else:
                    # Otherwise, nums[i] too small → move i forward
                    i += 1

        # Final count of valid triangles
        return ans

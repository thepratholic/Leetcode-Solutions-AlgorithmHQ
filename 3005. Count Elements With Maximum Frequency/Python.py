# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import Counter, List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums) # calculating the frequency for elements

        maxi = max(freq.values()) # get the maximum out of all the frequencies
        ans = 0

        for k, v in freq.items():
            if v == maxi: # if the frequency is same as max, then add it
                ans += v

        return ans # return the total frequencies
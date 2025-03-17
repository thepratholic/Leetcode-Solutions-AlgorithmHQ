# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mpp = defaultdict(int)

        for i in nums:
            mpp[i] += 1 # storing frequency of each element

        for k, v in mpp.items():
            if v % 2 == 1: # if the frequency is odd, then it is impossible to make the pair
                return False

        return True # return true, if the frequency of all elements is even
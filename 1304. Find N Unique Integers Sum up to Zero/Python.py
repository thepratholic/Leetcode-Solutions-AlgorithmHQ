# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0] # if one element, is needed then return only 0

        ans = []

        for i in range(1, n // 2 + 1): # by observing, only add the -ve's and +ve's in this range
            ans.append(i) 
            ans.append(-i)


        if n & 1: # if n is odd, then add one zero to satisfy then n value
            ans.append(0)

        return ans # return the answer list
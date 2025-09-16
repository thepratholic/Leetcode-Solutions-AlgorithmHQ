# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from math import gcd, lcm
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = [] # declare a stack to check from last element with the current one

        for num in nums:
            stack.append(num) # append the new number

            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1: # check wheather stack has 2 elements and if has, then check wheather it is non co-prime or not
                x = stack.pop()
                y = stack.pop()

                stack.append(lcm(x, y)) # if it is non co-prime, then remove both of them and push the lcm of them

        return stack # return the stack as result
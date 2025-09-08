# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    # Helper function: checks if a number has NO zero digits
    def isValid(self, num):
        temp = num
        while temp > 0:
            ld = temp % 10          # extract last digit
            if ld == 0:             # if digit is 0, number is not valid
                return False
            temp //= 10             # move to next digit
        return True                 # if no digit was 0 → valid

    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = []

        # Try all pairs (i, j) where i + j = n
        # i goes from 1 to n
        for i in range(1, n + 1):

            # j starts from i to avoid duplicate checking of same pair (i, j) and (j, i)
            for j in range(i, n + 1):
                fl = False  # flag to check if solution found

                # Check: both numbers must have no 0 digit and sum = n
                if self.isValid(i) and self.isValid(j) and i + j == n:
                    fl = True
                    ans.extend([i, j])  # store the answer pair
                    break  # break inner loop since pair is found

            if fl:  # if pair found, break outer loop too
                break

        return ans

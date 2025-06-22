# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)  # Length of the input string

        ans = []  # This will store the final groups

        # Loop over the string in steps of size k
        for i in range(0, n, k):
            temp = s[i : i + k]  # Take a substring of length up to k

            # If the last substring is shorter than k, pad it with 'fill'
            if len(temp) < k:
                temp += fill * (k - len(temp))
            
            ans.append(temp)  # Add the (padded) substring to the answer

        return ans  # Return the list of groups

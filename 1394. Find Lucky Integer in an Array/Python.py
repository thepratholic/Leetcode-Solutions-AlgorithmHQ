# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import Counter, List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr) # taking the frequencies of all the elements

        maxi = float("-inf") # setting the answer by -INF

        for k, v in freq.items():
            if k == v: # check wheather this element has frequencies same as his number
                maxi = max(maxi, k) # update the answer as we want the largest one

        return maxi if maxi != float("-inf") else -1 # return the answer if it is not -INF else return -1
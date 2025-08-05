# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        unplaced = 0 # count the ans

        unused = [True] * n # to mark the basket is used or not
        for i in range(n):
            placed = False

            for j in range(n):
                if unused[j] and baskets[j] >= fruits[i]:
                    unused[j] = False # basket got used
                    placed = True # fruit is placed in the basket
                    break

            if not placed:
                unplaced += 1 # fruit remain unplaced

        return unplaced # return the answer
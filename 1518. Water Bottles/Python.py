# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import deque

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Queue to simulate drinking bottles
        q = deque()

        ans = 0  # total bottles drunk

        # Initially, you have numBottles full bottles to drink
        for i in range(numBottles):
            q.append(1)  # each '1' means one full bottle

        # While you have enough empty bottles to exchange
        while len(q) >= numExchange:
            empty = 0  # counter for empty bottles

            # Drink numExchange bottles (remove them from queue)
            for i in range(numExchange):
                q.popleft()
                empty += 1

            # Count those drunk bottles
            ans += empty

            # After exchanging numExchange empty bottles → get 1 new full bottle
            q.append(1)

        # Drink the remaining bottles (less than numExchange, can't exchange anymore)
        while q:
            ans += q.popleft()

        return ans

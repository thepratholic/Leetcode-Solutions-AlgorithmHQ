# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import deque

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        q = deque()
        exchange = numExchange   # starting exchange rate

        # Put all initial bottles in the queue (all are full at the start)
        for i in range(numBottles):
            q.append(1)   # each "1" means a full bottle

        ans = 0  # total bottles drunk

        # Keep exchanging while you have at least "exchange" empty bottles
        while len(q) >= exchange:
            empty = 0  # counter for empty bottles we just drank

            # Drink 'exchange' bottles
            for i in range(exchange):
                q.popleft()
                empty += 1

            # Add those to total
            ans += empty

            # After exchanging → get 1 new full bottle
            q.append(1)

            # The trick: each time, the exchange rate increases by 1
            exchange += 1

        # After you can no longer exchange, just drink the remaining bottles
        while q:
            ans += q.popleft()

        return ans

# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

MOD = 10**9 + 7   # Large prime for modulo to avoid overflow

class Solution:

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        # dp[day] = number of people who learn the secret for the first time on 'day'
        dp = [0] * (n + 1)
        dp[1] = 1   # On day 1, exactly 1 person knows the secret

        # Fill dp for each day
        for day in range(2, n + 1):
            ans = 0

            # A person who learned on day 'd' can share the secret between
            # (d + delay) and (d + forget - 1)
            # So to find how many new people learn on 'day',
            # we add contributions from all valid previous days 'd'
            for d in range(day - forget + 1, day - delay + 1):
                if d > 0:   # Only consider valid days
                    ans = (ans + dp[d]) % MOD

            # Store total new people who learned the secret on this day
            dp[day] = ans % MOD

        # After n days, some people may have already forgotten the secret
        # We only count people who learned it between (n - forget + 1) and n
        total = 0
        for day in range(n - forget + 1, n + 1):
            total = (total + dp[day]) % MOD

        return total
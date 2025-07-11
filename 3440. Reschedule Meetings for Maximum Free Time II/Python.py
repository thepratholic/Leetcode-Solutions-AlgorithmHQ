# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


class Solution:
    def maxFreeTime(self, endpoint: int, st: list[int], et: list[int]) -> int:
        n = len(st)

        # Step 1: Calculate free time intervals
        # Time before first event
        free = [st[0]]

        # Time between events
        for i in range(1, n):
            free.append(st[i] - et[i - 1])
        
        # Time after last event until endpoint
        free.append(endpoint - et[-1])

        m = len(free)  # Number of free intervals

        # Step 2: Preprocess prefix max and suffix max of free intervals
        pre = [0] * m
        suf = [0] * m

        # pre[i] = max of free[0..i]
        pre[0] = free[0]
        for i in range(1, m):
            pre[i] = max(pre[i - 1], free[i])

        # suf[i] = max of free[i..m-1]
        suf[-1] = free[-1]
        for i in range(m - 2, -1, -1):
            suf[i] = max(suf[i + 1], free[i])

        mx = 0  # Store maximum free time

        # Step 3: Iterate over each event and try to maximize free time by skipping it
        for i in range(n):
            cur_time = et[i] - st[i]  # Time taken by current event

            # Calculate gaps before and after the event
            prev_end = 0 if i == 0 else et[i - 1]
            next_st = endpoint if i == n - 1 else st[i + 1]

            prev_free = st[i] - prev_end
            next_free = next_st - et[i]

            total_gap = prev_free + next_free  # Combined gap without current event
            mx = max(mx, total_gap)

            # Check if skipping this event helps increase total free time
            max_outside = 0
            if i > 0:
                max_outside = max(max_outside, pre[i - 1])
            if i + 2 < m:
                max_outside = max(max_outside, suf[i + 2])

            # If some other gap is big enough to accommodate this event's time
            if max_outside >= cur_time:
                extended = total_gap + cur_time
                mx = max(mx, extended)

        return mx

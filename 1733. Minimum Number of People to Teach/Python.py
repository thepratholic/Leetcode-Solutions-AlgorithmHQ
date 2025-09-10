# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Step 1: Sort friendships just for consistency (not strictly required)
        friendships.sort(key=lambda x: (x[0], x[1]))

        pairs = []  # store friendships where users cannot communicate
        size = len(friendships)

        # Step 2: Check each friendship pair
        for i in range(size):

            first_user = friendships[i][0] - 1  # users are 1-indexed → convert to 0-index
            second_user = friendships[i][1] - 1

            fl = False  # flag to check if they already share a language

            # Step 2a: Check if they have at least one common language
            for lang in languages[first_user]:
                if lang in languages[second_user]:
                    fl = True
                    break  # they can communicate, no problem

            # Step 2b: If no common language → add to problem pairs
            if not fl:
                pairs.append([first_user, second_user])

        # Step 3: Collect all users who are in problematic pairs
        users_to_fix = set()
        for u, v in pairs:
            users_to_fix.add(u)
            users_to_fix.add(v)

        # Step 4: For each language, count how many of these "problem users"
        # already know it. We want to minimize teaching.
        maxi = 0
        for lang in range(1, n + 1):  # check every language
            count = 0
            for user in users_to_fix:
                if lang in languages[user]:
                    count += 1
            # keep track of max count = best candidate language
            maxi = max(maxi, count)

        # Step 5: Answer = total users to fix - maximum users already knowing a common language
        return len(users_to_fix) - maxi

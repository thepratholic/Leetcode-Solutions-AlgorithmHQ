# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        sum = 1  # Start with 1 candy for the first child
        i = 1

        while i < n:
            # If current rating is equal to the previous one
            if ratings[i] == ratings[i - 1]:
                sum += 1  # Give only one candy
                i += 1
                continue

            # Handle increasing slope
            peak = 1  # Peak starts at 1 (the previous child already had at least 1 candy)
            while i < n and ratings[i] > ratings[i - 1]:
                peak += 1
                sum += peak  # Give more candies as rating increases
                i += 1

            # Handle decreasing slope
            down = 1  # Start descending slope
            while i < n and ratings[i] < ratings[i - 1]:
                sum += down  # Give fewer candies going downhill
                down += 1
                i += 1

            # If the descending slope is longer than the increasing one,
            # we need to adjust the peak (since it was counted only once)
            if down > peak:
                sum += (down - peak)

        return sum
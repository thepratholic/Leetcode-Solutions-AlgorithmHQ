# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        # Iterate through numbers greater than n up to 1224444
        # (This is the largest "beautiful number" within 7 digits)
        for num in range(n + 1, 1224445):

            # Count frequency of each digit in the current number
            freq = Counter(str(num))

            # Check if the number is "beautiful":
            # A number is beautiful if each digit appears exactly
            # as many times as its own value.
            # Example: 1333 -> '1' appears 1 time, '3' appears 3 times
            if all(int(k) == v for k, v in freq.items()):
                return num  # Return the first such number found
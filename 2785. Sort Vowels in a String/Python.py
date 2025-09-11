# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import heapq

class Solution:
    def sortVowels(self, s: str) -> str:
        # Define all vowels (both uppercase and lowercase)
        vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
        n = len(s)

        # Create a temporary list of characters (final string will be built from this)
        t = [''] * n

        # Min-heap (priority queue) for storing vowels sorted by ASCII value
        pq = []

        # Step 1: Traverse the string
        for i in range(n):
            if s[i] not in vowels:
                # If it's NOT a vowel → directly put it in place
                t[i] = s[i]
            else:
                # If it's a vowel → push it into min-heap based on ASCII value
                # heapq ensures smallest ASCII value comes out first
                heapq.heappush(pq, (ord(s[i]), s[i]))

        # Step 2: Fill back vowels in sorted order from the heap
        for i in range(n):
            if t[i] == '':  # means this was originally a vowel
                ascii_val, ch = heapq.heappop(pq)  # get smallest available vowel
                t[i] = ch

        # Step 3: Join list back into a string
        return "".join(t)

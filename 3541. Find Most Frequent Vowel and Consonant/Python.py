# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Define the set of vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Count frequency of each character in the string
        freq = Counter(s)

        # Variables to store the maximum frequency among vowels and consonants
        max_vowel_freq = 0
        max_consonent_freq = 0

        # Step 1: Traverse through each character and its frequency
        for k, v in freq.items():
            if k in vowels:
                # If it's a vowel, check if its frequency is the highest seen so far
                if v > max_vowel_freq:
                    max_vowel_freq = v
            else:
                # If it's a consonant, check if its frequency is the highest seen so far
                if v > max_consonent_freq:
                    max_consonent_freq = v

        # Step 2: Return sum of highest vowel frequency + highest consonant frequency
        return max_consonent_freq + max_vowel_freq

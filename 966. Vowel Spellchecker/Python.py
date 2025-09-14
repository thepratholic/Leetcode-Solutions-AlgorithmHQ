# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import defaultdict
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Define vowels for vowel replacement rules
        vowels = set("aeiou")

        # Store original words for direct match
        wl = set(wordlist)

        # Maps for case-insensitive and vowel-error matching
        case_map = defaultdict(str)   # maps lowercase word -> first word in wordlist
        vowel_map = defaultdict(str)  # maps devoweled word -> first word in wordlist

        # Helper function to "devowel" a word:
        # Replace every vowel (a,e,i,o,u) with '*'
        def devowel(s):
            return "".join("*" if ch in vowels else ch for ch in s)

        # Step 1: Build case_map and vowel_map from wordlist
        for word in wordlist:
            w = word.lower()

            # Case-insensitive match: only store the FIRST occurrence
            if w not in case_map:
                case_map[w] = word

            # Vowel-error match: convert to devowel form
            s = devowel(w)
            if s not in vowel_map:
                vowel_map[s] = word

        ans = []

        # Step 2: Process each query
        for q in queries:
            if q in wl:
                # Case 1: Exact match → return same word
                ans.append(q)

            elif q.lower() in case_map:
                # Case 2: Case-insensitive match
                ans.append(case_map[q.lower()])

            elif devowel(q.lower()) in vowel_map:
                # Case 3: Vowel-error match
                ans.append(vowel_map[devowel(q.lower())])

            else:
                # Case 4: No match found
                ans.append("")

        return ans

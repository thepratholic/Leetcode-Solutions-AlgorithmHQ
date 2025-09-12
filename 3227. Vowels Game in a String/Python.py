# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Define a set of vowels (only lowercase as per problem statement assumption)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)   # length of the string
        v = []       # list to store vowels found in the string

        # Step 1: Traverse through the string
        for ch in s:
            if ch in vowels:
                v.append(ch)   # collect vowels

        # Step 2: If no vowels were found → Alice cannot win
        if not v:
            return False

        # Step 3: If at least one vowel exists → Alice wins
        else:
            return True

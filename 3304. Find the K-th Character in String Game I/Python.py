# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def kthCharacter(self, k: int) -> str:
        # Start with initial string as "a"
        initial = "a"

        # Keep expanding the string until its length >= k
        while len(initial) < k:
            temp = ""

            # For each character, generate its "next" character
            for ch in initial:
                # Convert character to index (0–25), increment by 1, wrap using %26, and convert back to character
                next_ch = chr(((ord(ch) - ord("a") + 1) % 26) + ord("a"))
                temp += next_ch

            # Append the generated string to the original
            initial += temp

        # Return the k-th character (1-indexed)
        return initial[k - 1]
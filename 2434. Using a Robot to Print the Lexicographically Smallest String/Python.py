# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)

        # Precompute the minimum character from the right for each position
        minCharToRight = [''] * n
        minCharToRight[-1] = s[-1]  # Last character is the minimum at the end
        for i in range(n - 2, -1, -1):
            # Store the minimum of the current character and the one on the right
            minCharToRight[i] = min(minCharToRight[i + 1], s[i])

        t = []       # Stack representing temporary string t
        paper = []   # Final result string

        # Simulate the robot operations
        for i in range(n):
            t.append(s[i])  # Push current character to t

            # Get the minimum character remaining in the rest of the string
            min_char = minCharToRight[i + 1] if i + 1 < n else s[i]

            # Keep popping from t to paper as long as the top of t is <= min_char
            while t and t[-1] <= min_char:
                paper.append(t.pop())

        # Append remaining characters in t to paper
        while t:
            paper.append(t.pop())

        return "".join(paper)  # Return the final string

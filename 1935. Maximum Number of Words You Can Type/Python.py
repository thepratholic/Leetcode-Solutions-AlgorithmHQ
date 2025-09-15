# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Split the input text into individual words
        words = text.split()

        # Variable to count how many words can be typed without broken letters
        ans = 0

        # Iterate through each word
        for word in words:
            f = True  # Assume the word is typeable initially

            # Check if any broken letter is present in the current word
            for ch in brokenLetters:
                if ch in word:   # If broken letter is found in the word
                    f = False    # The word cannot be typed
            # If word is typeable (no broken letters found), increase count
            if f:
                ans += 1

        # Return the total number of words that can be typed
        return ans

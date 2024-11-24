# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0] * 3
        n = len(s)

        # Count occurrences of 'a', 'b', and 'c' in the entire string
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        # If any of 'a', 'b', or 'c' has fewer than k occurrences, return -1 (not possible)
        for i in range(3):
            if cnt[i] < k:
                return -1

        # Initialize a window of counts for 'a', 'b', and 'c'
        window = [0] * 3
        left, max_window = 0, 0

        # Slide a window across the string to find the longest window
        for right in range(n):
            window[ord(s[right]) - ord("a")] += 1  # Add the character at the right pointer to the window

            # Shrink the window if the count of any character in the window is insufficient
            while left <= right and (cnt[0] - window[0] < k or cnt[1] - window[1] < k or cnt[2] - window[2] < k):
                window[ord(s[left]) - ord("a")] -= 1  # Remove the character at the left pointer from the window
                left += 1

            max_window = max(max_window, right - left + 1)

        return n - max_window  # Return the minimum number of characters to remove

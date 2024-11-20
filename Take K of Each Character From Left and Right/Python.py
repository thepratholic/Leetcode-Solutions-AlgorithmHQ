class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0] * 3
        n = len(s)

        for c in s:
            cnt[ord(c) - ord("a")] += 1

        for i in range(3):
            if cnt[i] < k:
                return -1

        window = [0] * 3
        left, max_window = 0, 0

        # Find the longest window
        for right in range(n):
            window[ord(s[right]) - ord("a")] += 1

            # Shrink window if we take too many characters
            while left <= right and (cnt[0] - window[0] < k or cnt[1] - window[1] < k or cnt[2] - window[2] < k):
                window[ord(s[left]) - ord("a")] -= 1
                left += 1

            max_window = max(max_window, right - left + 1)

        return n - max_window


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
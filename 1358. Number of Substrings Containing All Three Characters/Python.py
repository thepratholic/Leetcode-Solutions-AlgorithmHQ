# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastSeen = [-1] * 3  # Stores last seen indices of 'a', 'b', 'c'
        cnt = 0

        for i, ch in enumerate(s):
            lastSeen[ord(ch) - ord('a')] = i  # Update last seen index
            cnt += 1 + min(lastSeen)  # Count valid substrings ending at i

        return cnt

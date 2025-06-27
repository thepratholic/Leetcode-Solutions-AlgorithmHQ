# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)

        # Step 1: Keep only characters that occur at least 'k' times
        # These characters can potentially form a repeated subsequence
        freq = [c for c, v in Counter(s).items() if v >= k]
        freq = sorted(freq, reverse=True)  # Sort in reverse lexicographical order to get lexicographically larger subsequences first

        q = deque(freq)  # Start BFS with single-character strings that satisfy frequency >= k

        ans = ""
        
        # Step 2: BFS to generate candidates
        while q:
            cur = q.popleft()

            # Update answer if this candidate is longer than current answer
            if len(cur) > len(ans):
                ans = cur

            # Step 3: Try appending each valid character to the current string
            for ch in freq:
                nxt = cur + ch

                # Step 4: Check if `nxt` repeated k times is a subsequence of s
                # Use iterator to efficiently check subsequence
                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)  # If valid, add this new string for further exploration

        return ans

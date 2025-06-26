# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        length = 0            # Stores the length of the valid subsequence
        bits = k.bit_length() # Number of bits required to represent k in binary

        sum_ = 0              # Current binary number formed (from right to left)
        pos = 0               # Position from the right (i.e., bit index)

        # Traverse the string from the end (least significant bit)
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                # If we haven't used more bits than needed and adding this bit stays within k
                if pos < bits and sum_ + (1 << pos) <= k:
                    sum_ += (1 << pos)  # Add the current bit's value to the number
                    length += 1         # Include this '1' in the subsequence
                # else: we skip this '1' since adding it will exceed k
            else:
                # Always include '0' since it doesn't increase the value of the number
                length += 1

            pos += 1  # Move to next higher bit (to the left)

        return length

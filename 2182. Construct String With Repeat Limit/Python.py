# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from collections import Counter  # To count character frequencies
import heapq  # For max-heap operations

class Solution:
    def lastRepeatLen(self, s, currc, replen):

        n = len(s)  # Length of the result string
        # If the string is empty or the last character matches the current one, increment repeat count
        if n == 0 or currc == s[-1]:
            return replen + 1
        # Otherwise, reset the repeat count to 1
        return 1

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Count the frequency of each character in the input string
        ctr = Counter(s)  # Example: "cczazcc" -> {'c': 4, 'z': 1, 'a': 1}

        # Step 2: Initialize variables
        op = ""  # This will store the resultant string
        replen = 0  # Tracks consecutive occurrences of the last character
        heap = []  # Max-heap to store characters based on their ASCII values (negated to simulate max-heap)

        # Step 3: Push all characters into the heap with negative ASCII values (for max-heap behavior)
        for c in ctr:
            heapq.heappush(heap, (-ord(c), c))  # (-ASCII value, character)

        # Step 4: Build the resultant string
        while len(heap) > 0:  # Continue until the heap is empty
            k, currc = heapq.heappop(heap)  # Extract the largest character (lexicographically largest)

            # Skip characters that are no longer available in the counter
            while len(heap) > 0 and currc not in ctr:
                k, currc = heapq.heappop(heap)

            # Case 1: Adding the current character exceeds the repeat limit
            if self.lastRepeatLen(op, currc, replen) > repeatLimit:
                # Check if there is another character to use temporarily
                if len(heap) > 0:
                    # Use the next largest character (temporary character)
                    newk, newc = heapq.heappop(heap)
                    replen = self.lastRepeatLen(op, newc, replen)  # Reset or update repeat length
                    op += newc  # Add the temporary character to the result string

                    # Update the counter for the temporary character
                    ctr[newc] -= 1
                    if ctr[newc] == 0:  # Remove from counter if exhausted
                        del ctr[newc]
                    else:
                        heapq.heappush(heap, (newk, newc))  # Push it back to the heap

                    # Push the current character back to the heap for future use
                    heapq.heappush(heap, (k, currc))
                else:
                    # If no alternative character exists, stop building the string
                    break

            # Case 2: Adding the current character does not exceed the repeat limit
            else:
                replen = self.lastRepeatLen(op, currc, replen)  # Update repeat count
                op += currc  # Add the current character to the result string

                # Update the counter for the current character
                ctr[currc] -= 1
                if ctr[currc] == 0:  # If exhausted, remove from the counter
                    del ctr[currc]
                else:
                    heapq.heappush(heap, (k, currc))  # Push back to the heap with updated count

        # Step 5: Return the resultant string
        return op

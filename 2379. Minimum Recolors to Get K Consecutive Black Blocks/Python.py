# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)  # Length of string
        l, r = 0, k - 1  # Define window boundaries

        mini = float('inf')  # Store the minimum number of 'W' found
        whites = 0  # Count of 'W' in the current window

        # Step 1: Initialize the first window of size k
        for i in range(k):  
            if blocks[i] == "W":  # Count 'W' in the first window
                whites += 1

        mini = min(mini, whites)  # Update minimum repaint needed

        # Step 2: Slide the window across the string
        for i in range(k, n):  
            if blocks[i - k] == "W":  # Remove the leftmost element from the window
                whites -= 1
            if blocks[i] == "W":  # Add the new rightmost element
                whites += 1
            mini = min(mini, whites)  # Update the minimum repaint count

        return mini  # Return the least number of repaints needed

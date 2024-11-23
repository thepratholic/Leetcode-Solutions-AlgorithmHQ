from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Get dimensions of the box
        rows, cols = len(box), len(box[0])

        # Step 1: Simulate gravity for stones in each row
        for r in reversed(range(rows)):  # Traverse rows from bottom to top
            i = cols - 1  # Start at the rightmost available position
            for c in reversed(range(cols)):  # Traverse columns from right to left
                if box[r][c] == "#":  # If it's a stone
                    # Swap the stone with the empty space at index `i`
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1  # Move the `i` pointer to the left
                elif box[r][c] == "*":  # If it's an obstacle
                    # Reset `i` to the position just before the obstacle
                    i = c - 1

        # Step 2: Rotate the box 90 degrees clockwise
        res = []  # Initialize the result matrix
        for c in range(cols):  # Traverse each column of the box
            col = []  # Initialize a new row for the result matrix
            for r in reversed(range(rows)):  # Traverse rows in reverse order
                col.append(box[r][c])  # Add elements to the new row
            res.append(col)  # Append the new row to the result matrix

        return res  # Return the rotated matrix


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
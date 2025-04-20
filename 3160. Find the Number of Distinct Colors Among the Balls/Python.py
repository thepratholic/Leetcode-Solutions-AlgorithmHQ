# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        result = [-1] * n  # Initialize result array with -1 (will store the count of unique colors at each step)

        mpp = {}  # Dictionary to store the last assigned color for each index x
        color_count = {}  # Dictionary to keep track of how many times each color is assigned

        for i in range(n):
            x, y = queries[i][0], queries[i][1]  # Extract the x (position) and y (color) from the query

            # If x already has a color, decrement its count from color_count
            if x in mpp:
                color = mpp[x]  # Get the previously assigned color at x
                color_count[color] -= 1  # Reduce count of that color

                # If no elements remain with that color, remove it from color_count
                if color_count[color] == 0:
                    del color_count[color]

            # Assign the new color y to position x
            mpp[x] = y
            color_count[y] = color_count.get(y, 0) + 1  # Increment count of the new color

            # Store the number of distinct colors currently in the result array
            result[i] = len(color_count)

        return result

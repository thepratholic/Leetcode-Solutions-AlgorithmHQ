# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/



from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]  # Initialize the triangle with the first row [1]

        # If we need more than one row, add the second row [1, 1]
        if numRows > 1:
            result.append([1, 1])

        # Generate the rest of the rows from row 2 onwards (0-based indexing)
        for i in range(2, numRows):
            v = [1]  # Each row starts with 1

            # Compute the intermediate values using the previous row
            for j in range(1, i):
                # Each element is the sum of the two elements directly above it
                val = result[i - 1][j - 1] + result[i - 1][j]
                v.append(val)

            v.append(1)  # Each row ends with 1
            result.append(v)  # Append the current row to the result

        return result  # Return the full triangle
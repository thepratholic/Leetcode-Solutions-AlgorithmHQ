# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Initialize the final value of X as 0
        ans = 0

        # Total number of operations given
        n = len(operations)

        # Loop through each operation
        for i in range(n):
            operation = operations[i]

            # If the operation contains '--' (either '--X' or 'X--'),
            # it means we need to decrement X by 1
            if operation[0] == '-' or operation[-1] == '-':
                ans -= 1

            # If the operation contains '++' (either '++X' or 'X++'),
            # it means we need to increment X by 1
            elif operation[0] == '+' or operation[-1] == '+':
                ans += 1

        # Return the final value of X after performing all operations
        return ans

# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def can_partition(self, j, i2, target, cur):
        n = len(i2)

        if j == n:
            return cur == target  # If all digits are used, check if sum equals target

        for index in range(j, n):
            val = int(i2[j : index + 1])  # Convert substring to an integer
            if self.can_partition(index + 1, i2, target, cur + val):
                return True  # If partitioning is possible, return True

        return False  # Otherwise, return False
    
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        
        for i in range(1, n+1):
            mul = i * i  # Square of the number

            if self.can_partition(0, str(mul), i, 0):
                ans += mul  # Add square to the result if condition holds

        return ans
# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) == abs(y - z):
            return 0

        elif abs(x - z) < abs(y - z):
            return 1

        else:
            return 2
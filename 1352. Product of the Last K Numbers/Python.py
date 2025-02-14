# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]  # Stores the prefix product sequence

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # Reset the prefix product when `0` is added
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0  # If `k` exceeds available numbers, return 0
        return self.prefix[-1] // self.prefix[-k-1]

# obj = ProductOfNumbers()
# obj.add(3)  # [1, 3]
# obj.add(0)  # Reset → [1]
# obj.add(2)  # [1, 2]
# obj.add(5)  # [1, 2, 10]
# obj.add(4)  # [1, 2, 10, 40]

# print(obj.getProduct(2))  # Last 2 elements: 5 * 4 = 20
# print(obj.getProduct(3))  # Last 3 elements: 2 * 5 * 4 = 40

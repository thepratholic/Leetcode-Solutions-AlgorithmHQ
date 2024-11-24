from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)  # Initialize the result array with zeros

        if k == 0:
            # If k is 0, all elements in the result array remain 0
            return result

        for i in range(len(result)):
            if k > 0:
                # If k is positive, sum the next k elements (circularly)
                for j in range(i + 1, i + k + 1):
                    result[i] += code[j % len(code)]  # Use modulo for circular indexing
            else:
                # If k is negative, sum the previous |k| elements (circularly)
                for j in range(i - abs(k), i):
                    result[i] += code[(j + len(code)) % len(code)]  # Adjust index using modulo
        return result


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        if k == 0:
            return result
        for i in range(len(result)):
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    result[i] += code[j % len(code)]
            else:
                for j in range(i - abs(k), i):
                    result[i] += code[(j + len(code)) % len(code)]
        return result


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
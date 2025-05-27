# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n_list = []
        # Collect numbers from 1 to n that are NOT divisible by m
        for i in range(1, n + 1):
            if i % m != 0:
                n_list.append(i)

        m_list = []
        # Collect numbers from 1 to n that ARE divisible by m
        for i in range(1, n + 1):
            if i % m == 0:
                m_list.append(i)

        # Return the difference between the sum of non-divisible and divisible numbers
        return sum(n_list) - sum(m_list)
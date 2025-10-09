# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        finish_time = [0] * n

        # potion loop
        for j in range(m):

            for i in range(n):

                if i == 0:
                    finish_time[0] += (mana[j] * skill[i])

                else:
                    finish_time[i] = max(finish_time[i - 1], finish_time[i]) + (mana[j] * skill[i])

            
            # now the correction loop
            for i in range(n - 1, 0, -1):
                finish_time[i - 1] = finish_time[i] - (mana[j] * skill[i])

        return finish_time[-1]
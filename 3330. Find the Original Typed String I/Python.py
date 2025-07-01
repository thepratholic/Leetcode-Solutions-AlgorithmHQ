# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word) - 1
        cnt = 0

        for i in range(n):
            if word[i] == word[i+1]:
                cnt+=1
            else: pass
        return cnt + 1
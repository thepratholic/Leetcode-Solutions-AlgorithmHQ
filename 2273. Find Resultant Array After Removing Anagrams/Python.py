# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]

        def check(s1, s2):
            cnt = [0] * 26

            for ch in s1:
                cnt[ord(ch) - ord('a')] += 1

            for ch in s2:
                cnt[ord(ch) - ord('a')] -= 1

            for i in cnt:
                if i != 0:
                    return False

            return True


        for i in range(1, len(words)):
            prev, cur = ans[-1], words[i]
            if not check(prev, cur):
                ans.append(cur)

        return ans
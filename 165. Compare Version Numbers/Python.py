# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # splitting both the strings into list on the basis of .
        v1 = version1.split(".") 
        v2 = version2.split(".")
        
        n = len(v1)
        m = len(v2)

        if n < m: # the list which has less number of revisions, we will add 0 to it
            v1 += ['0'] * (m - n)
        else:
            v2 += ['0'] * (n - m)

        for a, b in zip(v1, v2): # we will compare revision by revision from both the strings 
            x, y = int(a), int(b)

            if x < y:
                return -1 # return -1 if revision from version1 < version2

            elif x > y:
                return 1 # return 1 if revision from version1 > version2

        return 0 # return 0 if all revisions from version1 == version2
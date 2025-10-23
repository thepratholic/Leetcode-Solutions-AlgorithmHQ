# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        tmp = s
        while len(tmp) > 2:
            ans = [] # reset each time ans list
            for i in range(len(tmp) - 1): # traverse the numbers
                first = int(tmp[i])
                second = int(tmp[i + 1])

                ans.append((first + second) % 10) # append the ans by doing modulo 10 in ans list

            tmp = "".join(str(x) for x in ans) # after finishing the

        return tmp[0] == tmp[-1] # check wheather the last two elements are equal or not
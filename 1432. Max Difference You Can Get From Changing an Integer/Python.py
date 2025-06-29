# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def maxDiff(self, num: int) -> int:
        maxi, mini = str(num), str(num)

        for digit in maxi:
            if digit != "9":
                maxi = maxi.replace(digit, "9")
                break


        for i, d in enumerate(mini):
            if i == 0:
                if d != "1":
                    mini = mini.replace(d, "1")
                    break

            else:
                if d != "0" and d != mini[0]:
                    mini = mini.replace(d, "0")
                    break

        return int(maxi) - int(mini)
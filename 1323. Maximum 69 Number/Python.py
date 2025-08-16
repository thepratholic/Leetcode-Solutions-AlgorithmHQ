# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num) # convert into string for looping into it
        temp = ""

        f = False
        for i in range(len(num)):
            if num[i] == '6' and not f: # for the very first 6 coming in num, convert it into 9 and then make flag = True 
                temp += '9'
                f = True
            else:
                temp += num[i] # copy other characters as same

        num = int(temp) # convert the string into integer for returning it in answer 
        return num # returning the answer
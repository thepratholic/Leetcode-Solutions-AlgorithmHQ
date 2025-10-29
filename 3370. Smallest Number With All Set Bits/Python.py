# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def smallestNumber(self, n: int) -> int:

        def check(num):
            return (num & (num + 1)) == 0 # helper function to check wheather all bits are set or not

        result = n # initial answer starts from here
        while not check(result): # if the particular number is not have all set bits, then increment the result
            result += 1

        return result # return the first number whose all bits are set 
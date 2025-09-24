# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        # Case 1: If numerator is divisible by denominator, just return the integer result
        if n % d == 0:
            return str(n // d)

        ans = []

        # Case 2: If result is negative → check using XOR (^)
        # XOR means if exactly one of them is negative, result is negative
        if (n < 0) ^ (d < 0):
            ans.append("-")

        # Work with absolute values (handle sign separately above)
        n, d = abs(n), abs(d)

        # Append integer part of the division
        ans.append(str(n // d))
        ans.append(".")  # Decimal point

        # Start handling fractional part
        r = n % d  # remainder
        mpp = {}   # map to store remainder → index in ans

        # Keep dividing until remainder becomes 0 or repeats
        while r != 0:
            # If remainder repeats, it means decimal is recurring
            if r in mpp.keys():
                idx = mpp[r]   # position where repeating remainder first occurred
                ans.insert(idx, "(")  # insert '(' at that index
                ans.append(")")       # append ')' at the end
                break

            # Store remainder position in ans list
            mpp[r] = len(ans)

            r *= 10  # Bring down a zero (long division)
            ans.append(str(r // d))  # Quotient digit
            r %= d  # Update remainder

        # Join list into a string and return
        return "".join(ans)

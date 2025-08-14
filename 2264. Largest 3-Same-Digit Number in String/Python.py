# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""             # To store the largest "good" integer found
        n = len(num)         # Length of the string number
        l, r = 0, 2          # Left and right pointers for checking 3-digit windows

        maxi = float('-inf') # Keeps track of the largest digit found among triples

        # Loop while the right pointer is within bounds
        while r < n:
            # Check if we have three identical consecutive digits
            if (int(num[l]) == int(num[l + 1]) == int(num[l + 2])) and int(num[l]) > maxi:
                ans = ""  # Reset answer since we found a bigger good integer
                ans += num[l] + num[l + 1] + num[l + 2]  # Append the three identical digits
                maxi = int(num[l])  # Update max digit value

            else:
                # Move the window forward
                r += 1
                l += 1

        return ans  # Return the largest good integer as a string

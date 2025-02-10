# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)  # Get the length of the input string
        
        stack = []  # Stack to store characters
        
        for i in range(n):  # Iterate through each character in the string
            if s[i].isalpha():  # If the character is an alphabet (letter)
                stack.append(s[i])  # Push it onto the stack
            
            elif s[i].isdigit():  # If the character is a digit
                if stack:  # Ensure the stack is not empty before popping
                    stack.pop()  # Remove the last added letter

        # Convert the stack back to a string and return it
        return "".join(stack) if stack else ""

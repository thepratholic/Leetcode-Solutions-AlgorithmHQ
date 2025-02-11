# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def is_match(self, stack, part_len, part): #helper function to check wheather last elements of length equal to part are equal to part string or not
        return "".join(stack[-part_len:]) == part

    def removeOccurrences(self, s: str, part: str) -> str:

        stack = []  # Stack to store characters while processing the string

        part_len = len(part)  # Length of the target substring to be removed

        for i in s:  # Iterate through each character in the string `s`
            stack.append(i)  # Push the current character onto the stack

            # If the last `part_len` characters in the stack match `part`, remove them
            if len(stack) >= part_len and self.is_match(stack, part_len, part):
                for _ in range(part_len):  # Remove `part_len` elements from the stack
                    stack.pop()

        return "".join(stack)  # Convert the final stack into a string and return

# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head) -> int:
        ans = 0
        res = []
        temp = head

        # Traverse the linked list and collect all node values (binary digits) in a list
        while temp is not None:
            res.append(temp.val)
            temp = temp.next

        # Reverse the list so we can process from least significant bit to most
        res.reverse()

        # Convert binary to decimal by summing powers of 2
        for i in range(len(res)):
            if res[i] == 1:
                ans += (2 ** i)

        return ans

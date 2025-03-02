# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/


from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)  # Length of the first list
        m = len(nums2)  # Length of the second list

        res = []  # Result list to store merged arrays
        ptr1, ptr2 = 0, 0  # Pointers for iterating nums1 and nums2

        # Merge process using two-pointer technique
        while ptr1 < n and ptr2 < m:
            id1, id2 = nums1[ptr1][0], nums2[ptr2][0]  # Extracting IDs
            val1, val2 = nums1[ptr1][1], nums2[ptr2][1]  # Extracting values

            if id1 == id2:  # If both IDs are the same, sum the values
                res.append([id1, val1 + val2])
                ptr1 += 1
                ptr2 += 1  # Move both pointers

            elif id1 < id2:  # If ID from nums1 is smaller, add it to result
                res.append([id1, val1])
                ptr1 += 1  # Move pointer in nums1

            else:  # If ID from nums2 is smaller, add it to result
                res.append([id2, val2])
                ptr2 += 1  # Move pointer in nums2

        # If there are remaining elements in nums1, add them to result
        while ptr1 < n:
            id1, val1 = nums1[ptr1][0], nums1[ptr1][1]
            res.append([id1, val1])
            ptr1 += 1

        # If there are remaining elements in nums2, add them to result
        while ptr2 < m:
            id2, val2 = nums2[ptr2][0], nums2[ptr2][1]
            res.append([id2, val2])
            ptr2 += 1

        return res

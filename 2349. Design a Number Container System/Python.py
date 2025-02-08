# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from sortedcontainers import SortedSet  # Importing SortedSet for efficient ordered index storage

class NumberContainers:
    def __init__(self):
        # Dictionary mapping numbers to their sorted set of indices
        self.min_indexes = {}
        # Dictionary mapping indices to their assigned numbers
        self.mpp = {}

    def change(self, index: int, number: int) -> None:
        # If index is already assigned to a different number, remove it from the old number's index set
        if index in self.mpp:
            prev = self.mpp[index]  # Retrieve previous number at this index
            if prev in self.min_indexes:
                self.min_indexes[prev].discard(index)  # Remove index from old number's sorted set

        # Update the index with the new number
        self.mpp[index] = number

        # Ensure the number has an associated SortedSet
        if number not in self.min_indexes:
            self.min_indexes[number] = SortedSet()

        # Add the index to the new number's sorted set
        self.min_indexes[number].add(index)

    def find(self, number: int) -> int:
        """
        Returns the smallest index at which the given number is present. 
        If the number is not found, return -1.
        """
        if number not in self.min_indexes or not self.min_indexes[number]:
            return -1  # Number not present in any index

        return next(iter(self.min_indexes[number]))  # Return the smallest index stored in SortedSet


# Example usage:
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)

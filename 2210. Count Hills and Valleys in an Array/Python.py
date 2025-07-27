# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        # First remove consecutive duplicates
        arr = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                arr.append(nums[i])

        # Now check for hills and valleys
        count = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                count += 1  # Hill
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                count += 1  # Valley

        return count

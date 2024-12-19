# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)  # Total number of items
        answer = prices[:]  # Create a copy of prices to store the final results

        # Iterate through each item's price
        for i in range(n):
            # Check for the first item after 'i' with a price <= prices[i]
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    # Apply the discount to the current item's price
                    answer[i] = prices[i] - prices[j]
                    break  # Stop searching as we found the first valid discount

        # Return the final prices list after applying discounts
        return answer

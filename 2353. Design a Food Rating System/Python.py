# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List
from sortedcontainers import SortedList   # SortedList keeps elements sorted automatically


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Map each food → its cuisine
        self.food_to_cuisine = defaultdict(str)

        # Map each food → its rating
        self.food_to_rating = defaultdict(str)

        # Map each cuisine → SortedList of ( -rating, food )
        # Why -rating?  → because SortedList sorts in ascending order,
        # so by storing negative ratings, the largest rating comes first
        # If ratings are same, then food name lexicographically decides the order
        self.mpp = defaultdict(SortedList)

        # Fill the maps with initial data
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            self.mpp[c].add((-r, f))   # insert (-rating, food) into cuisine's SortedList


    def changeRating(self, food: str, newRating: int) -> None:
        # Get cuisine of the given food
        cuisine_of_food = self.food_to_cuisine[food]

        # Get old rating of this food
        old_rating = self.food_to_rating[food]

        # Remove old entry from the cuisine's SortedList
        self.mpp[cuisine_of_food].remove((-old_rating, food))

        # Insert new rating with same food
        self.mpp[cuisine_of_food].add((-newRating, food))

        # Update food's rating in the food_to_rating map
        self.food_to_rating[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        # Since SortedList is sorted by (-rating, food), 
        # the first element is always the highest-rated (and lexicographically smallest if tie)
        return self.mpp[cuisine][0][1]


# Example usage:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

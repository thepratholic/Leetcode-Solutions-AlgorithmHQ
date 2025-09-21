from collections import defaultdict
from sortedcontainers import SortedSet

class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]):
        # available[movie] → SortedSet of (price, shop) for that movie
        self.available = defaultdict(SortedSet) 
        
        # movie_to_price[movie] → SortedSet of (shop, price)
        # helps quickly find price of movie at a given shop
        self.movie_to_price = defaultdict(SortedSet) 
        
        # rented → SortedSet of (price, shop, movie)
        # maintains rented movies globally, sorted by (price, shop, movie)
        self.rented = SortedSet() 

        # Initialize system with all available movies
        for shop, movie, price in entries:
            self.available[movie].add((price, shop))
            self.movie_to_price[movie].add((shop, price))

    def search(self, movie: int) -> list[int]:
        """
        Returns up to 5 shops (lowest price, then lowest shop index)
        that currently have the given movie available.
        """
        res = []
        cnt = 0

        if movie in self.available:
            # available[movie] is already sorted by (price, shop)
            for price, shop in self.available[movie]:
                res.append(shop)
                cnt += 1
                if cnt == 5:
                    break

        return res

    def rent(self, shop: int, movie: int) -> None:
        """
        Rent a movie from a given shop (remove from available, add to rented).
        """
        # Find (shop, price) for this movie
        it_index = self.movie_to_price[movie].bisect_left((shop, -1))
        if it_index < len(self.movie_to_price[movie]):
            shop_key, price = self.movie_to_price[movie][it_index]

            if shop_key == shop: 
                # Remove from available pool
                self.available[movie].discard((price, shop))
                # Add to rented pool
                self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        """
        Return a rented movie back to available.
        """
        # Find (shop, price) for this movie
        it_index = self.movie_to_price[movie].bisect_left((shop, -1))
        if it_index < len(self.movie_to_price[movie]):
            shop_key, price = self.movie_to_price[movie][it_index]

            if shop_key == shop:
                # Add back to available pool
                self.available[movie].add((price, shop))
                # Remove from rented pool
                self.rented.discard((price, shop, movie))

    def report(self) -> list[list[int]]:
        """
        Return up to 5 rented movies sorted by (price, shop, movie).
        Each entry = [shop, movie].
        """
        res = []
        cnt = 0
        for price, shop, movie in self.rented:
            res.append([shop, movie])
            cnt += 1
            if cnt == 5:
                break
        return res

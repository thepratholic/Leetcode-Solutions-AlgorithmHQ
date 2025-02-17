# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def helper(self, tiles, ans, cur, used):
        if cur:
            ans.add(cur)  # Add the current sequence to the set

        for i in range(len(tiles)):
            if used[i]:  # Skip if the tile is already used
                continue

            used[i] = True  # Mark the tile as used
            self.helper(tiles, ans, cur + tiles[i], used)  # Recur with new sequence
            used[i] = False  # Backtrack to try other sequences

    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()  # Stores unique sequences
        used = [False] * len(tiles)  # Tracks used tiles
        self.helper(tiles, ans, "", used)
        return len(ans)

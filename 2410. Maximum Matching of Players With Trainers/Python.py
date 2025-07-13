# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sort both players and trainers by their strength/capacity
        players.sort()
        trainers.sort()

        n, m = len(players), len(trainers)

        i, j = 0, 0  # i: player index, j: trainer index
        ans = 0      # count of successful matches

        # Iterate over both arrays to find matches
        while i < n and j < m:
            # If current trainer can handle current player
            if players[i] <= trainers[j]:
                ans += 1   # successful match
                i += 1     # move to next player
                j += 1     # move to next trainer
            else:
                j += 1     # trainer can't handle player, try next trainer

        return ans  # total matched player-trainer pairs

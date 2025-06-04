class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # If only 1 friend, the entire string is the only choice
        if numFriends == 1:
            return word

        n = len(word)
        maxi = ""
        m = n - numFriends + 1  # Number of characters each friend will get

        # Try all substrings of length m and take the lexicographically largest
        for i in range(n):
            maxi = max(maxi, word[i:i + m])

        return maxi

# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict

class Solution:
    # DFS to find the lexicographically smallest character in the connected component
    def dfs(self, adj, ch, vis):
        vis[ord(ch) - ord("a")] = True  # Mark current character as visited
        mini = ch  # Start with current character as the minimum

        # Visit all neighbors
        for v in adj[ch]:
            if not vis[ord(v) - ord("a")]:
                candidate = self.dfs(adj, v, vis)  # DFS on unvisited neighbor
                if candidate < mini:  # Keep track of smallest character found
                    mini = candidate

        return mini  # Return the smallest character in the component

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)  # Adjacency list to represent graph of character equivalence

        # Build the graph: add edges between equivalent characters
        for u, v in zip(s1, s2):
            adj[u].append(v)
            adj[v].append(u)

        result = []

        # For each character in baseStr, find the smallest equivalent character
        for ch in baseStr:
            vis = [False] * 26  # Reset visited array for every character
            smallest_char = self.dfs(adj, ch, vis)  # Perform DFS to find smallest equivalent
            result.append(smallest_char)  # Append result

        return ''.join(result)  # Join characters to form the final transformed string

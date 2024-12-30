# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/thepratholic/


from typing import List

class Solution:
    # Function to calculate the diameter of a tree
    def diameter(self, edges):
        # Number of nodes in the tree
        n = len(edges) + 1
        
        # Build an adjacency list representation of the tree
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Array to store the subtree sizes for each node
        sizes = [0] * n
        
        # DFS to calculate subtree sizes
        def dfs(i, prev):
            sizes[i] = 100  # Set a base size (arbitrary value 100 in this case)
            for j in graph[i]:
                if j != prev:  # Avoid revisiting the parent node
                    sizes[i] += dfs(j, i)  # Add the size of the child subtree
            return sizes[i]
        
        # Calculate the total size of the tree starting from node 0
        total = dfs(0, -1)
        
        # Function to find the centroid of the tree
        def getcentroid(i, prev, total):
            for j in graph[i]:
                # If a child subtree size is greater than half the total size, move to it
                if j != prev and sizes[j] > total // 2:
                    return getcentroid(j, i, total)
            return i  # Return the current node as the centroid
        
        # Find the centroid of the tree
        centroid = getcentroid(0, -1, total)
        
        # Function to calculate the longest path from a given node
        def longest(i, prev):
            res = 1  # Base case: path length is at least 1 (the node itself)
            for j in graph[i]:
                if j != prev:  # Avoid revisiting the parent node
                    res = max(res, 1 + longest(j, i))  # Update the longest path
            return res
        
        # Calculate the longest paths from the centroid
        a = b = 0  # Store the two longest paths
        for j in graph[centroid]:
            # Update the two longest paths using the children of the centroid
            temp, a, b = sorted([a, b, longest(j, centroid)])
        
        # Return the sum of the two longest paths as the diameter
        return a + b
    
    # Function to calculate the minimum diameter after merging two trees
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Calculate the diameter of the first tree
        a = self.diameter(edges1)
        
        # Calculate the diameter of the second tree
        b = self.diameter(edges2)
        
        # Calculate the minimum possible diameter after merging the trees
        return max(
            a,  # Original diameter of the first tree
            b,  # Original diameter of the second tree
            (a + 1) // 2 + (b + 1) // 2 + 1  # Merged tree diameter
        )

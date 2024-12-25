# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    # Function to find the largest value in each row (level) of a binary tree
    def largestValues(self, root):
        # Dictionary to store the largest value for each level
        mvals = {}
        
        # Stack to perform iterative DFS, storing nodes along with their level
        nodes = [(root, 0)]
        
        # Variable to track the maximum level encountered in the tree
        mlevel = -1
        
        # Iterative Depth-First Search (DFS)
        while len(nodes) > 0:
            # Pop the current node and its level from the stack
            curr, l = nodes.pop()
            
            if curr:  # Process the node if it exists
                # Update the maximum level seen so far
                mlevel = max(mlevel, l)
                
                # Update the largest value for the current level
                mvals[l] = max(mvals.get(l, float('-inf')), curr.val)
                
                # Add the left and right child nodes to the stack with incremented level
                nodes.append((curr.left, l + 1))
                nodes.append((curr.right, l + 1))
        
        # Return a list of largest values for each level, in order
        return [mvals[l] for l in range(mlevel + 1)]

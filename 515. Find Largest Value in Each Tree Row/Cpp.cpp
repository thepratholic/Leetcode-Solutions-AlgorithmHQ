Contributed by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 

1 : Level Order Traversal:
Use a queue to traverse the tree level by level (Breadth-First Search).

2 : Find Maximum in Each Level
3 : Store the Maximum Value:

class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        if (!root) return {}; // Handle the case where root is null

        vector<int> result;
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int qSize = q.size();
            int maxVal = INT_MIN;

            while (qSize--) {
                TreeNode* currentNode = q.front();
                q.pop();
                maxVal = max(maxVal, currentNode->val);

                if (currentNode->left) q.push(currentNode->left);
                if (currentNode->right) q.push(currentNode->right);
            }

            result.push_back(maxVal);
        }

        return result;
    }
};


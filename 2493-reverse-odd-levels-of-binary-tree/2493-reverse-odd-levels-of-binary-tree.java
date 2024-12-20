/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode reverseOddLevels(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        boolean odd = false;
        while(!q.isEmpty()) {
            int size = q.size();
            List<TreeNode> nodes = new ArrayList<>();
            for(int i=0; i<size; i++) {
                TreeNode node = q.remove();
                nodes.add(node);
                if(node.left!=null) q.add(node.left);
                if(node.right!=null) q.add(node.right);
            }
            if(odd) reverse(nodes);
            odd = !odd;
        }
        return root;
    }

    private void reverse(List<TreeNode> nodes) {
        int start = 0, end = nodes.size()-1;
        while(start<end) {
            int temp = nodes.get(start).val;
            nodes.get(start).val = nodes.get(end).val;
            nodes.get(end).val = temp;
            start+=1;
            end-=1;
        }
    }
}
class Solution {
    public TreeNode reverseOddLevels(TreeNode root) {
        // create queue to implement level order traversal
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        boolean odd = false;
        while(!q.isEmpty()) {
            int size = q.size();
            // make a list of nodes at every level
            List<TreeNode> nodes = new ArrayList<>();
            // iterate over the nodes at a particular level
            for(int i=0; i<size; i++) {
                TreeNode node = q.remove();
                nodes.add(node);
                if(node.left!=null) q.add(node.left);
                if(node.right!=null) q.add(node.right);
            }
            // reverse node values if level is odd
            if(odd) reverse(nodes);
            // toggle odd flag at every iteration
            odd = !odd;
        }
        return root;
    }

    private void reverse(List<TreeNode> nodes) {
        int start = 0, end = nodes.size()-1;
        // reverse values using two pointer swapping
        while(start<end) {
            int temp = nodes.get(start).val;
            nodes.get(start).val = nodes.get(end).val;
            nodes.get(end).val = temp;
            start+=1;
            end-=1;
        }
    

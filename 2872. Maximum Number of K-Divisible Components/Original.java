class Solution {
    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] nbrs = new int[n];
        for(int i=0; i<n; i++) adj.add(new ArrayList<>());
        // convert edges to adjacency list
        for(int[] edge: edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i=0; i<n; i++) {
            // nbrs contain number of unprocessed neighbors
            nbrs[i] = adj.get(i).size();
            // add leaf nodes to the queue
            if(nbrs[i]==1) q.add(i);
        }
        int ans = 0;
        // bfs flow
        while(!q.isEmpty()) {
            int node = q.remove();
            nbrs[node]-=1;
            // value at any node represents sum of itself and leaf nodes, check if its divisible by k to make a split
            if(values[node]%k==0) ans+=1;
            for(int nbr: adj.get(node)) {
                // check if neighbor is unprocessed
                if(nbrs[nbr]!=0) {
                    values[nbr]+=(values[node]%k);
                    // add to queue if nbr becomes a leaf node after the processing of this node
                    if(--nbrs[nbr]==1) q.add(nbr);
                }
            }
        }
        // ans is atleast 1 as number of nodes is >=1
        return ans==0?1:ans;
    }
}

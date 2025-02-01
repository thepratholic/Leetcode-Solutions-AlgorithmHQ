class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int[] degree = new int[graph.length];
        List<List<Integer>> adj = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        List<Integer> ans = new ArrayList<>();
        for(int i=0; i<graph.length; i++) {
            adj.add(new ArrayList<>());
        }
        // graph reversal
        for(int i=0; i<graph.length; i++) {
            for(int nbr: graph[i]) {
                degree[i]+=1;
                adj.get(nbr).add(i);
            }
        }
        // add terminal nodes to the queue
        for(int i=0; i<graph.length; i++) {
            if(degree[i]==0) q.add(i);
        }
        while(!q.isEmpty()) {
            int curr = q.remove();
            // add terminal nodes to answer
            ans.add(curr);
            for(int nbr: adj.get(curr)) {
                degree[nbr]-=1;
                // add newly converted terminal nodes
                if(degree[nbr]==0) q.add(nbr);
            }
        }
        Collections.sort(ans);
        return ans;
    }
}

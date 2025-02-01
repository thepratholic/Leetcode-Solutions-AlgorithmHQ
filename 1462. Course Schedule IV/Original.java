class Solution {
    public List<Boolean> checkIfPrerequisite(int n, int[][] prerequisites, int[][] queries) {
        int[] indegree = new int[n];
        List<List<Integer>> adj = new ArrayList<>();
        for(int i=0; i<n; i++) adj.add(new ArrayList<>());
        for(int[] p: prerequisites) {
            adj.get(p[0]).add(p[1]);
            indegree[p[1]]+=1;
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i=0; i<n; i++){
            if(indegree[i]==0) q.add(i);
        }
        // store prerequisites in sets to check in O(1)
        List<Set<Integer>> prs = new ArrayList<>();
        for(int i=0; i<n; i++) {
            prs.add(new HashSet<>());
        }
        while(!q.isEmpty()) {
            int curr = q.remove();
            for(int nbr: adj.get(curr)) {
                // direct prerequisites
                prs.get(nbr).add(curr);
                // indirect prequisites
                prs.get(nbr).addAll(prs.get(curr));
                indegree[nbr]-=1;
                if(indegree[nbr]==0) q.add(nbr);
            }
        }
        List<Boolean> ans = new ArrayList<>();
        for(int i=0; i<queries.length; i++) {
            // use prs to check if a course is a prerequisite of another
            ans.add(prs.get(queries[i][1]).contains(queries[i][0]));
        }
        return ans;
    }
}

class Solution {
    public int countServers(int[][] grid) {
        int m=grid.length, n=grid[0].length;
        int[] rowServers = new int[m];
        int[] colServers = new int[n];
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                // store total number of servers in each row
                if(grid[i][j]==1) {
                    rowServers[i]+=1;
                    colServers[j]+=1;
                }
            }
        }
        int ans = 0;
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                // check if row or column has more than 1 server for each server
                if(grid[i][j]==1 && (rowServers[i]>1 || colServers[j]>1)) {
                    ans+=1;
                }
            }
        }
        return ans;
    }
}

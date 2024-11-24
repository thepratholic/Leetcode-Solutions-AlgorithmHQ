contributed by : Sundaram Agnihotri
Likedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 

1 : Create a m×n grid with . (unoccupied cells).

2 : Place G for guards and W for walls based on the input.

3 : For each guard, use a helper function to mark all visible cells in the four directions (north, south, east, west) as V (guarded).

4 : Stop marking when encountering a wall (W) or another guard (G).

5 : Iterate over the grid and count cells that remain . (unoccupied and unguarded).

6 : Return the count of unguarded cells

class Solution {
public:
    void helper(int r, int c, vector<vector<char>>& grid) {
        for (int i = r - 1; i >= 0; i--) {
            if (grid[i][c] == 'G' || grid[i][c] == 'W') break;
            grid[i][c] = 'V';
        }
        for (int i = r + 1; i < grid.size(); i++) {
            if (grid[i][c] == 'G' || grid[i][c] == 'W') break;
            grid[i][c] = 'V';
        }
        for (int i = c - 1; i >= 0; i--) {
            if (grid[r][i] == 'G' || grid[r][i] == 'W') break;
            grid[r][i] = 'V';
        }
        for (int i = c + 1; i < grid[0].size(); i++) {
            if (grid[r][i] == 'G' || grid[r][i] == 'W') break;
            grid[r][i] = 'V';
        }
    }

    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<char>> grid(m, vector<char>(n, '.'));
        for (auto& guard : guards) {
            grid[guard[0]][guard[1]] = 'G';
        }
        for (auto& wall : walls) {
            grid[wall[0]][wall[1]] = 'W';
        }
        for (auto& guard : guards) {
            helper(guard[0], guard[1], grid);
        }
        int ans = 0;
        for (auto& row : grid) {
            for (auto cell : row) {
                if (cell == '.') {
                    ans++;
                }
            }
        }
        return ans;
    }
};


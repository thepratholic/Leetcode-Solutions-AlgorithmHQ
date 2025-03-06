// Contributed by Pratham Chelaramani (Student)
// LinkedIn: https://www.linkedin.com/in/thepratholic/

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>> &grid)
    {
        vector<int> ans;
        int repeat = 0, n = grid.size();

        // Flatten the 2D grid into a 1D array
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                ans.push_back(grid[i][j]);
            }
        }

        // Count frequency of each number
        unordered_map<int, int> freq;
        for (int num : ans)
        {
            freq[num]++;
        }

        // Find the repeated number
        for (auto &p : freq)
        {
            if (p.second == 2) // If a number appears twice, it's the repeated number
            {
                repeat = p.first;
                break;
            }
        }

        // Calculate expected sum using the formula for sum of first N natural numbers
        int expectedSum = (n * n * (n * n + 1)) / 2;
        int actualSum = accumulate(ans.begin(), ans.end(), 0); // Sum of all elements in the grid

        // Find the missing number
        int missing = repeat + (expectedSum - actualSum);
        
        return {repeat, missing}; // Return [repeated number, missing number]
    }
};

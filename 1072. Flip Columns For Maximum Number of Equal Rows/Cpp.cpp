Cotriuted by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 

1 : For each row, determine its "pattern" relative to the first element:
   
  a : If an element matches the first element, record 'T' (True).
  b : Otherwise, record 'F' (False).

2 : This pattern represents how the row can be flipped into a row with all equal values
3 : Use a hash map to store the frequency of each unique pattern across all rows.
4 : The maximum frequency of any pattern in the hash map gives the maximum number of rows that can have all values equal after flipping columns.
5 : Return the highest frequency as the result.

#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        unordered_map<string, int> patternFrequency;

        for (const auto& row : matrix) {
            string pattern;
            for (int col = 0; col < row.size(); ++col) {
                pattern += (row[0] == row[col] ? 'T' : 'F');
            }
            patternFrequency[pattern]++;
        }

        int maxFrequency = 0;
        for (const auto& entry : patternFrequency) {
            maxFrequency = max(maxFrequency, entry.second);
        }

        return maxFrequency;
    }
};

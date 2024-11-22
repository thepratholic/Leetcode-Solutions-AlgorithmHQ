Cotriuted by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

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

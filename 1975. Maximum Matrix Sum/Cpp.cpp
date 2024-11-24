Contributed by : Sundaram (student)
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 
1 : Compute the sum of the absolute values of all elements in the matrix (totalSum)
2 : Identify the smallest absolute value in the matrix (minAbsVal).
3 : Count how many elements in the matrix are negative (negativeCount).
4 : If negativeCount is even, all elements can be made positive, and totalSum is the result.
5 : If negativeCount is odd, one negative element must remain. Subtract twice the smallest absolute value from totalSum to maximize the sum.

class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long totalSum = 0;
        int minAbsVal = INT_MAX, negativeCount = 0;
        
        for (auto& row : matrix) {
            for (auto val : row) {
                totalSum += abs(val);
                if (val < 0) {
                    negativeCount++;
                }
                minAbsVal = min(minAbsVal, abs(val));
            }
        }
        
        if (negativeCount % 2 != 0) {
            totalSum -= 2 * minAbsVal;
        }
        
        return totalSum;
    }
};

Contributed by : Sundaram Agnihotri (student)
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 

1 : Calculate Total Sum: Compute the total sum of the array, totalSum.

2 : Iterate Through the Array:

a : Maintain a running leftSum starting from 0.
b : Update totalSum to represent the right sum as elements are added to leftSum.
c : Check Condition: At each index i (up to n-2), check if leftSum >= totalSum.
d : If true, increment the count of valid splits.

class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        long long leftSum = 0, totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int count = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            leftSum += nums[i];
            totalSum -= nums[i];
            if (leftSum >= totalSum) {
                count++;
            }
        }

        return count;
    }
};


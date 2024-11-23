Contributed by : Sundaram Agnihotri (Student)
Linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approah : 

1 : Sort the array nums to facilitate efficient range queries using binary search.

2 : For each element nums[i], consider it as the first element of a pair.

3 : Use binary search to find:
  a : low: The first index where the sum nums[i]+nums[j]≥lower.
  b : up: The first index where nums[i]+nums[j]>upper.

4 : Add the number of indices in the range [low, up) to the result.

class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        long long result = 0;
        for (int i = 0; i < n; i++) {
            auto low = lower_bound(nums.begin() + i + 1, nums.end(), lower - nums[i]);
            auto up = upper_bound(nums.begin() + i + 1, nums.end(), upper - nums[i]);           
            
            result += (0LL + (up - low));
        }
        return result;
    }
};

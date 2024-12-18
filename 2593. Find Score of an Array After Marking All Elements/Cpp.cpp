Contributed by : Sundaram Agnihotri (student)
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

class Solution {
public:
    long long findScore(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int, int>> copy(n);
        for (int i = 0; i < n; i++) {
            copy[i] = {nums[i], i};
        }
        sort(copy.begin(), copy.end());
        long long res = 0;
        for (int i = 0; i < n; i++) {
            int element = copy[i].first;
            int ind = copy[i].second;
            if (nums[ind] < 0) continue;
            res += nums[ind];
            nums[ind] = -nums[ind];
            if (ind - 1 >= 0 && nums[ind - 1] > 0) {
                nums[ind - 1] = -nums[ind - 1];
            }
            if (ind + 1 < n && nums[ind + 1] > 0) {
                nums[ind + 1] = -nums[ind + 1];
            }
        }
        return res;
    }
};

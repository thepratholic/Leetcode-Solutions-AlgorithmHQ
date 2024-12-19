Contributed by : Sundaram Agnihotri (student)
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

/* Approach 1 : Brute Force
Consider all subarrays. Find min, max and check if diff is <=2
Time : O(n^2)
Space : O(1)
*/

class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        int n = nums.size();
        long long int ans = 0;
        for(int i=0; i<n; i++){
            int minimum = INT_MAX;
            int maximum = INT_MIN;
            for(int j=i; j<n; j++){
                minimum = min(minimum, nums[j]);
                maximum = max(maximum, nums[j]);
                if(maximum - minimum <= 2)
                    ans++;
            }
        }
        return ans;
    }
};

/* Approach : Sliding Window + Monotonic queues
1. Maintain maxQ -> monotonic decreasing queue - store largest element at front 
for max element of current window
2. Maintain minQ -> monotonic increasing queue - store smallest element at front
for min element of current window
3. Use sliding window technique to maintain a valid window with given constraints
4. Add valid window size r-l+1 to ans
Time : O(n)
Space : O(n)
*/

class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        deque<int> maxQ;    // monotonic decreasing queue - {5 , 3 , 2, 1}
        deque<int> minQ;    // monotonic increasing queue - {1, 2, 5}
        int l=0, r=0;       //sliding window parameters
        while(r<n){
            // maintain monotonicity of maxQ and minQ including rth element
            while(!maxQ.empty() && nums[r] > maxQ.back())
                maxQ.pop_back();
            while(!minQ.empty() && nums[r] < minQ.back())
                minQ.pop_back();

            // insert rth element in queues
            maxQ.push_back(nums[r]);
            minQ.push_back(nums[r]);

            // shrink left side based on given condition after including rth element
            while(maxQ.front() - minQ.front() > 2){
                // update maxQ, minQ and left boundary 
                if(nums[l] == maxQ.front())     // if lth element is max of this window
                    maxQ.pop_front();
                if(nums[l] == minQ.front())     // if lth element is min of this window
                    minQ.pop_front();
                l++;
            }
            ans += r - l + 1;                   // update ans
            r++;                                // expand right side
        }
        return ans;
    }
};

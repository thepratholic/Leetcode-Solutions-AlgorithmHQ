Contributed by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 

1 : As the elements are given in strictly increasing order , and the present element is the sum of its last two previous
2 : To find the previous elements , I have to keep the searching in map to find its index
3 : If the element is present in map and its index is less than present element index
4 : It means then 
     dp[j][i] = dp[previndex][j] + 1;
     means adding thw 1 into previous sequence length



class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        unordered_map<int,int>indexing;  // for indexing the element wth index;
        //by default there is at least 2 elements honge fibonacci
        int n = arr.size();
        vector<vector<int>>dp(n,vector<int>(n,2));

        

        for(int i=0;i<n;i++){
            indexing[arr[i]] = i;  ///mapping
        }

        int maxi = 0;
        for(int i=0;i<n;i++){
            int prev;
            for(int j=0;j<i;j++){
                prev = arr[i]-arr[j];
                if(indexing.count(prev) && indexing[prev]<j){
                    dp[j][i] = dp[indexing[prev]][j] + 1;
                    maxi = max(maxi,dp[j][i]);
                }
            }
        }

        if(maxi>2){
            return maxi;
        }else{
            return 0;
        }
    }
};

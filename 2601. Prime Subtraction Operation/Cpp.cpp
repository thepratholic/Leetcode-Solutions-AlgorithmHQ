Contributed by : Sundaram Agnihotri (Student)
Linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approah : 

1 : Find the maximum value in the array (element) to generate all primes less than this value

2 : Create a boolean array to mark all prime numbers less than element.

3 : Use the sieve to efficiently identify all primes.

4 : Start from the second-to-last element and compare it with the next element (prev).

5 : If the current element is not less than prev, attempt to reduce it.

6 : Subtract the largest possible prime p such that nums[i]−𝑝<prev , If no valid prime p is found, return false.

7 : If the current element is successfully reduced, update prev to the new value and move to the previous element.

class Solution {
public:
    bool primeSubOperation(vector<int>& nums) {
        int n = nums.size();
        //Step1)
        int element = INT_MIN;
        for(int i = 0; i < n; i++) element = max(element,nums[i]);

        //Step2)
        vector<int> prime(element,1);

        for(int i=2; i < element; i++){
            if(prime[i] == 1){
                for(int j = i+i; j < element; j += i){
                    prime[j] = 0;
                }
            }
        }

        //Step3)
        int i = n-2;
        int prev = nums[n-1];
        while(i >= 0){
            if(nums[i] >= prev){

                int flag = 0;
                for(int j = 2; j < nums[i]; j++){

                    if(prime[j] == 1){
                        if(nums[i] - j < prev){
                            nums[i] = nums[i] - j;
                            flag = 1;
                            break;
                        }
                    }
                }
                if(flag == 0) return false;
            }
            prev = nums[i];
            i--;
        }

        return true;
    }
};

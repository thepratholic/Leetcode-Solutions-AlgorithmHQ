Contributed by : Sundaram Agnihotri (Student)
Linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

// Approach : 

// 1 : If k=0: Replace every element with 
// 0(return an array of zeroes).

// 2 : If k>0: Replace each element with the sum of the next k elements.

// 3 : If k<0: Replace each element with the sum of the previous ∣k∣ elements.
// Sliding Window Technique:

// 4 : Use a window of size ∣k∣ to calculate the sum for the first element.

// 5 : Slide the window across the array:
//      a : Subtract the element leaving the window.
//      b : Add the element entering the window.

// 6 : Use modulo arithmetic to handle the circular nature of the array.
    

class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int []ans = new int[n];

        if(k==0)
        return ans;

        int start = 1;
        int end = k;
        int sum = 0;

        if(k<0){
            start = n - Math.abs(k);
            end = n-1;
        }

        for(int i=start;i<=end;i++){
            sum+=code[i];
        }

        for(int i=0;i<n;i++){
            ans[i] = sum;
            sum -= code[start %n];
            sum += code[(end+1)%n];
            start++;
            end++;
        }
        return ans;
    }
}

contributed by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 

1 : zero_count to track the number of zeros encountered so far (for the left substring).
2 : one_count starts as the total count of ones, representing the initial right substring.
3 : Iterate through each character of the string (except the last character, as both substrings need to be non-empty).
4 : If the character is 0, increment zero_count (indicating a zero is added to the left substring).
5 : If the character is 1, decrement one_count (indicating a one is removed from the right substring).
6 : Calculate the current score as zero_count + one_count and update the maximum score if the current score is greater.


class Solution {
public:
    int maxScore(string s) {
        int one_count = count(s.begin(), s.end(),'1');
        int res=0;
        int zero_count= 0;
        for(int i=0;i<s.length()-1;i++)
        {
            if(s[i] == '1')
            {
                one_count--;
            }
            else
            {
                zero_count++;
            }
            res = max(res, zero_count + one_count );
        }
        return res;
    }
};

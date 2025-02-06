contributed by : sundaram agnihotri (student)
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 

1 : Use a prefix sum array prefixVowelCount to store the cumulative count of words starting and ending with vowels.
For each word in the words array:
	
2 : Check if the first and last characters of the word are vowels using isVowel.

3 : Update the prefix sum array by adding 1 if the condition is true; otherwise, carry forward the previous count.
Process Each Query:

4 : For each query [li, ri], calculate the result using the formula:
prefixVowelCount[ri + 1] - prefixVowelCount[li]

class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        
        int n = words.size();
        vector<int> prefixVowelCount(n + 1, 0), results;
        
        for (int i = 1; i <= n; ++i) {
            prefixVowelCount[i] = prefixVowelCount[i - 1] + 
                        (isVowel(words[i - 1].front()) && isVowel(words[i - 1].back()) ? 1 : 0);
        }
        
        for (const auto& query : queries) {
            results.push_back(prefixVowelCount[query[1] + 1] - prefixVowelCount[query[0]]);
        }
        
        return results;
    }
};

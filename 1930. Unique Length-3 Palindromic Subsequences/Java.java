contributed by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach :

1 : Track First and Last Occurrences Simultaneously:

Instead of iterating twice for each character to find its first and last occurrence, use a single pass with an array of size 26 (first[26] and last[26]) 
to store these indices for all characters.

2 : Directly Process Characters Between Indices:

Once the first and last occurrences of a character are identified, use a boolean array of size 26 to track unique characters between these indices 
instead of a HashSet. This avoids the overhead of maintaining a dynamic structure.
3 : Iterate Only Over Valid Characters:

Use another loop to process only characters that have distinct first and last indices, skipping characters that cannot form palindromes early.

4 : Reduce Space for Unique Characters:

By using a fixed-size array for tracking intermediate characters (size 26 for lowercase letters), memory usage is minimized.

// hash set 
class Solution {
    public int countPalindromicSubsequence(String s) {
        // find unique chars
        HashSet<Character> set = new HashSet<>();
        int n = s.length();
        for(int i=0;i<n;i++){
            set.add(s.charAt(i)); //a,b,c
        }

        int count=0;
        for(char ch : set){
            int first=-1;
            int last = -1;
            for(int i=0;i<n;i++){
                if(ch == s.charAt(i)){
                    if(first == -1){
                        first = i;
                    }
                    last = i;
                }
            }
            if(first == last) continue;
            HashSet<Character> set1 = new HashSet<>();
            for(int i=first+1;i<last;i++){
                set1.add(s.charAt(i));
            }
            count += set1.size();
        }
        return count;
    }
}

class Solution {
    public int countPalindromicSubsequence(String s) {
        // Time complexity: O(N)
        // use fo and lo to know the positions of first and last occurances of every character 
        int[] fo = new int[26], lo = new int[26];
        Arrays.fill(fo, Integer.MAX_VALUE);
        for(int i=0; i<s.length(); i++) {
            fo[s.charAt(i)-'a'] = Math.min(fo[s.charAt(i)-'a'], i);
            lo[s.charAt(i)-'a'] = i;
        }
        int ans = 0;
        for(int i=0; i<26; i++) {
            int f=fo[i], l=lo[i];
            // use set to count number of unique characters
            Set<Character> unique = new HashSet<>();
            if(f<l) {
                for(int j=f+1; j<l; j++) {
                    unique.add(s.charAt(j));
                }
            }
            // add the number of unique characters to ans
            ans+=unique.size();
        }
        return ans;
    }
}

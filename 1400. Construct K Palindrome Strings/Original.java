class Solution {
    public boolean canConstruct(String s, int k) {
        // total number of characters are less than k
        if(s.length()<k) return false;
        int[] count = new int[26];
        for(int i=0; i<s.length(); i++) {
            count[s.charAt(i)-'a']+=1;
        }
        int odd = 0;
        for(int i: count) {
            if((i&1)==1) odd+=1;
        }
        // total number of characters with odd count are greater than k
        if(odd>k) return false;
        return true;
    }
}

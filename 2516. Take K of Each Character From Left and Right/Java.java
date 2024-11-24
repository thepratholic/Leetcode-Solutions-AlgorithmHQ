class Solution {
    public int takeCharacters(String s, int k) {
        // store number of occurances of each character
        int[] count = new int[3];
        for(char c: s.toCharArray()) count[c-'a']+=1;
        // return -1 if all 3 characters are not present atleast k times
        if(count[0]<k || count[1]<k || count[2]<k) return -1;
        int min = s.length(), start = 0;
        // expand the window if all 3 characters are present atleast k times
        for(int end = 0; end<s.length(); end+=1) {
            count[s.charAt(end)-'a']-=1;
            // shrink the window if all 3 characters are not present atleast k times
            while(start<=end && (count[0]<k || count[1]<k || count[2]<k)) {
                count[s.charAt(start++)-'a']+=1;
            }
            min = Math.min(min, s.length()-(end-start+1));
        }
        return min;
    }
}

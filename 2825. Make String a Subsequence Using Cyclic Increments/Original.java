class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        int j=0;
        for(int i=0; i<str1.length(); i++) {
            // check if ith character of str1 can be made equal to jth character of str2
            if((str2.charAt(j)-str1.charAt(i)+26)%26<=1) j+=1;
            // return true if all characters are found
            if(j==str2.length()) return true;
        }
        return false;
    }
}

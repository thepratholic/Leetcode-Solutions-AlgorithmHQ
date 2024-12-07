class Solution {
    public String addSpaces(String s, int[] spaces) {
        //use stringbuilder to append characters instead of using substring function
        StringBuilder sb = new StringBuilder();
        int j = 0;
        for(int i=0; i<s.length(); i++) {
            // insert space if required
            if(j<spaces.length && spaces[j]==i) {
                sb.append(" ");
                j+=1;
            }
            // insert characters irrespective of anything
            sb.append(s.charAt(i));
        }
        return sb.toString();
    }
}

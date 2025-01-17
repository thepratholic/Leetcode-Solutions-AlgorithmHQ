class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
       // use two sets to store integers till index i
       Set<Integer> setA = new HashSet<>();
       Set<Integer> setB = new HashSet<>();
       int[] ans = new int[A.length];
       // keep track of common integers till index i using count
       int count = 0;
       for(int i=0; i<ans.length; i++) {
            setA.add(A[i]); // O(1)
            setB.add(B[i]);
            // add 1 to count if there are same integers in both A and B at index i
            if(A[i]==B[i]) count+=1;
            // check for presence of current integers in the opposite array sets 
            else {
                if(setB.contains(A[i])) count+=1; // O(1)
                if(setA.contains(B[i])) count+=1;
            }
            ans[i] = count;
       }
       return ans;
    }
}

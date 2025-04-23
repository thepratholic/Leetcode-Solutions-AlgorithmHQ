class Solution {
    public int numberOfArrays(int[] differences, int lower, int upper) {
        // assume the first element to be 0
        long a=0, min=0, max=0;
        for(int i: differences) {
            // try and form a sequence using differences array
            a+=i;
            // keep track of max and min
            min=Math.min(a, min);
            max=Math.max(a, max);
        }
        // see if the range formed using differences array is less than or equal to the actual range given
        return (int)Math.max(0, upper-lower-(max-min)+1);
    }
}

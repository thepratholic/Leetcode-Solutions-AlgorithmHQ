class Solution {
    public int[] finalPrices(int[] prices) {
        // stack to keep track of minimum j
        Stack<Integer> stack = new Stack<>();
        for(int i=prices.length-1; i>=0; i--) {
            // pop until an item is found with price lesser than the current item
            while(!stack.isEmpty() && stack.peek()>prices[i]) stack.pop();
            int finalPrice = stack.isEmpty() ? prices[i] : prices[i]-stack.peek();
            // push current price
            stack.push(prices[i]);
            // store finalPrice in prices array to avoid extra space usage
            prices[i] = finalPrice;
        }
        return prices;
    }
}

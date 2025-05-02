class Solution {
    public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {

        // Sort tasks and workers to make greedy decisions easier
        Arrays.sort(tasks);  // O(n log n)
        Arrays.sort(workers); // O(m log m)

        // Store workers in a TreeMap for quick access to ceiling and floor keys
        TreeMap<Integer, Integer> map = new TreeMap<>();
        for(int w: workers) map.put(w, map.getOrDefault(w, 0)+1);

        int n = tasks.length, m = workers.length;
        int start = 0, end = Math.min(n, m);
        int ans = 0;

        // Binary search on the maximum number of tasks that can be assigned
        while(start <= end) {
            int mid = (start + end) / 2;
            // Check if it is possible to assign 'mid' number of tasks
            if(isPossible(mid, tasks, map, pills, strength)) {
                ans = mid; // Store current best
                start = mid + 1; // Try assigning more tasks
            } else {
                end = mid - 1; // Try assigning fewer tasks
            }
        }

        return ans; // Maximum number of tasks that can be assigned
    }

    private boolean isPossible(int mid, int[] tasks, TreeMap<Integer, Integer> map, int pills, int strength) {
        // Clone the map to avoid modifying the original worker pool
        TreeMap<Integer, Integer> clone = new TreeMap<>(map);

        // Try assigning the 'mid' most difficult tasks
        for(int i = mid - 1; i >= 0; i--) {
            int t = tasks[i];  // Current task's requirement

            // Try assigning the strongest available worker
            Integer hi = clone.lastKey();
            if(hi >= t) {
                // Assign task without pill
                if(clone.get(hi) == 1) clone.remove(hi);
                else clone.put(hi, clone.get(hi) - 1);
            } else {
                // Try assigning a weaker worker using a pill
                if(pills == 0) return false;
                Integer lo = clone.ceilingKey(t - strength);
                if(lo == null) return false; // No suitable worker even with pill
                if(clone.get(lo) == 1) clone.remove(lo);
                else clone.put(lo, clone.get(lo) - 1);
                pills--; // Use a pill
            }
        }
        return true; // Successfully assigned all 'mid' tasks
    }
}

class Solution {
    // build a trie to store folders
    class TrieNode{
        TrieNode children[];
        boolean isLast;
        TrieNode() {
            children = new TrieNode[27];
            isLast = false;
        }
    }

    TrieNode root;

    // remove sub-folders if required
    public List<String> removeSubfolders(String[] folder) {
        root = new TrieNode();
        Arrays.sort(folder, (a,b)->a.length()-b.length());
        List<String> ans = new ArrayList<>();
        for(String f: folder) {
            if(!search(f)) {
                insert(f);
                ans.add(f);
            }
        }
        return ans;
    }

    // get index of the folder
    private int getIndex(char c) {
        return c=='/' ? 26 : c-'a'; 
    }

    // insert folder into the trie
    private void insert(String s) {
        TrieNode node = root;
        for(char c: s.toCharArray()) {
            int index = getIndex(c);
            if(node.children[index]==null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
        }
        node.children[26] = new TrieNode();
        node = node.children[26];
        node.isLast = true;
    }

    private boolean search(String s) {
        TrieNode node = root;
        for(char c: s.toCharArray()) {
            if(node.isLast) return true;
            int index = getIndex(c);
            if(node.children[index]==null) return false;
            node = node.children[index];
        }
        return node.isLast;
    }
}

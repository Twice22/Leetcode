/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    int maxi = 0;
    
    void helper(Node* root, int depth) {
        if (!root) return;
        
        maxi = max(maxi, depth);
        
        for (auto child: root->children) {
            helper(child, depth+1);
        }
    }
    
    int maxDepth(Node* root) {
        helper(root, 1);
        return maxi;
    }
};
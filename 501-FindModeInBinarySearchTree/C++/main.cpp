/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    int maxfreq = 1;
    vector<int> result;
    
public:
    pair<int, int> inOrderTraversal(TreeNode* root, int prev, int cur_max, int version) {
        if (!root) return make_pair(prev, cur_max);
        
        pair<int, int> p = inOrderTraversal(root->left, prev, cur_max, version);
        
        p.second = root->val == p.first ? p.second + 1 : 1;
        if (version == 0) maxfreq = max(maxfreq, p.second);
        else if (version == 1) {
            if (p.second == maxfreq) {
                result.push_back(root->val);
            }
        }
        
        p = inOrderTraversal(root->right, root->val, p.second, version);
        return p;
        
    }
    
    vector<int> findMode(TreeNode* root) {
        /* by the definition of a BST we are sure that
        root->val + 1 is != from the leftmost node of the tree */
        if (!root) return result;
        
        inOrderTraversal(root, root->val + 1, 1, 0);
        inOrderTraversal(root, root->val + 1, 1, 1);
        return result;
        
    }
};
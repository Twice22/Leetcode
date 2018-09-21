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
    int mini = INT_MAX;
    
public:
    int inOrderTraversal(TreeNode* root, int prev) {
        if (!root) return prev;
        
        int prev_ = inOrderTraversal(root->left, prev);
        
        if (prev_ >= 0) {
            mini = min(mini, abs(root->val - prev_));
        }
        
        // The magic operates here: we passe prev = root->val
        prev_ = inOrderTraversal(root->right, root->val);
        return prev_;
    }
    
    int getMinimumDifference(TreeNode* root) {
        // little trick: we are sure there is no negative value in the tree
        // so pass a negative value as the initial value and don't compute
        // mini if we see a negative value in inOrderTraversal
        inOrderTraversal(root, -1);
        return mini;
    }
};
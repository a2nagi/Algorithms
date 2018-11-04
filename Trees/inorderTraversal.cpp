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
public:
    void inorder_helper(TreeNode* root, vector<int>& nodes)
    {
        if (root == nullptr)
        {
            return;
        }

        inorder_helper(root->left, nodes);
        nodes.emplace_back(root->val);
        inorder_helper(root->right, nodes);
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>nodes;
        inorder_helper(root, nodes);
        return nodes;
    }
};

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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int>single_path;
        vector<vector<int>>leaves;
        calculate_leaves_sum(root, leaves, single_path, sum);
        return leaves;
    }
    
    void calculate_leaves_sum(TreeNode* root, vector<vector<int>>& leaves, vector<int>& single_path, int sum)
    {
        if (root == NULL)
        {
            return;
        }
        single_path.emplace_back(root->val);
        if (root->left == NULL && root->right == NULL)
        {
            if (root->val == sum)
            {
                leaves.emplace_back(single_path);
            }
        }
        
        calculate_leaves_sum(root->left, leaves, single_path, sum-(root->val));
        calculate_leaves_sum(root->right, leaves, single_path, sum-(root->val));
        single_path.pop_back();
    }
};

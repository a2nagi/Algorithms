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
    bool hasPathSum(TreeNode* root, int sum) {
        return cal_value(root, sum, 0);
    }
    
    bool cal_value(TreeNode* root, int sum, int cur_sum)
    {  
        if (root == NULL)
        {
            return false;
        }
        cur_sum += root->val;
        if (cur_sum == sum && root->left == NULL && root->right == NULL)
        {
            return true;
        }
        
        return cal_value(root->left, sum, cur_sum) || cal_value(root->right, sum, cur_sum);
    }
};

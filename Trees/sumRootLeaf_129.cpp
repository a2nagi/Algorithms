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
    int sumNumbers(TreeNode* root) {
        if (root == NULL)
        {
            return 0;
        }
        int total_sum = 0;
        sum_helper(root, total_sum, 0);
        return total_sum;
    }
    
    void sum_helper(TreeNode* root, int& total_sum, int sum)
    {
        if (root == NULL)
        {
            return;
        }
        
        if (root->left == NULL && root->right == NULL)
        {
            sum = (10*sum) + root->val;
            total_sum += sum;
            return;
        }
        
        sum = (10*sum) + root->val;
        sum_helper(root->left, total_sum, sum);
        sum_helper(root->right, total_sum, sum);
    }
};

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
    vector<int> largestValues(TreeNode* root) {
        vector<TreeNode*>queue;
        vector<int> answers;
        if (root == NULL)
        {
            return answers;
        }
        queue.emplace_back(root);
        while (queue.size() > 0)
        {
            int size = queue.size();
            int i=0;
            int cur_max = INT_MIN;
            while (i < size)
            {
                TreeNode* temp = queue.at(0);
                queue.erase(queue.begin());
                cur_max = max(cur_max, temp->val);
                if (temp->left)
                {
                    queue.emplace_back(temp->left);
                }
                
                if(temp->right)
                {
                    queue.emplace_back(temp->right);
                }
                
                i += 1;
            }
            answers.emplace_back(cur_max);
        }
        return answers;
    }
};

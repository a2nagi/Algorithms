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
    vector<int> rightSideView(TreeNode* root) {
        vector<TreeNode*>queue;
        queue.emplace_back(root);
        int x = 0;
        vector<int>answer;
        vector<int>answer_final;
        if(root == NULL)
        {
            return answer;
        }
        while(queue.size())
        {
            while (!answer.empty())
            {
                 answer.pop_back();
            }
            int size = queue.size();
            for(int i=0;i<size;i++)
            {
                TreeNode* temp = queue.at(0);
                queue.erase(queue.begin());

                if(temp->left)
                {
                    queue.emplace_back(temp->left);
                }

                if(temp->right)
                {
                    queue.emplace_back(temp->right);
                }
                answer.emplace_back(temp->val);
            } 
            answer_final.emplace_back(answer.at(answer.size()-1));
        }
        return answer_final;
    }
};

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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>>outside;
        vector<TreeNode*>queue;
        queue.emplace_back(root);
    
        if (root == NULL)
        {
            return outside;
        }
        
        while(queue.size())
        {
            vector<int> inside;
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
                
                inside.emplace_back(temp->val);
                
            }
            
            outside.emplace_back(inside);
        
        }
        
        vector<vector<int>>convert;
        for(int i=outside.size()-1;i>=0;i--)
        {
            convert.emplace_back(outside.at(i));
        }
        return convert;
        
    }
};

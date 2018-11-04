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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>level;
        vector<TreeNode*>queue;
        if(root == NULL)
        {
            return level;
        }
        queue.emplace_back(root);
        while(queue.size())
        {
            int size = queue.size();
            vector<int>single_level;
            for(int i=0;i<single_level.size();i++)
            {
                single_level.pop_back();
            }
            for(int i=0;i<size;i++)
            {
                TreeNode* temp = queue.at(0);
                queue.erase(queue.begin());
                
                if(i%2 == 0)
                {
                    if(temp->left)
                    {
                        queue.emplace_back(temp->left);
                    }
                
                    if (temp->right)
                    {
                        queue.emplace_back(temp->right);
                    }
                }
                
                else if(i%2 == 1)
                {
                    if(temp->right)
                    {
                        queue.emplace_back(temp->right);
                    }
                
                    if (temp->left)
                    {
                        queue.emplace_back(temp->left);
                    }
                }
                
                
                
                single_level.emplace_back(temp->val);
            }
            level.emplace_back(single_level);
        }
        
        for(int i=0;i<level.size();i++)
        {
            if(i%2 ==1)
            {
                reverse(level.at(i));
            }
        }
        
        return level;
        
        
        
        
    }
    
    void reverse(vector<int>&level)
    {
        int size = level.size();
        for(int i=0;i<size/2;i++)
        {
            int j = size-i-1;
            int temp = level.at(i);
            level.at(i) = level.at(j);
            level.at(j) = temp;
        }
    }
};

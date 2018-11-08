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
    void print_stack(vector<TreeNode*> stack, vector<string>& answer)
    {   
        string build_string;
        int index=0;
    
        for(int i=0;i<stack.size()-1;i++)
        {
            index = i;
            build_string += to_string(stack.at(i)->val) + "->";
        }
        build_string += to_string(stack.at(index+1)->val);
        answer.emplace_back(build_string);
    }
    
    
    void find_all_paths(TreeNode* root, vector<string>& answer, vector<TreeNode*> stack)
    {
        if (root == NULL)
        {
            return;
        }
        
        stack.emplace_back(root);
        find_all_paths(root->left, answer, stack);
        if (root->left == NULL && root->right == NULL)
        {
            if (stack.size() == 1)
            {
               answer.emplace_back(to_string(stack.at(0)->val));
            }
            else
            {
                print_stack(stack, answer);
            }
        }
        find_all_paths(root->right, answer, stack);
        stack.pop_back();
    }
    
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> answer;
        if (root == NULL)
        {
            return answer;
        }
        
        vector<TreeNode*> stack;
        find_all_paths(root, answer, stack);
        return answer;
    }
};

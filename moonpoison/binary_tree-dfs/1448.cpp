#include<bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    int ans=1;
    int goodNodes(TreeNode* root)
    {
        dfs(root, root->val);
        return ans;
    }
    void dfs(TreeNode* root, int num)
    {
        if(root->left!=nullptr)
        {
            if(root->left->val>=num) ans++;
            dfs(root->left, max(num, root->left->val));   
        }
        if(root->right!=nullptr)
        {
            if(root->right->val>=num) ans++;
            dfs(root->right, max(num, root->right->val));
        }
    }
};
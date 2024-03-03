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
    vector<int> b;
    bool leafSimilar(TreeNode* root1, TreeNode* root2) 
    {
        dfs(root1);
        vector<int> a=b;
        b.clear();
        dfs(root2);
        return a==b;
    }
    void dfs(TreeNode* root)
    {
        if(root->left!=nullptr) dfs(root->left);
        if(root->right!=nullptr) dfs(root->right);
        if(root->left==nullptr&&root->right==nullptr) b.push_back(root->val);
    }
};
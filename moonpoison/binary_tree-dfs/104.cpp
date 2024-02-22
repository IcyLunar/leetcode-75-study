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
    int MAX=0;
    int maxDepth(TreeNode* root)
    {
        if(root==NULL) return NULL;
        dfs(root, 1);
        return MAX;
    }
    void dfs(TreeNode* root, int cnt)
    {
        if(root->left!=nullptr) dfs(root->left, cnt+1);
        if(root->right!=nullptr) dfs(root->right, cnt+1);
        if(root->left==nullptr&&root->right==nullptr) MAX=max(MAX, cnt);
    }
};
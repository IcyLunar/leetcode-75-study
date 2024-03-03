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
    int ans=0;
    int longestZigZag(TreeNode* root) 
    {
        if(!root) return 0;
        return max(dfs(root->left, 0, 0), dfs(root->right, 1, 0));
    }
    int dfs(TreeNode* root, int a, int cnt)
    {
        if(!root) return cnt;
        if(a==0) return max(dfs(root->left, 0, 0), dfs(root->right, 1, cnt+1));
        else return max(dfs(root->left, 0, cnt+1), dfs(root->right, 1, 0));
    }
};
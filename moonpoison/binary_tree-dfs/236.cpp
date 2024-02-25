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
    typedef TreeNode* T;
    TreeNode* lowestCommonAncestor(T root, T p, T q) 
    {
        vector<T> vp; vector<T> vq;
        vis(root, p, vp); vis(root, q, vq);
        for(int i=vq.size()-1;i>=0;--i)
            if(find(vp.begin(), vp.end(), vq[i])!=vp.end()) return vq[i];
        return NULL;
    }
    bool vis(T root, T p, vector<T> &v)
    {
        if(!root) return false;
        v.push_back(root);
        if(root==p) return true;
        if(vis(root->left, p, v)||vis(root->right, p, v)) return true;
        v.pop_back();
        return false;
    }
};
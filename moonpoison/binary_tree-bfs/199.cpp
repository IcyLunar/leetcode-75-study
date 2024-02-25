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
    vector<int> ans;
    queue<pair<int, TreeNode *> > q;
    vector<int> rightSideView(TreeNode* root) 
    {
        if(!root) return ans;
        ans.push_back(root->val);
        bfs(root);
        return ans;
    }
    void bfs(TreeNode* root)
    {
        if(root->right!=nullptr) q.push({2, root->right});
        if(root->left!=nullptr) q.push({2, root->left});
        int cnt=1;
        while(!q.empty())
        {
            if(cnt!=q.front().first)
            {
                ans.push_back(q.front().second->val);
                cnt=q.front().first;
            }
            root=q.front().second;
            cout<<q.front().second->val<<endl;
            if(root->right!=nullptr) q.push({cnt+1, root->right});
            if(root->left!=nullptr) q.push({cnt+1, root->left});
            q.pop();
        }
    }
};
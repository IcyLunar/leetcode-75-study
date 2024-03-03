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
    pair<long long, int> MAX={INT_MIN, 0};
    queue<pair<int, TreeNode *> > q;
    int maxLevelSum(TreeNode* root)
    {
        MAX={root->val, 1};
        bfs(root);
        return MAX.second;
    }
    void bfs(TreeNode* root)
    {
        if(root->right!=nullptr) q.push({2, root->right});
        if(root->left!=nullptr) q.push({2, root->left});
        int cnt=1;
        long long ins=INT_MIN;
        while(!q.empty())
        {
            if(cnt!=q.front().first)
            {
                if(MAX.first<ins)
                {
                    MAX.first=ins;
                    cout<<ins;
                    MAX.second=cnt;
                }
                cnt=q.front().first;
                ins=0;
            }
            root=q.front().second;
            ins+=q.front().second->val;
            if(root->right!=nullptr) q.push({cnt+1, root->right});
            if(root->left!=nullptr) q.push({cnt+1, root->left});
            q.pop();
        }
        if(MAX.first<ins)
        {
            MAX.first=ins;
            cout<<ins;
            MAX.second=cnt;
        }
    }
};
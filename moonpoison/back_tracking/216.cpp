#include<bits/stdc++.h>
using namespace std;
class Solution {
    vector<vector<int>> ans;
    void dfs(int start, vector<int> &v, int cnt, int target)
    {
        if(cnt==0)
        {
            if(target==0)
            {
                ans.push_back(v);
                return;
            }
        }
        for(int i=start;i<=9;++i)
        {
            v.push_back(i);
            dfs(i+1, v, cnt-1, target-i);
            v.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum3(int k, int n) 
    {
        vector<int> v;
        dfs(1, v, k, n);
        return ans;
    }
};
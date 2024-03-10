#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    vector<double> ans;
    unordered_map<string, vector<pair<string, double>>> m;
    unordered_map<string, bool> vis;

    void dfs(int a, string s1, string s2, double val)
    {
        if(vis[s1]==true) return;
        if(s1==s2)
        {
            ans[a]=val;
            return;
        }
        vis[s1]=true;
        for(int i=0;i<m[s1].size();++i)
            dfs(a, m[s1][i].first, s2, val*m[s1][i].second);
        vis[s1]=false;
    }
public:
    
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) 
    {
        ans=vector<double>(queries.size(), 0);
        for(int i=0;i<equations.size();++i)
        {
            m[equations[i][0]].push_back({equations[i][1], values[i]});
            m[equations[i][1]].push_back({equations[i][0], 1/values[i]});
        }
        for(int i=0;i<queries.size();++i)
        {
            if(m.find(queries[i][0])==m.end()||m.find(queries[i][1])==m.end())
            {
                ans[i]=(double)-1;
                continue;
            }
            dfs(i, queries[i][0], queries[i][1], 1);
            if(ans[i]==0) ans[i]=(double)-1;
        }
        return ans;
    }
};
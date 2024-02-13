#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) 
    {
        map<vector<int>, int> m;
        int ans=0;
        for(int i=0;i<grid.size();++i)
           m[grid[i]]++;
        for(int i=0;i<grid.size();++i)
        {
            vector<int> v;
            for(int j=0;j<grid.size();++j)
            {
                v.push_back(grid[j][i]);
            }
            ans+=m[v];
        }
        return ans;
    }
};
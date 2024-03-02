#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) 
    {
        vector<vector<int>> a(n), b(n);
        vector<int> v(n, 0);
        v[0]=1;
        for(auto i:connections)
        {
            a[i[0]].push_back(i[1]);
            b[i[1]].push_back(i[0]);
        }
        int ans=0;
        queue<int> q;
        q.push(0);
        while(!q.empty())
        {
            int tmp=q.front();
            v[tmp]=1;
            q.pop();
            for(int i:a[tmp])
            {
                if(!v[i])
                {
                    ans++;
                    q.push(i);
                }
            }
            for(int i:b[tmp])
                if(!v[i]) q.push(i);
        }
        return ans;
    }
};
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected)
    {
        int v[201]={0};
        stack<int> s;
        int cnt=0;
        for(int q=0;q<isConnected.size();++q)
        {
            if(!v[q])
            {
                for(int i=0;i<isConnected[q].size();++i)
                    if(isConnected[q][i]&&i!=q) s.push(i);
                v[q]++;
                while(!s.empty())
                {
                    int a=s.top();
                    s.pop();
                    if(!v[a])
                    {
                        v[a]++;
                        for(int i=0;i<isConnected[a].size();++i)
                            if(isConnected[a][i]&&i!=a) s.push(i);
                    }
                } 
                cnt++;
            }
        }
        return cnt;
    }
};
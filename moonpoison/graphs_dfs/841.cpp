#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms)
    {
        int v[1001]={0};
        stack<int> s;
        for(int i=0;i<rooms[0].size();++i)
            s.push(rooms[0][i]);
        v[0]++;
        while(!s.empty())
        {
            int a=s.top();
            s.pop();
            if(!v[a])
            {
                v[a]++;
                for(int i=0;i<rooms[a].size();++i)
                    s.push(rooms[a][i]);
            }
        }
        for(int i=0;i<rooms.size();++i)
            if(v[i]==0) return false;
        return true;
    }
};
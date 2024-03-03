#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int dx[4]={0, 0, -1, 1};
    int dy[4]={1, -1, 0, 0};
    int vis[11][11]={0};
    int ans=0;
    int orangesRotting(vector<vector<int>>& grid)
    {
        queue<tuple<int, int, int>> q;
        for(int i=0;i<grid.size();++i)
            for(int j=0;j<grid[0].size();++j)
                if(grid[i][j]==2)
                {
                    q.push({i, j, 0});
                    vis[i][j]++;
                }
        while(!q.empty())
        {
            int ax=get<0>(q.front());
            int ay=get<1>(q.front());
            int cnt=get<2>(q.front());
            q.pop();
            for(int i=0;i<4;++i)
            {
                int x=ax+dx[i];
                int y=ay+dy[i];
                if(x>=0&&x<grid.size()&&y>=0&&y<grid[0].size())
                {
                    if(!vis[x][y]&&grid[x][y]==1)
                    {
                        vis[x][y]=1;
                        grid[x][y]=2;
                        q.push({x, y, cnt+1});
                        ans=cnt+1;
                    }
                }   
            }
        }
        for(int i=0;i<grid.size();++i)
            for(int j=0;j<grid[0].size();++j)
                if(grid[i][j]==1) return -1;
        return ans;
    }
};
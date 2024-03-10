#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int dx[4]={0, 0, 1, -1};
    int dy[4]={1, -1, 0, 0};
    int vis[101][101]={0};
    int m[101][101]={0};
    int MIN=INT_MAX;
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) 
    {
        queue<tuple<int, int, int>> q;
        q.push({0, entrance[0], entrance[1]});
        vis[entrance[0]][entrance[1]]=1;
        while(!q.empty())
        {
            int cnt=get<0>(q.front());
            int ax=get<1>(q.front());
            int ay=get<2>(q.front());
            q.pop();
            if(ax==0||ax==maze.size()-1||ay==0||ay==maze[0].size()-1)
            {
                if(ax==entrance[0]&&ay==entrance[1]) {}
                else MIN=min(MIN, cnt);
            }
            for(int i=0;i<4;++i)
            {
                int x=ax+dx[i];
                int y=ay+dy[i];
                if(x>=0&&x<maze.size()&&y>=0&&y<maze[0].size())
                {
                    if(vis[x][y]!=1&&maze[x][y]=='.')
                    {
                        vis[x][y]=1;
                        q.push({cnt+1, x, y});
                    }
                }
            }
        }
        if(MIN==INT_MAX) return -1;
        else return MIN;
    }
};
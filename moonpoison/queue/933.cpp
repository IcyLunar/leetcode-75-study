#include<bits/stdc++.h>
using namespace std;
class RecentCounter {
public:
    queue<int> q;
    int ping(int t)
    {
        q.push(t);
        while(q.front()<t-3000&&q.size())
            q.pop();
        return q.size();
    }
};
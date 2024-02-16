#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string predictPartyVictory(string senate)
    {
        queue<int> r, d;
        int s=senate.size();
        for(int i=0;i<s;++i)
            senate[i]=='R' ? r.push(i) : d.push(i);
        while(!r.empty()&&!d.empty())
        {
            r.front()<d.front() ? r.push(r.front()+s) : d.push(d.front()+s);
            r.pop(); d.pop();
        }
        return d.size()==0 ? "Radiant" : "Dire";
    }
};
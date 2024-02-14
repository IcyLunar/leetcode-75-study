#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int largestAltitude(vector<int>& gain) 
    {
        vector<int> v;
        v.push_back(0);
        int ans=0;
        for(int i=0;i<gain.size();++i)
        {
            v.push_back(v[i]+gain[i]);
            if(ans<v[i+1]) ans=v[i+1];
        }
        return ans;
    }
};
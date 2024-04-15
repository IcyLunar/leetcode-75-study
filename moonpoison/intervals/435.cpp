#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    static bool cmp(const pair<int, int> &a,const pair<int, int> &b)
    {
        return a.second < b.second;
    }
    int eraseOverlapIntervals(vector<vector<int>>& intervals) 
    {
        if (intervals.size() == 0) return 0;
        int n = intervals.size();
        vector<pair<int, int>> v(n);
        for(int i=0; i<n; i++)
        {
            v[i].first = intervals[i][0];
            v[i].second = intervals[i][1];
        }
        sort(v.begin(), v.end(), cmp);

        int end = v[0].second;
        int count = 0; 

        for(int i=1; i<n; i++)
        {
            if(v[i].first < end) count++;
            else end = v[i].second;
        }      
        return count;
    }
};
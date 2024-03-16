#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) 
    {
        vector<pair<int, int>> v;
        for(int i=0;i<nums1.size();++i)
            v.push_back({nums2[i], nums1[i]});
        sort(v.rbegin(), v.rend());
        long long ans=0;
        long long sum=0;
        priority_queue<int> pq;
        for(int i=0;i<k-1;++i)
        {
            sum+=v[i].second;
            pq.push(-v[i].second);
        }
        for(int i=k-1;i<nums1.size();++i)
        {
            sum+=v[i].second;
            pq.push(-v[i].second);
            ans=max(ans, sum*v[i].first);
            sum+=pq.top();
            pq.pop();
        }
        return ans;
    }
};
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) 
    {
        priority_queue<int, vector<int>, greater<>> q1, q2;
        int n=costs.size();
        for (int i=0;i<candidates&&i<n; i++)
        {
            q1.push(costs[i]);
        }
        for (int i=n-1,j=0;i>=candidates&&j<candidates;j++,i--)
        {
            q2.push(costs[i]);
        }
        long long ans=0;
        int i=candidates, j=costs.size()-candidates-1;
        while(k)
        {
            int v1=INT_MAX, v2=INT_MAX;
            if(!q1.empty()) v1=q1.top();
            if(!q2.empty()) v2=q2.top();
            if(v1<=v2)
            {
                ans+=v1; q1.pop();
                if(i<=j)
                {
                    q1.push(costs[i]);
                    ++i;
                }
            }
            else if(v1>v2)
            {
                ans+=v2; q2.pop();
                if(i<=j)
                {
                    q2.push(costs[j]);
                    --j;
                }
            }
            --k;
        }
        return ans;
    }
};
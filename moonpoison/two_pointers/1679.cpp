#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) 
    {
        int ans=0;
        int p1=0, p2=nums.size()-1;
        sort(nums.begin(), nums.end());
        while(p1<p2)
        {
            int sum=nums[p1]+nums[p2];
            if(sum==k)
            {
                ans++;
                p1++; p2--;
            }
            else if(sum<k) p1++;
            else p2--;
        }
        return ans;
    }
};
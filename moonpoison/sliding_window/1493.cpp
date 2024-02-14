#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int longestSubarray(vector<int>& nums) 
    {
        int x1=0, x2=0;
        int ans=0;
        int flag=0;
        int cnt=0;
        for(int i=0;i<nums.size();++i)
        {
            if(nums[i]==0)
            {
                if(flag==1)
                {
                    if(nums[i-1]==0)
                    {
                        ans=max(ans, x1);
                        x1=0;
                        flag=0;
                    }
                    else
                    {
                        x2=cnt;
                        cnt=0;
                        ans=max(ans, x1+x2);
                        x1=x2; x2=0;
                    }
                }
                else
                {
                    if(cnt!=0) x1=cnt;
                    flag=1;
                    cnt=0;
                }
            }
            else cnt++;
        }
        if(cnt!=0)
        {
            x2=cnt;
            ans=max(ans, x1+x2);
        }
        if(cnt==nums.size()) return cnt-1;
        return ans;
    }
};
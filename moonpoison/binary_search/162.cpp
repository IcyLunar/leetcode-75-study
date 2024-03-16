#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findPeakElement(vector<int>& nums) 
    {
        int i;
        if(nums.size()==1) return 0;
        else if(nums.size()==2)
        {
            if(nums[0]>nums[1]) return 0;
            else return 1;
        }
        else
        {
            for(i=1;i<nums.size()-1;++i)
                if(nums[i]>nums[i-1]&&nums[i]>nums[i+1]) return i;
        }
        if(nums[0]>nums[i]) return 0;
        else return i;
    }
};
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int rob(vector<int>& nums) 
    {
        vector<int> arr(401);
        if(nums.size()==0) return 0;
        if(nums.size()==1) return nums[0];
        if(nums.size()==2) return max(nums[0], nums[1]);
        arr[0]=nums[0]; arr[1]=nums[1]; arr[2]=nums[0]+nums[2];
        for(int i=3;i<nums.size();++i)
            arr[i]=max(arr[i-2], arr[i-3])+nums[i];
        return *max_element(arr.begin(), arr.end());
    }
};
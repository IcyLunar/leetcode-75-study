#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) 
    {
        double a=0;
        for(int i=0;i<k;++i)
            a+=nums[i];
        double max=a;
        for(int i=0;i<nums.size()-k;++i)
        {
            a+=(nums[i+k]-nums[i]);
            if(max<a) max=a;
        }
        return max/k;
    }
};
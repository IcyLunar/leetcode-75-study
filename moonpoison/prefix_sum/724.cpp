#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int pivotIndex(vector<int>& nums) 
    {
        int p1=0, p2=0;
        for(int i=1;i<nums.size();++i)
            p2+=nums[i];
        int ind=0;
        while(ind+1!=nums.size())
        {
            if(p1==p2) return ind;
            p1+=nums[ind];
            p2-=nums[ind+1];
            ind++;
        }
        if(p1==p2) return ind;
        return -1;
    }
};
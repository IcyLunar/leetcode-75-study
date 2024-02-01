#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) 
    {
        int i=0;
        int flag=nums.size();
        while(flag!=0)
        {
            flag--;
            if(nums[i]==0)
            {
                nums.push_back(0);
                nums.erase(nums.begin()+i);
            }
            else ++i;
        }
    }
};

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) 
    {
        int ans=0;
        int x1=0, x2=height.size()-1;
        while(x1<x2)
        {
            int x=x2-x1;
            int y=min(height[x1], height[x2]);
            int area=x*y;
            if(ans<area) ans=area;
            if(height[x1]<height[x2]) x1++;
            else x2--;
        }
        return ans;
    }
};

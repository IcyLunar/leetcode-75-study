#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) 
    {
        int cnt=0;
        int p1=0, p2=0;
        int ans=0;
        while(p2<nums.size())
        {
            if(nums[p2]==1) p2++; //p2가 1일때 p2증가
            else//p2가 0일때
            {
                if(k>0)//k를 감소하며 p2증가
                {
                    k--;
                    p2++;
                }
                else//감소할 k가 없으면 배열길이계산, p1을 0이있는곳까지 이동후 슬라이딩윈도우
                {
                    ans=max(ans, p2-p1);
                    while(nums[p1]==1) 
                        p1++;    
                    p1++;
                    p2++;
                }
            }
        }
        ans=max(ans, p2-p1);
        return ans;
    }
};
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) 
    {
        int n=piles.size();
        long int left=1, right=INT_MAX;
        while(left<right)
        {
            long int mid=(left+right)/2;
            int k=0;
            for(auto i:piles)
            {
                if(i%mid!=0) k++;
                k+=i/mid;
            }
            if(k>h) left=mid+1;
            else right=mid;
        }
        return left;
    }
};
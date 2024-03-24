#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int dp[38]={0};
    int func(int n)
    {
        if(n==0) return 0;
        else if(dp[n]!=0) return dp[n];
        else 
        {
            dp[n]=func(n-3)+func(n-2)+func(n-1);
            return dp[n];
        }
    }
    int tribonacci(int n) 
    {
        dp[0]=0; dp[1]=1; dp[2]=1;
        return func(n);
    }
};
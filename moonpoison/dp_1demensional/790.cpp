#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int numTilings(int n) 
    {
        long long dp[1001], M=1e9+7;
        dp[1]=1; dp[2]=2; dp[3]=5;
        if(n==1) return 1;
        if(n==2) return 2;
        if(n==3) return 5;
        for(int i=4;i<=n;++i)
            dp[i]=(2*(dp[i-1]%M)+dp[i-3]%M)%M;
        return dp[n];
    }
};
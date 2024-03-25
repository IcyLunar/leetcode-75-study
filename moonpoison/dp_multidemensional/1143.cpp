#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int longestCommonSubsequence(string t1, string t2) 
    {
        t1='0'+t1;
        t2='0'+t2;
        int dp[1001][1001];
        for(int i=0;i<t1.size();++i)
        {
            for(int j=0;j<t2.size();++j)
            {
                if(i==0||j==0)
                {
                    dp[i][j]=0;
                    continue;
                }
                if(t1[i]==t2[j]) dp[i][j]=dp[i-1][j-1]+1;
                else
                {
                    if(dp[i-1][j]>dp[i][j-1]) dp[i][j]=dp[i-1][j];
                    else dp[i][j]=dp[i][j-1];
                }
            }
        }
        return dp[t1.size()-1][t2.size()-1];
    }
};
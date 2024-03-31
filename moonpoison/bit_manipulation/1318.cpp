#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minFlips(int a, int b, int c) 
    {
        int ans=0;
        for(int i=0;i<32;++i)
        {
            int mask=0;
            if(((1<<i)&c)==0)
            {
                if((a&(1<<i))!=0&&(b&(1<<i))!=0) ans+=2;
                else if((a&(1<<i))!=0||(b&(1<<i))!=0) ans+=1;
            }
            else
                if((a&(1<<i))==0&&(b&(1<<i))==0) ans+=1;
        }
        return ans;
    }
};
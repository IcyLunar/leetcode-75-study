#include<bits/stdc++.h>
using namespace std;
class StockSpanner {
public:
    const int N = 1e5+5;
    vector<int> dp;
    vector<int> arr;
    StockSpanner() 
    {
        dp.resize(N);
    }
    
    int next(int price) 
    {
        if(!arr.empty())
        {
            int i = (int)arr.size()-1;
            while(i >= 0 && arr[i] <= price)
                i -= dp[arr[i]];
            dp[price] = (int)arr.size()-i;
        }
        else dp[price] = 1;
        arr.push_back(price);
        return dp[price];
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
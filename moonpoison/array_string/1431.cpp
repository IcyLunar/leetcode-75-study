#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& a, int b) {
        int max=*max_element(a.begin(), a.end());
        vector<bool> ans;
        for(int i=0;i<a.size();++i)
        {
            a[i]+=b;
            if(a[i]<max) ans.push_back(0);
            else ans.push_back(1);
        }
        return ans;
    }
};

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) 
    {
        map<int, int> m;
        int a[1001]={0};
        for(int i=0;i<arr.size();++i)
            m[arr[i]]++;
        for(auto i=m.begin();i!=m.end();++i)
        {
            a[i->second]++;
            if(a[i->second]>1) return false;
        }
        return true;
    }
};
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string removeStars(string s) 
    {
        string ans;
        for(int i=0;i<s.size();++i)
        {
            if(s[i]!='*') ans.push_back(s[i]);
            else ans.pop_back();
        }
        return ans;
    }
};
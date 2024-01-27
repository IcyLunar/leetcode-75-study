#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int compress(vector<char>& chars) 
    {
        vector<char> ans;
        int a=1;
        char b=chars[0];
        for(int i=1;i<chars.size();++i)
        {
            if(b==chars[i]) a++;
            else
            {
                ans.push_back(b);
                if(a!=1)
                {
                    for(const char c : to_string(a))  
                        ans.push_back(c);
                } 
                a=1;
                b=chars[i];
            }
        }
        ans.push_back(b);
        if(a!=1)
        {
            for(const char c : to_string(a))  
                ans.push_back(c);
        } 
        chars.swap(ans);
        return chars.size();
    }
};

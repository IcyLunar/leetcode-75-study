#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string decodeString(string s) 
    {
        stack<char> s1;
        stack<int> s2;
        string n;
        int num;
        for(int i=0;i<s.size();++i)
        {
            if(s[i]>='0'&&s[i]<='9') n+=s[i];
            else if(s[i]=='[')
            {
                stringstream ss;
                ss<<n;
                ss>>num;
                n.clear();
                s1.push(s[i]);
                s2.push(num);
            }
            else if(s[i]==']')
            {
                string tmp;
                while(s1.top()!='[')
                {
                    tmp+=s1.top();
                    s1.pop();
                }
                s1.pop();
                reverse(tmp.begin(), tmp.end());
                for(int j=0;j<s2.top();++j)
                {
                    for(int q=0;q<tmp.size();++q)
                    {
                        s1.push(tmp[q]);
                    }
                }
                s2.pop();
            }
            else s1.push(s[i]);
        }
        string ans;
        while(!s1.empty())
        {
            ans+=s1.top();
            s1.pop();
        }    
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
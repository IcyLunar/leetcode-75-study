#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<char> chars;
    int c;
    cin>>c;
    for(int i=0;i<c;++i)
    {
        char h;
        cin>>h;
        chars.push_back(h);
    }
    sort(chars.begin(), chars.end());
    vector<char> ans;
    int a=1;
    char b=chars[0];
    for(int i=1;i<chars.size();++i)
    {
        if(b==chars[i]) a++;
        else
        {
            ans.push_back(b);
            ans.push_back(a+48);
            a=1;
            b=chars[i];
        }
    }
    ans.push_back(b);
    ans.push_back(a+48);
    chars.swap(ans);
    for(auto &i:chars)
    {
        cout<<i;
    }
}

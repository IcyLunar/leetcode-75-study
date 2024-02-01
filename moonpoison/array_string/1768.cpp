#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    string a, b;
    cin>>a>>b;
    int ca=a.size();
    int cb=b.size();
    int size=min(ca, cb);
    vector<char> ans;
    int i;
    for(i=0;i<size;++i)
    {
        ans.push_back(a[i]);
        ans.push_back(b[i]);
    }
    if(cb==size)
    {
        for(i=cb;i<ca;++i)
        {
            ans.push_back(a[i]);
        }
    }
    else if(ca==size)
    {
        for(i=ca;i<cb;++i)
        {
            ans.push_back(b[i]);
        }
    }
    for(i=0;i<ans.size();++i)   cout<<ans[i];
}

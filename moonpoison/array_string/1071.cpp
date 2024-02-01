#include<iostream>
#include<string>
using namespace std;
string a, b;
string mod(string a1, string b1)
{
    while(a1.find(b1)==0) a1=a1.substr(b1.length());
    return a1;
}
string gcd(string a1, string b1)
{
    if(a1.find(b1)==string::npos) return "";
    if(b1.empty()) return a1;
    return gcd(b1, mod(a1, b1));
}
int main()
{
    cin>>a>>b;
    string ans;
    if(a.length()<b.length()) ans=gcd(b, a);
    else ans=gcd(a, b);
    cout<<ans;
}

#include<bits/stdc++.h>
using namespace std;
bool closeStrings(string word1, string word2) 
{
    map<char, int> m, n;
    set<char> s1, s2;
    vector<int> a, b;
    if(word1.length()!=word2.length()) return false;
    for(auto i:word1)
    {
        m[i]++;
        s1.insert(i);
    }
    for(auto i:word2)
    {
        n[i]++;
        s2.insert(i);
    }
    if(s1!=s2) return false;
    for(auto i=m.begin();i!=m.end();++i)
        a.push_back(i->second);
    for(auto i=n.begin();i!=n.end();++i)
        b.push_back(i->second);
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    if(a!=b) return false;
    return true;
}
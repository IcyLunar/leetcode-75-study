#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    string reverseVowels(string s) 
    {
        vector<char> gather;
        vector<int> pos;
        for(int i=0;i<s.size();++i)
        {
            if(s[i]=='a'||s[i]=='A'||s[i]=='e'||s[i]=='E'||s[i]=='i'||s[i]=='I'||s[i]=='o'||s[i]=='O'||s[i]=='u'||s[i]=='U')
            {
                gather.push_back(s[i]);
                pos.push_back(i);
            }
        }
        reverse(gather.begin(), gather.end());
        for(int i=0;i<pos.size();++i)
        {
            s[pos[i]]=gather[i];
        }
        return s;
    }
};

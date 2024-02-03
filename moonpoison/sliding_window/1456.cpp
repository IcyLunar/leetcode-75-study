#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxVowels(string s, int k) 
    {
        int a=0;
        int max=0;
        for(int i=0;i<k;++i)
        {
            if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u') a++;
        }
        max=a;
        for(int i=0;i<s.size()-k;++i)
        {
            if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u') a--;
            if(s[i+k]=='a'||s[i+k]=='e'||s[i+k]=='i'||s[i+k]=='o'||s[i+k]=='u') a++;
            if(max<a) max=a;
        }
        return max;
    }
};
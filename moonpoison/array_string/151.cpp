#include<iostream>
#include<string>
#include<stack>
using namespace std;
class Solution {
public:
    string reverseWords(string s) 
    {
        stack<string> words;
        string a="";
        for (int i=0; i<s.length(); i++) 
        {
            if (s[i]==' ') 
            {
                if (a.length()>0) 
                {
                    words.push(a);
                    a="";
                }
            } 
            else 
            {
                a+=s[i];
            }
        }
        if (a.length()>0)
            words.push(a);
        
        string res="";
        while (words.size()>1) 
        {
            res+=words.top() + " ";
            words.pop();
        }
        res+=words.top();
        return res;
    }
};

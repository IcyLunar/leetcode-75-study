#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    map<char, vector<char>> mp = {
        {'2', {'a', 'b', 'c'}},
        {'3', {'d', 'e', 'f'}},
        {'4', {'g', 'h', 'i'}},
        {'5', {'j', 'k', 'l'}},
        {'6', {'m', 'n', 'o'}},
        {'7', {'p', 'q', 'r', 's'}},
        {'8', {'t', 'u', 'v'}},
        {'9', {'w', 'x', 'y', 'z'}}};
    void backtracking(int i, string digits, string s, vector<string> &ans)
    {
        if(i==digits.length())
        {
            if(s.length()) ans.push_back(s);
            return;
        }
        for(auto C:mp[digits[i]])
            backtracking(i+1, digits, s+C, ans);
    }
    vector<string> letterCombinations(string digits) 
    {
        vector<string> ans;
        backtracking(0, digits, "", ans);
        return ans;
    }
};
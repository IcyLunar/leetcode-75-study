#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& ast) 
    {
        stack<int> pos, neg;
        vector<int> ans;
        for(int i=0;i<ast.size();++i)
        {
            if(ast[i]>0) pos.push(ast[i]); //if pos
            else //if neg
            {
                if(pos.empty()) ans.push_back(ast[i]); //if pos stack is empty
                else //if pos stack isnt empty
                {
                    neg.push(ast[i]);
                    while(!pos.empty()&&!neg.empty())
                    {
                        if(abs(pos.top())>abs(neg.top())) neg.pop();
                        else if(abs(pos.top())==abs(neg.top()))
                        {
                            pos.pop();
                            neg.pop();
                        }
                        else pos.pop();
                    }
                    if(!neg.empty())
                    {
                        ans.push_back(neg.top());
                        neg.pop();
                    }
                }
            }
        }
        if(!pos.empty())
        {
            vector<int> v;
            while(!pos.empty())
            {
                v.push_back(pos.top());
                pos.pop();
            }
            reverse(v.begin(), v.end());
            ans.insert(ans.end(), v.begin(), v.end());
        }
        return ans;
    }
};
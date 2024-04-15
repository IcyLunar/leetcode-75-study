#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) 
    {
        sort(products.begin(), products.end());
        string tmp;
        vector<vector<string>> ans(searchWord.size());
        for(int i=0;i<searchWord.size();++i)
        {
            tmp+=searchWord[i];
            for(int j=0;j<products.size();++j)
            {
                string s=products[j].substr(0, i+1);
                if(s==tmp&&ans[i].size()<3) ans[i].push_back(products[j]);
            }
        }
        return ans;
    }
};
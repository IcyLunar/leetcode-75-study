#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) 
    {
        vector<int> ans;
        sort(potions.begin(), potions.end());
        for(int i=0;i<spells.size();++i)
        {
            long long cmp= success%spells[i] ? success/spells[i]+1 : success/spells[i];
            int index=lower_bound(potions.begin(), potions.end(), cmp)-potions.begin();
            if(index<potions.size()) ans.push_back(potions.size()-index);
            else ans.push_back(0);
        }
        return ans;
    }
};
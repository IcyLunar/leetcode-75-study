#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) 
    {
        unordered_set<int> s1(nums1.begin(), nums1.end()), s2(nums2.begin(), nums2.end());
        vector<int> ans1, ans2;
        for(int i:s1)
            if(s2.count(i)==0) ans1.push_back(i);
        for(int i:s2)
            if(s1.count(i)==0) ans2.push_back(i);
        return {ans1, ans2};
    }
};
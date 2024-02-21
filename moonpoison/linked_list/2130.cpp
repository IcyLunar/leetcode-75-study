#include<bits/stdc++.h>
using namespace std;
struct ListNode 
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    int pairSum(ListNode* head) 
    {
        int mx=0;
        vector<int> v;
        while(head)
        {
            v.push_back(head->val);
            head=head->next;
        }
        for(int i=0;i<v.size();++i)
            mx=max(mx, v[v.size()-1-i]+v[i]);
        return mx;
    }
};
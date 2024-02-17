#include<bits/stdc++.h>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) 
    {
        ListNode ans(0, head);
        ListNode *p1=&ans;
        ListNode *p2=&ans;
        while(p1->next!=nullptr&&p1->next->next!=nullptr)
        {
            p2=p2->next;
            p1=p1->next->next;
        }
        p2->next=p2->next->next;
        return ans.next;
    }
};
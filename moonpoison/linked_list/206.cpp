
#include<iostream>
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
    ListNode* reverseList(ListNode* head) 
    {
        ListNode *first=head, *second=NULL;
        if(head==NULL) return head;
        for(ListNode *tmp=first->next;tmp!=NULL;tmp=tmp->next)
        {
            first->next=second;
            second=first;
            first=tmp;
        }
        first->next=second;
        return first;
    }
};
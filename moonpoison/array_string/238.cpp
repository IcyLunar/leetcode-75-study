#include<iostream>
#include<vector>
using namespace std;
int main()
{
    vector<int> nums;
    int a=0;
    cin>>a;
    for(int i=0;i<a;++i)
    {
        int b;
        cin>>b;
        nums.push_back(b);
    }
    a=0;
    int b;
    int tmp=1;
    int size=nums.size();
    vector<int> ans(size, 0);
    for(int i=0;i<size;++i)
    {
        if(nums[i]==0)
        {
            a++;
            b=i;
        }
        else tmp*=nums[i];
    }
    if(a==1) 
    {
        for(int i=0;i<size;++i) 
            if(i==b) ans[i]=tmp;
    }
    else if(a==0)
    {
        for(int i=0;i<size;++i)
        {
            ans[i]=tmp/nums[i];
        } 
    } 
    for(auto &i:ans)
    {
        cout<<i<<' ';
    }
}

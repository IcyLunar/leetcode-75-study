#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isSubsequence(string s, string t) 
    {
        int start=0; //문자열 t의 시작위치
        for(int i=0;i<s.size();++i)
        {
            int flag=0; //s[i]==t[i]여부 확인
            for(int j=start;j<t.size();++j)
            {
                if(s[i]==t[j]) //있을경우 flag=1, 다음 t의 시작위치는 찾은값+1, 반복문 탈출
                {
                    flag++;
                    start=j+1;
                    break;
                }
            }
            if(flag!=1) return false; //s[i]==t[i]인 경우가 없었으므로 return false
        }
        return true; //위 반복문중 return false의 경우가 없으므로 true 반환
    }
};

#include<bits/stdc++.h>
using namespace std;
int guess(int num){}
class Solution {
public:
    int guessNumber(int n) 
    {
        int l=1, r=n;
        int m;
        while(l<=r)
        {
            m=l+(r-l)/2;
            if(guess(m)==-1) r=m-1;
            else if(guess(m)==1) l=m+1;
            else if(guess(m)==0) break;
        }
        return m;
    }
};
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
class Solution {
public:
    int reverse(int x) {
        int  revN = 0;
        while(x!=0)
        {
          if(revN>INT_MAX / 10 || revN<INT_MIN/10) return 0;
          int dig = x % 10;
          x = x/10 ;
          revN = revN*10 + dig;
        }
        return revN;
    }
};
class Solution:
    def myAtoi(self, s: str) -> int:
        num = ''
        negflag = 1
        i = 0

        while i < len(s) and s[i] == ' ' :
            i += 1
        
        if i < len(s) and s[i] == '-' : 
            negflag = -1
            i+=1
        elif i < len(s) and s[i] == '+' :
            i += 1

        while i < len(s) and s[i].isdigit() :
            if not num and s[i] == '0' :
                i +=1
                continue
            num += s[i]
            i+=1

        if not num :
            return 0

        result = negflag*int(num)

        INT_MIN , INT_MAX = -2**31,2**31-1
        if result < INT_MIN :
            return INT_MIN
        if result > INT_MAX :
            return INT_MAX
        
        return result
    
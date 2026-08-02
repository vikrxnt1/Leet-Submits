class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        # bsd = 9
        # if s > bsd*n:
        #     return -1
        # q = s // 9
        # r = s % 9
        # # if n != 1:
        # if s%n == 0 and q != 0:
        #     return int('9'*q)
        # return int('9'*q+str(r)+'0'*(n-(q+1)))
        c = 0
        ans = ""
        if s > 9*n:
            return -1
        while s>8 :
            ans += '9'
            s -= 9
            n -= 1
        if s!= 0:
            ans += str(s)
            n -= 1
        if n>0:
            ans += '0'*n
        return int(ans)
        
        
        
        
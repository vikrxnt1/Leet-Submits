class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        # Dictionary Solution Time -> O(n) Space -> O(n)
        
        # d = {}
        # for i in s:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # if x not in d or y not in d:
        #     return s
        # ans = y*d[y] + x*d[x]
        # del d[x]
        # del d[y]
        # for a,b in d.items():
        #     ans += a*b
        # return ans

        # Stack Solution Time -> O(n) Space -> O(1)
        ans = ""
        st = ""
        for i in s:
            if i == x:
                st += x
            else:
                ans += i
        return ans + st
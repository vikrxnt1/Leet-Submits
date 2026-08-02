class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        d = {}
        mx_rng = -1
        ans = 0
        for i in nums:
            num = str(i)
            mx, mn = -1, float('inf')
            for k in num:
                mx = max(mx,int(k))
                mn = min(mn,int(k))
            rng = mx - mn
            d[i] = rng
            mx_rng = max(mx_rng,rng)
        for x in nums:
            if d[x] == mx_rng:
                ans += x
        return ans
        
            
        
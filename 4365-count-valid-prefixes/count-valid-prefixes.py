class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zero, ones = 0, 0
        ans = 0
        for i in s:
            if i == '0':
                zero += 1
            else:
                ones += 1
            diff = abs(zero - ones)
            if diff == 0 or diff == 1:
                ans += 1
        return ans
        
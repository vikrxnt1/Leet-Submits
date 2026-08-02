class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        st,et = startTime.split(':'), endTime.split(':')
        diff = [int(et[i])-int(st[i]) for i in range(3)]
        return diff[-1] + 60*diff[-2] + 3600*diff[-3]
        
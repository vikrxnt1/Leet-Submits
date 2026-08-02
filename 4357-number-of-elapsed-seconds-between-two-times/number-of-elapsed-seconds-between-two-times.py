class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        st,et = startTime.split(':'), endTime.split(':')
        diff = [int(et[i])-int(st[i]) for i in range(3)]
        print(diff)
        if diff[-1] < 0:
            diff[-1] = 60 + diff[-1]
            diff[-2] -= 1
            if diff[-2] < 0:
                diff[-2] = 60 + diff[-2]
                diff[-3] -= 1
        else:
            if diff[-2] < 0:
                diff[-2] = 60 + diff[-2]
                diff[-3] -= 1
            
        # print(diff)
        # return -1

        # for i in range(len(diff)):
        #     if diff[i] < 0:
        #         diff[i] = 60 + diff[i]
        #     if diff[i] > 0:
        #         diff[i] -= 1
        # diff[-1] += 1
        # print (diff)
        return diff[-1] + 60*diff[-2] + 3600*diff[-3]
        
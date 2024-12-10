class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        tgas=0
        tcost=0
        ccost=0
        start=0
        for i in range(len(cost)):
            tcost+=cost[i]
            tgas+=gas[i]
            ccost+=gas[i]-cost[i]
            if ccost<0:
                start=i+1
                ccost=0
        if tgas<tcost:
            return -1
        return start   

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank = tank - cost[i] + gas[i]

            if tank < 0:
                start = i+1
                tank = 0
        return start
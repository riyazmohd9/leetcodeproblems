class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        s = 0
        nums.sort()
        index = len(nums)//2
        mid = nums[index]
        for i in nums:
            s += abs(mid-i)
        return s 
        
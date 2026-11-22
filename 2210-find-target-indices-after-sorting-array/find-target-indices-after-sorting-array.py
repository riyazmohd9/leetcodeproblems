class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        re = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                re.append(i)
        return re
       

        
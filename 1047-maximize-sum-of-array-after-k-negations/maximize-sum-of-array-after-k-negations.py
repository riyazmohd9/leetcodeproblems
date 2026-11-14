class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i] = nums[i]*-1
                k -= 1 
        if k == 0 or k %2 == 0:
            return sum(nums)
        else:
            nums.sort()
            nums[0] *= -1
            return sum(nums)
                
                
                    

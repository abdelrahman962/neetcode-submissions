class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)

        prefix=1

        res=[1]*size
        for i in range(size):
            res[i]*=prefix
            prefix*=nums[i]
        
        suffix=1
        for i in range(size-1,-1,-1):
            res[i] *=suffix
            suffix*=nums[i]

        
        return res

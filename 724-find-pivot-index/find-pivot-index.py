class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        pivIndex = -1
        for i in range(len(nums)):
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i+1:])
            if leftSum == rightSum:
                return i
        return pivIndex
                
                


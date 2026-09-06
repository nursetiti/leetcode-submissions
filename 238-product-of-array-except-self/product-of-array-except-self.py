import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = math.prod(nums)
        # answer = []
        # for i in range(len(nums)):
        #     product = math.prod(nums[:i]) * math.prod(nums[i+1:])
        #     answer.append(product)
        # return answer

        answer = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
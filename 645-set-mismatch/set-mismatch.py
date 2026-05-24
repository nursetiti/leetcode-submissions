# class Solution(object):
#     def findErrorNums(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         newArray = []
#         indexOfnum = -1
#         lengthOfArray = len(nums)

#         for i in range(1, lengthOfArray + 1):
#             if nums.count(i) == 2:
#                 newArray.append(i)
#                 indexOfnum = nums.index(i)
#             if i not in nums:
#                 newArray.insert(indexOfnum + 1, i)
#         return newArray



class Solution(object):
    def findErrorNums(self, nums):
        duplicate = -1
        missing = -1

        for i in range(1, len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                duplicate = i
            elif count == 0:
                missing = i

        return [duplicate, missing]
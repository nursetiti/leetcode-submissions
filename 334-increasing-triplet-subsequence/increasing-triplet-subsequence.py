class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # arrayTriple = []
        # # while len(arrayTriple) != 3:
        # for i in range(len(nums)):
        #     if i == 0:
        #         arrayTriple.append(nums[i])
        #     if i != 0 and nums[i] > max(arrayTriple):
        #         arrayTriple.append(nums[i])
        #     # elif i !=0 and (nums[i] < nums[i-1]):
        #     #     arrayTriple = []
        # print(arrayTriple)
        # if len(arrayTriple) >= 3:
        #     return True
        # else:
        #     return False

        arrayTriple = [float('inf'), float('inf')]

        for num in nums:
            if num <= arrayTriple[0]:
                arrayTriple[0] = num

            elif num <= arrayTriple[1]:
                arrayTriple[1] = num

            else:
                return True

        return False

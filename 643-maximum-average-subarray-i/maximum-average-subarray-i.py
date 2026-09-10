class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left = 0
        right = k

        window = sum(nums[left:right])
        maxAverage = window / k

        while right < len(nums):

            window -= nums[left]
            window += nums[right]

            left += 1
            right += 1

            averageVal = window / k 

            if averageVal > maxAverage:
                maxAverage = averageVal

        return maxAverage
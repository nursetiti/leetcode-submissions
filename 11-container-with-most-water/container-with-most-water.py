class Solution:
    def maxArea(self, height: List[int]) -> int:
        left =0;
        right = len(height) -1
        max = 0;
        while left < right:
            minHeight = min(height[left], height[right])
            width = right-left
            prod = minHeight * width
            if(prod > max):
                max = prod
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max
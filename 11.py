class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        container = 0
        while left < right:
            curr = min(height[left], height[right]) * (right - left)
            if container < curr:
                container = curr
            i = 1
            if height[left] < height[right]:
                prev = left
                while height[prev] >= height[left] and left < right:
                    left += 1
            else:
                prev = right
                while height[prev] >= height[right] and left < right:
                    right -= 1

        
        return container
        
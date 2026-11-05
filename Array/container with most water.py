# Problem: Container With Most Water
# LeetCode: 11
# Pattern: Two Pointers
# Approach:
# Start with two pointers at opposite ends.
# Calculate area and move the pointer at the shorter height.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
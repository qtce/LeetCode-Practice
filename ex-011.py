class Solution(object):
    """
        11. Container With Most Water
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_column = 0
        p = 0
        q = len(height) - 1

        while p < q:
            max_column = max(min(height[p], height[q]) * (q - p), max_column)
            if height[p] >= height[q]:
                q = q - 1
            else:
                p = p + 1

        return max_column
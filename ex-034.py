class Solution(object):
    """
    34.Search for a Range
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def searchTarget(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def searchRange(self, nums, target):
        start = self.searchTarget(nums, target)

        if not nums or start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = self.searchTarget(nums, target + 1) - 1

        return [start, end]

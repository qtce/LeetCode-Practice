class Solution(object):
    def removeElement(self, nums, val):
        """
        27. Remove Element
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count, i = 0, 0

        if not nums:
            return count

        m = len(nums)

        while i < m:
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
            i += 1

        return count
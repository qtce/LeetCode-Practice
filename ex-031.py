class Solution(object):
    def nextPermutation(self, nums):
        """
        31.Next Permutation
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return None
        i = len(nums)-1
        j = -1
        while i > 0:
            if nums[i-1] < nums[i]:
              j = i-1
              break
            i-=1
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[j+1:] = sorted(nums[j+1:])
                return
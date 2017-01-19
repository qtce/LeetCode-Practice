class Solution(object):
    def threeSum(self, nums):
        """
        15. 3Sum
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for m in range(len(nums) - 2):
            if m > 0 and nums[m] == nums[m - 1]:
                continue

            c, n = m + 1, len(nums) - 1

            while c < n:
                s = nums[m] + nums[c] + nums[n]
                if s < 0:
                    c = c + 1
                elif s > 0:
                    n = n - 1
                else:
                    res.append([nums[m], nums[c], nums[n]])
                    while c < n and nums[c] == nums[c + 1]:
                        c = c + 1
                    while c < n and nums[n] == nums[n - 1]:
                        n = n - 1
                    c = c + 1
                    n = n - 1

        return res
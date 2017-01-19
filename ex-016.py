class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        16. 3Sum Closest
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        min_gap = sys.maxint
        nums.sort()

        for m in range(len(nums) - 2):
            if m > 0 and nums[m] == nums[m - 1]:
                continue

            c, n = m + 1, len(nums) - 1

            while c < n:
                s = nums[m] + nums[c] + nums[n]
                gap = abs(s - target)

                if gap < min_gap:
                    res = s
                    min_gap = gap

                if s < target:
                    c = c + 1
                else:
                    n = n - 1

        return res
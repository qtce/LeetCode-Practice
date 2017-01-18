class Solution(object):
    """
    14. Longest Common Prefix
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            prefix = strs[0]

        for item in strs:
            if len(item) < len(prefix):
                prefix = item

        n = 0

        for item in strs:
            while n <= len(prefix) - 1:
                if prefix[n] == item[n]:
                    n = n + 1
                else:
                    break

            if n == 0:
                prefix = ""
            else:
                prefix = prefix[0:n]

            n = 0

        return prefix
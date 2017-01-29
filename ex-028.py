class Solution(object):
    def strStr(self, haystack, needle):
        """
        28. Implement strStr()
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle): return -1

        i = 0

        while i < len(haystack) - len(needle) + 1:
            j = 0;
            k = i
            while j < len(needle):
                if haystack[k] == needle[j]:
                    j += 1;
                    k += 1
                else:
                    break
            if j == len(needle):
                break
            else:
                i += 1

        if i == len(haystack) - len(needle) + 1:
            return -1
        else:
            return i
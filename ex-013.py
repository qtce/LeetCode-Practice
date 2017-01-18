class Solution(object):
    """
    13. Roman to Integer
    """
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans = 0
        c = len(s) - 1

        rome_dic = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                    'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        while c >= 0:
            if c > 0:
                if (s[c - 1] + s[c]) in rome_dic:
                    trans = trans + rome_dic[s[c - 1] + s[c]]
                    c = c - 2
                elif s[c] in rome_dic:
                    trans = trans + rome_dic[s[c]]
                    c = c - 1
            else:
                trans = trans + rome_dic[s[c]]
                c = c - 1

        return trans
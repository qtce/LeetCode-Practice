class Solution(object):
    """
    12. Integer to Roman
    """
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        trans = ''
        tmp = num
        rome_dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                    100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        rome_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        for key in rome_list:
            trans = trans + tmp / key * rome_dic[key]
            tmp = tmp % key

        return trans
class Solution(object):
    def letterCombinations(self, digits):
        """
        17. Letter Combinations of a Phone Number
        :type digits: str
        :rtype: List[str]
        """

        res = []
        pres = []
        num_dict = [[' '], ['*'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
                    ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        i = 0

        for item in digits:
            item = int(item)

            if i != 0:
                pres = res
                res = []
                for m in num_dict[item]:
                    for n in pres:
                        res.append(n + m)
            else:
                for m in num_dict[item]:
                    res.append(m)

            i += 1

        return res
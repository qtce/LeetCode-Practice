class Solution(object):
    """
    22. Generate Parentheses
    """
    def generatePar(self, n, s, l, r, res):
        if l == n:
            res.append(s + (n - r) * ")")
            return res

        self.generatePar(n, s + '(', l + 1, r, res)
        if l > r: self.generatePar(n, s + ')', l, r + 1, res)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n > 0: self.generatePar(n, "", 0, 0, res)

        return res
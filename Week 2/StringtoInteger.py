import re
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = s.strip()
        if not str:
            return 0
        res = re.findall(r"^[+-]?\d+", str)
        if not res:
            return 0
        res = int(res[0])
        return max(min(res, 2 ** 31 - 1), -2 ** 31)

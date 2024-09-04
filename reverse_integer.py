class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            digit = x % 10
            if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and digit > 7):
                return 0
            if rev < (-2**31) // 10 or (rev == (-2**31) // 10 and digit < -8):
                return 0
            rev = rev * 10 + digit
            x //= 10
        return rev * sign
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = ["" for _ in range(numRows)]
        index, direction = 0, 1
        for char in s:
            result[index] += char
            index += direction
            if index == 0 or index == numRows - 1:
                direction *= -1
        return ''.join(result)
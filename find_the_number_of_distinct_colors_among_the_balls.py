class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ball_colors = {}
        color_count = {}
        result = []

        for x, y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            ball_colors[x] = y
            if y in color_count:
                color_count[y] += 1
            else:
                color_count[y] = 1
            result.append(len(color_count))

        return result

solution = Solution()
print(solution.queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]]))
print(solution.queryResults(4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]))
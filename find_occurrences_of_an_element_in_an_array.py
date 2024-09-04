class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        occurrence_indices = []
        for i in range(len(nums)):
            if nums[i] == x:
                occurrence_indices.append(i)
        
        answer = []
        for q in queries:
            if q <= len(occurrence_indices):
                answer.append(occurrence_indices[q - 1])
            else:
                answer.append(-1)
        
        return answer

solution = Solution()
print(solution.occurrencesOfElement([1, 3, 1, 7], [1, 3, 2, 4], 1))
print(solution.occurrencesOfElement([1, 2, 3], [10], 5))    
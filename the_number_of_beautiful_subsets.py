class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.count = 0
        
        def backtrack(start, current_subset):
            if current_subset:
                self.count += 1
            
            for i in range(start, len(nums)):
                if all(abs(nums[i] - num) != k for num in current_subset):
                    current_subset.append(nums[i])
                    backtrack(i + 1, current_subset)
                    current_subset.pop()
        
        backtrack(0, [])
        return self.count

solution = Solution()
print(solution.beautifulSubsets([2, 4, 6], 2)) 
print(solution.beautifulSubsets([1], 1))
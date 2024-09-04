class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True

solution = Solution()
print(solution.isArraySpecial([1]))         
print(solution.isArraySpecial([2, 1, 4]))   
print(solution.isArraySpecial([4, 3, 1, 6])) 
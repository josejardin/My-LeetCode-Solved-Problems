class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        xor_result = 0
        for num, cnt in count.items():
            if cnt == 2:
                xor_result ^= num
        
        return xor_result


solution = Solution()
print(solution.duplicateNumbersXOR([1, 2, 1, 3]))  
print(solution.duplicateNumbersXOR([1, 2, 3]))  
print(solution.duplicateNumbersXOR([1, 2, 2, 1]))
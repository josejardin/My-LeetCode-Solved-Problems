class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1
        return count

sol = Solution()
print(sol.numberOfPairs([1, 3, 4], [1, 3, 4], 1))  # Output: 5
print(sol.numberOfPairs([1, 2, 4, 12], [2, 4], 3))  # Output: 2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=[]
        l=len(nums)
        for i in range(0,l):
            for j in range(0,l):
                if nums[i]+nums[j]==target and j!=i:
                    a.append(j)             
        return a

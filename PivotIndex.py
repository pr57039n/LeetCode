class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        start = 0
        end = sum(nums)
        for index, nums in enumerate(nums):
            end-=nums
            if start==end:
                return index
            start+=nums
        return -1

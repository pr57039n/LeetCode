class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        arraysum = []
        for i in nums:
            sum+=i
            arraysum.append(sum)
        return arraysum

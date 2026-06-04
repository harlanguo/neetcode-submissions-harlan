class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]

        for cur in nums[1:]:
            curSum = max(cur, cur + curSum)
            maxSum = max(curSum, maxSum)
        
        return maxSum
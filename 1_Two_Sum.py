class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in prevMap:
                prevMap[nums[i]] = i
            else:
                return [i, prevMap[diff]]
        

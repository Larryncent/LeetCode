class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        if len(nums) == 0:
            return 0
        l = sorted(list(set(nums)))
        i = 0
        _max = 1
        length = 1
        while i < len(l) - 1:
            if l[i + 1] - l[i] == 1:
                length += 1
                _max = max(length, _max)
            else:
                length = 1
            i += 1
        return _max
        '''
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

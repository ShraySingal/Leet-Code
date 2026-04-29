class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0 
        x = 1
        while x < len(nums):
            if nums[c] != nums[x]:
                c = c + 1
                nums[c] = nums[x]
            x = x + 1
        return c + 1

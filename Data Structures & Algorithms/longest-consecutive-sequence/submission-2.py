class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(list(set(nums)))
        maxi,curr,prev=1,1,nums[0]
        nums.pop(0)
        while nums != []:
            if prev + 1 == nums[0]:
                curr += 1
                maxi = max(maxi,curr)
                prev = nums[0]
                nums.pop(0)
            else:
                curr = 1
                prev = nums[0]
                nums.pop(0)
        return maxi

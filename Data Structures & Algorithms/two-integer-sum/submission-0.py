class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = defaultdict(int)
        for i,j in enumerate(nums):
            if target - j in res:
                return [res[target-j],i]
            res[j] = i
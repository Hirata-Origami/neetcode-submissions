class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = defaultdict(list)
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp[nums[i] + nums[j]].append([i,j])
        for i in range(len(nums)):
            if -nums[i] in temp.keys():
                for j in temp[-nums[i]]:
                    te = sorted([nums[i],nums[j[0]],nums[j[1]]])
                    if i not in j and te not in res:
                        res.append(te)
        return res

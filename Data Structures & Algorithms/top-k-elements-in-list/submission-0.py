class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)
        temp = Counter(nums)
        for i,j in temp.items():
            res[j].append(i)
        result = []
        for i in range(len(nums),0,-1):
            if i in res:
                result.extend(res[i])
                if len(result) >= k:
                    return result[:k]
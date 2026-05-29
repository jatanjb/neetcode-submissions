class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        datadict ={}
        res = []
        for i in nums:
            datadict[i] = 1 + datadict.get(i,0)
        
        for value,cnt in datadict.items():
            res.append([cnt, value])
        res.sort()
        result = []
        while len(result) < k:
            result.append(res.pop()[1])
        return result

        
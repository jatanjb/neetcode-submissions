class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        arr = []
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for j,d in count.items():
            arr.append([d,j])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        
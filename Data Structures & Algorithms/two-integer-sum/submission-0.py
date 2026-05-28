class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newmap ={}
        for i,n in enumerate(nums):
            x = target - n
            if x in newmap:
                return [newmap[x],i]
            newmap[n] = i
        
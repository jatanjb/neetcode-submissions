class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ddict =defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')] += 1
            ddict[tuple(count)].append(word)
        return list(ddict.values())
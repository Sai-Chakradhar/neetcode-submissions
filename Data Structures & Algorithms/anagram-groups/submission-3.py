class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in range(0,len(strs)):
            key = "".join(sorted(strs[i]))
            if key in hash_map:
                hash_map[key].append(strs[i])
            else:
                hash_map[key] = [strs[i]]

        return list(hash_map.values())


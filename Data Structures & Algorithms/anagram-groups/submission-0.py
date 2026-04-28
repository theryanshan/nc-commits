from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)
        for st in strs:
            freq_list = [0] * 26
            for char in st:
                idx = ord(char) - ord('a')
                freq_list[idx] += 1
            key = tuple(freq_list)
            freq_map[key].append(st)

        return list(freq_map.values())
            
        
class Solution(object):
    def groupAnagrams(self, strs):
        h_map = {}

        for idx, word in enumerate(strs):
            s_word = "".join(sorted(word))

            if s_word in h_map:
                h_map[s_word].append(word)
            else:
                h_map[s_word] = [word]
            
        return list(h_map.values())
        

strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams(strs))
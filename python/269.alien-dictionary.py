from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
                    
        visited = {}
        result = []
        
        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = False

            for neigh in adj_list[char]:
                if not dfs(neigh):
                    return False
                
            visited[char] = True
            result.append(char)

            return True
        
        for c in adj_list:
            if c not in visited:
                if not dfs(c):
                    return ""
                
        return "".join(reversed(result))

words = ["z","o"] # "zo"
words = ["hrn","hrf","er","enn","rfnn"] # "hernf"


print(Solution().foreignDictionary(words))
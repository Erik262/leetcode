from typing import List
from collections import deque, defaultdict
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neigh = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neigh[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
            
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    for nword in neigh[pattern]:
                        if nword not in visit:
                            visit.add(nword)
                            q.append(nword)
            res += 1

        return 0
        
beginWord = "cat"
endWord = "sag"
wordList = ["bat","bag","sag","dag","dot"] # 4

# beginWord = "cat"
# endWord = "sag"
# wordList = ["bat","bag","sat","dag","dot"] # 0

print(Solution().ladderLength(beginWord, endWord, wordList))
# @lc code=end

